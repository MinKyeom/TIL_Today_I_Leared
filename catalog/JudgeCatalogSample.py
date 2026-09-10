import numpy as np
from dataclasses import dataclass

MATCH_THRESHOLD = 0.88  # 임계값 이상이면 동일 카탈로그로 매칭

@dataclass
class Offer:
    offer_id: str
    seller_id: str
    ean_barcode: str
    normalized_data: NormalizedProduct
    text_vector: np.ndarray   # BERT/SentenceTransformer 임베딩
    image_vector: np.ndarray  # ResNet/CLIP 이미지 임베딩

class CatalogMatchingEngine:
    def __init__(self, catalog_repository):
        self.repo = catalog_repository

    def compute_similarity(self, offer_a: Offer, offer_b: Offer) -> float:
        # 1. EAN 바코드가 완벽히 일치하는 경우 강제 매칭
        if offer_a.ean_barcode and offer_a.ean_barcode == offer_b.ean_barcode:
            return 1.0

        # 2. 브랜드나 규격 단위가 다르면 매칭 거부
        if offer_a.normalized_data.brand != offer_b.normalized_data.brand:
            return 0.0
        if offer_a.normalized_data.standard_volume_ml != offer_b.normalized_data.standard_volume_ml:
            return 0.0

        # 3. 코사인 유사도를 통한 텍스트/이미지 벡터 유사도 산출
        text_sim = np.dot(offer_a.text_vector, offer_b.text_vector) / (
            np.linalg.norm(offer_a.text_vector) * np.linalg.norm(offer_b.text_vector)
        )
        image_sim = np.dot(offer_a.image_vector, offer_b.image_vector) / (
            np.linalg.norm(offer_a.image_vector) * np.linalg.norm(offer_b.image_vector)
        )

        # 4. 가중치 합산 (텍스트 60%, 이미지 40%)
        return float(0.6 * text_sim + 0.4 * image_sim)

    def match_and_route(self, incoming_offer: Offer) -> str:
        candidates = self.repo.find_candidates_by_brand(incoming_offer.normalized_data.brand)
        
        best_match_catalog_id = None
        max_score = 0.0

        for catalog in candidates:
            score = self.compute_similarity(incoming_offer, catalog.representative_offer)
            if score > max_score:
                max_score = score
                best_match_catalog_id = catalog.id

        # Threshold 판단
        if max_score >= MATCH_THRESHOLD:
            self.repo.bind_to_catalog(catalog_id=best_match_catalog_id, offer=incoming_offer)
            return f"BOUND_TO_CATALOG_{best_match_catalog_id}"
        else:
            new_catalog_id = self.repo.create_new_catalog(incoming_offer)
            return f"CREATED_NEW_CATALOG_{new_catalog_id}"