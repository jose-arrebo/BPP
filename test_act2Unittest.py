import unittest
from act2BPP import ListaConvocados, MaximoJugadores, InsuficientesJugadores, JugadorNoConvocado

class TestLista(unittest.TestCase):
    
    def test_convocar(self):
        mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
        mi_lista.convocar_jugador("Xavi Hernandez")
        self.assertEqual(mi_lista.lista, ["Sergio Ramos", "Iker Casillas", "Xavi Hernandez"])

    def test_convocar2(self):
        mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas",
                                    "David Villa", "Jesus Navas",
                                    "Xavi Alonso"])
        self.assertRaises(MaximoJugadores, mi_lista.convocar_jugador, "Xavi Hernandez")
            
    def test_desconvocar(self):
        mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
        mi_lista.desconvocar_jugador("Iker Casillas")
        self.assertEqual(mi_lista.lista, ["Sergio Ramos"])

    def test_desconvocar2(self):
        mi_lista = ListaConvocados()
        self.assertRaises(InsuficientesJugadores, mi_lista.desconvocar_jugador, "Iker Casillas")


    def test_desconvocar3(self):
        mi_lista = ListaConvocados(["Sergio Ramos"])
        self.assertRaises(JugadorNoConvocado, mi_lista.desconvocar_jugador, "Iker Casillas")
            
    def test_ultimo(self):
        mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
        mi_lista.desconvocar_ultimo()
        self.assertEqual(mi_lista.lista, ["Sergio Ramos"])
        
    def test_ultimo2(self):
        mi_lista = ListaConvocados()
        self.assertRaises(InsuficientesJugadores, mi_lista.desconvocar_ultimo)

    def test_primero(self):
        mi_lista = ListaConvocados(["Sergio Ramos", "Iker Casillas"])
        mi_lista.desconvocar_primero()
        self.assertEqual(mi_lista.lista, ["Iker Casillas"])
        
    def test_primero2(self):
        mi_lista = ListaConvocados()
        self.assertRaises(InsuficientesJugadores, mi_lista.desconvocar_primero)