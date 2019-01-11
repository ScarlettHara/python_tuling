
print('直角三角形')
for i in range(1, 5):
    for k in range(5-i):
        print(' ', end=" ")     # 打印空格的个数
    for j in range(1, i+1):
        print('*', end=" ")     # 打印星星的个数
    print()

print('######################')
print('等腰三角形')
for i in range(1, 5):
    for k in range(5-i):
        print('', end=" ")     # 两个空格一个字符，变为一个空格
    for j in range(1, i+1):
        print('*', end=" ")     # 打印星星的个数
    print()
print('######################')
print("空心三角形")
for i in range(1, 6):
    for k in range(6-i):
        print(' ', end="")
    for j in range(1, i+1):
        if i == 1 or i ==5 or j == 1 or j == i:
            # 第一行 最后一行 全打印，其他行纸打印第一列和最后一列
            print("*", end=" ")
        else:
            print(' ', end=" ")
    print()


