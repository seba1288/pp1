father_income = int(input('father income: '))
mother_income = int(input('father income: '))
fam_num = int(input('famili number:'))
total_income = F'total income {(father_income + mother_income)}\n'
income_per = f'income per person {(father_income + mother_income)//fam_num}'
print(total_income,income_per)