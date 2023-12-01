import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
outcome = os.path.join("analysis","budget_analysis.txt")


months = 0
month_change =[]
pybank_change =[]
Net_total = 0
greatest_increase =["",0]
greatest_decrease = ["",100000000000]

with open(csvpath) as PyBank:
    reader = csv.reader(PyBank)
    header = next(reader)
    row_one = next(reader)
    months += 1
    Net_total += int(row_one[1])
    old_net = int(row_one[1])
    for row in reader:
        months += 1
        Net_total += int(row[1])
        net_change =int(row[1])-old_net
        pybank_change +=[net_change]
        month_change +=[row[0]]
        if net_change>greatest_increase[1]: 
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change<greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        old_net = int(row[1])
        

average_net_monthly =sum(pybank_change)/len(pybank_change)

output=(
    f"Financial Analysis\n"
    f"---------------------------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${Net_total}\n"
    f"Average Change: ${average_net_monthly:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)










    

