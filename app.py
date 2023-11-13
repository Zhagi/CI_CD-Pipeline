from flask import Flask

app = Flask(__name__)

@app.route('/')
def CI__CD_Pipeline():
    return 'Your CI-CD Pipeline Works!'

if __name__ == '__main__':
    app.run(debug=True)