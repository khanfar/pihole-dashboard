from flask import Flask, render_template, jsonify
import requests
import psutil

app = Flask(__name__)

# Pi-hole configuration
PIHOLE_IP = "192.168.0.192"
API_KEY = "544007abfaca3a06a950e619c9e8d82b4affb28d29e963802215358bbe3856b7"

# Route to display the dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API route to fetch Pi-hole data and system stats
@app.route('/api/data')
def get_data():
    # Pi-hole data
    url = f"http://{PIHOLE_IP}/admin/api.php?summaryRaw&auth={API_KEY}"
    response = requests.get(url)
    pihole_data = response.json()

    # System metrics
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent

    data = {
        "pihole": pihole_data,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
