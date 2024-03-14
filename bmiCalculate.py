print('''
,-----.  ,--.   ,--.,--.  ,-----.  ,---.  ,--.    ,-----.,--. ,--.,--.     ,---. ,--------. ,-----. ,------.  
|  |) /_ |   `.'   ||  | '  .--./ /  O  \ |  |   '  .--./|  | |  ||  |    /  O  \'--.  .--''  .-.  '|  .--. ' 
|  .-.  \|  |'.'|  ||  | |  |    |  .-.  ||  |   |  |    |  | |  ||  |   |  .-.  |  |  |   |  | |  ||  '--'.' 
|  '--' /|  |   |  ||  | '  '--'\|  | |  ||  '--.'  '--'\'  '-'  '|  '--.|  | |  |  |  |   '  '-'  '|  |\  \  
`------' `--'   `--'`--'  `-----'`--' `--'`-----' `-----' `-----' `-----'`--' `--'  `--'    `-----' `--' '--' 
                                                                                                              
      ''')

import random

def calculateBMI(Berat, Tinggi):
    # Convert inputs to float
    Berat = float(Berat)
    Tinggi = float(Tinggi)
    
    # Calculate BMI
    BMI = Berat / (Tinggi * Tinggi)
    
    # Return the calculated BMI
    return BMI

def print_health_quotes():
    health_quotes = ["Health is wealth", "Take care of your body. It's the only place you have to live.", "An apple a day keeps the doctor away."]
    random_index = random.randint(1, 2)
    print(health_quotes[random_index])

def classifyBMI(BMI):
    if BMI < 18.5:
        print("underweight")
    elif 18.5 <= BMI < 25:
        print("normal weight")
    elif 25 <= BMI < 30:
        print("slightly overweight")
    elif 30 <= BMI < 35:
        print("obese")
    else:
        print("clinically obese")

print_health_quotes()

Berat = float(input("Berat dalam KG: "))
Tinggi = input("Tinggi dalam meter: ")

nilaiBMI = calculateBMI(Berat, Tinggi)
print("BMI:", nilaiBMI)

print("Classification: ")
classifyBMI(nilaiBMI)