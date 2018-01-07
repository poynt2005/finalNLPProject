def parseInput(inputStr):
    inputStr = [i for i in inputStr.split(' ') if i]
    return [inputStr[i : i+2] for i in range(0 , len(inputStr) , 2) if inputStr[i]]

def parseInputMultiple(inputStr):
    x0 = [i for i in inputStr.split(' ') if i]
    x1 = []
    x2 = []


    def s(a, b):
        sa = a[:]
        sb = b[:]
        if not sb:
            x2.append(sa)
            return
        sa.append(b[0])
        s(sa, sb[1:])

        if len(sb) == 1:
            return
        sa[-1] = b[0] + ' ' + b[1]
        s(sa, sb[2:])


    s(x1, x0)
    return(x2)

if __name__ == '__main__':
    s = 'jin tian tian qi bu cuo'

    print(parseInputMultiple(s))
