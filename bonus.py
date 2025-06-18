Wieght = input("Enter your Wieght: ")
Height = input("Enter your Height: ")
BMI = float(Wieght) / (float(Height) ** 2)

if BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI <= 24.9 and BMI >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")

#i found that it A BMI between 18.5 and 24.9 is generally considered healthy, while a BMI of 25 or higher may indicate overweight or obesity, and a BMI below 18.5 may indicate underweigh
#the formula was (BMI = kg/m²)
