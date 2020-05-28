import socket
import random
import json


def printBoard(theBoard):
    print(theBoard[0][0] + '|' + theBoard[0][1] + '|' + theBoard[0][2])
    print('-+-+-')
    print(theBoard[1][0] + '|' + theBoard[1][1] + '|' + theBoard[1][2])
    print('-+-+-')
    print(theBoard[2][0] + '|' + theBoard[2][1] + '|' + theBoard[2][2])


def clientStep(theBoard, row, col):
    theBoard[row - 1][col - 1] = "X"
    return theBoard


def serverStep(theBoard):
    while True:
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        if theBoard[row - 1][col - 1] == " ":
            theBoard[row - 1][col - 1] = "O"
            return theBoard


def result(theBoard, steps):  # to check if there is an outcome of the game
    winner = 0
    if steps < 5:  # can not be outcome
        return winner
    elif steps == 9:  # max step
        winner = "Draw"
        print("\nGame Over.")
        print(" **** {} ****".format(winner))
        return winner
    else:
        X = [0, 1, 2]
        x1, x2, x3 = X
        for i in range(3):
            if theBoard[i][x1] == theBoard[i][x2] == theBoard[i][x3] != " ":  # horizontal
                winner = theBoard[i][x1]
                pass
            if theBoard[x1][i] == theBoard[x2][i] == theBoard[x3][i] != " ":  # vertical
                winner = theBoard[x1][i]
                pass
        if theBoard[x1][x1] == theBoard[x2][x2] == theBoard[x3][x3] != " " or \
                theBoard[len(X) - 1 - x1][x1] == theBoard[len(X) - x2][x2] == theBoard[len(X) - 1 - x3][
            x3] != " ":  # diagonals
            winner = theBoard[x1][x1]
        if winner:
            print("\nGame Over.")
            print(" **** {} won. ****".format(winner))
    return winner



if __name__ == "__main__":
    theBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 9000))
        sock.listen(5)
        print("Accepting data")
        conn, addr = sock.accept()
        with conn:
            print("Connected by", addr)
            conn.sendall("Lets play? (Yes or No)".encode())
            data = conn.recv(1024)
            data = data.decode()
            if data == "Yes":
                info_sent = json.dumps(list([theBoard, 0]))
                conn.sendall(info_sent.encode())
                steps = 0
                while True:
                    data = conn.recv(102)
                    data = data.decode()
                    steps += 1
                    if data != "":
                        row, col = map(int, data.split(","))
                        theBoard = clientStep(theBoard, row, col)
                        current_result = result(theBoard, steps)
                        if current_result == 0:
                            theBoard = serverStep(theBoard)
                            steps += 1
                            current_result = result(theBoard, steps)
                        info_sent = json.dumps(list([theBoard, current_result]))
                        conn.sendall(info_sent.encode())
                    else:
                        break

