from flask import Flask,render_template,request,url_for,jsonify
import sys
sys.path.append('samplePinyin')


from samplePinyin.pinyinTranslate import pinyinTranslate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html' ,
                            page_title = 'NLP Project' , brandName = 'NLP Final Project' ,
                            gitHubPage = 'https://github.com/poynt2005/finalNLPProject' , brandLogoText = 'Pinyin')

@app.route('/getQuery' , methods = ['POST'])
def getQuery():
    if request.method == 'POST':
        param = request.form['param']

        result = pinyinTranslate(param)

        if not result == 'inputError':
            return jsonify(result.wordProb)
        else:
            return('error')
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
