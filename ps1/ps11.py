print('please input the starting annual salary(annual_salary):')
annual_salary=float(input())
print('please input The portion of salary to be saved (portion_saved):')
portion_saved=float(input())
print("The cost of your dream home (total_cost):")
total_cost=float(input())

portion_down_payment=0.25
current_savings=0
number_of_months=0
savings=0
r=0.04
while(current_savings<total_cost*portion_down_payment):
    current_savings=annual_salary/12*portion_saved+current_savings*(1+r/12)
    number_of_months=number_of_months+1
print(number_of_months)
