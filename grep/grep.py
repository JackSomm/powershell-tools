"""
Replica of the grep command
"""
import argparse
import os
import glob
import re

def main():
    """
    grep functionality
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('regex', type=str, nargs='?', help="A string to search for")
    parser.add_argument('file', type=str, nargs='?', help="File to search in")

    args = parser.parse_args()

    files = glob.glob(f'{args.file}')

    for file in files:
        if os.path.exists(file):
            with open(file, encoding='utf-8') as in_file:
                contents = in_file.read().splitlines()
                re_text = [re.findall(fr'{args.regex}', line) for line in contents]
                print(re_text)
        else:
            print('File not found.')

if __name__ == '__main__':
    main()