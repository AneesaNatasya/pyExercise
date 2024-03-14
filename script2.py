import random

#r1 = random.random()
#print(r1)

#r2 = random.choice([1,2,3,4,5])
#print(r2)

#r3 = random.randint(1,1000)
#print(r3)

total = 0
expense = []
for i in range(5):
    expense.append(float(input("Please enter a number: ")))
    
    total = sum(expense)
print("Total",total)

roll = random.randint(1,3)
print(roll)
if roll == 1:
    loot ="emas"