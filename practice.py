def listsum (ls, result):
    if not ls:
        return result
    return listsum (ls[1:], result+ls[0])

print (listsum([1,2,3,4,[7,8]],0))
