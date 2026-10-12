import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 1. 모델과 토크나이저 불러오기 (예: 한국어 성능이 뛰어난 Bllossom 또는 EEVE 모델)
model_id = "MLP-KTLim/llama-3-Korean-Bllossom-8B"  # 또는 로컬에 다운로드한 경로
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",  # GPU가 여러 개거나 단일 GPU일 때 자동 할당
)

# 2. 번역 프롬프트 작성
source_text = "Artificial intelligence is changing the way we work and live."
prompt = f"""다음 영어를 자연스러운 한국어로 번역해 주세요. 번역 결과만 출력하세요.

원문: {source_text}
번역:"""

# 3. 토크나이징 및 인퍼런스(추론)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=128,
    temperature=0.3,  # 창의성을 낮추고 정확한 번역을 유도
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id,
)

# 4. 결과 디코딩 및 출력
result = tokenizer.decode(outputs[0], skip_special_tokens=True)
# 프롬프트 부분을 제외한 번역 결과만 추출
translated_text = result.split("번역:")[-1].strip()

print(f"원문: {source_text}")
print(f"번역: {translated_text}")