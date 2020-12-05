#输出结果与题目给定值不同，但如果用ps1b改造程序验证所得数值是否正确的话，也是能算出来number_of_months=36，所以可能是计算时候的精度问题导致的
import sys
#给定条件
semi_annual_raise=0.07
r=0.04
step_in_bisection_search=0
total_cost=1000000
portion_down_payment=0.25
#portion_saved 是所求量
portion_saved=[0,10000]


print('please enter the annual salary:')
annual_salary=set_value=float(input())
current_savings=0
number_of_months=0


while(current_savings<total_cost*portion_down_payment):
        current_savings=annual_salary/12+current_savings*(1+r/12)
        number_of_months=number_of_months+1
        if(number_of_months%6==0):
             annual_salary=annual_salary+annual_salary*semi_annual_raise
if (number_of_months > 36):
        print('It is not possible to pay the down payment in three years')
        sys.exit()
print(number_of_months)
#reset
number_of_months = 0
annual_salary=set_value
current_savings=0

while(True):
    while(current_savings<total_cost*portion_down_payment):
        current_savings=annual_salary/12*(portion_saved[1]+portion_saved[0])/20000\
                        +current_savings*(1+r/12)
        number_of_months=number_of_months+1
        if((number_of_months%6==0)):
             annual_salary=annual_salary+annual_salary*semi_annual_raise
    if (number_of_months == 36):
        print('have found it !!!!!')
        print('the value is:', (portion_saved[1] + portion_saved[0]) / 20000.0)
        portion_saved[1] = (portion_saved[1] + portion_saved[0]) // 20000
        break
    if(number_of_months < 36):
            portion_saved[1] = (portion_saved[0] + portion_saved[1])//2
            #print new Interval
            print( portion_saved[0],portion_saved[1])
            #reset
            number_of_months = 0
            current_savings=0
            annual_salary = set_value

            step_in_bisection_search = step_in_bisection_search+1
    if (number_of_months > 36):
            portion_saved[0] = (portion_saved[0] + portion_saved[1])//2
            #print new Interval
            print(portion_saved[0], portion_saved[1])

            #reset
            number_of_months = 0
            current_savings = 0
            annual_salary = set_value

    step_in_bisection_search = step_in_bisection_search + 1



print(float(portion_saved[1])/10000)
print(step_in_bisection_search)






