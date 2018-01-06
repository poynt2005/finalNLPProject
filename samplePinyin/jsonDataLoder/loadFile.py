import os
import json



def fileLoader(fileName):
    filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)) , fileName)

    with open(filePath , encoding = 'utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    firstFile = fileLoader('samePinyin.json')
    print(firstFile)
