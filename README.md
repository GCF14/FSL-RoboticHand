# Robotic Hand Controlled via Web Interface

## Project Overview
This project is a web-based interface for controlling a robotic hand that performs Filipino Sign Language (FSL). The Robotic hand is connected wia an Arduino, allowing users to send commands through the web interface and control the hand in real-time.

## Installation and Setup
### Steps:
1. **Clone the repository:**
   ```sh
   git clone https://github.com/GCF14/FSL-RoboticHand.git
2. **Upload the Arduino sketch** to your Arduino board using the **Arduino IDE.**
3. **Install necessary Python dependencies:**
   ```sh
   pip install flask serial
5. **Navigate to project directory**
   ```sh
   cd project
7. **Run the backend server:**
   ```sh
   python app.py
9. **Open the web interface in a browser:**
   ```sh
   http://localhost:5000
11. **Connect the robotic hand and start controlling it via the interface.**
