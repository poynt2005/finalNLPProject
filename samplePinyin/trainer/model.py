class wordNode:
    def __init__(self , pinyin , wordProb = None , accuracy = 50):
        self.pinyin = pinyin

        self.accuracy = accuracy
        if not wordProb:
            self.wordProb = []
        else:
            self.wordProb = wordProb

    # get Probility from json and get model
    def readProb(self , samePinyinData , samePinyinDiffWordData):
        samePinyinProb = samePinyinData[self.pinyin]
        samePinyinDiffWordProb = samePinyinDiffWordData[self.pinyin]



        tmpList = []

        for i in samePinyinDiffWordProb:
            currentProb = float(samePinyinProb) * float(list(i.values())[0])
            currentWord = list(i.keys())[0]

            tmpList.append({currentWord : currentProb})

        self.wordProb = sorted(tmpList , key = lambda x : list(x.values())[0] , reverse = True)

    # overloading the multiple operator and get the sentence probility
    def __mul__(self , other):
        res = []
        if isinstance(other , list):
            for i in range(len(self.wordProb)):
                if i >= self.accuracy:
                    break;
                for j in range(len(other)):
                    if j >= self.accuracy:
                        break;
                    newWord = str(list(self.wordProb[i].keys())[0]) + str(list(other[j].keys())[0])
                    newProb = float(list(self.wordProb[i].values())[0]) * float(list(other[j].values())[0])
                    res.append({newWord : newProb})

            res = sorted(res , key = lambda x : list(x.values())[0] , reverse = True)
            return wordNode('abc' , res)
        else:
            for i in range(len(self.wordProb)):
                if i >= self.accuracy:
                    break;
                for j in range(len(other.wordProb)):
                    if j >= self.accuracy:
                        break;
                    newWord = str(list(self.wordProb[i].keys())[0]) + str(list(other.wordProb[j].keys())[0])
                    newProb = float(list(self.wordProb[i].values())[0]) * float(list(other.wordProb[j].values())[0])
                    res.append({newWord : newProb})
            res = sorted(res , key = lambda x : list(x.values())[0] , reverse = True)
            return wordNode('abc' , res)

    #get the smellest prob of the wordNode
    def getSmallest(self):
        return float(list(self.wordProb[-1].values())[0])

    #get the biggest prob of the wordNode
    def getBiggest(self):
        return float(list(self.wordProb[0].values())[0])

    #return a formatted string of result
    def formatResult(self):
        formatted = []
        for i in self.wordProb:
            formatted.append('\"%s\"的機率是 : %s' % (list(i.keys())[0] , list(i.values())[0]))
        return formatted

    # filter the smae probility
    def probFilter(self):
        old = self.wordProb
        res = []

        detectProb = []
        for i in old:
            currentWord = list(i.keys())[0]
            currentProb = list(i.values())[0]

            if not currentProb in detectProb:
                detectProb.append(currentProb)
                res.append({currentWord : currentProb})
        return wordNode('abc' , res)




def main():
    import sys
    sys.path.append('../')
    from jsonDataLoder.loadFile import fileLoader
    samePinyinDict = fileLoader('samePinyin.json')
    samePinyinDiffWordDict = fileLoader('differentWordSamePinyin.json')

    firstNode = wordNode('jin tian')
    firstNode.readProb(samePinyinDict , samePinyinDiffWordDict)

    secondNode = wordNode('tian qi')
    secondNode.readProb(samePinyinDict , samePinyinDiffWordDict)

    thirdNode = wordNode('bu cuo')
    thirdNode.readProb(samePinyinDict , samePinyinDiffWordDict)

    multied = firstNode * secondNode * thirdNode

    print('\n'.join(multied.formatResult()))


    #print(firstNode.wordProb , secondNode.wordProb , thirdNode.wordProb , sep = '\n')

if __name__ == '__main__':
    main()
