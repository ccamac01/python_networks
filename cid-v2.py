import sys, socket

try: 
	comp_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply a COMP number as first arg')

# separate host from URL because socket has no understanding or URLs
host = 'www.cs.tufts.edu'
# port 80 for HTTP
port = 80

# create_connection always creates a TCP connection
sock = socket.create_connection((host, port))

# create GET request
req = (
    'GET /comp/{compnum}/index.html HTTP/1.1\r\n'
    'Host: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: close\r\n'
    '\r\n'
)

# replace every left-side variable with the right-side value in GET request
req = req.format(
    compnum = comp_number,
    host = host,
    port = port,
    version = sys.version_info[0]
)

# data sent through TCP must be raw bytes, so encode as ascii
sock.sendall(req.encode('ascii'))
comp_raw = bytearray()
while True:
    buf = sock.recv(4096)
    # checks if empty string is returned, meaning TCP stream finished
    if not len(buf):
        break
    comp_raw += buf
comp = comp_raw.decode('utf-8')
print(comp)
