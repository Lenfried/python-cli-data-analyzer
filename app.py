from flask import Flask, render_template, request
from analyzer import analyze_numbers

app = Flask(__name__) # initialize Flask app

@app.route('/')
def index():
    your_name = "Zihao Chen"
    return render_template('index.html', name = your_name)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    request_data = request.form.get('numbers', '')
    if request_data:
        try:
            numbers = list(map(float, request_data.split(',')))
        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter a comma-separated list of numbers.")
        results = analyze_numbers(numbers)
        return render_template("results.html", numbers=numbers, results=results)
    return render_template("index.html", error="Please enter some numbers to analyze.")

if __name__ == '__main__':
    app.run(debug=True)