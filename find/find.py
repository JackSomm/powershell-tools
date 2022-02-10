"""
Copy of the find command. Missing lots of args
"""
import argparse
import os
import glob
import sys

def main():
    """
    Main find functionality
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, default='/usr/local', nargs='?',
                        help='Path to directory.')
    parser.add_argument('-name', type=str, help='name of file')
    parser.add_argument('-type', type=str, help='type of object to look for, either "d" or "f"')
    parser.add_argument('-print', action='store_true', help='prints file')

    args = parser.parse_args()

    if os.path.exists(args.dir):
        if args.name:
            files = glob.glob(f'{args.dir}/{args.name}')
        elif args.type:
            files = glob.glob(f'{args.dir}/*')
            if args.type not in ['d', 'f']:
                print('Could not find that type.')
                sys.exit(1)
            elif args.type == 'd':
                directories = glob.glob('*/')
                for directory in directories:
                    print(directory)
            elif args.type == 'f':
                for file in files:
                    print(file)

        if args.print:
            for file in files:
                with open(file, encoding='utf-8', errors='ignore') as in_file:
                    print(in_file.read())

if __name__ == '__main__':
    main()
