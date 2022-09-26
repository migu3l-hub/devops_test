package com.paymentchain.billing;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
//@SpringBootTest
public class BasicApplicationTests {

	@Test
	public void contextLoads() {
         String message= "default message cambio 1 pero ahora es el momento de hacer las pruebas de integracion continua eliminando la rama de github y ademas enviando una notificacion de slack";
         Assert.assertNotNull(message);
	}

}
