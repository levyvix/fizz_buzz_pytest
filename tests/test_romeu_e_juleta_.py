from codigo.romeu_julieta import romeu_julieta


def test_romeu_julieta():
    pass


def test_romeu_juleta_multiplo_5_goiabada():
    assert romeu_julieta(10) == "Goiabada"


def test_romeu_juleta_multiplo_3_queijo():
    assert romeu_julieta(3) == "Queijo"
