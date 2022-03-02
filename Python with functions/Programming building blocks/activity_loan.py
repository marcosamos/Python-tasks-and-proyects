# Este programa realiza el analisis de una persona para solicitar un prestamo.


print("Please  insert the rating between 1 to 10 for answer the questions.")

large_loan = int(input("How large is the loan? ")) 
good_credit_history = int(input("How good is your credit history? "))
high_income = int(input("How high is your income? "))
large_down_payment = int(input("How large is your down payment? "))
should_loan = False
if large_loan >= 5:
    if good_credit_history >= 7 and high_income >= 7:
        should_loan = True
    elif good_credit_history >= 7 or high_income >= 7:
        if large_down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else: #This means its small loan
    if good_credit_history < 4:
        should_loan = False
    else:
        if high_income >= 7 or large_down_payment >= 7:
            should_loan = True
        elif high_income >= 4 and large_down_payment >= 4:
            should_loan = True
        else:
            should_loan = False
if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")