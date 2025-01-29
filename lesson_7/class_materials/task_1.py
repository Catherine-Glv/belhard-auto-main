def avg(ranks):
    assert len(ranks) !=0, f'Ожидали пустой список - {ranks}, вернулся список длиной {len(ranks)}' # проверка ожидаемого ответа и фактического результата
    return sum(ranks) / len(ranks)

ranks = [40, 41, 42]
ranks = []
print(f'Среднее арифметическое списка {avg(ranks=ranks)}')