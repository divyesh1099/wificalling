# Wi-Fi Calling App

## Description
This project is a Python-based application enabling voice calls over a local Wi-Fi network without the need for an internet connection. Utilizing socket programming and audio handling, it demonstrates a basic implementation of a Wi-Fi calling system.

## Features
- Voice calls over local Wi-Fi networks.
- Automatic discovery of devices on the same network.
- Real-time audio transmission and reception.
- Simple and intuitive user interface.

## Getting Started

### Dependencies
- Python 3.x
- PyAudio
- Your local Wi-Fi network.

### Installing
- Clone this repository: `git clone https://github.com/divyesh1099/wificalling.git`
- Navigate to the project directory: `cd wifi-calling-app`
- Install the required packages: `pip install -r requirements.txt`

### Executing the Program
1. Run the server (broadcasting device) script on one device:
   ```
   python broadcast.py
   ```
2. Run the client (receiving device) script on another device:
   ```
   python listen.py
   ```
3. Ensure both devices are connected to the same Wi-Fi network.
4. Start communicating!

## How It Works
- The application uses UDP sockets for network communication to broadcast discovery messages and establish connections between devices on the same network.
- Audio data is captured, encoded, and transmitted in real-time, and then decoded and played back on the receiving device.

## Help
Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors
Your Name  
Contact info

## Version History
- 0.1
    - Initial Release

## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE.md file for details

## Acknowledgments
Inspiration, code snippets, etc.
- [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)