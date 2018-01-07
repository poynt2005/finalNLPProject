from parse_input import parseInputMultiple
from trainer.model import wordNode
from jsonDataLoder.loadFile import fileLoader
import sys

# main test function
def pinyinTranslate(inputStr = None , accuracy = None):

    s = ''
    sPed = []

    if len(sys.argv) >= 2:
        print(sys.argv[1])
    elif inputStr:
        if isinstance(inputStr , str):
            s = inputStr
            sPed = parseInputMultiple(s)
        else:
            sPed = inputStr
    else:
        s = input('請輸入句子 : ').lower()



    samePinyinDict = fileLoader('samePinyin.json')
    samePinyinDiffWordDict = fileLoader('differentWordSamePinyin.json')

    #new code
    totalRes = []
    lastMax = 0

    for i in sPed:
        tmp = []

        sentenceVaild = True
        for j in i:
            try:
                if accuracy:
                    pinyinObj = wordNode(j , accuracy = accuracy)
                else:
                    pinyinObj = wordNode(j)
                pinyinObj.readProb(samePinyinDict , samePinyinDiffWordDict)
                tmp.append(pinyinObj)
            except:
                sentenceVaild = False

        if not sentenceVaild:
            continue


        calculRes = tmp[0]
        for i in range(1 , len(tmp) , 1):
            calculRes *= tmp[i]

        currentSentense = calculRes.probFilter()

        appendToTotalRes = False
        if currentSentense.getSmallest() > lastMax:
            if totalRes:
                totalRes.pop()
            #totalRes.append(currentSentense)
            appendToTotalRes = True
            lastMax = currentSentense.getBiggest()
        else:
            appendToTotalRes = True
            #totalRes.append(currentSentense)

        if appendToTotalRes:
            for k in currentSentense.wordProb:
                totalRes.append(k)

    if totalRes:
        return sorted(totalRes , key = lambda x : list(x.values())[0] , reverse = True)
    else:
        return 'inputError'

def main():
    s = input('請輸入句子 : ').lower()
    #s = 'jin tian tian qi bu cuo'
    #s = 'jin tian wan can hen hao chi'
    #s = 'wo zuo tian xin qing hen cha'
    #s = 'ying yun bao biao ju ti xu yao cheng bao'
    #s = 'jin tian wan shang wo yao chi shui jiao'
    #s = 'jin tian wan can bu yao shui jiao'
    #s = 'cao zuo xing zhi yue'
    #s = 'wo jue de bu xing'
    #s = 'wo jue de woie weifj'
    #s = 'wo ke yi hui da yi ju wu ke feng gao'
    result = pinyinTranslate(s)

    print('輸入的拼音\"%s\"' % (s) , ';計算結果為:(由機率大至小排列)' , sep = '')

    print()

    if not result == 'inputError':
        for i in result:
            print(list(i.keys())[0] , list(i.values())[0])
    else:
        print('error')
    #test code (cut word by self)
    '''samePinyinDict = fileLoader('samePinyin.json')
    samePinyinDiffWordDict = fileLoader('differentWordSamePinyin.json')

    #s = 'ying yun bao biao ju ti xu yao cheng bao'.split()
    #s = ['ying yun' , 'bao biao' , 'ju ti' , 'xu yao' , 'cheng bao']
    s = ['jin tian', 'wan shang', 'wo', 'yao', 'chi', 'shui jiao']
    res = []
    for i in s:
        try:
            pinyinObj = wordNode(i)
            pinyinObj.readProb(samePinyinDict , samePinyinDiffWordDict)
            res.append(pinyinObj)
        except:
            pass
    calculRes = res[0]
    for i in range(1 , len(res) , 1):
        calculRes *= res[i]

    k = calculRes.probFilter()

    print(k.wordProb)'''

if __name__ == '__main__':
    main()
