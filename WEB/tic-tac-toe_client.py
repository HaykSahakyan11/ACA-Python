import socket
import json


def printBoard(theBoard):
    print(theBoard[0][0] + '|' + theBoard[0][1] + '|' + theBoard[0][2])
    print('-+-+-')
    print(theBoard[1][0] + '|' + theBoard[1][1] + '|' + theBoard[1][2])
    print('-+-+-')
    print(theBoard[2][0] + '|' + theBoard[2][1] + '|' + theBoard[2][2])


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def input_validation(user_input):
    if len(user_input.split(",")) == 2:
        row, col = user_input.split(",")
        if is_integer(row) and is_integer(col):
            message_about_validation = int(row), int(col)
            return True, message_about_validation
        message_about_validation = "Inputs must be integers"
        return False, message_about_validation
    else:
        message_about_validation = "Inputs must be 2 separated by comma X,Y"
        return False, message_about_validation


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 9000))
        data = client.recv(1024)

        print(data.decode())
        user_answer = input("Answer:")
        user_answers = ["Yes", "No"]
        while user_answer not in user_answers:
            user_answer = input("Answer Yes or No :")
        client.sendall(user_answer.encode())

        if user_answer == "Yes":
            dictionary = {"X": "You win", "O": "You lose", "Draw": "Draw"}

            while True:
                data = client.recv(1024)
                data = data.decode()
                data = json.loads(data)
                theBoard, result = data[0], data[1]
                if result in dictionary:
                    printBoard(theBoard)
                    print("\nGame Over. \n***{}***".format(dictionary[result]))
                    break
                printBoard(theBoard)
                user_input = input("Your turn:")  # 1,3
                input_validated, message_about_validation = input_validation(user_input)[0], \
                                                            input_validation(user_input)[1]
                while True:
                    if input_validated:
                        row, col = message_about_validation
                        if theBoard[row - 1][col - 1] == " ":
                            break
                        else:
                            print("The place is taken, try new one!!")
                    else:
                        print(message_about_validation)
                    user_input = input("Still your turn:")
                    input_validated, message_about_validation = input_validation(user_input)[0], \
                                                                input_validation(user_input)[1]
                client.sendall(user_input.encode())
