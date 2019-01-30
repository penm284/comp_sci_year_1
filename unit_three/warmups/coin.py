penny = 1
nickel = 5
dime = 10
def coin(num):
    if num == 1:
        print('Use a 1$ coin')
#divide input by ten and then if remainder > 5 divide by 5 if remainder greater than 1 count up the ones
    if num > dime:
        num / 10
        return %

    if % > 5:
        % / 5
        return %

    if % > 1

    num = int(input('Enter $ amount: '))





    def while_statement(amount, coin_value, coin):
        n = 0
        while amount-coun_value >= 0:
            amount = amount - coin_value
            n = n + 1
        print (str(n) + coin + "used")
        return amount

    def coins (amount):
        amount = while_statement(amount, 10,"dime")
        amount = while_statement(amount, 5,"nickel")
        amount = while_statement(amount, 1,"penny")
    coins()



def coin(n):
    count = 0
    while n > 0:
        if n >= 10:
            n -= 10
            count+= 1
        elif n >=5:
            n -=5:
            count += 1
        else:
            n -= 1
            count += 1
    return count
