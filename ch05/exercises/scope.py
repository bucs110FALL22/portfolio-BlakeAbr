#ScopeandAccumulation
def multiplybyadding():
    num1 = int(input("Pick a number: "))
    num2 = int(input("Pick a number to multiply by that number: "))
    total = 0
    for i in range(num2):
        total = total + num1
    print(total)
multiplybyadding()