#include <stdio.h>
#include <iostream>

using namespace std;

class Aula{
    public:
        int _piso;
        int _identificador;
        int _pupitres;
        bool _proyector;
};

class Edificio{
    public:
        bool _ascensor;
        string _nombre;
};

class Edicifio_aulas:public Edificio{
    public:
        bool _soda;
        Aula _aulas[];
};

class Edificio_parqueo:public Edificio{
    public:
};

class Finca{
    public:
        string _nombre;
        bool _bus;
        Edificio _edificios[];
};

class Campus{
    public:
        string _nombre;
        Finca _fincas[];
};

int main(void){
    cout << "Hola" << endl;
    return(0);
}
