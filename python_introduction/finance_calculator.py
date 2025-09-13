# CLI finance calculator that computes monthly savings and annual savings with interest.
# Assumes a fixed interest rate of 5% for annual savings projection.
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are:", monthly_savings)

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:", projected_annual_savings)