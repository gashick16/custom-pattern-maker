import math

VALID_PATTERNS = ("stripes", "checker","waves")


def make_pattern(kind="stripes", size=10, symbol="#"):
    """Возвращает список строк с паттерном указанного вида."""
    if kind not in VALID_PATTERNS:
        raise ValueError(f"Неизвестный паттерн: {kind}")
    if size < 2:
        raise ValueError("Размер должен быть не меньше 2")

    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            if kind == "stripes":
                on = (x // 2) % 2 == 0
            else:  # checker
                on = (x + y) % 2 == 0
            row.append(symbol if on else " ")
        rows.append("".join(row))
    return rows


def print_pattern(rows):
    for row in rows:
        print(row)