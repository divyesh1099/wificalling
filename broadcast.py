# import socket
# import time
# def broadcast():
#     server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#     # Set a timeout so the socket does not block indefinitely
#     server.settimeout(0.2)
#     message = b"Hello, I am Divyesh"
#     while True:
#         server.sendto(message, ('<broadcast>', 37020))
#         print("Message sent!")
#         time.sleep(1)

# broadcast()

import pyaudio
import socket

# Audio configuration
chunk_size = 1024
audio_format = pyaudio.paInt16
channels = 1
rate = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream for recording
stream = p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)

# Socket setup
host = '192.168.0.109'  # Receiver's IP address
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = stream.read(chunk_size)
    sock.sendto(data, (host, port))
