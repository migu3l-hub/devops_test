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
         String message= "default message pero ahora todo automatico prueba para creacion de imagenes docker";
         Assert.assertNotNull(message);
	}

}
