from flask import Flask, render_template, request, jsonify
import serial  # For communication with Arduino or microcontroller

app = Flask(__name__)

# Configure Serial Communication (Modify for your setup)
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust for your port
except:
    ser = None

@app.route('/')
def index():
    return render_template('index.html')  # Load the frontend

@app.route('/control', methods=['POST'])
def control():
    if ser:
        data = request.json
        command = data.get('command', '')
        ser.write(command.encode())  # Send command to the robot hand
        return jsonify({'status': 'success', 'command': command})
    return jsonify({'status': 'error', 'message': 'Serial not connected'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Access from any device
