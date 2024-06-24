import socket 

            
if __name__ == "__main__":
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server.bind(("78:AF:08:D6:54:56", 4))
    server.listen(1)
    client, address = server.accept()

    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"Message: {data.decode('utf-8')}")
            message = input("Enter message: ")
            client.send(message.encode('utf-8'))

    except OSError as e:
        pass

    
    client.close()
    server.close()
    