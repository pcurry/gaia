# this sub-program covers step 4 ("Star System Age") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

Population = None
base_age = None
age_range = None
roll_for_stellar_population = d100()

if 1 <= roll_for_stellar_population <= 42: 
    Population = "Young Population I"
    Base_Age = 0.0
    Age_Range = 2.0
elif 43 <= roll_for_stellar_population <= 76: 
    Population = "Intermediate Population"
    Base_Age = 2.0
    Age_Range = 1.0
elif 77 <= roll_for_stellar_population <= 95: 
    Population = "Old Population I"
    Base_Age = 5.0
    Age_Range= 3.0
elif 96 <= roll_for_stellar_population <= 99: 
    Population = "Disk Population II"
    Base_Age = 8.0
    Age_Range = 1.5
elif 100 == roll_for_stellar_population: 
    Population = "Halo Population II"
    Base_Age = 9.5
    Age_Range = 3.0

roll_for_age_range = d100()
system_age = Base_Age + (Age_Range*(roll_for_age_range/100))

print(f"Stellar Population: {Population}")
system_age = round(system_age, 2)
print(f"System Age: {system_age} Gyr")
