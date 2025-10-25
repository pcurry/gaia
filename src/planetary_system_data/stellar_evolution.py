# this sub-program covers step 6 ("Stellar Evolution") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

if Number_of_Stars >= 1:
    Temperature_Effective_of_Star_A = None
    Luminosity_of_Star_A = None
    Radius_of_Star_A = None
    Main_Sequence_Lifespan_of_Star_A = None

    if Mass_A < 0.08:
        Temperature_Effective_of_Star_A = 18600 * ((Mass_A ** 0.8) / (system_age ** 0.3))
        Luminosity_of_Star_A = (Temperature_Effective_of_Star_A ** 4) / (1.1e+17)
        Radius_of_Star_A = 0.00047
        Main_Sequence_Lifespan_of_Star_A = (1 / (Mass_A ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= Mass_A <= 0.5:
        Temperature_Effective_of_Star_A = -78806*(Mass_A ** 4) + 125050*(Mass_A ** 3) - 74194*(Mass_A ** 2) + (20692*Mass_A) + 1272.2
        Luminosity_of_Star_A = 2.1901*(Mass_A ** 4) - 2.2436*(Mass_A ** 3) + 0.919*(Mass_A ** 2) - (0.1023*Mass_A) + 0.0039
        Main_Sequence_Lifespan_of_Star_A = (1 / (Mass_A ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe
        
    elif 0.5 < Mass_A:
        Initial_Effective_Temperature_of_Star_A = None
        Final_Effective_Temperature_of_Star_A = None
        Initial_Luminosity_of_Star_A = None
        Luminosity_Growth_Rate_of_Star_A = None

        Initial_Effective_Temperature_of_Star_A = 15.992*(Mass_A ** 4) - 198.64*(Mass_A ** 3) + 578.86*(Mass_A ** 2) + (3020.1*Mass_A) + 2060
        Final_Effective_Temperature_of_Star_A = 15.893*(Mass_A ** 4) + 154.37*(Mass_A ** 3) + 384.94*(Mass_A ** 2) + (2105.7*Mass_A) + 3631.6
        Initial_Luminosity_of_Star_A = -0.2707*(Mass_A ** 4) + 10.15*(Mass_A ** 3) + 28.137*(Mass_A ** 2) + (31.268*Mass_A) + 11.559
        if Mass_A <= 4:
            Luminosity_Growth_Rate_of_Star_A = 0.8295*(Mass_A ** 6) - 9.2448*(Mass_A ** 5) + 40.931*(Mass_A ** 4) - 90.562*(Mass_A ** 3) + 104.59*(Mass_A ** 2) - (59.148*Mass_A) + 13.745
        elif Mass_A > 4:
            Luminosity_Growth_Rate_of_Star_A = (0.000005 ** (3.9985*Mass_A)) 
        Main_Sequence_Lifespan_of_Star_A = 11.452*(Mass_A ** -3.157)

        Temperature_Effective_of_Star_A = Initial_Effective_Temperature_of_Star_A + (system_age / Main_Sequence_Lifespan_of_Star_A) * (Final_Effective_Temperature_of_Star_A - Initial_Effective_Temperature_of_Star_A)

        if (system_age <= (0.8*Main_Sequence_Lifespan_of_Star_A)):
                Luminosity_of_Star_A = Initial_Luminosity_of_Star_A * (Luminosity_Growth_Rate_of_Star_A ** system_age)
        elif (system_age > (0.8*Main_Sequence_Lifespan_of_Star_A)):
                Luminosity_of_Star_A = Initial_Luminosity_of_Star_A * (Luminosity_Growth_Rate_of_Star_A ** (3*system_age - 1.6*Main_Sequence_Lifespan_of_Star_A))
        
    if 0.08 <= Mass_A:
        Radius_of_Star_A = 155000 * ((math.sqrt(Luminosity_of_Star_A))/(Temperature_Effective_of_Star_A * Temperature_Effective_of_Star_A))

    Temperature_Effective_of_Star_A = round(Temperature_Effective_of_Star_A, 1)
    Luminosity_of_Star_A = round(Luminosity_of_Star_A, 5)
    Radius_of_Star_A = round(Radius_of_Star_A, 5)
    print(f"Effective Temperature of Star A: {Temperature_Effective_of_Star_A} Kelvin")
    print(f"Luminosity of Star A: {Luminosity_of_Star_A} solar luminosities")
    print(f"Radius of Star A: {Radius_of_Star_A} AU")

if Number_of_Stars >= 2:
    Temperature_Effective_of_Star_B = None
    Luminosity_of_Star_B = None
    Radius_of_Star_B = None
    Main_Sequence_Lifespan_of_Star_B = None
    
    if Mass_B < 0.08:
        Temperature_Effective_of_Star_B = 18600 * ((Mass_B ** 0.8) / (system_age ** 0.3))
        Luminosity_of_Star_B = (Temperature_Effective_of_Star_B ** 4) / (1.1e+17)
        Radius_of_Star_B = 0.00047
        Main_Sequence_Lifespan_of_Star_B = (1 / (Mass_B ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= Mass_B <= 0.5:
        Temperature_Effective_of_Star_B = -78806*(Mass_B ** 4) + 125050*(Mass_B ** 3) - 74194*(Mass_B ** 2) + (20692*Mass_B) + 1272.2
        Luminosity_of_Star_B = 2.1901*(Mass_B ** 4) - 2.2436*(Mass_B ** 3) + 0.919*(Mass_B ** 2) - (0.1023*Mass_B) + 0.0039
        Main_Sequence_Lifespan_of_Star_B = (1 / (Mass_B ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe

    elif 0.5 < Mass_B:
        Initial_Effective_Temperature_of_Star_B = None
        Final_Effective_Temperature_of_Star_B = None
        Initial_Luminosity_of_Star_B = None
        Luminosity_Growth_Rate_of_Star_B = None

        Initial_Effective_Temperature_of_Star_B = 15.992*(Mass_B ** 4) - 198.64*(Mass_B ** 3) + 578.86*(Mass_B ** 2) + (3020.1*Mass_B) + 2060
        Final_Effective_Temperature_of_Star_B = 15.893*(Mass_B ** 4) + 154.37*(Mass_B ** 3) + 384.94*(Mass_B ** 2) + (2105.7*Mass_B) + 3631.6
        Initial_Luminosity_of_Star_B = -0.2707*(Mass_B ** 4) + 10.15*(Mass_B ** 3) + 28.137*(Mass_B ** 2) + (31.268*Mass_B) + 11.559
        if Mass_B <= 4:
            Luminosity_Growth_Rate_of_Star_B = 0.8295*(Mass_B ** 6) - 9.2448*(Mass_B ** 5) + 40.931*(Mass_B ** 4) - 90.562*(Mass_B ** 3) + 104.59*(Mass_B ** 2) - (59.148*Mass_B) + 13.745
        elif Mass_B > 4:
            Luminosity_Growth_Rate_of_Star_B = (0.000005 ** (3.9985*Mass_B)) 
        Main_Sequence_Lifespan_of_Star_B = 11.452*(Mass_B ** -3.157)

        Temperature_Effective_of_Star_B = Initial_Effective_Temperature_of_Star_B + (system_age / Main_Sequence_Lifespan_of_Star_B) * (Final_Effective_Temperature_of_Star_B-Initial_Effective_Temperature_of_Star_B)

        if (system_age <= (0.8*Main_Sequence_Lifespan_of_Star_B)):
                Luminosity_of_Star_B = Initial_Luminosity_of_Star_B * (Luminosity_Growth_Rate_of_Star_B ** system_age)
        elif (system_age > (0.8*Main_Sequence_Lifespan_of_Star_B)):
                Luminosity_of_Star_B = Initial_Luminosity_of_Star_B * (Luminosity_Growth_Rate_of_Star_B ** (3*system_age - 1.6*Main_Sequence_Lifespan_of_Star_B))

    if 0.08 <= Mass_B:
        Radius_of_Star_B = 155000 * ((math.sqrt(Luminosity_of_Star_B))/(Temperature_Effective_of_Star_B * Temperature_Effective_of_Star_B))

    Temperature_Effective_of_Star_B = round(Temperature_Effective_of_Star_B, 1)
    Luminosity_of_Star_B = round(Luminosity_of_Star_B, 5)
    Radius_of_Star_B = round(Radius_of_Star_B, 5)
    print(f"Effective Temperature of Star B: {Temperature_Effective_of_Star_B} Kelvin")
    print(f"Luminosity of Star B: {Luminosity_of_Star_B} solar luminosities")
    print(f"Radius of Star B: {Radius_of_Star_B} AU")

if Number_of_Stars >= 3:
    
    Temperature_Effective_of_Star_C = None
    Luminosity_of_Star_C = None
    Radius_of_Star_C = None
    Main_Sequence_Lifespan_of_Star_C = None

    if Mass_C < 0.08:
        Temperature_Effective_of_Star_C = 18600 * ((Mass_C ** 0.8) / (system_age ** 0.3))
        Luminosity_of_Star_C = (Temperature_Effective_of_Star_C ** 4) / (1.1e+17)
        Radius_of_Star_C = 0.00047
        Main_Sequence_Lifespan_of_Star_C = (1 / (Mass_C ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= Mass_C <= 0.5:
        Temperature_Effective_of_Star_C = -78806*(Mass_C ** 4) + 125050*(Mass_C ** 3) - 74194*(Mass_C ** 2) + (20692*Mass_C) + 1272.2
        Luminosity_of_Star_C = 2.1901*(Mass_C ** 4) - 2.2436*(Mass_C ** 3) + 0.919*(Mass_C ** 2) - (0.1023*Mass_C) + 0.0039
        Main_Sequence_Lifespan_of_Star_C = (1 / (Mass_C ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe

    elif 0.5 < Mass_C:
        Initial_Effective_Temperature_of_Star_C = None
        Final_Effective_Temperature_of_Star_C = None
        Initial_Luminosity_of_Star_C = None
        Luminosity_Growth_Rate_of_Star_C = None

        Initial_Effective_Temperature_of_Star_C = 15.992*(Mass_C ** 4) - 198.64*(Mass_C ** 3) + 578.86*(Mass_C ** 2) + (3020.1*Mass_C) + 2060
        Final_Effective_Temperature_of_Star_C = 15.893*(Mass_C ** 4) + 154.37*(Mass_C ** 3) + 384.94*(Mass_C ** 2) + (2105.7*Mass_C) + 3631.6
        Initial_Luminosity_of_Star_C = -0.2707*(Mass_C ** 4) + 10.15*(Mass_C ** 3) + 28.137*(Mass_C ** 2) + (31.268*Mass_C) + 11.559
        if Mass_C <= 4:
            Luminosity_Growth_Rate_of_Star_C = 0.8295*(Mass_C ** 6) - 9.2448*(Mass_C ** 5) + 40.931*(Mass_C ** 4) - 90.562*(Mass_C ** 3) + 104.59*(Mass_C ** 2) - (59.148*Mass_C) + 13.745
        elif Mass_C > 4:
            Luminosity_Growth_Rate_of_Star_C = (0.000005 ** (3.9985*Mass_C)) 
        Main_Sequence_Lifespan_of_Star_C = 11.452*(Mass_C ** -3.157)

        Temperature_Effective_of_Star_C = Initial_Effective_Temperature_of_Star_C + (system_age / Main_Sequence_Lifespan_of_Star_C) * (Final_Effective_Temperature_of_Star_C-Initial_Effective_Temperature_of_Star_C)

        if (system_age <= (0.8*Main_Sequence_Lifespan_of_Star_C)):
                Luminosity_of_Star_C = Initial_Luminosity_of_Star_C * (Luminosity_Growth_Rate_of_Star_C ** system_age)
        elif (system_age > (0.8*Main_Sequence_Lifespan_of_Star_C)):
                Luminosity_of_Star_C = Initial_Luminosity_of_Star_C * (Luminosity_Growth_Rate_of_Star_C ** (3*system_age - 1.6*Main_Sequence_Lifespan_of_Star_C))

    if 0.08 <= Mass_C:
        Radius_of_Star_C = 155000 * ((math.sqrt(Luminosity_of_Star_C))/(Temperature_Effective_of_Star_C * Temperature_Effective_of_Star_C))

    Temperature_Effective_of_Star_C = round(Temperature_Effective_of_Star_C, 1)
    Luminosity_of_Star_C = round(Luminosity_of_Star_C, 5)
    Radius_of_Star_C = round(Radius_of_Star_C, 5)
    print(f"Effective Temperature of Star C: {Temperature_Effective_of_Star_C} Kelvin")
    print(f"Luminosity of Star C: {Luminosity_of_Star_C} solar luminosities")
    print(f"Radius of Star C: {Radius_of_Star_C} AU")

if Number_of_Stars == 4:
    
    Temperature_Effective_of_Star_D = None
    Luminosity_of_Star_D = None
    Radius_of_Star_D = None
    Main_Sequence_Lifespan_of_Star_D = None
    
    if Mass_D < 0.08:
        Temperature_Effective_of_Star_D = 18600 * ((Mass_D ** 0.8) / (system_age ** 0.3))
        Luminosity_of_Star_D = (Temperature_Effective_of_Star_D ** 4) / (1.1e+17)
        Radius_of_Star_D = 0.00047
        Main_Sequence_Lifespan_of_Star_D = (1 / (Mass_D ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice brown dwarf lifespans are longer than the current age of the universe

    elif 0.08 <= Mass_D <= 0.5:
        Temperature_Effective_of_Star_D = -78806*(Mass_D ** 4) + 125050*(Mass_D ** 3) - 74194*(Mass_D ** 2) + (20692*Mass_D) + 1272.2
        Luminosity_of_Star_D = 2.1901*(Mass_D ** 4) - 2.2436*(Mass_D ** 3) + 0.919*(Mass_D ** 2) - (0.1023*Mass_D) + 0.0039
        Main_Sequence_Lifespan_of_Star_D = (1 / (Mass_D ** 2.5)) / 10
        # theoretical main sequence lifespan, in practice red dwarf lifespans are longer than the current age of the universe

    elif 0.5 < Mass_D:
        Initial_Effective_Temperature_of_Star_D = None
        Final_Effective_Temperature_of_Star_D = None
        Initial_Luminosity_of_Star_D = None
        Luminosity_Growth_Rate_of_Star_D = None

        Initial_Effective_Temperature_of_Star_D = 15.992*(Mass_D ** 4) - 198.64*(Mass_D ** 3) + 578.86*(Mass_D ** 2) + (3020.1*Mass_D) + 2060
        Final_Effective_Temperature_of_Star_D = 15.893*(Mass_D ** 4) + 154.37*(Mass_D ** 3) + 384.94*(Mass_D ** 2) + (2105.7*Mass_D) + 3631.6
        Initial_Luminosity_of_Star_D = -0.2707*(Mass_D ** 4) + 10.15*(Mass_D ** 3) + 28.137*(Mass_D ** 2) + (31.268*Mass_D) + 11.559
        if Mass_D <= 4:
            Luminosity_Growth_Rate_of_Star_D = 0.8295*(Mass_D ** 6) - 9.2448*(Mass_D ** 5) + 40.931*(Mass_D ** 4) - 90.562*(Mass_D ** 3) + 104.59*(Mass_D ** 2) - (59.148*Mass_D) + 13.745
        elif Mass_D > 4:
            Luminosity_Growth_Rate_of_Star_D = (0.000005 ** (3.9985*Mass_D)) 
        Main_Sequence_Lifespan_of_Star_D = 11.452*(Mass_D ** -3.157)

        Temperature_Effective_of_Star_D = Initial_Effective_Temperature_of_Star_D + (system_age / Main_Sequence_Lifespan_of_Star_D) * (Final_Effective_Temperature_of_Star_D-Initial_Effective_Temperature_of_Star_D)

        if (system_age <= (0.8*Main_Sequence_Lifespan_of_Star_D)):
                Luminosity_of_Star_D = Initial_Luminosity_of_Star_D * (Luminosity_Growth_Rate_of_Star_D ** system_age)
        elif (system_age > (0.8*Main_Sequence_Lifespan_of_Star_D)):
                Luminosity_of_Star_D = Initial_Luminosity_of_Star_D * (Luminosity_Growth_Rate_of_Star_D ** (3*system_age - 1.6*Main_Sequence_Lifespan_of_Star_D))

    if 0.08 <= Mass_D:
        Radius_of_Star_D = 155000 * ((math.sqrt(Luminosity_of_Star_D))/(Temperature_Effective_of_Star_D * Temperature_Effective_of_Star_D))
    
    Temperature_Effective_of_Star_D = round(Temperature_Effective_of_Star_D, 1)
    Luminosity_of_Star_D = round(Luminosity_of_Star_D, 5)
    Radius_of_Star_D = round(Radius_of_Star_D, 5)

    print(f"Effective Temperature of Star D: {Temperature_Effective_of_Star_D} Kelvin")
    print(f"Luminosity of Star D: {Luminosity_of_Star_D} solar luminosities")
    print(f"Radius of Star D: {Radius_of_Star_D} AU")

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
