# This program will calculate sales tax
# Date-9/20/2019
# CTI-110 P2T1 - Sales Prediction
# Jeffrey Price-Maupin

#Ask user tp enter projected amoun of total sales
#Display the profit to be made from purchase


#Get the projected sales
total_sales = float(input("Enter the projected sales:"))

#calculate the profit as 23 percent of sales.
profit = total_sales * .23

#Display the profit
print("The profit is $",format(profit,".2f"),sep=(""))

