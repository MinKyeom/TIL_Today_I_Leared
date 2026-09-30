class Parent {
    String name = "부모";

    void hello() {
        System.out.println("부모의 인사");
    }
}

class Child extends Parent {
    String nickname = "자식 닉네임"; // 자식만의 필드

    @Override
    void hello() {
        System.out.println("자식의 재정의된 인사"); // 오버라이딩
    }

    void play() {
        System.out.println("자식의 전용 놀이"); // 자식만의 메서드
    }
}