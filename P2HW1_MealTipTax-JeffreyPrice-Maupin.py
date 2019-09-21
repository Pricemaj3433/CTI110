#This program will calculate the total cost of your meal
#Date: 9/18/2019
#CTI-110 P2HW1 - Meal Tip Tax Calulator
#Jeffrey Price-Maupin
#
#Ask for food charge
#Ask for Tip amount
#Ask for Tax amount
#Calculate Tip and Tax
#Display calculate Tip, Tax anf Total cost of meal

#Ask for food price
foodprice = float(input("Enter the charge for food:"))
#Ask for the tip amount
tip = float(input("Enter the Tip percentage:"))
#Ask for the tax amount
tax = float(input("Enter the Tax percentage:"))

#calulate the Tip and Tax amount
calc_tip = foodprice * tip
calc_tax = foodprice * tax

#Calclate the total
total = foodprice + calc_tip + calc_tax

#Display calculate Tip, Tax anf Total cost of meal
print("Tip amount: $", format(calc_tip,'.2f' ),sep="")
print("Tax amount: $", format(calc_tax ,'.2f' ),sep="")
print("Your total amount paid is: $",format(total ,'.2f' ),sep="")
