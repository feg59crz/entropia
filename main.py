import math

def log2(x):
    return log(x, 2)

def log(x, base):
    return math.log(x) / math.log(base)
    
def calcEntropia(dadosEntropia):
    resultEntropia = 0
    
    for i in dadosEntropia:
        if i != 0:
            resultEntropia -= i * log2(i)
    return resultEntropia
    
# teste01 = [0.2, 0.2, 0.2, 0.3, 0.1]
classes = [0.146, 0.285, 0.283, 0.078, 0.168, 0.04]

# print("Resultado Da Entropia:", round(calcEntropia(teste01),3))
print("Resultado Da Entropia:", round(calcEntropia(classes),3))
print("Resultado Da Entropia Máxima:", round(log2(6),2))
