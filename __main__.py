import os

from os import system
from sys import argv
from glob import glob


def main():
    codeon_number = int(argv[1])

    print(f"\033[1m# 코드온 {codeon_number}번 문제\033[0m")

    files = search_files(codeon_number)
    
    for file, ext in files:
        if ext == "py":
            run_python(file)


def search_files(number: int) -> list:
    files = []
    for path in glob(f"**/{number}.*", recursive=True):
        if os.path.isfile(path):
            ext = os.path.splitext(path)[-1][1:]
            files.append([path, ext])
    return files


def run_python(path: str):
    system(f"python3 -d {path}")


if __name__ == "__main__":
    main()
