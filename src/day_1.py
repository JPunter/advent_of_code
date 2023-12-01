

def _parse_line(calibration: str) -> int:
    for i in range(0, len(calibration)):
        if calibration[i].isnumeric():
            coord = calibration[i]
            break
    for i in range(len(calibration) - 1, -1, -1):
        if calibration[i].isnumeric():
            coord += calibration[i]
            break
    return int(coord)


def run(calibrations: list) -> int:
    coordinates = 0
    for calibration in calibrations:
        coordinates += _parse_line(calibration)

    return coordinates


if __name__ == '__main__':
    inp = open('data/day_1.txt').read().split('\n')

    print(run(inp))