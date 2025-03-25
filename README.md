# Robotic Hand Controlled via Web Interface

## Project Overview
This project is a web-based interface for controlling a robotic hand that performs Filipino Sign Language (FSL). The Robotic hand is connected wia an Arduino, allowing users to send commands through the web interface and control the hand in real-time.

## Installation and Setup
### Steps:
1. Clone the repository:
git clone https://github.com/GCF14/FSL-RoboticHand
2. Upload the Arduino sketch to your Arduino board using the Arduino IDE.
3. Install necessary Python dependencies
pip install flask serial
4. Navigate to project directory
   cd project
5. Run the backend server:
   python app.py
6. Open the web interface in a browser:
   http://localhost:5000
7. Connect the robotic hand and start controlling it via the interface.
