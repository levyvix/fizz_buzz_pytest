from typing import *


def romeu_julieta(numero: int) -> Union[str, int]:

    if numero % 3 == 0:
        return "Romeu e Julieta" if numero % 5 == 0 else "Queijo"
    return "Goiabada" if numero % 5 == 0 else numero


if __name__ == "__main__":
    resultados = [(numero, romeu_julieta(numero)) for numero in range(1, 101)]
    print(resultados)
