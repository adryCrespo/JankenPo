## Juego2.py
# Este archivo es para la version con tkinker
class jugador(object):
    def __init__(self, nombre="anonimo") -> None:
        self.nombre = nombre
        self.jugada = None
 

        

    def set_eleccion(self,jugada) -> None:
        self.jugada = jugada
        return None
    
    def get_eleccion(self) -> str:
        return self.jugada

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self,nombre) -> None:
        self.nombre = nombre
        return None
    
class NPC(jugador):
    """
    NPC que selecciona una de las opciones aleatoriamente
    """
    def __init__(self) -> None:
        self.set_nombre("NPC")
    
    def eleccion(self) -> None:
        """
        NPC elige una opcion aleatoriamente
        """
        elecciones = {"Piedra", "Papel", "Tijera"}
        from random import choice
        self.jugada= choice(list(elecciones) )
        print("NPC ha elegido "+self.jugada)

        return None
    
class partida():  
        def __init__(self,jugador_humano,NPC) -> None:
            self.elecciones =["Piedra", "Papel", "Tijera"]
            self.resultado = None
            self.player1 = None
            self.player2 = None
            self.jugar_partida(jugador_humano,NPC)
            # self.post_partida(jugador_humano,NPC )
            self.resumen_partida(jugador_humano,NPC)

        def pre_juego(self,jugador1)-> None:
            "'calculos previos para poner todo en order'"
            if jugador1 == "Piedra":
                self.elecciones = self.elecciones[-1:]+self.elecciones[:-1]
            elif jugador1 == "Tijera":
                self.elecciones = self.elecciones[1:]+ self.elecciones[0:1]
            return None

        def ganador(self,numero1, numero2)->None:
            if numero1 == numero2: self.resultado = "empate"
            elif numero1 > numero2: self.resultado = "jugador 1"
            elif numero1 < numero2: self.resultado = "jugador 2"
            return None
        
        def set_jugada_Player(self,jugada1,jugada2)-> None:
            """ escribes la jugada del jugardor 1 y 2"""
            self.player1 = jugada1
            self.player2 = jugada2
            return None


        def jugar_partida(self,jugador_humano,NPC )-> None:
 
            NPC.eleccion()
            self.pre_juego( jugador_humano.get_eleccion() )
            jugador1 = self.elecciones.index(jugador_humano.get_eleccion() )
            jugador2 = self.elecciones.index( NPC.get_eleccion() )
            self.ganador(jugador1,jugador2)
            self.set_jugada_Player(jugador1,jugador2)
            return None

        def resumen_partida(self,jugador_humano,NPC):
            print("jugada Jugador 1: " + jugador_humano.get_eleccion())
            print("jugada Jugador 2: " + NPC.get_eleccion())
            print("ganador: " + self.resultado)
            return None

        def get_resultado(self):
            return self.resultado


if __name__ == "__main__":

    jugador = jugador("Adr")
    jugador.set_eleccion("Papel")
    robot = NPC()
    play = partida(jugador,robot)
    