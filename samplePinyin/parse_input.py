def parseInput(inputStr):
    inputStr = inputStr.split(' ')
    return [inputStr[i : i+2] for i in range(0 , len(inputStr) , 2)]

if __name__ == '__main__':
    s = 'jin tian tian qi bu cuo'
    print(parseInput(s))
