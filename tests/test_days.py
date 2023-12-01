from src import day_1

def test_day_1():
    inp = open('data/day_1_inp.txt').read().split('\n')
    exp = open('data/day_1_exp.txt').read()
    by_line_exp = open('data/day_1_by_line_exp.txt').read().split('\n')

    for i, line in enumerate(inp):
        assert day_1._parse_line(line) == int(by_line_exp[i])

    assert day_1.run(inp) == int(exp)