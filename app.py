from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Simulated weather data
    weather = {"city": "Karachi", "temp": "28°C", "condition": "Cloudy"}
    return render_template('index.html', weather=weather)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
