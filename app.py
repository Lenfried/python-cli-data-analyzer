from os import times
from flask import Flask, jsonify, render_template, request
from analyzer import analyze_numbers
from external_api import fetch_hourly_temperature
from weather_analysis import analyze_time_series

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

@app.route("/test-weather")
def test_weather():
    latitude = 40.7128
    longitude = -74.0060
    try:
        times, temperatures = fetch_hourly_temperature(latitude, longitude)
        weather_data = list(zip(times, temperatures))
        return render_template('weather_analysis_results.html', weather_data=weather_data)
    except Exception as e:
        error_msg = f"Error fetching weather data: {str(e)}"
        return render_template('weather_analysis_results.html', error=error_msg)

@app.route('/weather-input')
def weather_input():
    return render_template('weather_input.html')

@app.route("/analyze-weather", methods=['POST'])
def analyze_weather():
    try:
        latitude = request.form.get("lat", type=float)
        longitude = request.form.get("lon", type=float)
        
        if latitude is None or longitude is None:
            return render_template('weather_input.html', error="Please provide valid latitude and longitude values.")
        
        times, temperatures = fetch_hourly_temperature(latitude, longitude)
        results = analyze_time_series(times, temperatures)
        weather_data = list(zip(times, temperatures))
        
        return render_template('weather_analysis_results.html', results=results, weather_data=weather_data, latitude=latitude, longitude=longitude)
    except ValueError as e:
        error_msg = f"Invalid data: {str(e)}"
        return render_template('weather_input.html', error=error_msg)
    except Exception as e:
        error_msg = f"Error fetching weather data: {str(e)}"
        return render_template('weather_input.html', error=error_msg)


if __name__ == '__main__':
    app.run(debug=True)