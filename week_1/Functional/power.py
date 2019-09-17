num = int(input("Enter : "))


def myp(num):
    if num == 0:
        return 1
    return 2 * myp(num - 1)


print(myp(num))
