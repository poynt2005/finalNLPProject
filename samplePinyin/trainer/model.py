class wordNode:
    def __init__(self , pinyin , wordProb = None):
        self.pinyin = pinyin

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
            for i in self.wordProb:
                for j in other:
                    newWord = str(list(i.keys())[0]) + str(list(j.keys())[0])
                    newProb = float(list(i.values())[0]) * float(list(j.values())[0])
                    res.append({newWord : newProb})

            res = sorted(res , key = lambda x : list(x.values())[0] , reverse = True)
            return res
        else:
            for i in self.wordProb:
                for j in other.wordProb:
                    newWord = str(list(i.keys())[0]) + str(list(j.keys())[0])
                    newProb = float(list(i.values())[0]) * float(list(j.values())[0])
                    res.append({newWord : newProb})
            res = sorted(res , key = lambda x : list(x.values())[0] , reverse = True)
            return wordNode('abc' , res)

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
