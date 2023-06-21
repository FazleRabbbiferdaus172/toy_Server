import socket

HOST, PORT = '', 8000

# Declearing Socket type
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket: # AF_INET = Address Family ipv4, SOCK_STREAM = socket type TCP
    # Setting socket options: # Avoid bind() exception: OSError: [Errno 48] Address already in use
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Binding to socket to HOST and port for identificaiton
    server_socket.bind((HOST, PORT))
    # Now our server starts listening at port localhot:8000
    server_socket.listen(1)
    print("Server listening on port {} ...".format(PORT))

    # Never Ending Loop to accept incoming Requests
    while True:
        client_connection, client_address = server_socket.accept()
        with client_connection:
            request_data = client_connection.recv(1024)
            if not request_data:
                break
            print("Client request: \n {}".format(request_data.decode('utf-8')))
            response = b'''\
HTTP/1.1 200 OK

Hello Client
            '''
            client_connection.sendall(response)


