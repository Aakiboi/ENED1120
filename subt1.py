def barcodeCheck(barcodeList):
    barcodeDict = {1:[0, 1, 1, 1], 
                   2:[0, 1, 0, 1], 
                   3:[0, 0, 1, 1], 
                   4:[0, 1, 1, 0]}

    keys = list(barcodeDict.keys())
    values = list(barcodeDict.values())
    barcodeList.reverse()
    print(keys[values.index(barcodeList)])


barcodeCheck([1, 1, 1, 1])