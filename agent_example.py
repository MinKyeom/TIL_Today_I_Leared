"""
에에이전트 코드 예시 
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