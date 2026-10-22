import argparse
from pattern_maker import make_pattern, print_pattern, VALID_PATTERNS


def main():
    parser = argparse.ArgumentParser(description="Конструктор паттернов")
    parser.add_argument("--kind", default="stripes", choices=VALID_PATTERNS)
    parser.add_argument("--size", type=int, default=10)
    parser.add_argument("--symbol", default="#")
    args = parser.parse_args()
    print_pattern(make_pattern(args.kind, args.size, args.symbol))


if __name__ == "__main__":
    main()