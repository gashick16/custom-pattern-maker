from pattern_maker import make_pattern


def to_svg(rows, cell=10, fill="#333"):
    height = len(rows)
    width = len(rows[0]) if rows else 0
    rects = []
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch != " ":
                rects.append(
                    f'<rect x="{x * cell}" y="{y * cell}" '
                    f'width="{cell}" height="{cell}" fill="{fill}"/>'
                )
    body = "\n  ".join(rects)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{width * cell}" height="{height * cell}">\n  {body}\n</svg>')


def save_svg(rows, path="pattern.svg", **kwargs):
    with open(path, "w", encoding="utf-8") as f:
        f.write(to_svg(rows, **kwargs))