temperature = float(input("What is the temperature? "))
forecast = input("Enter the forecast? ")

if temperature <80 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside")