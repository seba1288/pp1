
height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))
height = height/100
bmi_index = round(weight/ height ** 2,2)
print('Your BMI index: ',bmi_index)
if bmi_index <= 24.99 and bmi_index >= 18.5:
    print('Correct weight: True')
else:
    print('Correct weight: False')


