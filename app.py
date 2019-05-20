from flask import Flask,render_template,request
import jieba

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("fenlei.html")

@app.route('/getsourcetext',methods=['POST'])
def handlesourcetext():
    if request.method == 'POST':
        source = request.args.get('source')
        print source
        jieba.load_userdict('medicaldic.txt')
        wordslist=jieba.cut(source)
        # wordslist=jieba.cut(source,True,True)
        return '/'.join(wordslist)


if __name__ == '__main__':
    app.run()
