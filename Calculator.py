from Class import Tax_Bracket

# Variables
monthly_sal = input("How much is your monthly salary: ")
donation = 0
epf_perc = 0.09
socso_perc = 0.004115

taxbrac_1 = 5000
taxbrac_2 = 15000
taxbrac_3 = 15000
taxbrac_4 = 15000
taxbrac_5 = 20000
taxbrac_6 = 30000

taxbrac_1prec = 0
taxbrac_2perc = 0.01
taxbrac_3perc = 0.03
taxbrac_4perc = 0.08
taxbrac_5perc = 0.13
taxbrac_6perc = 0.21

def calc_tax (monthly_sal):
    epf = float(monthly_sal) * epf_perc * 12
    print(epf)
    socso = float(monthly_sal) * socso_perc * 12
    print(socso)
    annual_sal = monthly_sal * 12

    total_relief = round(9000 + epf + socso,2)
    print(total_relief)
    chargeable_income = float(annual_sal) - donation - total_relief
    print(chargeable_income)

a = calc_tax(monthly_sal)
print(a)





