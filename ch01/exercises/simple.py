print("Hello World")
print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
## print(10 / 15)
## The last answer is repeating which causes high cpu usage.
rate = float(input("What is the current exchange rate for Euro to USD? "))
amount = float(input("How much Euro would you like to be exchanged for USD? "))
total = amount * rate
result = total - 3
print("We will be taking $3 for a service fee. Here is " + str(result) + " USD")
