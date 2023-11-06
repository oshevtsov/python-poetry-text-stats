from argparse import ArgumentParser

from text_stats.stats import count_characters, count_lines, count_words


def run():
    parser = ArgumentParser(description="Count character, words, lines in a text file")
    parser.add_argument("input", help="Text input")
    parser.add_argument("-c", "--characters", action="store_true", help="Count characters")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")

    args = parser.parse_args()

    if args.characters:
        print(f"Number of characters: {count_characters(args.input)}")
    if args.words:
        print(f"Number of words: {count_words(args.input)}")
    if args.lines:
        print(f"Number of lines: {count_lines(args.input)}")


if __name__ == "__main__":
    run()
