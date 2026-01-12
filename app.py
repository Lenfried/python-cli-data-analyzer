from flask import Flask, render_template

app = Flask(__name__) # initialize Flask app

@app.route('/')
def index():
    your_name = "Zihao Chen"
    return render_template('index.html', name = your_name)

if __name__ == '__main__':
    app.run(debug=True)