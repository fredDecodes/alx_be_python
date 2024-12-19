# script to calculate potential future savings
monthly_income = float(input("Enter your monthly salary: ")); 
monthly_expenses = float(input("Enter your total monthly expenses: ")); 
interest_rate = 0.05; 
months_in_year = 12; 

monthly_savings = monthly_income - monthly_expenses; 
annual_savings = monthly_savings * months_in_year; 

interest = monthly_savings * months_in_year * interest_rate; 
projected_savings = annual_savings + interest; 

print(f"Your monthly savings are: GHC${monthly_savings}"); 
print(f"Projected savings after one year, with interest is: GHC${projected_savings}"); 
