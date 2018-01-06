from parse_input import parseInput
from trainer.model import wordNode
from jsonDataLoder.loadFile import fileLoader
import sys

# main test function
def pinyinTranslate(inputStr = None):

    s = ''
    sPed = []

    if len(sys.argv) >= 2:
        print(sys.argv[1])
    elif inputStr:
        if isinstance(inputStr , str):
            s = inputStr
            sPed = parseInput(s)
        else:
            sPed = inputStr
    else:
        s = input('請輸入句子 : ').lower()



    samePinyinDict = fileLoader('samePinyin.json')
    samePinyinDiffWordDict = fileLoader('differentWordSamePinyin.json')

    res = []
    for i in [' '.join(j) for j in sPed]:
        try:
            pinyinObj = wordNode(i)
            pinyinObj.readProb(samePinyinDict , samePinyinDiffWordDict)
            res.append(pinyinObj)
        except:
            #print('資料庫無此單詞，請重新輸入')
            return 'inputError'


    calculRes = res[0]

    for i in range(1 , len(res) , 1):
        calculRes *= res[i]

    #without filter
    #return calculRes
    #with filter
    return calculRes.probFilter()

def main():
    s = input('請輸入句子 : ').lower()
    #s = 'jin tian tian qi bu cuo'
    #s = 'ying yun bao biao ju ti xu yao cheng bao'
    #s = 'jin tian wan can bu yao shui jiao'

    result = pinyinTranslate(s)

    print('輸入的拼音\"%s\"' % (s) , ';計算結果為:(由機率大至小排列)' , sep = '')

    print()
    print('\n'.join(result.formatResult()))



if __name__ == '__main__':
    main()
