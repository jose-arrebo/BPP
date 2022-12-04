class MaximoJugadores(Exception):
    """Clase utilizada para lanzar una excepcion
    cuando se excede el numero maximo de jugadores
    para convocar.
    
    Hereda de Exception
    """
    pass

class InsuficientesJugadores(Exception):
    """Clase utilizada para lanzar una excepcion
    cuando no hay sufucientes jugadores convocados
    para llevar a acabo la operacion.
    
    Hereda de Exception
    """
    pass

class JugadorNoConvocado(Exception):
    """Clase utilizada para lanzar una excepcion
    cuando el jugador al que se hace referencia
    no estaba previamente convocado.
    
    Hereda de Exception
    """
    pass

class ListaConvocados():
    """Clase de la lista de convocados
    
    Methods:
    
    convocar_jugador
    
    desconvocar_jugador
    
    desconvocar_ultimo
    
    desconvocar_primero
    """
    
    def __init__(self,lista=[]):
        """Metodo para inicializar los atributos.
    
        Por defecto, el atributo lista se inicializa
        como la lista vacia
        """
        self.lista = lista
    
    def convocar_jugador(self, jugador):
        """Metodo que anade el jugador deseado a
        la lista de convocados.

        Args:
        El parametro self autoreferencia el objeto.
        Se omite a la hora de llamar a la funcion.
        
        jugador (str): jugador que se quiere convocar

        La funcion modifica el atributo lista
        
        Raises:
        MaximoJugadores: lanza un error cuando no se pueden
        convocar a mas jugadores
        """
        if len(self.lista) >= 5:
            raise MaximoJugadores("No se pueden convocar a mas de 5 jugadores")
        else:
            self.lista.append(jugador)
    
    def desconvocar_jugador(self, jugador):
        """Metodo que elimina el jugador deseado de
        a la lista de convocados.

        Args:
        El parametro self autoreferencia el objeto.
        Se omite a la hora de llamar a la funcion.
        
        jugador (str): jugador que se desconvocar

        La funcion modifica el atributo lista
        
        Raises:
        InsuficientesJugadores: lanza un error cuando
        no hay jugadores para desconvocar
        
        JugadorNoConvocado: lanza un error cuando el 
        jugador que se quiere desconvocar no estaba convocado"
        """
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            if jugador not in self.lista:
                raise JugadorNoConvocado("El jugador no estaba convocado")
            else:
                self.lista.remove(jugador)
    
    def desconvocar_ultimo(self):
        """Metodo que elimina el ultimo jugador de
        a la lista de convocados.

        Args:
        El parametro self autoreferencia el objeto.
        Se omite a la hora de llamar a la funcion.

        La funcion modifica el atributo lista
        
        Raises:
        InsuficientesJugadores: lanza un error cuando
        no hay jugadores para desconvocar
        """
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            long_previa = len(self.lista)
            self.lista = self.lista[:(long_previa - 1)]
            
    def desconvocar_primero(self):
        """Metodo que elimina el primer jugador de
        a la lista de convocados.

        Args:
        El parametro self autoreferencia el objeto.
        Se omite a la hora de llamar a la funcion.

        La funcion modifica el atributo lista
        
        Raises:
        InsuficientesJugadores: lanza un error cuando
        no hay jugadores para desconvocar
        """
        if len(self.lista) == 0:
            raise InsuficientesJugadores("No hay jugadores para desconvocar")
        else:
            self.lista = self.lista[1:]