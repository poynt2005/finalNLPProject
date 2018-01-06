def ProbFilter(nodeObj):
    old = nodeObj.wordProb
    res = []

    detectProb = []
    for i in old:
        currentWord = list(i.keys())[0]
        currentProb = list(i.values())[0]

        if not currentProb in detectProb:
            detectProb.append(currentProb)
            res.append({currentWord : currentProb})

    return res

def main():
    from jsonDataLoder.loadFile import fileLoader
    from trainer.model import wordNode
    samePinyinDict = fileLoader('samePinyin.json')
    samePinyinDiffWordDict = fileLoader('differentWordSamePinyin.json')

    firstNode = wordNode('jin tian')
    firstNode.readProb(samePinyinDict , samePinyinDiffWordDict)

    print(ProbFilter(firstNode))

if __name__ == '__main__':
    main()
