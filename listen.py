# import socket

# def listen():
#     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
#     client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     client.bind(("", 37020))

#     while True:
#         data, addr = client.recvfrom(1024)
#         print(f"received message: {data} from {addr}")

# listen()
# Receiver (Receives Audio from Network and Plays It)
import pyaudio
import socket

# Increase the buffer size if needed
chunk_size = 4096  # Try increasing this value
audio_format = pyaudio.paInt16
channels = 1
rate = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream for playback
stream = p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)

# Socket setup
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    data, addr = sock.recvfrom(chunk_size)
    stream.write(data)
