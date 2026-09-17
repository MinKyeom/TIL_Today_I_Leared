// AJAX 예시 코드
// 서버에서 사용자 정보를 비동기로 가져오는 함수
function getUserData() {
  fetch("https://jsonplaceholder.typicode.com/users/1")
    .then((response) => {
      // 응답이 성공적인지 확인
      if (!response.ok) {
        throw new Error("네트워크 응답에 문제가 있습니다.");
      }
      return response.json(); // 응답 데이터를 JSON 객체로 변환
    })
    .then((data) => {
      // 서버에서 받은 데이터로 화면의 일부만 업데이트
      console.log("가져온 데이터:", data);
      document.getElementById("user-name").innerText = data.name;
    })
    .catch((error) => {
      console.error("AJAX 요청 실패:", error);
    });
}
