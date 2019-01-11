for i in range(1, 5):
    for k in range(5 - i):
        print(' ', end=" ")
    for j in range(1, 6):
        print('*', end=" ")
    print()

print("#"*50)
k = 0
j = 0

for i in range(1, 5):
    for k in range(i):
        print(' ', end=" ")
    for j in range(1, 6):
        print('*', end=" ")
    print()
