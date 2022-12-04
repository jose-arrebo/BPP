class MaximoJugadores(Exception):
    pass

class InsuficientesJugadores(Exception):
    pass

class JugadorNoConvocado(Exception):
    pass

class ListaConvocados():
    
    def __init__(self,lista=[]):
        self.lista = lista
    
    def convocar_jugador(self, jugador):
        if len(self.lista) >= 5:
            raise MaximoJugadores("No se pueden convocar a mas de 5 jugadores")
        else:
            self.lista.append(jugador)
    
    def desconvocar_jugador(self, jugador):
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            if jugador not in self.lista:
                raise JugadorNoConvocado("El jugador no estaba convocado")
            else:
                self.lista.remove(jugador)
    
    def desconvocar_ultimo(self):
        '''Esta funcion desconvoca al ultimo
        jugador de la lista de convocados'''
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            long_previa = len(self.lista)
            self.lista = self.lista[:(long_previa - 1)]
            
    def desconvocar_primero(self):
        '''Esta funcion desconvoca al primer
        jugador de la lista de convocados'''
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            self.lista = self.lista[1:]
        