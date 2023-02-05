from typing import Union, List


def romeu_julieta(numero: List[int]) -> List[Union[str, int]]:

    if not isinstance(numero, list):
        raise TypeError("O parâmetro deve ser uma lista")

    res = []
    for n in numero:
        if not isinstance(n, int):
            raise TypeError("Os elementos da lista devem ser inteiros")
        if n % 3 == 0:
            res.append("Romeu e Julieta" if n % 5 == 0 else "Queijo")
        else:
            res.append("Goiabada" if n % 5 == 0 else n)

    return res


if __name__ == "__main__":
    resultado = romeu_julieta(900)
    print(resultado)
