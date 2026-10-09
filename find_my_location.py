import json
from urllib.request import urlopen

def get_current_location():
    # IP 기반 위치 정보를 제공하는 무료 API 호출
    url = "http://ip-api.com/json/"
    
    try:
        response = urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        
        if data['status'] == 'success':
            print(f"국가: {data.get('country')}")
            print(f"도시: {data.get('city')}")
            print(f"지역: {data.get('regionName')}")
            print(f"위도(Latitude): {data.get('lat')}")
            print(f"경도(Longitude): {data.get('lon')}")
            print(f"IP 주소: {data.get('query')}")
        else:
            print("위치 정보를 가져오는 데 실패했습니다.")
            
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    get_current_location()