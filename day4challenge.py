def list_sum(myList):

    mysum = 0
    if not isinstance(myList,list):
        raise TypeError ('invalid input')
    for i in myList:
        if not (isinstance (i,int) or isinstance (i,list)):
            raise TypeError ('expected list or number')
        if isinstance(i, int):
            mysum += i
        else:
            sub = list_sum(i)
            mysum += sub
    return mysum


# print(list_sum("welcome"))


def power_num(num, power):
    if not (isinstance(power,int) or isinstance(num,int)):
    
        raise TypeError ('Specify value')

    if power == 0:
        return 1
    if power >= 1:
        return num*power_num(num, power-1)
    if power < 0:
        power = abs(power)
        return 1/(num*power_num(num, power-1))


print(power_num(2.6, -5))