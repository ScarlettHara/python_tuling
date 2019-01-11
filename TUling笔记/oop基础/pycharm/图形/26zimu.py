# 打印字母 A
def A():
    for i in range(1, 7):
        for k in range(6 - i):
            print(' ', end="")
        for j in range(1, i + 1):
            if i == 1 or i == 4 or j == 1 or j == i:
                print("*", end=" ")
            else:
                print(' ', end=" ")
        print()

# 打印字母 B
def B():
    for i in range(1, 4):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(1, 5):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=" ")
            else:
                print(" ", end=" ")
        print()


# 打印字母 C
def C():
    for i in range(1, 5):
        for j in range(1, 4):
            if i in (1, 4) :
                if j != 1:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            elif j == 1:
                print('*', end=" ")
            else:
                print(' ', end=' ')
        print()


# 打印字母 D
def D():
    for i in range(1, 5):
        for j in range(1, 4):
            if i == 1 or i == 4 or j == 1:
                if j < 3:
                    print('*', end=' ')
            elif j == 3:
                if i == 2 or i == 3:
                    print('*', end=" ")
            else:
                print(" ", end=" ")
        print()


# 打印字母 E
def E():
    for i in range(1,8):
        for j in range(1, 5):
            if i in (1, 4, 7) or j == 1:
                print('*', end=' ')
        print()


# 打印字母 F：
def F():
    for i in range(1,8):
        for j in range(1, 5):
            if i in (1, 4) or j == 1:
                print('*', end=' ')
        print()


# 打印字母 G
for i in range(1, 6):
    for j in range(1, 6):
        if i in (1, 5) or j in (1, 5):
            if i in (1, 5) and j == 1:
                print(' ', end=' ')
            elif i == 2 and j == 5:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        elif i == 3 and j != 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()



































# 打印字母 O
def O():
    for i in range(1, 6):
        for j in range(1, 7):
            if i in (1, 5) :
                if j not in (1,6):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            elif j == 1 or j == 6:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()



