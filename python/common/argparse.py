import argparse


def parse_args():

    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')

    # positional argument
    parser.add_argument('filename')
    # option that takes a value
    parser.add_argument('-c', '--count', type=int, default=1)
    # on/off flag
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()
