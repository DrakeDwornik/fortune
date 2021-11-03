#! /bin/python3
from random import randrange
import sys


def open_file(file_name: str = "fortunedat.txt", file_path: str = "") -> object:
    try:
        fortune_file = open(file_path+file_name,"r")
    except:
        print("unable to open file, sorry")
        exit(1)
    else:
        return fortune_file


if __name__ == "__main__":
    fortunes_list = []
    with open_file() as fortune_file:
        fortune = ""
        for line in fortune_file:
            if line != "%\n":
                fortune += line
            else:
                fortunes_list.append(fortune)
                fortune = ""
    number_of_fortunes = len(fortunes_list)
    i_fortune_to_read = randrange(0, number_of_fortunes - 1)
    fortune_to_read = fortunes_list[i_fortune_to_read]
    print(fortune_to_read)


