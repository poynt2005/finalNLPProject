from fileReader import readFile as rF
from pypinyin import lazy_pinyin
from json import dumps



def parseFile():
    tmp = {}
    totalFreq = 0

    print('reading file...')

    for word , freq in rF():
        pinyin = (' '.join(lazy_pinyin(word))).lower()

        totalFreq += freq

        if pinyin not in tmp:
            tmp[pinyin] = {word : freq}
        else:
            tmp[pinyin][word] = freq

    print('finished reading')

    samePinyin = {}
    differentWordSamePinyin = {}

    print('calculing frequency and sort them')
    for pinyin , data in tmp.items():
        currentPinyinTotal = sum(data.values())
        samePinyin[pinyin] = (currentPinyinTotal / totalFreq)

        tmpList = []
        for word , freq in data.items():
            tmpList.append({word : (freq / currentPinyinTotal)})
        differentWordSamePinyin[pinyin] = sorted(tmpList , key = lambda x : list(x.values())[0] , reverse=True)


    print('write to json file...')

    with open('samePinyin.json' , 'w' , encoding = 'utf-8') as f:
        f.write(dumps(samePinyin , indent=4 , ensure_ascii=False))

    with open('differentWordSamePinyin.json' , 'w' , encoding = 'utf-8') as f:
        f.write(dumps(differentWordSamePinyin , indent=4 , ensure_ascii=False))

if __name__ == '__main__':
    print('start')
    parseFile()
    print('done')
