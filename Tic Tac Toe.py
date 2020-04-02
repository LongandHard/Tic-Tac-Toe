## TIC TACK TOE

a = [0, 1, 2,
     3, 4, 5,
     6, 7, 8]

def show():
    print(a[0], '|', a[1], '|', a[2])
    print('----------')
    print(a[3], '|', a[4], '|', a[5])
    print('-----------')
    print(a[6], '|', a[7], '|', a[8])
show()

def player1():
    if a[0] == a[1] and a[1] == a[2] and a[2] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[3] == a[4] and a[4] == a[5] and a[5] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[6] == a[7] and a[7] == a[8] and a[8] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[0] == a[3] and a[3] == a[6] and a[6] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[1] == a[4] and a[4] == a[7] and a[7] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[2] == a[5] and a[5] == a[8] and a[8] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[0] == a[4] and a[4] == a[8] and a[8] == 'X':
        print("Player 1 wins!!")
        return False
    elif a[6] == a[4] and a[4] == a[2] and a[2] == 'X':
        print("Player 1 wins!!")
        return False
    else:
        return True

def player2():
    if a[0] == a[1] and a[1] == a[2] and a[2] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[3] == a[4] and a[4] == a[5] and a[5] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[6] == a[7] and a[7] == a[8] and a[8] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[0] == a[3] and a[3] == a[6] and a[6] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[1] == a[4] and a[4] == a[7] and a[7] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[2] == a[5] and a[5] == a[8] and a[8] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[0] == a[4] and a[4] == a[8] and a[8] == 'O':
        print("Player 2 wins!!")
        return False
    elif a[6] == a[4] and a[4] == a[2] and a[2] == 'O':
        print("Player 2 wins!!")
        return False
    else:
        return True


while True:
    print("Player 1!!!")
    while True:
        choose_num = int(input("Choose number 0 - 8: "))
        if a[choose_num] != 'O' or a[choose_num] != 'X':
            a[choose_num] = 'X'
            show()
            break
        else:
            print("Invalid Input!! Try Again!")

    player1()
    if player1() is False:
        break


    print("Player 2!!!")

    while True:
        choose_num1 = int(input("Choose number 0 - 8: "))
        if a[choose_num1] != 'O' or a[choose_num1] != 'X':
            a[choose_num1] = 'O'
            show()
            break
        else:
            print("Invalid Input!! Try Again!")
    player2()
    if player2() is False:
        break





