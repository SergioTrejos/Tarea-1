#include <iostream>
#include <sstream>

using namespace std;

//defino la clase calculadora con las 4 funciones y constructores y demás
class calculadora {
    private:

    public:
        calculadora();
        ~calculadora();
        float suma(float num1, float num2);
        float resta(float num1, float num2);
        float division(float num1, float num2);
        float multiplicacion(float num1, float num2);
};

calculadora::calculadora(){

};

calculadora::~calculadora(){

};

//defino la suma
float calculadora::suma(float num1, float num2){
    float resultado = (num1 + num2);
    return resultado;
};
//defino la resta
float calculadora::resta(float num1, float num2){
    float resultado = (num1 - num2);
    return resultado;
};
//defino la multi
float calculadora::multiplicacion(float num1, float num2){
    float resultado = (num1 * num2);
    return resultado;
};
//defino la division (mucho de los mismo)
float calculadora::division(float num1, float num2){
    float resultado = (num1 / num2);
    return resultado;
};

int main(){
    int opc = 0;
    float num1;
    float num2;
    calculadora calc = calculadora();
    
    cout << "Ingrese el primer número: \n";
    cin >> num1;
    cout << "Ingrese el segundo número: \n";
    cin >> num2;
        cout << "Digite la opción de la operación a realizar: \n 1) Suma \n 2) Resta \n 3) Multiplicación \n 4) División \n 5) Salir \n";
    cin >> opc;
    if (opc == 1) {
        cout << "El resultado es \n";
        cout << calc.suma(num1,num2) << endl;
    };
    if (opc == 2) {
        cout << "El resultado es \n";
        cout << calc.resta(num1,num2) << endl;
    };
    if (opc == 3) {
        cout << "El resultado es \n";
        cout << calc.multiplicacion(num1,num2) << endl;
    };
    if (opc == 4) {
        cout << "El resultado es \n";
        cout << calc.division(num1,num2) << endl;
    };
    if (opc == 5)  {
        cout << "¡Adiós! \n";
        return 1;
    };
    
    cout << "¡Adiós! \n";
    return 1;
};
