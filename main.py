#! /usr/bin/python
import sys
import argparse

VERSION="1.0"

def ShowVersion(output=''):
        print("Version: %s" % (VERSION))

def main():
    parser = argparse.ArgumentParser(description='Template python appliction')
    parser.add_argument('--version', action='store_true', help='Displays the application version')

    args = parser.parse_args()

    if args.version:
        ShowVersion()

if __name__ == '__main__':
    main()
