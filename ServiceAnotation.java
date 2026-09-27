package org.springframework.stereotype;

import java.lang.annotation.Documented;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import org.springframework.core.annotation.AliasFor;

@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Component // ★ 핵심: @Component를 메타 어노테이션으로 가지고 있음
public @interface ServiceAnotation {

    @AliasFor(annotation = Component.class)
    String value() default "";

}

/*

주요 요소 상세 분석
@Component (핵심)

@Service 내부에 @Component가 붙어 있기 때문에, 스프링이 컴포넌트 스캔(Component Scan)을 진행할 때 @Service가 붙은 클래스도 자동으로 스프링 빈(Bean)으로 등록됩니다.

기술적으로는 @Component와 완벽히 동일하게 동작합니다.

@Target({ElementType.TYPE})

이 어노테이션을 클래스, 인터페이스, 에놈(Enum)에만 붙일 수 있도록 제한합니다. (메서드나 필드에는 붙일 수 없음)

@Retention(RetentionPolicy.RUNTIME)

어노테이션 정보가 실행 시점(Runtime)까지 유지되도록 설정합니다. 스프링이 애플리케이션을 실행할 때 리플렉션(Reflection)을 통해 @Service 클래스를 찾아내고 빈으로 등록할 수 있는 이유입니다.

@AliasFor(annotation = Component.class)

@Service("myService")와 같이 빈의 이름을 별도로 지정할 때, 이 값이 내부의 @Component의 value 속성으로 전달되도록 별칭(Alias)을 매핑해 줍니다.

그렇다면 @Component를 직접 안 쓰고 굳이 @Service를 쓰는 이유는?
스프링 프레임워크 입장에서는 기능적으로 둘 다 동일한 스프링 빈입니다. 하지만 개발 관점에서 다음과 같은 이점이 있습니다.

명확한 역할 분담 (Domain-Driven Design / 계층 명시)

코드를 보는 사람에게 이 클래스가 비즈니스 로직을 처리하는 서비스 레이어임을 명확하게 전달합니다.

AOP 및 예외 처리의 확장 가능성

@Repository의 경우 DB 예외를 스프링의 DataAccessException으로 다듬어 변환해 주는 기능이 추가되어 있는 것처럼, 차후 프레임워크나 AOP 설정에서 계층별(@Controller, @Service, @Repository)로 특화된 공통 처리를 적용하기 용이해집니다.

*/