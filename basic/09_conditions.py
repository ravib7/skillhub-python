price = 100
isAvaliable = True

if(price < 100 and isAvaliable):
    print("cheap")
elif(price == 100 and isAvaliable):
    print("avarage")
elif(price > 100 and isAvaliable):
    print("expensive")
else:
    print("outof stock")