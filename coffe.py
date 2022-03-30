coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("get coffee")
        coffee -= coffee

    elif money > 300:
        print("change %d and get coffee" % (money - 300))
        coffee -= coffee
    else:
        print("lack of money")
    if coffee == 0:
        print("lack of coffee")
        break

