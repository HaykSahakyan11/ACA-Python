import socket
import json


def printBoard(board):
    print(theBoard[0][0] + '|' + theBoard[0][1] + '|' + theBoard[0][2])
    print('-+-+-')
    print(theBoard[1][0] + '|' + theBoard[1][1] + '|' + theBoard[1][2])
    print('-+-+-')
    print(theBoard[2][0] + '|' + theBoard[2][1] + '|' + theBoard[2][2])

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 9000))
        data = client.recv(1024)
        print(data.decode())
        user_answer = input("Answer:")
        client.sendall(user_answer.encode())
        while True:

            if user_answer == "Yes":
                while True:
                    data = client.recv(1024)
                    data = data.decode()
                    theBoard = json.loads(data)
                    printBoard(theBoard)
                    user_input = input("Turn:")
                    print(user_input)
                    row, col = user_input.split(",")
                    row = int(row)
                    col = int(col)
                    while theBoard[row-1][col-1] != " ":
                        user_input = input("Turn:")
                    theBoard[row - 1][col - 1] = "X"
                    client.sendall(user_input.encode())


