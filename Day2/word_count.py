def words(s):
    num = {}
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = s.split()
    for i in count:
        if i in numbers:
            i = int(i)
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    return num