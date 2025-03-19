import math

def isCorrectFormat(wymiary: list) ->bool:
    for i in wymiary:
        if i<=0:
            return False
    return True

def oblicz_pole(figura: str, wymiary: list, oblicz_obwod: bool) -> list :
    area = 0
    perimeter = 0
    result = []
    if not isCorrectFormat(wymiary):
        result.append(0)
        if oblicz_obwod:
            result.append(0)
    else:
        if figura == "kwadrat":
            area = wymiary[0]*wymiary[0]
            perimeter = 4*wymiary[0]
        elif figura == "prostokat":
            area = wymiary[0]*wymiary[1]
            perimeter = 2*wymiary[0]+2*wymiary[1]
        elif figura == "kolo":
            area = math.pi*wymiary[0]**2
            perimeter = 2*math.pi*wymiary[0]
        else:
            area = 0
            perimeter = 0
        result.append(area)
        if oblicz_obwod:
            result.append(perimeter)
    return result
