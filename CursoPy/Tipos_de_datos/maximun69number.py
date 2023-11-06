
def max69num(num):
    arrNum = list(str(num))
    for i in range(len(arrNum)):
        if arrNum[i] == '6':
            arrNum[i] = '9'
            break

    return int("".join(arrNum))

print(max69num(9669))

print(list('Mayber'))