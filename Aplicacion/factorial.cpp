#include <iostream>
using namespace std;

/** \fn: long obtenerFactorial(int numero)
 * \brief: Obtiene el factorial de un numero
 * \param numero : Numero del cual se obtiene el factorial
 * \return: Devuelve el factorial del numero dado. */

long obtenerFactorial(int numero){
	if (numero < 0){
		cout<<"El numero no debe ser negativo"<<endl;
		return -1;
	}else if(numero==1 || numero==0){
		return 1;
	}else{
		return numero*obtenerFactorial(numero-1);
	}
}
int main(){
	int n=0;
	cout<<"Dame un numero"<<endl;
	cin>>n;
	long v= obtenerFactorial(n);
	cout<<v;
}
