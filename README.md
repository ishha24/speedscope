# SpeedScope - Internet Speed Analyzer

SpeedScope is a modern, user-friendly Python GUI application for testing and analyzing your internet connection speed. Built with Tkinter, it provides real-time speed measurements including download speed, upload speed, and ping, with a simple and responsive interface.

## Features

- Real-time internet speed testing  
- Download speed in Mbps  
- Upload speed in Mbps  
- Ping in milliseconds  
- Simple and clean GUI built using Tkinter  
- Multi-threaded for non-blocking UI  
- Progress bar indicator during speed test  

## Technologies Used

- Python  
- Tkinter (GUI)  
- `speedtest` module (for speed testing)  
- Threading (for responsiveness)  

## Installation

1. **Clone the repository or download the script**
   ```bash
   git clone https://github.com/yourusername/speedscope.git
   cd speedscope
Install the required module

bash
Copy
Edit
pip install speedtest-cli
Run the application

bash
Copy
Edit
python speedscope_app.py
How It Works
When the user clicks "Start Test", the app uses the speedtest module to fetch the best server and measure:

Download Speed: How fast you can pull data from the server

Upload Speed: How fast you can send data to the server

Ping: Time taken for a signal to travel to the server and back

License
This project is open-source and available under the MIT License.

Author
isha.
Feel free to connect or contribute!
