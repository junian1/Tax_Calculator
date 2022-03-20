from Class import Tax_Bracket

# Variables
monthly_sal = float(input("How much is your monthly salary: "))
donation = float(input("How much is your deduction (donation): "))
epf_perc = 0.09
socso_perc = 0.004115

tax_bracket1 = Tax_Bracket(5000, 0)
tax_bracket2 = Tax_Bracket(15000, 0.01)
tax_bracket3 = Tax_Bracket(15000, 0.03)
tax_bracket4 = Tax_Bracket(15000, 0.08)
tax_bracket5 = Tax_Bracket(20000, 0.13)
tax_bracket6 = Tax_Bracket(30000, 0.21)

def calc_tax (monthly_sal):
    epf = monthly_sal * epf_perc * 12
    socso = monthly_sal * socso_perc * 12
    annual_sal = monthly_sal * 12

    total_relief = round(9000 + epf + socso, 2)
    chargeable_income = float(annual_sal) - donation - total_relief

    total_tax = 0
    remainder = 0
    if chargeable_income >= tax_bracket1.amount:
        total_tax = tax_bracket1.amount * tax_bracket1.rate
        remainder = chargeable_income - tax_bracket1.amount
        if remainder > 0:
            total_tax += min(remainder, tax_bracket2.amount) * tax_bracket2.rate
            remainder -= tax_bracket2.amount
            if remainder > 0:
                total_tax += min(remainder, tax_bracket3.amount) * tax_bracket3.rate
                remainder -= tax_bracket3.amount
                if remainder > 0:
                    total_tax += min(remainder, tax_bracket4.amount) * tax_bracket4.rate
                    remainder -= tax_bracket4.amount
                    if remainder > 0:
                        total_tax += min(remainder, tax_bracket5.amount) * tax_bracket5.rate
                        remainder -= tax_bracket5.amount
    final_tax = round(total_tax - 400, 2)
    return(final_tax)

a = calc_tax(monthly_sal)
print(a)





