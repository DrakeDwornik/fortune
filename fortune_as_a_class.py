#! /bin/python3
from random import randrange


class FortuneTeller:
    """
    Parses a text file with fortunes delimited but lines containing only a '%' character
    and returns a random fortune
    """

    def __init__(self, fortune_file: str = "fortunedat.txt", file_path: str = ""):
        self.fortune_file = fortune_file
        self.fortune_path = file_path
        self.fortunes_list = []
        self.number_of_fortunes = 0
        self.create_fortune_list()

    def open_file(self, file_name: str, file_path: str):
        """
        Opens a returning a file handler object
        :param file_name: str #file to be opened
        :param file_path: str #path if file is located somewhere else
        :return: file handler
        """
        try:
            fortune_file = open(file_path + file_name, "r")
        except:
            print("unable to open file, sorry")
            exit(1)
        else:
            return fortune_file

    def create_fortune_list(self):
        """
        Iterates a file line by line creating a list of fortunes split on lines with containing only a '%' character
        :return: N/A
        """
        self.fortunes_list = []
        with self.open_file(self.fortune_file, self.fortune_path) as fortunes_file:
            fortune = ""
            for line in fortunes_file:
                if line != "%\n":
                    fortune += line
                else:
                    self.fortunes_list.append(fortune)
                    fortune = ""
        self.number_of_fortunes = len(self.fortunes_list)

    def print_fortune(self):

        i_fortune_to_read = randrange(0, self.number_of_fortunes)
        fortune_to_read = self.fortunes_list[i_fortune_to_read]
        print(fortune_to_read)

    def append_fortune_list(self):
        """
        Iterates a file line by line creating a list of fortunes split on lines with containing only a '%' character
        clears existing list before loading

        Appends to an existing fortunes_list
        :return: N/A
        """
        with self.open_file(self.fortune_file, self.fortune_path) as fortunes_file:
            fortune = ""
            for line in fortunes_file:
                if line != "%\n":
                    fortune += line
                else:
                    self.fortunes_list.append(fortune)
                    fortune = ""
        self.number_of_fortunes = len(self.fortunes_list)
if __name__ == "__main__":
    fortune_teller = FortuneTeller()
    fortune_teller.print_fortune()
