age = int(input("What is your current age?: "))
ageLimit = 90
resultAge = ageLimit - age
print(resultAge)
inDays = 365 * resultAge
inWeeks = 52 * resultAge
inMonths = 12 * resultAge

print(f"You have {inDays} days, {inWeeks} weeks, and {inMonths} months left.")

