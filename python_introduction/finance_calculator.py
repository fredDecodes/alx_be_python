# script to calculate potential future savings
monthly_income = int(input("Enter your monthly salary: ")); 
monthly_expense = int(input("Enter your total monthly expenses: ")); 
interest_rate = 0.05; 
months_in_year = 12; 

monthly_savings = monthly_income - monthly_expense; 
annual_savings = monthly_savings * months_in_year; 

interest = monthly_savings * months_in_year * interest_rate; 
projected_savings = annual_savings + interest; 

print("Your monthly savings are: GHC" + str(monthly_savings)); 
print("Projected savings after one year, with interest is: GHC" + str(projected_savings)); 
