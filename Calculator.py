from Class import Tax_Bracket
import json

# Socso percentage
socso_perc = 0.004115

# Personal relief
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

def calc_tax(monthlysalary, donations, deductibles, epf_perc, debug=False):
    
    # Convert radio buttons to EPF percentage
    if epf_perc == 1:
        epf_perc = 0.09
    else:
        epf_perc = 0.12
    
    # Convert variables from monthly to annually
    annual_epf = monthlysalary * epf_perc * 12
    annual_socso = monthlysalary * socso_perc * 12
    annual_sal = monthlysalary * 12

    # Total reliefs
    total_relief = round(self + donations + deductibles + annual_epf + annual_socso, 2)
    # chargeable_income is the final amount gov can tax from you
    chargeable_income = float(annual_sal) - total_relief

    # Rebate deduction for lower income individuals
    if chargeable_income < 35000:
        rebate = 400
    else:
        rebate = 0

    # Main tax calculation
    loop_cnt = 0
    total_tax = 0

    # Loop through each tax bracket until chargeable_income is less than or equal to 0
    while chargeable_income >= 0:
        # Summing up tax amount after looping through each tax bracket based on available chargeable income
        total_tax += min(chargeable_income, tax_array[loop_cnt].amount) * tax_array[loop_cnt].rate
        chargeable_income -= tax_array[loop_cnt].amount
        loop_cnt += 1

    calc_amt = round(total_tax - rebate, 2)
    final_tax = (abs(calc_amt)+calc_amt)/2

    # To turn on debugging, manually change debug=True in the function parameter
    if debug == True:
        print("monthlysalary: " + str(monthlysalary))
        print("donations: " + str(donations))
        print("deductibles: " + str(deductibles))
        print("epf_perc: " + str(epf_perc))
        print("annual_epf: " + str(annual_epf))
        print("annual_socso: " + str(annual_socso))
        print("annual_sal: " + str(annual_sal))
        print("total_relief: " + str(total_relief))
        print("self: " + str(self))
        print("donations: " + str(donations))
        print("chargeable_income: " + str(chargeable_income))
        print("rebate: " + str(rebate))
        print("loop_cnt: " + str(loop_cnt))
        print("total_tax: " + str(total_relief))
        print("calc_amt: " + str(calc_amt))
        print("final_tax: " + str(final_tax))
    
    return final_tax


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns

    with open("./columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']


def get_data_columns():
    return __data_columns




