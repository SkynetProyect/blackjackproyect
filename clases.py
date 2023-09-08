import random


class Carta:
    def __init__(self, pinta: str, valor: int, tapada: bool):
        self.pinta = pinta
        self.valor = valor
        self.tapada = tapada

    def visible(self, tapada: bool):
        self.tapada = tapada


class Mano:
    def __init__(self, carta_uno: Carta, carta_dos: Carta):
        self.cartas_en_mano: list = []
        self.cartas_en_mano.append(carta_uno)
        self.cartas_en_mano.append(carta_dos)

    def pedir_carta(self, carta: Carta):
        self.cartas_en_mano.append(carta)

    def calcular_valor(self) -> int:
        contador = 0
        for i in self.cartas_en_mano:
            contador += i.valor
        return contador

    def es_blackjack(self):
        if self.calcular_valor() == 21:
            return True
        else:
            return False


class Baraja:
    def __init__(self):
        self.lista_cartas: list = \
            [("A", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
             ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 10),
             ("Q", 10), ("K", 10)]

    def revolver(self):
        random.shuffle(self.lista_cartas)

    def repartir_carta(self, tapada: bool):
        seleccion = random.choice(self.lista_cartas)
        carta: Carta = Carta(seleccion[0], seleccion[1], tapada)
        return carta


class Casa:
    def __init__(self):
        self.baraja: Baraja = Baraja()
        self.baraja.revolver()

    def iniciar_mano(self):
        self.mano: Mano = Mano(self.baraja.repartir_carta(False), self.baraja.repartir_carta(True))


class Jugador:
    def __init__(self, nombre_jugador: str):
        self.nombre_jugador = nombre_jugador
        self.fichas: int = 100
        self.baraja: Baraja = Baraja()

    def revolver(self):
        self.baraja.revolver()

    def iniciar_mano(self):
        self.mano: Mano = Mano(self.baraja.repartir_carta(False), self.baraja.repartir_carta(False))

    def solicitar_carta(self):
        carta = self.baraja.repartir_carta(False)
        self.mano.pedir_carta(carta)

    def calcular_valor(self):
        llave: bool = self.mano.es_blackjack()
        if not llave:
            return self.mano.calcular_valor()

class Apuesta:
    def __init__(self, apuesta: int):
        self.apuesta = apuesta


class Blackjack:
    def registrar_jugador(self, nombre_jugador: str):
        self.jugador: Jugador = Jugador(nombre_jugador)

    def iniciar_juego(self, apuesta: int):
        self.apuesta: Apuesta = Apuesta(apuesta)
