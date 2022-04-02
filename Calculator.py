from Class import Tax_Bracket
import sys

# Variables
try:
    monthly_sal = float(input("How much is your monthly salary?: "))
except:
    print("Invalid amount")
    sys.exit(1)

try:
    donation = float(input("How much are your donations?: "))
except:
    print("Invalid amount")
    sys.exit(1)

try:
    deductibles = float(input("How much are your deductibles after restriction"
                              " (eg. lifestyle purchase, medical, insurance...)?: "))
except:
    print("Invalid amount")
    sys.exit(1)

epf_q = input("Is your EPF percentage 9%? (True/False): ")

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


def calc_tax(monthly_sal):
    if epf_q.lower() == 'true':
        epf_perc = 0.09
    elif epf_q.lower() == 'false':
        epf_perc = 0.12
    else:
        return("Invalid response")

    # converting variables from monthly to annually
    annual_epf = monthly_sal * epf_perc * 12
    annual_socso = monthly_sal * socso_perc * 12
    annual_sal = monthly_sal * 12

    # all reliefs
    total_relief = round(self + donation + deductibles + annual_epf + annual_socso, 2)
    # chargeable_income is the final amount gov can tax from you
    chargeable_income = float(annual_sal) - total_relief

    # individual rebate deduction
    if chargeable_income < 35000:
        rebate = 400
    else:
        rebate = 0

    loop_cnt = 0
    total_tax = 0

    # loop through each tax bracket until chargeable_income is less than 0
    while chargeable_income >= 0:
        total_tax += min(chargeable_income, tax_array[loop_cnt].amount) * tax_array[loop_cnt].rate
        chargeable_income -= tax_array[loop_cnt].amount
        loop_cnt += 1
    calc_amt = round(total_tax - rebate, 2)
    final_tax = (abs(calc_amt)+calc_amt)/2
    return final_tax


print(calc_tax(monthly_sal))