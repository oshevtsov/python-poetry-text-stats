from argparse import ArgumentParser

import print_color

from text_stats.stats import count_characters, count_lines, count_words


def run():
    parser = ArgumentParser(description="Count character, words, lines in a text file")
    parser.add_argument("input", help="Text input")
    parser.add_argument("-c", "--characters", action="store_true", help="Count characters")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")

    args = parser.parse_args()

    if any([args.characters, args.words, args.lines]):
        print_color.print("Input stats:", format="bold")
    if args.characters:
        print_color.print(count_characters(args.input), tag="chars", tag_color="green")
    if args.words:
        print_color.print(count_words(args.input), tag="words", tag_color="yellow")
    if args.lines:
        print_color.print(count_lines(args.input), tag="lines", tag_color="red")


if __name__ == "__main__":
    run()
