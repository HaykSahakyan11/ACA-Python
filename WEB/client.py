import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", 9999))
    while True:
        user_input = input("Say something: ")
        client.sendall(user_input.encode())
        data = client.recv(1024)
        print(data.decode("utf-8"))
        if user_input == "exit":
            break
