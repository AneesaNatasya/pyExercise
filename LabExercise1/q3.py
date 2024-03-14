carPrice = 90000
interestRate = 0.027
monthInYear = 12
downPayment = float(input("Plase enter your downpayment: "))
loan_period_years = int(input("How long you want to make a loan in year(1 to 9 years only):"))

min_down_payment = carPrice * 0.10

if downPayment < min_down_payment:
    print("You are eligible for the bank loan.")
    
else:
    loan_amount = carPrice - downPayment
    total_interest = interestRate * loan_amount * loan_period_years
    totalLoanAmount = loan_amount + total_interest
    
    loan_period_month = loan_period_years * monthInYear
    monthly_installment = totalLoanAmount / loan_period_month
    
    print("You need to pay RM", round(monthly_installment, 2), "monthly as your monthly payment.")