import argparse
import os.path

def main():
    parser = argparse.ArgumentParser(description='cat Clone')
    parser.add_argument('files', metavar='F', type=str, nargs='+')

    args = parser.parse_args()

    for file in args.files:
        if os.path.exists(file):
            with open(file, encoding='utf-8') as in_file:
                contents = in_file.read()
                print(contents)
        else:
            print('File not found.')


if __name__ == '__main__':
    main()