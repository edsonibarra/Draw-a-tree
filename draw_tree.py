import argparse


def draw_tree(height: int) -> None:
    """
    It prints out a tree based on the height
    and repeting characters from WORD.
    """
    WORD = "CAR"
    word_len = len(WORD)
    
    for i in range(1, height + 1):
        side_length = i - 1
        left_part = ''.join(WORD[(side_length - j) % word_len] for j in range(side_length))
        right_part = ''.join(WORD[(j + 1) % word_len] for j in range(side_length))   
        row = left_part + 'C' + right_part
        space = ' ' * (height - i)
        print(space + row + space)


def main():
    parser = argparse.ArgumentParser(description="Draw a tree using a repeating word pattern.")
    parser.add_argument('--height', type=int, required=True, help="Height of the tree")
    args = parser.parse_args()
    draw_tree(args.height)

if __name__ == "__main__":
    main()
