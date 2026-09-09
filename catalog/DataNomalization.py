import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class NormalizedProduct:
    raw_title: str
    brand: str
    standard_volume_ml: Optional[float]
    clean_title: str

class ProductDataNormalizer:
    def __init__(self):
        # 용량 규격 정규화를 위한 정규식
        self.volume_pattern = re.compile(r'(\d+(?:\.\d+)?)\s*(ml|l|리터|밀리리터)', re.IGNORECASE)

    def normalize_volume(self, text: str) -> Optional[float]:
        match = self.volume_pattern.search(text)
        if not match:
            return None
        
        val, unit = float(match.group(1)), match.group(2).lower()
        if unit in ['l', '리터']:
            return val * 1000.0  # L 단위를 ml로 표준화
        return val

    def process(self, raw_title: str, brand: str) -> NormalizedProduct:
        # 노이즈 문구 및 특수문자 제거
        clean_title = re.sub(r'\[.*?\]|\(.*?\)|★|특가|무료배송', '', raw_title).strip()
        volume_ml = self.normalize_volume(raw_title)
        
        return NormalizedProduct(
            raw_title=raw_title,
            brand=brand.strip().upper(),  # 브랜드명 대문자 통일
            standard_volume_ml=volume_ml,
            clean_title=clean_title
        )