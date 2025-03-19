
class PionekSzachowy():
    def __init__(self,color: bool, position: str) -> None:
        self.color = color
        self.position = position
        self.didMove = False
    
    def mozliwe_ruchy(self) -> list:
        result = []
        if self.color:
            pos_int = int(self.position[1])
            if pos_int+1 <= 8:
                result.append(self.position[0] + str(pos_int +1))
            if not self.didMove:
                result.append(self.position[0] + str(pos_int +2))
        else:
            pos_int = int(self.position[1])
            if pos_int-1 >= 0:
                result.append(self.position[0] + str(pos_int -1))
            if not self.didMove:
                result.append(self.position[0] + str(pos_int -2))
        return result

test = PionekSzachowy(True,"E1")
print(test.mozliwe_ruchy())