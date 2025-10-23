import math

from planetary_system_data.dataclasses_and_enumerations import Star


def temperature_of_low_mass_star(mass: float, age: float) -> float:
    return 18600 * ((mass ** 0.8) / (age ** 0.3))


def steller_conditions(star: Star, system_age: float) -> Star:
    
    mass_to_the_4th = star.mass ** 4
    mass_to_the_3rd = star.mass ** 3
    mass_to_the_2nd = star.mass ** 2

    def fourth_power_equation_in_mass(a: float, b: float, c: float, d: float, e: float) -> float:
        return a * mass_to_the_4th + b * mass_to_the_3rd + c * mass_to_the_2nd + d * mass + e
    
    if star.mass < 0.08:
        star.effective_temperature = temperature_of_low_mass_star(star.mass, system_age)
        star.luminosity = (star.effective_temperature ** 4) / (1.1e+17)
        star.main_sequence_lifespan = (1 / (star.mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= star.mass <= 0.5:
        star.effective_temperature = fourth_power_equation_in_mass(-78806, 125050, -74194, 20692, 1272.2)
        star.luminosity = fourth_power_equation_in_mass(2.1901, -2.2436, 0.919, -0.1023, 0.0039)
        star.main_sequence_lifespan = (1 / (star.mass ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe
        
    else:  # mass > 0.5
        star.initial_effective_temperature = fourth_power_equation_in_mass(15.992, -198.64, 578.86, 3020.1, 2060)
        star.final_effective_temperature = fourth_power_equation_in_mass(15.893, 154.37, 384.94, 2105.7, 3631.6)
        star.initial_luminosity = fourth_power_equation_in_mass(-0.2707, 10.15, 28.137, 31.268, 11.559)
        if star.mass <= 4:
            star.luminosity_growth_rate = (
                0.8295 * (star.mass ** 6) - 9.2448 * (star.mass ** 5) + 
                fourth_power_equation_in_mass(40.931, -90.562, 104.59, -59.148, 13.745)
            )
        else:  # mass > 4
            star.luminosity_growth_rate = (0.000005 ** (3.9985 * star.mass)) 
        
        star.main_sequence_lifespan = 11.452 * (star.mass ** -3.157)
        star.effective_temperature = (
            star.initial_effective_temperature + 
            (system_age / star.main_sequence_lifespan) * 
            (star.final_effective_temperature - star.initial_effective_temperature)
        )

        if system_age <= (0.8 * star.main_sequence_lifespan):
            growth_rate_power = system_age
        else:  # system_age > (0.8 * Main_Sequence_Lifespan_of_Star_A)
            growth_rate_power = (
                3 * system_age - 1.6 * star.main_sequence_lifespan
            )
        star.luminosity = star.initial_luminosity * (star.luminosity_growth_rate ** growth_rate_power)
        
    star.radius = (
        155000 * ((math.sqrt(star.luminosity)) / (star.effective_temperature ** 2))
        if 0.08 <= star.mass
        else 0.00047 
    )
    star.effective_temperature = round(star.effective_temperature, 1)
    star.luminosity = round(star.luminosity, 5)
    star.radius = round(star.radius, 5)
    print(f"Effective Temperature of {star.name} {star.effective_temperature} Kelvin")
    print(f"Luminosity of {star.name}: {star.luminosity} solar luminosities")
    print(f"Radius of {star.name}: {star.radius} AU")
    return star


def evolve_star_system(star_system, system_age: float):
    print("\n--- Step 6: Stellar Evolution ---")
    print(f"System Age: {system_age} billion years\n")
    number_of_stars = star_system.number_of_stars
    print(f"Number of Stars in System: {number_of_stars}\n")
    
    if number_of_stars >= 1:
        star_system.star_A = steller_conditions(star_system.star_A, system_age)
    if number_of_stars >= 2:
        star_system.star_B = steller_conditions(star_system.star_B, system_age)
    if number_of_stars >= 3:
        star_system.star_C = steller_conditions(star_system.star_C, system_age)
    if number_of_stars == 4:
        star_system.star_D = steller_conditions(star_system.star_D, system_age)
    
    determine_evolutionary_stage(star_system, system_age)
    return star_system


Evolutionary_Stage_of_Star_A = None
Evolutionary_Stage_of_Star_B = None
Evolutionary_Stage_of_Star_C = None
Evolutionary_Stage_of_Star_D = None

if Number_of_Stars >= 1:
    if system_age < Main_Sequence_Lifespan_of_Star_A:
        Evolutionary_Stage_of_Star_A = "Main Sequence"
        print("Star A is still on the main sequence")
        # If the system’s age is less than the star’s Main Sequence Lifespan, then the star is still on the main sequence.

    if Main_Sequence_Lifespan_of_Star_A <= system_age <= (1.15 * Main_Sequence_Lifespan_of_Star_A):
        print("Star A has evolved beyond the Main Sequence")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by no more than 15%, then the star will be a subgiant or red giant
        roll_for_giant_type = d100()
        if roll_for_giant_type <= 60:
            Evolutionary_Stage_of_Star_A = "Subgiant"
            print("Specifically - Star A has evolved into a subgiant")
            # On a roll of 01-60, the star is a subgiant
            Luminosity_of_Star_A = Initial_Luminosity_of_Star_A * (Luminosity_Growth_Rate_of_Star_A ** (1.4 * Main_Sequence_Lifespan_of_Star_A))
            print(f"Luminosity of Star A has increased to: {Luminosity_of_Star_A} solar luminosities")

        if 61 <= roll_for_giant_type <= 90:
            Evolutionary_Stage_of_Star_A = "Red Giant Branch"
            print("Specifically Star has evolved onto the Red Giant Branch")
            # On a roll of 61-90, the star is on the red giant branch
            roll_for_red_giant_varriable = (d100() / 100)
            Temperature_Effective_of_Star_A = 5000 - (roll_for_red_giant_varriable * 2000)
            Luminosity_of_Star_A = 50 ** (1 + roll_for_red_giant_varriable)
            print(f"Temperature of Star A has cooled to: {Temperature_Effective_of_Star_A} Kelvin")
            print(f"Luminosity of Star A has increased to: {Luminosity_of_Star_A} solar luminosities")

        if 91 <= roll_for_giant_type <= 100:
            Evolutionary_Stage_of_Star_A = "Horizonal Branch"
            print("Specifically Star A has evolved onto the Horizontal Branch")
            # On a roll of 91-00, the star is on the horizontal branch
            Temperature_Effective_of_Star_A = 5000
            print("Temperature of Star A is now approximately 5000 Kelvin")
            roll_for_horizontal_giant_varriable = d100()
            Luminosity_of_Star_A = 50 + (roll_for_horizontal_giant_varriable / 2)
            print(f"Luminosity of Star A has increased to: {Luminosity_of_Star_A} solar luminosities")

        Radius_of_Star_A = 155000 * ((math.sqrt(Luminosity_of_Star_A))/(Temperature_Effective_of_Star_A * Temperature_Effective_of_Star_A))
        Radius_of_Star_A = round(Radius_of_Star_A, 5)
        print(f"Radius of Star A has evolved to: {Radius_of_Star_A} AU")

    if system_age > (1.15 * Main_Sequence_Lifespan_of_Star_A):
        Evolutionary_Stage_of_Star_A = "White Dwarf"
        print("Star A has evolved into a White Dwarf")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by more than 15%, then the star will have become a white dwarf
        Mass_WDA = 0.43 + (Mass_A / 10.4)
        Mass_WDA = round(Mass_WDA, 2)
        print(f"Mass of Star A has decreased to: {Mass_WDA} solar masses")
        Temperature_Effective_of_White_Dwarf_A = 13500 * ((Mass_WDA ** 0.25) / (((system_age - (1.15 * Main_Sequence_Lifespan_of_Star_A)) ** 0.35)))
        Temperature_Effective_of_White_Dwarf_A = round(Temperature_Effective_of_White_Dwarf_A, 1)
        print(f"Temperature of Star A has evolved to: {Temperature_Effective_of_White_Dwarf_A} Kelvin")
        Radius_of_White_Dwarf_A = 5500 / (math.cbrt(Mass_WDA))
        Radius_of_White_Dwarf_A = round(Radius_of_White_Dwarf_A, 1)
        print(f"Radius of Star A has decreased to: {Radius_of_White_Dwarf_A} kilometers")
        Luminosity_of_White_Dwarf_A = ((Radius_of_White_Dwarf_A ** 2) * (Temperature_Effective_of_White_Dwarf_A ** 4))/ (5.4e26)
        Luminosity_of_White_Dwarf_A = round(Luminosity_of_White_Dwarf_A, 5)
        print(f"Luminosity of Star A has evolved to: {Luminosity_of_White_Dwarf_A} solar lumunosities")






if Number_of_Stars >= 2:
    if system_age < Main_Sequence_Lifespan_of_Star_B:
        Evolutionary_Stage_of_Star_B = "Main Sequence"
        print("Star B is still on the main sequence")
        # If the system’s age is less than the star’s Main Sequence Lifespan, then the star is still on the main sequence.

    if Main_Sequence_Lifespan_of_Star_B <= system_age <= (1.15 * Main_Sequence_Lifespan_of_Star_B):
        print("Star B has evolved beyond the Main Sequence")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by no more than 15%, then the star will be a subgiant or red giant
        roll_for_giant_type = d100()
        if roll_for_giant_type <= 60:
            Evolutionary_Stage_of_Star_B = "Subgiant"
            print("Specifically - Star B has evolved into a subgiant")
            # On a roll of 01-60, the star is a subgiant
            Luminosity_of_Star_B = Initial_Luminosity_of_Star_B * (Luminosity_Growth_Rate_of_Star_B ** (1.4 * Main_Sequence_Lifespan_of_Star_B))
            print(f"Luminosity of Star B has increased to: {Luminosity_of_Star_B} solar luminosities")
        
        if 61 <= roll_for_giant_type <= 90:
            Evolutionary_Stage_of_Star_B = "Red Giant Branch"
            print("Specifically Star has evolved onto the Red Giant Branch")
            # On a roll of 61-90, the star is on the red giant branch
            roll_for_red_giant_varriable = (d100() / 100)
            Temperature_Effective_of_Star_B = 5000 - (roll_for_red_giant_varriable * 2000)
            Luminosity_of_Star_B = 50 ** (1 + roll_for_red_giant_varriable)
            print(f"Temperature of Star B has cooled to: {Temperature_Effective_of_Star_B} Kelvin")
            print(f"Luminosity of Star B has increased to: {Luminosity_of_Star_B} solar luminosities")

        if 91 <= roll_for_giant_type <= 100:
            Evolutionary_Stage_of_Star_B = "Horizonal Branch"
            print("Specifically Star B has evolved onto the Horizontal Branch")
            # On a roll of 91-00, the star is on the horizontal branch
            Temperature_Effective_of_Star_B = 5000
            print("Temperature of Star B is now approximately 5000 Kelvin")
            roll_for_horizontal_giant_varriable = d100()
            Luminosity_of_Star_B = 50 + (roll_for_horizontal_giant_varriable / 2)
            print(f"Luminosity of Star B has increased to: {Luminosity_of_Star_B} solar luminosities")

        Radius_of_Star_B = 155000 * ((math.sqrt(Luminosity_of_Star_B))/(Temperature_Effective_of_Star_B * Temperature_Effective_of_Star_B))
        Radius_of_Star_B = round(Radius_of_Star_B, 5)
        print(f"Radius of Star B has evolved to: {Radius_of_Star_B} AU")

    if system_age > (1.15 * Main_Sequence_Lifespan_of_Star_B):
        Evolutionary_Stage_of_Star_B = "White Dwarf"
        print("Star B has evolved into a White Dwarf")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by more than 15%, then the star will have become a white dwarf
        Mass_WDB = 0.43 + (Mass_B / 10.4)
        Mass_WDB = round(Mass_WDB, 2)
        print(f"Mass of Star B has decreased to: {Mass_WDB} solar masses")
        Temperature_Effective_of_White_Dwarf_B = 13500 * ((Mass_WDB ** 0.25) / (((system_age - (1.15 * Main_Sequence_Lifespan_of_Star_B)) ** 0.35)))
        Temperature_Effective_of_White_Dwarf_B = round(Temperature_Effective_of_White_Dwarf_B, 1)
        print(f"Temperature of Star B has evolved to: {Temperature_Effective_of_White_Dwarf_B} Kelvin")
        Radius_of_White_Dwarf_B = 5500 / (math.cbrt(Mass_WDB))
        Radius_of_White_Dwarf_B = round(Radius_of_White_Dwarf_B, 1)
        print(f"Radius of Star B has decreased to: {Radius_of_White_Dwarf_B} kilometers")
        Luminosity_of_White_Dwarf_B = ((Radius_of_White_Dwarf_B ** 2) * (Temperature_Effective_of_White_Dwarf_B ** 4)) / (5.4e26)
        Luminosity_of_White_Dwarf_B = round(Luminosity_of_White_Dwarf_B, 5)
        print(f"Luminosity of Star B has evolved to: {Luminosity_of_White_Dwarf_B} solar lumunosities")

if Number_of_Stars >= 3:
    if system_age < Main_Sequence_Lifespan_of_Star_C:
        Evolutionary_Stage_of_Star_C = "Main Sequence"
        print("Star C is still on the main sequence")
        # If the system’s age is less than the star’s Main Sequence Lifespan, then the star is still on the main sequence.

    if Main_Sequence_Lifespan_of_Star_C <= system_age <= (1.15 * Main_Sequence_Lifespan_of_Star_C):
        print("Star C has evolved beyond the Main Sequence")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by no more than 15%, then the star will be a subgiant or red giant
        roll_for_giant_type = d100()
        if roll_for_giant_type <= 60:
            Evolutionary_Stage_of_Star_C = "Subgiant"
            print("Specifically - Star C has evolved into a subgiant")
            # On a roll of 01-60, the star is a subgiant
            Luminosity_of_Star_C = Initial_Luminosity_of_Star_C * (Luminosity_Growth_Rate_of_Star_C ** (1.4 * Main_Sequence_Lifespan_of_Star_C))
            print(f"Luminosity of Star C has increased to: {Luminosity_of_Star_A} solar luminosities")

        if 61 <= roll_for_giant_type <= 90:
            Evolutionary_Stage_of_Star_C = "Red Giant Branch"
            print("Specifically Star has evolved onto the Red Giant Branch")
            # On a roll of 61-90, the star is on the red giant branch
            roll_for_red_giant_varriable = (d100() / 100)
            Temperature_Effective_of_Star_C = 5000 - (roll_for_red_giant_varriable * 2000)
            Luminosity_of_Star_C = 50 ** (1 + roll_for_red_giant_varriable)
            print(f"Temperature of Star C has cooled to: {Temperature_Effective_of_Star_C} Kelvin")
            print(f"Luminosity of Star C has increased to: {Luminosity_of_Star_C} solar luminosities")

        if 91 <= roll_for_giant_type <= 100:
            Evolutionary_Stage_of_Star_C = "Horizonal Branch"
            print("Specifically Star C has evolved onto the Horizontal Branch")
            # On a roll of 91-00, the star is on the horizontal branch
            Temperature_Effective_of_Star_C = 5000
            print("Temperature of Star C is now approximately 5000 Kelvin")
            roll_for_horizontal_giant_varriable = d100()
            Luminosity_of_Star_C = 50 + (roll_for_horizontal_giant_varriable / 2)
            print(f"Luminosity of Star C has increased to: {Luminosity_of_Star_C} solar luminosities")

        Radius_of_Star_C = 155000 * ((math.sqrt(Luminosity_of_Star_C))/(Temperature_Effective_of_Star_C * Temperature_Effective_of_Star_C))
        Radius_of_Star_C = round(Radius_of_Star_C, 5)
        print(f"Radius of Star C has evolved to: {Radius_of_Star_C} AU")

    if system_age > (1.15 * Main_Sequence_Lifespan_of_Star_C):
        Evolutionary_Stage_of_Star_C = "White Dwarf"
        print("Star C has evolved into a White Dwarf")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by more than 15%, then the star will have become a white dwarf
        Mass_WDC = 0.43 + (Mass_C / 10.4)
        Mass_WDC = round(Mass_WDC, 2)
        print(f"Mass of Star C has decreased to: {Mass_WDC} solar masses")
        Temperature_Effective_of_White_Dwarf_C = 13500 * ((Mass_WDC ** 0.25) / (((system_age - (1.15 * Main_Sequence_Lifespan_of_Star_C)) ** 0.35)))
        Temperature_Effective_of_White_Dwarf_C = round(Temperature_Effective_of_White_Dwarf_C, 1)
        print(f"Temperature of Star C has evolved to: {Temperature_Effective_of_White_Dwarf_C} Kelvin")
        Radius_of_White_Dwarf_C = 5500 / (math.cbrt(Mass_WDC))
        Radius_of_White_Dwarf_C = round(Radius_of_White_Dwarf_C, 1)
        print(f"Radius of Star C has decreased to: {Radius_of_White_Dwarf_C} kilometers")
        Luminosity_of_White_Dwarf_C = ((Radius_of_White_Dwarf_C ** 2) * (Temperature_Effective_of_White_Dwarf_C ** 4)) / (5.4e26)
        Luminosity_of_White_Dwarf_C = round(Luminosity_of_White_Dwarf_C, 5)
        print(f"Luminosity of Star C has evolved to: {Luminosity_of_White_Dwarf_C} solar lumunosities")

if Number_of_Stars == 4:
    if system_age < Main_Sequence_Lifespan_of_Star_D:
        Evolutionary_Stage_of_Star_D = "Main Sequence"
        print("Star D is still on the main sequence")
        # If the system’s age is less than the star’s Main Sequence Lifespan, then the star is still on the main sequence.

    if Main_Sequence_Lifespan_of_Star_D <= system_age <= (1.15 * Main_Sequence_Lifespan_of_Star_D):
        print("Star D has evolved beyond the Main Sequence")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by no more than 15%, then the star will be a subgiant or red giant
        roll_for_giant_type = d100()
        if roll_for_giant_type <= 60:
            Evolutionary_Stage_of_Star_D = "Subgiant"
            print("Specifically - Star D has evolved into a subgiant")
            # On a roll of 01-60, the star is a subgiant
            Luminosity_of_Star_D = Initial_Luminosity_of_Star_D * (Luminosity_Growth_Rate_of_Star_D ** (1.4 * Main_Sequence_Lifespan_of_Star_D))
            print(f"Luminosity of Star D has increased to: {Luminosity_of_Star_A} solar luminosities")

        if 61 <= roll_for_giant_type <= 90:
            Evolutionary_Stage_of_Star_D = "Red Giant Branch"
            print("Specifically Star has evolved onto the Red Giant Branch")
            # On a roll of 61-90, the star is on the red giant branch
            roll_for_red_giant_varriable = (d100() / 100)
            Temperature_Effective_of_Star_D = 5000 - (roll_for_red_giant_varriable * 2000)
            Luminosity_of_Star_D = 50 ** (1 + roll_for_red_giant_varriable)
            print(f"Temperature of Star D has cooled to: {Temperature_Effective_of_Star_D} Kelvin")
            print(f"Luminosity of Star D has increased to: {Luminosity_of_Star_D} solar luminosities")

        if 91 <= roll_for_giant_type <= 100:
            Evolutionary_Stage_of_Star_D = "Horizonal Branch"
            print("Specifically Star D has evolved onto the Horizontal Branch")
            # On a roll of 91-00, the star is on the horizontal branch
            Temperature_Effective_of_Star_D = 5000
            print("Temperature of Star D is now approximately 5000 Kelvin")
            roll_for_horizontal_giant_varriable = d100()
            Luminosity_of_Star_D = 50 + (roll_for_horizontal_giant_varriable / 2)
            print(f"Luminosity of Star D has increased to: {Luminosity_of_Star_D} solar luminosities")

        Radius_of_Star_D = 155000 * ((math.sqrt(Luminosity_of_Star_D))/(Temperature_Effective_of_Star_D * Temperature_Effective_of_Star_D))
        Radius_of_Star_D = round(Radius_of_Star_D, 5)
        print(f"Radius of Star D has evolved to: {Radius_of_Star_D} AU")

    if system_age > (1.15 * Main_Sequence_Lifespan_of_Star_D):
        Evolutionary_Stage_of_Star_D = "White Dwarf"
        print("Star D has evolved into a White Dwarf")
        # If the system’s age exceeds the star’s Main Sequence Lifespan by more than 15%, then the star will have become a white dwarf
        Mass_WDD = 0.43 + (Mass_D / 10.4)
        Mass_WDD = round(Mass_WDD, 2)
        print(f"Mass of Star D has decreased to: {Mass_WDD} solar masses")
        Temperature_Effective_of_White_Dwarf_D = 13500 * ((Mass_WDD ** 0.25) / (((system_age - (1.15 * Main_Sequence_Lifespan_of_Star_D)) ** 0.35)))
        Temperature_Effective_of_White_Dwarf_D = round(Temperature_Effective_of_White_Dwarf_D, 1)
        print(f"Temperature of Star D has evolved to: {Temperature_Effective_of_White_Dwarf_D} Kelvin")
        Radius_of_White_Dwarf_D = 5500 / (math.cbrt(Mass_WDD))
        Radius_of_White_Dwarf_D = round(Radius_of_White_Dwarf_D, 1)
        print(f"Radius of Star D has decreased to: {Radius_of_White_Dwarf_D} kilometers")
        Luminosity_of_White_Dwarf_D = ((Radius_of_White_Dwarf_D ** 2) * (Temperature_Effective_of_White_Dwarf_D ** 4)) / (5.4e26)
        Luminosity_of_White_Dwarf_D = round(Luminosity_of_White_Dwarf_D, 5)
        print(f"Luminosity of Star D has evolved to: {Luminosity_of_White_Dwarf_D} solar lumunosities")
