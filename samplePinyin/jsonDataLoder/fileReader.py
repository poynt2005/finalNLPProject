def readFile():
    with open('dict.txt.big' , encoding = 'utf-8') as f:
        '''
        jieba's doc : 每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开
        '''
        for line in f:
            line = line.split(' ')

            word = line[0]
            freq = line[1]

            yield word , int(freq)
