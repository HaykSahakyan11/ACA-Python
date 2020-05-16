import socket
import random
import json





def printBoard(board):
    print(theBoard[0][0] + '|' + theBoard[0][1] + '|' + theBoard[0][2])
    print('-+-+-')
    print(theBoard[1][0] + '|' + theBoard[1][1] + '|' + theBoard[1][2])
    print('-+-+-')
    print(theBoard[2][0] + '|' + theBoard[2][1] + '|' + theBoard[2][2])

def clientStep(row,col, steps = 0):
    if theBoard[row-1][col-1] == " ":
        theBoard[row-1][col-1] = "X"
        steps +=1




def serverStep(steps = 0):
    row = random.randint(1,3)
    col = random.randint(1,3)
    if theBoard[row-1][col-1] == " ":
        theBoard[row-1][col-1] = "O"
        steps += 1

def status(theBoard):
    if theBoard[0][0] == theBoard[0][1] == theBoard[0][2] != ' ':  # across the top
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][0]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[1][0] == theBoard[1][1] == theBoard[1][2] != ' ':  # across the middle
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[1][0]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[2][0] == theBoard[2][1] == theBoard[2][2] != ' ':  # across the bottom
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[2][0]
        print(" **** {} won. ****".format(theBoard[2][0]))
        return 1
    elif theBoard[0][0] == theBoard[1][0] == theBoard[2][0] != ' ':  # down the left side
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][0]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[0][1] == theBoard[1][1] == theBoard[2][1] != ' ':  # down the middle
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][1]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[0][2] == theBoard[1][2] == theBoard[2][2] != ' ':  # down the right side
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][2]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[0][0] == theBoard[1][1] == theBoard[2][2] != ' ':  # diagonal
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][0]
        print(" **** {} won. ****".format(winner))
        return winner
    elif theBoard[0][2] == theBoard[1][1] == theBoard[2][0] != ' ':  # diagonal
        printBoard(theBoard)
        print("\nGame Over.\n")
        winner = theBoard[0][2]
        print(" **** {} won. ****".format(winner))
        return winner
    return 0

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
            data = conn.recv(102)
            data = data.decode()
            if data == "Yes":

                while True:
                    json_theBoard = json.dumps(theBoard)
                    conn.sendall(json_theBoard.encode())
                    data = conn.recv(102)
                    data = data.decode().split(",")
                    row, col = data[0], data[1]
                    row = int(row)
                    col = int(col)
                    steps = 0
                    clientStep(row,col)
                    a = status(theBoard)
                    if a != 0:
                        conn.sendall(a.encode())
                        break
                    else:
                        serverStep()
                        if status(theBoard) == 0:
                            json_theBoard = json.dumps(theBoard)
                            conn.sendall(json_theBoard.encode())

                        else:
                            conn.sendall(status(theBoard).encode())


















