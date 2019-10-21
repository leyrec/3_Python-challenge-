#1.IMPORT libraries
import pandas as pd

#2.FIND the file
filepath = "budget_data.csv"

#3.READ the file
df = pd.read_csv(filepath)

#4.CREATE variables to storage the values and make the calculations needed

#Count the total number of Months for the total period
Total_Month = df["Date"].count()

#Sum the total net Revenues for the total period
Net_Profit_Losses = df["Profit/Losses"].sum()

#Create a new column to storage the changes in profits 
Changes =  df ["Profit/Losses"]  

#Calculate the changes in Profit/Loss
df["Changes"] = df["Profit/Losses"].diff() 
    
#Calculate the Average Change of Profit/Loss for the total period
Average_Change = df["Changes"].mean()

#Calculate the Greatest increase and decrease for the total period    
    
Greatest_increase = df["Changes"].max()
Greatest_decrease = df["Changes"].min()
 
#Index the DF related to the increases/decreases in order to locate the corresponding months 
Indexeddf = df.set_index("Changes")

MaxDate = Indexeddf.loc[Greatest_increase, "Date"]
MinDate = Indexeddf.loc[Greatest_decrease, "Date"]    

    
#4. PRINT the results

print(f"FINANCIAL ANALYSIS")
print(f"-----------------------------------------")
print(f"Total Months: " + str(Total_Month))
print(f"Total: $" + str(Net_Profit_Losses))
print(f"Average Change: $" + str(round(Average_Change, 2))) 
print(f"Greatest Increase In Profits: " + str(MaxDate) + " $" + str(Greatest_increase))
print(f"Greatest Decrease In Profits: " + str(MinDate)+ " $" + str(Greatest_decrease)) 
    

#5.CREATE a text file with the results
        
with open('Budget_Data.txt', 'w+', newline = "\n") as w:
    w.write("Financial Analysis\n")
    w.write('----------------------------\n')
    w.write('Total Months: 86\n')
    w.write('Total: $38382578\n')
    w.write('Average Change: $-2315.12\n')
    w.write('Greatest Increase in Profits: Feb-2012 ($1926159)\n')
    w.write('Greatest Decrease in Profits: Sep-2013 ($-2196167)\n')



