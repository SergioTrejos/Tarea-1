#include <stdio.h>
#include <iostream>

using namespace std;

class Aula{
    public:
        int _piso;
        int _identificador;
        int _pupitres;
        bool _proyector;
    Aula(int piso, int identificador, int pupitres, bool proyector){
        _piso = piso;
        _identificador = identificador;
        _pupitres = pupitres;
        _proyector = proyector;
    };
};

class Edificio{
    public:
        bool _ascensor;
        string _nombre;
    Edificio(bool ascensor, string nombre){
        _ascensor = ascensor;
        _nombre = nombre;
    }
};

class Edicifio_aulas:public Edificio{
    public:
        bool _soda;
        Aula* _aulas;
    Edicifio_aulas(bool soda, Aula* aulas, bool ascensor, string nombre):Edificio(ascensor, nombre){
        _soda = soda;
        this -> _aulas = aulas;
    };
};

class Edificio_parqueo:public Edificio{
    public:
};

class Finca{
    public:
        string _nombre;
        bool _bus;
        Edificio* _edificios;
    Finca(string nombre, bool bus, Edificio* edificios, bool ascensor){
        _nombre = nombre;
        _bus = bus;
        this -> _edificios = edificios;
    };
};

class Campus{
    public:
        string _nombre;
        Finca* _fincas;
    Campus(string nombre, Finca* fincas){
        _nombre = nombre;
        this -> _fincas = fincas;
    }
};

int main(void){
    cout << "Hola" << endl;
    return(0);
}
