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