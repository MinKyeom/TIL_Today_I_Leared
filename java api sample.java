public import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ApiExample {
    public static void main(String[] args) {
        // 1. HttpClient 객체 생성
        HttpClient client = HttpClient.newHttpClient();

        // 2. HttpRequest 설정 (요청 URL 및 메소드 지정)
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://jsonplaceholder.typicode.com/posts/1"))
                .GET() // 기본값이 GET이므로 생략 가능
                .build();

        try {
            // 3. 요청 전송 및 응답 수신
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // 4. 결과 출력
            System.out.println("응답 상태 코드: " + response.statusCode());
            System.out.println("응답 데이터: " + response.body());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
} {
  
}
