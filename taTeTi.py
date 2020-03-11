import pytest

# Representaremos cada columna del tablero como una lista, las cuales formaran
# parte de una lista general llamada tablero. Siendo:

#            A     B      C
#               |     |
#       1       |     |
#          _____|_____|______
#               |     |
#       2       |     |
#          _____|_____|_____
#               |     |
#       3       |     |
#               |     |

# tablero = [[A1, A2, A3], [B1, B2, B3], [C1, C2, C3]]
# Reglas:
# · El juego esta echo para 2 personas.
# · El tablero esta creado con 4 lineas entrecruzadas, creando un espacio de
#   9 casillas.
# · Cada jugador maneja 2 tipos de fichas diferente, siendo:
#       * Jugador 1: Utiliza la ficha X.
#       * Jugador 2: Utiliza la ficha O.
# · Se coloca por turno una ficha en cualquier casilla del tablero.
#   PD: No se puede colocar una ficha encima de una casilla donde esta colocada
#   una ficha tuya o del adversario.
# · Cuando alguno de los jugadores logra tener 3 fichas propias en una misma
#   linea, ya sea vertical, horizontal o diagonal, gana la partida.
# tatetiPlay: Str -> Str
# Ingresa en que posicion desea colocar la ficha y devuelve la ficha colocada en
# el tablero. Si las 3 fichas de un mismo jugador estan colocadas de manera
# vertical, horizontal o diagonal, devuelve un mensaje indicando que jugador
# gano.
def tatetiPlay(tateti=[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]):
    """Tenes que llenar con 3 fichas propias 3 casillas de la misma linea para ganar, ya sean vertixales, horizontales o diagonales."""
    repetir = 0
    repetir2 = 0
    tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    print(" ____________________________________________________________________")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|    ____________          _____________          _____________      |")
    print("|         |                      |        _____         |            |")
    print("|         |         /\           |       |              |       *    |")
    print("|         |        /  \   _____  |       |_____  _____  |       |    |")
    print("|         |       /----\         |       |              |       |    |")
    print("|         |      /      \        |       |_____         |       |    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                    * Ingrese J para comenzar a jugar.              |")
    print("|                                                                    |")
    print("|                    * Ingrese R para leer las reglas.               |")
    print("|                                                                    |")
    print("|                    * Ingrese S para salir.                         |")
    print("|____________________________________________________________________|")
    opcion = input("Ingrese que opcion desea realizar: ")
    if "R" == opcion or "r" == opcion:
        print("Reglas: \n · El juego esta echo para 2 personas. ")
        print(" · El tablero esta creado con 4 lineas entrecruzadas, creando un espacio de \n 9 casillas.")
        print(" · Cada jugador maneja 2 tipos de fichas diferente, siendo: \n       * Jugador 1: Utiliza la ficha X. \n       * Jugador 2: Utiliza la ficha O.")
        print(" · Se coloca por turno una ficha en cualquier casilla del tablero. \n PD: No se puede colocar una ficha encima de una casilla donde esta colocada \n una ficha tuya o del adversario.")
        print(" · Cuando alguno de los jugadores logra tener 3 fichas propias en una misma \n linea, ya sea vertical, horizontal o diagonal, gana la partida.")
        print(" PD: CUANDO SE DESEE COLOCAR EN UN FICHA EN UNA CASILLA, HACERLO UTILIZANDO UN \n PAR ORDENADO, POR EJEMPLO: B1 o C3.")
        return tatetiPlay()
    elif "S" == opcion or "s" == opcion:
        exit()
    elif "J" == opcion or "j" == opcion:
        terminar = 0
        while terminar != 1:
            print("            A     B      C ")
            print("               |     |")
            print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
            print("         ______|_____|______")
            print("               |     |")
            print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
            print("         ______|_____|______")
            print("               |     |")
            print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
            print("               |     |")
            while repetir != 1:
                repetir = 0
                piezaJ1 = input("Ingrese una ficha Jugador X: ").upper()
                if piezaJ1 == "A1" or piezaJ1 == "1A":
                    tateti[0][0:1] = ["X"]
                    repetir = 1
                elif piezaJ1 == "B1" or piezaJ1 == "1B":
                    tateti[1][0:1] = ["X"]
                    repetir = 1
                elif piezaJ1 == "C1" or piezaJ1 == "1C":
                    tateti[2][0:1] = ["X"]
                    repetir = 1
                elif piezaJ1 == "A2" or piezaJ1 == "2A":
                    tateti[0][1:2] = ["X"]
                    repetir = 1
                elif piezaJ1 == "B2" or piezaJ1 == "2B":
                    tateti[1][1:2] = ["X"]
                    repetir = 1
                elif piezaJ1 == "C2" or piezaJ1 == "2C":
                    tateti[2][1:2] = ["X"]
                    repetir = 1
                elif piezaJ1 == "A3" or piezaJ1 == "3A":
                    tateti[0][2:3] = ["X"]
                    repetir = 1
                elif piezaJ1 == "B3" or piezaJ1 == "3B":
                    tateti[1][2:3] = ["X"]
                    repetir = 1
                elif piezaJ1 == "C3" or piezaJ1 == "3C":
                    tateti[2][2:3] = ["X"]
                    repetir = 1
                else:
                    repetir = 0
                if (tateti[0][0] == "X" and tateti[1][1] == "X" and tateti[2][2] == "X") or (tateti[0][0] == "X" and tateti[1][0] == "X" and tateti[2][0] == "X") or (tateti[0][1] == "X" and tateti[1][1] == "X" and tateti[2][1] == "X") or (tateti[0][2] == "X" and tateti[1][2] == "X" and tateti[2][2] == "X") or (tateti[0][0] == "X" and tateti[0][1] == "X" and tateti[0][2] == "X") or (tateti[1][0] == "X" and tateti[1][1] == "X" and tateti[1][2] == "X") or (tateti[2][0] == "X" and tateti[2][1] == "X" and tateti[2][2] == "X") or (tateti[2][0] == "X" and tateti[1][1] == "X" and tateti[0][2] == "X"):
                    print("            A     B      C ")
                    print("               |     |")
                    print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
                    print("               |     |")
                    return "GANADOR: JUGADOR 1"
                elif (tateti[0][0] == "X" or tateti[0][0] == "O") and (tateti[1][0] == "X" or tateti[1][0] == "O") and (tateti[2][0] == "X" or tateti[2][0] == "O") and (tateti[0][1] == "X" or tateti[0][1] == "O") and (tateti[1][1] == "X" or tateti[1][1] == "O") and (tateti[2][1] == "X" or tateti[2][1] == "O") and (tateti[0][2] == "X" or tateti[0][2] == "O") and (tateti[1][2] == "X" or tateti[1][2] == "O") and (tateti[2][2] == "X" or tateti[2][2] == "O"):
                    print("            A     B      C ")
                    print("               |     |")
                    print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
                    print("               |     |")
                    return "EMPATE"
            print("            A     B      C ")
            print("               |     |")
            print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
            print("         ______|_____|______")
            print("               |     |")
            print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
            print("         ______|_____|______")
            print("               |     |")
            print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
            print("               |     |")
            repetir = 0
            while repetir2 != 1:
                repetir2 = 0
                piezaJ2 = input("Ingrese una ficha Jugador O: ").upper()
                if piezaJ2 == "A1" or piezaJ2 == "1A":
                    tateti[0][0:1] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "B1" or piezaJ2 == "1B":
                    tateti[1][0:1] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "C1" or piezaJ2 == "1C":
                    tateti[2][0:1] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "A2" or piezaJ2 == "2A":
                    tateti[0][1:2] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "B2" or piezaJ2 == "2B":
                    tateti[1][1:2] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "C2" or piezaJ2 == "2C":
                    tateti[2][1:2] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "A3" or piezaJ2 == "3A":
                    tateti[0][2:3] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "B3" or piezaJ2 == "3B":
                    tateti[1][2:3] = ["O"]
                    repetir2 = 1
                elif piezaJ2 == "C3" or piezaJ2 == "3C":
                    tateti[2][2:3] = ["O"]
                    repetir2 = 1
                else:
                    repetir2 = 0
                if (tateti[0][0] == "O" and tateti[1][1] == "O" and tateti[2][2] == "O") or (tateti[0][0] == "O" and tateti[1][0] == "O" and tateti[2][0] == "O") or (tateti[0][1] == "O" and tateti[1][1] == "O" and tateti[2][1] == "O") or (tateti[0][2] == "O" and tateti[1][2] == "O" and tateti[2][2] == "O") or (tateti[0][0] == "O" and tateti[0][1] == "O" and tateti[0][2] == "O") or (tateti[1][0] == "O" and tateti[1][1] == "O" and tateti[1][2] == "O") or (tateti[2][0] == "O" and tateti[2][1] == "O" and tateti[2][2] == "O") or (tateti[2][0] == "O" and tateti[1][1] == "O" and tateti[0][2] == "O"):
                    print("            A     B      C ")
                    print("               |     |")
                    print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
                    print("               |     |")
                    return "GANADOR: JUGADOR 2"
                elif (tateti[0][0] == "X" or tateti[0][0] == "O") and (tateti[1][0] == "X" or tateti[1][0] == "O") and (tateti[2][0] == "X" or tateti[2][0] == "O") and (tateti[0][1] == "X" or tateti[0][1] == "O") and (tateti[1][1] == "X" or tateti[1][1] == "O") and (tateti[2][1] == "X" or tateti[2][1] == "O") and (tateti[0][2] == "X" or tateti[0][2] == "O") and (tateti[1][2] == "X" or tateti[1][2] == "O") and (tateti[2][2] == "X" or tateti[2][2] == "O"):
                    print("            A     B      C ")
                    print("               |     |")
                    print("      1   ",tateti[0][0] , "  | ", tateti[1][0], " | ", tateti[2][0] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      2   ",tateti[0][1] , "  | ", tateti[1][1], " | ", tateti[2][1] )
                    print("         ______|_____|______")
                    print("               |     |")
                    print("      3   ",tateti[0][2] , "  | ", tateti[1][2], " | ", tateti[2][2] )
                    print("               |     |")
                    return "EMPATE"
            repetir2 = 0
    else:
        tatetiPlay()








def test_tatetiPlay():
    assert tatetiPlay([["X", "X", "X"], ["O", [], "O"], [[], [], "O"]]) == "El ganador es el Jugador X"
    assert tatetiPlay([["O", "X", "X"], ["O", "X", []], ["O", [], []]]) == "El ganador es el Jugador O"
    assert tatetiPlay([["O", "O", "X"], ["O", "X", []], ["X", [], []]]) == "El ganador es el Jugador X"

