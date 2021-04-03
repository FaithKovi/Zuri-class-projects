import datetime

now = datetime.datetime.now()
print("Current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))

print("Input your ATM card")
password = input("What is your password? \n")
currentBalance = 50000

optionList = "Select from the following options: \n 1. Withdraw \n 2. Deposit \n 3. Complaint"
print(optionList)
 
selectedOption = int(input("Select an option: "))

if (selectedOption == 1):
    withdraw = int(input("How much would you like to withdraw? \n"))
    balance = currentBalance - withdraw
    print("Your current balance: %d "%balance)
    print("Take your cash")
elif (selectedOption == 2):
    deposit = int(input("How much would you like to deposit? \n"))
    balance = currentBalance + deposit
    print("Your current balance: %d "%balance)
elif (selectedOption == 3):
    complaint = input("What issue would you like to report? \n")
    print("Thank you for contacting us")
else:
    print("Input a valid number")
