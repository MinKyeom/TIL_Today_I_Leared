"""
에이전트 코드 예시 
에이전트는 주변 환경 인식(Perceive) -> 판단(Decide) -> 행동(Act) 구조로 동작합니다.  
"""
class TemperatureAgent:
    def __init__(self, target_temp=22):
        self.target_temp = target_temp  # 에이전트의 목표 설정

    def perceive(self, current_temp):
        """환경으로부터 현재 상태(온도)를 인식"""
        return current_temp

    def decide(self, current_temp):
        """상태를 바탕으로 행동 결정"""
        if current_temp < self.target_temp:
            return "HEATING"
        elif current_temp > self.target_temp:
            return "COOLING"
        else:
            return "OFF"

    def act(self, action):
        """결정된 행동을 실행"""
        if action == "HEATING":
            print("Action: 난방을 가동합니다. 🔥")
        elif action == "COOLING":
            print("Action: 에어컨을 가동합니다. ❄️")
        else:
            print("Action: 현상태를 유지합니다. 🟢")

# --- 실행 테스트 ---
agent = TemperatureAgent(target_temp=22)
environment_temperatures = [18, 22, 26]  # 환경 데이터

for temp in environment_temperatures:
    print(f"\n[현재 환경 온도: {temp}°C]")
    perceived_temp = agent.perceive(temp)
    action = agent.decide(perceived_temp)
    agent.act(action)
    
"""
LLM이 판단하는 에이전트
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class LLMAgent:
    def __init__(self, target_goal):
        self.target_goal = target_goal
        
    def decide_and_act(self, current_observation):
        """LLM을 이용해 상황을 판단하고 행동을 결정"""
        prompt = f"""
        당신은 상황을 판단하여 시스템을 제어하는 인공지능 에이전트입니다.
        
        [목표]: {self.target_goal}
        [현재 관찰된 상태]: {current_observation}
        
        다음 규칙에 맞춰 응답하세요:
        1. 현재 상태가 목표와 어떻게 다른지 원인을 분석하세요.
        2. [HEATING], [COOLING], [OFF] 중 하나의 행동을 선택하세요.
        3. 반환 형식을 반드시 "행동: [선택한 행동] | 이유: [판단 이유]" 형태로 출력하세요.
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        
        return response.choices[0].message.content

# --- 실행 테스트 ---
# LLM에 부여된 목표
agent = LLMAgent(target_goal="실내 온도를 쾌적하게 유지하고, 사람이 감기에 걸리지 않도록 22도로 유지할 것")

# 다양한 환경 상황 (LLM이 추론해야 하는 복잡한 텍스트 상황)
observations = [
    "현재 실내 온도는 15도이며 창문이 약간 열려 있어 쌀쌀한 바람이 들어오고 있습니다.",
    "현재 온도는 22도이며 습도와 공기 질 모두 양호합니다.",
    "현재 온도는 28도이고 직사광선이 들어와 실내가 매우 덥습니다."
]

for obs in observations:
    print(f"\n[관찰된 상태]: {obs}")
    decision = agent.decide_and_act(obs)
    print(f"[LLM 판단 결과]:\n{decision}")



# 에이전트 기초 샘플2

import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.llms import OpenAI
from langchain.agents import initialize_agent, AgentType, tool

# 1. API 키 설정 (본인의 OpenAI API 키 입력)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# 2. Agent가 사용할 커스텀 도구(Tool) 정의
@tool
def get_word_length(word: str) -> int:
    """단어의 글자 수를 반환합니다."""
    return len(word)

# 도구 목록 리스트에 등록
tools = [get_word_length]

# 3. LLM(대형 언어 모델) 생성
llm = OpenAI(temperature=0)

# 4. Agent 초기화 (ZERO_SHOT_REACT_DESCRIPTION: 도구의 설명을 보고 스스로 판단하여 사용)
agent = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True # Agent의 사고 과정(Thought/Action/Observation)을 출력
)

# 5. Agent 실행
response = agent.run("educate라는 단어의 글자 수는 몇 개인가요?")
print("\n최종 결과:", response)