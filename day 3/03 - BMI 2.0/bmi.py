weight = float(input('Introduzca su peso en kg, porfavor: '))
height = float(input('Introduzca su altura en metros, porfavor: '))

bmi = (weight / (height * height))
bmi_formatted = f"{bmi:.1f}"

if bmi < 18.5:
    print(f'su BMI es {bmi_formatted} y es clasificado como underweight')
elif bmi >= 18.5 and bmi < 25:
    print(f'su BMI es {bmi_formatted} y es clasificado como normal')
elif bmi >= 25 and bmi < 30:
    print(f'su BMI es {bmi_formatted} y es clasificado como overweight')
elif bmi >= 30 and bmi < 35:
    print(f'su BMI es {bmi_formatted} y es clasificado como obese')
else:
    print(f'su BMI es {bmi_formatted} y es clasificado como clinically obese')