print("Decision Tree Example")

age = int(input("Enter Age: "))
income = int(input("Enter Monthly Income: "))

if age >= 18:
    if income >= 30000:
        print("Prediction: Eligible for Loan")
    else:
        print("Prediction: Not Eligible for Loan")
else:
    print("Prediction: Not Eligible for Loan")
