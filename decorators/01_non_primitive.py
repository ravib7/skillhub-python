def sum(n1,n2):
    return n1 + n2
    # result = sum(10,20) # function call / invoke
    # result = 30

    result = sum  # function refrance
    # print(result)

    x = result(100,200)
    print(x)