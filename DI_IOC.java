// DI IOC 적용 전

// 1. 메시지 전송 인터페이스 및 구현체
interface MessageService  {
    void sendMessage(String message);
}

public class DI_IOC implements MessageService {
    @Override
    public void sendMessage(String message) {
        System.out.println("이메일 발송: " + message);
    }
}

// 2. 메시지를 활용하는 클라이언트 클래스
class NotificationController {
    private MessageService messageService;

    public NotificationController() {
        // [문제점] 컨트롤러가 사용할 객체를 직접 new로 생성함
        // 객체 생성의 제어권이 NotificationController에게 있음
        this.messageService = new EmailService(); 
    }

    public void send(String msg) {
        this.messageService.sendMessage(msg);
    }
}