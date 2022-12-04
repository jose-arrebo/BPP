import pytest
from act2BPP import ListaConvocados, MaximoJugadores, InsuficientesJugadores, JugadorNoConvocado

def test_convocar():
    mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
    mi_lista.convocar_jugador("Xavi Hernandez")
    assert mi_lista.lista == ["Sergio Ramos", "Iker Casillas", "Xavi Hernandez"]

def test_convocar2():
    mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas",
                                "David Villa", "Jesus Navas",
                                "Xavi Alonso"])
    with pytest.raises(MaximoJugadores):
        mi_lista.convocar_jugador("Xavi Hernandez")
        
def test_desconvocar():
    mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
    mi_lista.desconvocar_jugador("Iker Casillas")
    assert mi_lista.lista == ["Sergio Ramos"]

def test_desconvocar2():
    mi_lista = ListaConvocados()
    with pytest.raises(InsuficientesJugadores):
        mi_lista.desconvocar_jugador("Iker Casillas")

def test_desconvocar3():
    mi_lista = ListaConvocados(["Sergio Ramos"])
    with pytest.raises(JugadorNoConvocado):
        mi_lista.desconvocar_jugador("Iker Casillas")
        
def test_ultimo():
    mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
    mi_lista.desconvocar_ultimo()
    assert mi_lista.lista == ["Sergio Ramos"]
    
def test_ultimo2():
    mi_lista = ListaConvocados()
    with pytest.raises(InsuficientesJugadores):
        mi_lista.desconvocar_ultimo()

def test_primero():
    mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
    mi_lista.desconvocar_primero()
    assert mi_lista.lista == ["Iker Casillas"]
    
def test_primero2():
    mi_lista = ListaConvocados()
    with pytest.raises(InsuficientesJugadores):
        mi_lista.desconvocar_primero()