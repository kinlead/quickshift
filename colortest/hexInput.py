import colorprocessing

listL = [0.0, 1.041666666666667, -1.041666666666667, -1.0416666666666665, 1.0416666666666665, 1.0416666666666672, -1.0416666666666672, -1.0416666666666667, 1.0416666666666667, 1.041666666666666, -1.041666666666666, -1.0416666666666665, 1.0416666666666665, 0.0]
hexList = (colorprocessing.listDeterminer(listL))
hexListA = []
for i in hexList:
    hexListA.append(i.zfill(6))
print(hexListA)
