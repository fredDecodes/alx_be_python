# script to calculate age of user
'''
future_year = 2050
asumme current_year = 2023
'''
current_year = 2023; 
future_year = 2050; 
year_interval = future_year - current_year; 

current_age = input("How old are your\?\s"); 

age = int(current_age) + year_interval; 
print("In " + str(future_year) + ", you will be " + str(age) + " years old."); 
