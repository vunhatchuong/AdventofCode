import enum

file = open("./input/Day02.in","r",encoding="UTF-8").read().splitlines()

class RPC(str,enum.Enum):
    X = 1
    Y = 2
    Z = 3

    def __init__(self,file) -> None:
        self.file: list[str] = file

    def find_winner(self):
        pass

print(file)
