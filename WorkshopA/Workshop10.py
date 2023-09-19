def NisitName():
    Name = input('กรอกชื่อ : ')
    return Name

def NisitYear():
    Year = int(input('กรอกปี : '))  # แปลงปีเป็น integer
    return Year

def WelcometoSAU(Year):
    if Year == 1:
        print('Welcome Freshman')
    elif Year == 2:
        print("Welcome Sophomore")
    elif Year == 3:
        print("Welcome Junior")
    elif Year == 4:
        print("Welcome Senior")

Name = NisitName()
Year = NisitYear()
WelcometoSAU(Year)








