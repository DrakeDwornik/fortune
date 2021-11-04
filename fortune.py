#! /bin/python3
from random import randrange

class FortuneTeller():
"""
Parses a text file with fortunes delimited but lines containing only a '%' character
and returns a random fortune
"""
    def __init__(self,fortune_file: str = "fortunedat.txt", file_path: str = ""):
        self.fortune_file = fortune_file
        self.fortune_path = fortune_path

    def open_file(self,file_name: str, file_path: str = ""):
        """"""
        try:
            fortune_file = open(file_path+file_name, "r")
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
    i_fortune_to_read = randrange(0, number_of_fortunes)
    fortune_to_read = fortunes_list[i_fortune_to_read]
    print(fortune_to_read)
