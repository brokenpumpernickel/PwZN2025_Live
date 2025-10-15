import sys
import argparse

# print(sys.argv)

parser = argparse.ArgumentParser(description='This is a test script for argparse')
parser.add_argument('filename', help='Filename to process')
parser.add_argument('-l', '--limit', help='Length limit', type=int, default=0)
parser.add_argument('-f', '--flag', help='A boolean flag', action='store_true')
parser.add_argument('-L', '--list', help='A list of values', nargs='*')
args = parser.parse_args()

print(args)
print(f'Processing file: {args.filename}')
print(f'Applying length limit: {args.limit} {type(args.limit)}')
print(f'Flag is set to: {args.flag} {type(args.flag)}')
print(f'List of values: {args.list} {type(args.list)}')

