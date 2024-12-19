# script to calculate potential future savings
# prompt user for inputs
monthly_income = float(input("Enter your monthly salary: ")); 
monthly_expenses = float(input("Enter your total monthly expenses: ")); 

# calculate monthly salary
monthly_savings = monthly_income - monthly_expenses; 

# calculate projected savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) 

print(f"Your monthly savings are: GHC${monthly_savings}"); 
print(f"Projected savings after one year, with interest is: GHC${projected_savings}"); 
