# Final NLP Project

* ### 使用非常簡易的HMM模型轉換拼音
* ### 語料庫是使用結巴中文分詞的預設辭典(以下引自官方頁)，讀取之後存成json格式，需要時取用
```
词典格式和 dict.txt 一样，一个词占一行；
每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，
顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
```
* ### 前端 : bootstrap3 + jquery ui ; 後端 : flask framework
* ### 使用的package : flask(網頁框架) 、 pypinyin(將中文轉成拼音，存入json)
* ### 使用方法 :

```
0. git clone "https://github.com/poynt2005/finalNLPProject.git" && cd finalNLPProject/
    (PS : 請在finalNLPProject創建一個名為"NLPProj"的Virtualenv，在該虛擬環境下安裝flask套件)
1. windows : 直接打開startServer.bat
2. 至local端的port 5000
3. 輸入拼音，以逗號隔開
```

