from Class import Tax_Bracket
import json
import numpy as np
import sys

# Variables
# try:
#     monthly_sal = float(input("How much is your monthly salary?: "))
# except:
#     print("Invalid amount")
#     sys.exit(1)

# try:
#     donation = float(input("How much are your donations?: "))
# except:
#     print("Invalid amount")
#     sys.exit(1)

# try:
#     deductibles = float(input("How much are your deductibles after restriction"
#                               " (eg. lifestyle purchase, medical, insurance...)?: "))
# except:
#     print("Invalid amount")
#     sys.exit(1)

# epf_q = input("Is your EPF percentage 9%? (True/False): ")

socso_perc = 0.004115

# personal relief
self = 9000

# Tax Bracket 2021
tax_array = []
tax_array.append(Tax_Bracket(5000, 0))
tax_array.append(Tax_Bracket(15000, 0.01))
tax_array.append(Tax_Bracket(15000, 0.03))
tax_array.append(Tax_Bracket(15000, 0.08))
tax_array.append(Tax_Bracket(20000, 0.13))
tax_array.append(Tax_Bracket(30000, 0.21))
tax_array.append(Tax_Bracket(150000, 0.24))
tax_array.append(Tax_Bracket(150000, 0.245))
tax_array.append(Tax_Bracket(200000, 0.25))
tax_array.append(Tax_Bracket(400000, 0.26))
tax_array.append(Tax_Bracket(1000000, 0.28))
tax_array.append(Tax_Bracket(9999999, 0.3))

__data_columns = None

def calc_tax(monthlysalary, donations, deductibles, percentage, debug=False):
    
    # Percentage switch
    if percentage == 1:
        percentage = 0.09
    else:
        percentage = 0.12
    
    # converting variables from monthly to annually
    annual_epf = monthlysalary * percentage * 12
    annual_socso = monthlysalary * socso_perc * 12
    annual_sal = monthlysalary * 12

    # all reliefs
    total_relief = round(self + donations + deductibles + annual_epf + annual_socso, 2)
    # chargeable_income is the final amount gov can tax from you
    chargeable_income = float(annual_sal) - total_relief

    # individual rebate deduction
    if chargeable_income < 35000:
        rebate = 400
    else:
        rebate = 0



    loop_cnt = 0
    total_tax = 0\
    # loop through each tax bracket until chargeable_income is less than 0
    while chargeable_income >= 0:
        # 
        total_tax += min(chargeable_income, tax_array[loop_cnt].amount) * tax_array[loop_cnt].rate
        # 
        
        chargeable_income -= tax_array[loop_cnt].amount
        # 
        
        loop_cnt += 1
        
    calc_amt = round(total_tax - rebate, 2)
    final_tax = (abs(calc_amt)+calc_amt)/2
    
    if debug == True:
        print("monthlysalary: " + str(monthlysalary))
        print("donations: " + str(donations))
        print("deductibles: " + str(deductibles))
        print("percentage: " + str(percentage))
        
        print("annual_epf: "+str(annual_epf))
        print("annual_socso: "+str(annual_socso))
        print("annual_sal: "+str(annual_sal))
        
        print("total_relief: "+str(total_relief))
        print("self: "+str(self))
        print("donations: "+str(donations))
        
        print("chargeable_income: "+str(chargeable_income))
        print("rebate: "+str(rebate))
        print("loop_cnt: "+str(loop_cnt))
        
        print("total_tax: "+str(total_relief))
        
        print("calc_amt: "+str(calc_amt))
        
        print("final_tax: "+str(final_tax))
    
    return final_tax

# print(calc_tax(monthly_sal))

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("./columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']


def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(calc_tax(4800,100, 100, 0.09))


