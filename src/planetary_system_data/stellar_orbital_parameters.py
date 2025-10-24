# this sub-program covers step 8 ("Stellar Orbital Parameters") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

if Number_of_Stars == 1:
    binary_separation_type = "None"
    print("Single Star System - skipping Step #8")

if Number_of_Stars == 2:
    roll_for_binary_separation_type = _3d6()
    if roll_for_binary_separation_type <= 3:
        binary_separation_type = "Extremely Close"
        binary_separation_base_distance = 0.015
    if 4 <= roll_for_binary_separation_type <= 5:
        binary_separation_type = "Very Close"
        binary_separation_base_distance = 0.15
    if 6 <= roll_for_binary_separation_type <= 8:
        binary_separation_type = "Close"
        binary_separation_base_distance = 1.5
    if 9 <= roll_for_binary_separation_type <= 12:
        binary_separation_type = "Moderate"
        binary_separation_base_distance = 15
    if 13 <= roll_for_binary_separation_type <= 15:
        binary_separation_type = "Wide"
        binary_separation_base_distance = 150
    if 16 <= roll_for_binary_separation_type:
        binary_separation_type = "Very Wide"
        binary_separation_base_distance = 1500
    print(f"Binary Star System with {binary_separation_type} Separation Between Star A and Star B")
    print(f"Base Distance Between Star A and Star B: {binary_separation_base_distance} AU")
    
    roll_for_binary_average_distance = ((d100())/100)
    binary_average_distance = binary_separation_base_distance * (10 ** roll_for_binary_average_distance)
    binary_distance_variance_factor = random.uniform(0.95, 1.05)
    binary_average_distance = (binary_distance_variance_factor * binary_average_distance)
    binary_average_distance = round(binary_average_distance, 3)
    print(f"Average Distance Between Star A and Star B: {binary_average_distance} AU")

    if binary_separation_type == "Extremely Close":
        binary_eccentricity_roll_modifier = -8
    if binary_separation_type == "Very Close":
        binary_eccentricity_roll_modifier = -6
    if binary_separation_type == "Close":
        binary_eccentricity_roll_modifier = -4
    if binary_separation_type == "Moderate":
        binary_eccentricity_roll_modifier = -2
    if binary_separation_type == "Wide":
        binary_eccentricity_roll_modifier = 0
    if binary_separation_type == "Very Wide":
        binary_eccentricity_roll_modifier = 0

    roll_for_binary_orbital_eccentricity = _3d6() + binary_eccentricity_roll_modifier 
    # If at Moderate separation, modify by -2.
    if roll_for_binary_orbital_eccentricity <= 3:
        binary_eccentricity = 0.0
    if roll_for_binary_orbital_eccentricity == 4:
        binary_eccentricity = 0.1
    if 5 <= roll_for_binary_orbital_eccentricity <= 6:
        binary_eccentricity = 0.2
    if 7 <= roll_for_binary_orbital_eccentricity <= 8:
        binary_eccentricity = 0.3
    if 9 <= roll_for_binary_orbital_eccentricity <= 11:
        binary_eccentricity = 0.4
    if 12 <= roll_for_binary_orbital_eccentricity <= 13:
        binary_eccentricity = 0.5
    if 14 <= roll_for_binary_orbital_eccentricity <= 15:
        binary_eccentricity = 0.6
    if roll_for_binary_orbital_eccentricity == 6:
        binary_eccentricity = 0.7
    if roll_for_binary_orbital_eccentricity == 17:
        binary_eccentricity = 0.8
    if roll_for_binary_orbital_eccentricity == 18:
        binary_eccentricity = 0.9
    print(f"Eccentricity of Binary Pair: {binary_eccentricity}")
    
    binary_minimum_distance = binary_average_distance * (1 - binary_eccentricity)
    binary_minimum_distance = round(binary_minimum_distance, 3)
    print(f"Minimum Distance Between Star A and Star B: {binary_minimum_distance} AU")

    binary_maximum_distance = binary_average_distance * (1 + binary_eccentricity)
    binary_maximum_distance = round(binary_maximum_distance, 3)
    print(f"Maximum Distance Between Star A and Star B: {binary_maximum_distance} AU")

    if Evolutionary_Stage_of_Star_A == "White Dwarf":
        Final_Mass_A = Mass_WDA
        Final_Radius_A = Radius_of_White_Dwarf_A
    if Evolutionary_Stage_of_Star_A != "White Dwarf":
        Final_Mass_A = Mass_A
        Final_Radius_A = Radius_of_Star_A
    if Evolutionary_Stage_of_Star_B == "White Dwarf":
        Final_Mass_B = Mass_WDB
        Final_Radius_B = Radius_of_White_Dwarf_B
    if Evolutionary_Stage_of_Star_B != "White Dwarf":
        Final_Mass_B = Mass_B
        Final_Radius_B = Radius_of_Star_B
    binary_orbital_period = math.sqrt(( binary_average_distance ** 3) / (Final_Mass_A + Final_Mass_B))
    binary_orbital_period = round(binary_orbital_period,2)
    print(f"Orbital Period of Star A and Star B: {binary_orbital_period} years")
    binary_orbital_period_days = binary_orbital_period * 365.26
    binary_orbital_period_days = round(binary_orbital_period_days,2)
    print(f"which is equivalent to {binary_orbital_period_days} days")

    # Check for Special Case: Close Binary Pairs
    Flag_for_Close_Binary = "No"
    if binary_separation_type == "Extremely Close":
        Flag_for_Close_Binary == "Yes"
    if binary_separation_type == "Very Close" or "Close":
        if Evolutionary_Stage_of_Star_A == "Red Giant Branch":
            Flag_for_Close_Binary == "Yes"            
        if Evolutionary_Stage_of_Star_B == "Red Giant Branch":
            Flag_for_Close_Binary == "Yes"

    if Flag_for_Close_Binary == "Yes":
        # Calculate radius of Roche Lobe of Star A
        Roche_Lobe_Radius_A = binary_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_A / Final_Mass_B)))
        # Calculate radius of Roche Lobe of Star B
        Roche_Lobe_Radius_B = binary_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_B / Final_Mass_A)))
        if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
            print("Binary Pair is a Contact Binary")
            print("Evolution of this star system is out of scope for this model")
        if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
            print("Binary Pair is Semi-Detached Biniary - Star A is larger than it's Roche Lobe")
            print("Evolution of a Semi-Detached Binary is out of scope for this model")
            if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                print("Star A is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                print("Star B is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
            print("Binary Pair is Semi-Detached Biniary - Star B is larger than it's Roche Lobe")
            print("Evolution of this star system is out of scope for this model")
            if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                print("Star A is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                print("Star B is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
            print("Confirmed - pair is a Detached Binary")
    
if Number_of_Stars == 3:

    # prepare mass and radius parameters for orbital calculations (final mass applies - Newton doesn't care if you are a white dwarf or main sequence)
    if Evolutionary_Stage_of_Star_A == "White Dwarf":
        Final_Mass_A = Mass_WDA
        Final_Radius_A = Radius_of_White_Dwarf_A
    if Evolutionary_Stage_of_Star_A != "White Dwarf":
        Final_Mass_A = Mass_A
        Final_Radius_A = Radius_of_Star_A
    if Evolutionary_Stage_of_Star_B == "White Dwarf":
        Final_Mass_B = Mass_WDB
        Final_Radius_B = Radius_of_White_Dwarf_A
    if Evolutionary_Stage_of_Star_B != "White Dwarf":
        Final_Mass_B = Mass_B
        Final_Radius_B = Radius_of_Star_B
    if Evolutionary_Stage_of_Star_C == "White Dwarf":
        Final_Mass_C = Mass_WDC
        Final_Raduis_C = Radius_of_White_Dwarf_C
    if Evolutionary_Stage_of_Star_C != "White Dwarf":
        Final_Mass_C = Mass_C
        Final_Radius_C = Radius_of_Star_C

    if Stellar_Arrangement == "A-BC":
        roll_for_BC_separation_type = ((_3d6())-3)
        if roll_for_BC_separation_type <= 3:
            BC_separation_type = "Extremely Close"
            BC_separation_base_distance = 0.015
        if 4 <= roll_for_BC_separation_type <= 5:
            BC_separation_type = "Very Close"
            BC_separation_base_distance = 0.15
        if 6 <= roll_for_BC_separation_type <= 8:
            BC_separation_type = "Close"
            BC_separation_base_distance = 1.5
        if 9 <= roll_for_BC_separation_type <= 12:
            BC_separation_type = "Moderate"
            BC_separation_base_distance = 15
        if 13 <= roll_for_BC_separation_type <= 15:
            BC_separation_type = "Wide"
            BC_separation_base_distance = 150
        print(f"A-BC Triple Star System with {BC_separation_type} Separation Between Star B and Star C")
        print(f"Base Distance Between Star B and Star C: {BC_separation_base_distance} AU")

        roll_for_BC_average_distance = ((d100())/100)
        BC_average_distance = BC_separation_base_distance * (10 ** roll_for_BC_average_distance)
        BC_distance_variance_factor = random.uniform(0.95, 1.05)
        BC_average_distance = (BC_distance_variance_factor * BC_average_distance)
        BC_average_distance = round(BC_average_distance, 3)
        print(f"Average Distance Between Star B and Star C: {BC_average_distance} AU")

        if BC_separation_type == "Extremely Close":
            BC_eccentricity_roll_modifier = -8
        if BC_separation_type == "Very Close":
            BC_eccentricity_roll_modifier = -6
        if BC_separation_type == "Close":
            BC_eccentricity_roll_modifier = -4
        if BC_separation_type == "Moderate":
            BC_eccentricity_roll_modifier = -2
        if BC_separation_type == "Wide":
            BC_eccentricity_roll_modifier = 0

        roll_for_BC_orbital_eccentricity = _3d6() + BC_eccentricity_roll_modifier 
        # If at Moderate separation, modify by -2.
        if roll_for_BC_orbital_eccentricity <= 3:
            BC_eccentricity = 0.0
        if roll_for_BC_orbital_eccentricity == 4:
            BC_eccentricity = 0.1
        if 5 <= roll_for_BC_orbital_eccentricity <= 6:
            BC_eccentricity = 0.2
        if 7 <= roll_for_BC_orbital_eccentricity <= 8:
            BC_eccentricity = 0.3
        if 9 <= roll_for_BC_orbital_eccentricity <= 11:
            BC_eccentricity = 0.4
        if 12 <= roll_for_BC_orbital_eccentricity <= 13:
            BC_eccentricity = 0.5
        if 14 <= roll_for_BC_orbital_eccentricity <= 15:
            BC_eccentricity = 0.6
        if roll_for_BC_orbital_eccentricity == 6:
            BC_eccentricity = 0.7
        if roll_for_BC_orbital_eccentricity == 17:
            BC_eccentricity = 0.8
        if roll_for_BC_orbital_eccentricity == 18:
            BC_eccentricity = 0.9
        print(f"Eccentricity of Star C orbit around Star B: {BC_eccentricity}")
    
        BC_minimum_distance = BC_average_distance * (1 - BC_eccentricity)
        BC_minimum_distance = round(BC_minimum_distance, 3)
        print(f"Minimum Distance Between Star B and Star C: {BC_minimum_distance} AU")

        BC_maximum_distance = BC_average_distance * (1 + BC_eccentricity)
        BC_maximum_distance = round(BC_maximum_distance, 3)
        print(f"Maximum Distance Between Star B and Star C: {BC_maximum_distance} AU")

        BC_orbital_period = math.sqrt(( BC_average_distance ** 3) / (Final_Mass_B + Final_Mass_C))
        BC_orbital_period = round(BC_orbital_period,2)
        print(f"Orbital Period of Star B and Star C: {BC_orbital_period} years")
        BC_orbital_period_days = BC_orbital_period * 365.26
        BC_orbital_period_days = round(BC_orbital_period_days,2)
        print(f"which is equivalent to {BC_orbital_period_days} days")

        # Check for Special Case: Close Binary Pair BC in an A-BC type triple system
        
        Flag_for_Close_Binary_BC_in_A_BC = "No"
        if BC_separation_type == "Extremely Close":
            Flag_for_Close_Binary_BC_in_A_BC == "Yes"
        if BC_separation_type == "Very Close" or "Close":
            if Evolutionary_Stage_of_Star_B == "Red Giant Branch":
                Flag_for_Close_Binary_BC_in_A_BC == "Yes"            
            if Evolutionary_Stage_of_Star_C == "Red Giant Branch":
                Flag_for_Close_Binary_BC_in_A_BC == "Yes"

        if Flag_for_Close_Binary_BC_in_A_BC == "Yes":
            # Calculate radius of Roche Lobe of Star A
            Roche_Lobe_Radius_B = BC_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_B / Final_Mass_C)))
            # Calculate radius of Roche Lobe of Star B
            Roche_Lobe_Radius_C = BC_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_C / Final_Mass_B)))
            if (Roche_Lobe_Radius_B < Final_Radius_B) and (Roche_Lobe_Radius_C < Final_Radius_C):
                print("Binary Pair BC in an A-BC type triple star system is a Contact Binary")
                print("Evolution of this star system is out of scope for this model")
            if (Roche_Lobe_Radius_B < Final_Radius_B) and (Roche_Lobe_Radius_C >= Final_Radius_C):
                print("Binary Pair BC in an A-BC type triple star system is Semi-Detached Biniary - Star B is larger than it's Roche Lobe")
                print("Evolution of this star system is out of scope for this model")
                if Evolutionary_Stage_of_Star_B == "White Dwarf" and Evolutionary_Stage_of_Star_C != "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                    print("Star B is a candidate to become a recurrent nova")
                if Evolutionary_Stage_of_Star_B != "White Dwarf" and Evolutionary_Stage_of_Star_C == "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star C) is a White Dwarf")
                    print("Star C is a candidate to become a recurrent nova")
            if (Roche_Lobe_Radius_B >= Final_Radius_B) and (Roche_Lobe_Radius_C < Final_Radius_C):
                print("Binary Pair BC in an A-BC type triple star system is Semi-Detached Biniary - Star C is larger than it's Roche Lobe")
                print("Evolution of this star system is out of scope for this model")
                if Evolutionary_Stage_of_Star_B == "White Dwarf" and Evolutionary_Stage_of_Star_C != "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                    print("Star B is a candidate to become a recurrent nova")
                if Evolutionary_Stage_of_Star_B != "White Dwarf" and Evolutionary_Stage_of_Star_C == "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star C) is a White Dwarf")
                    print("Star C is a candidate to become a recurrent nova")
            if (Roche_Lobe_Radius_B >= Final_Radius_B) and (Roche_Lobe_Radius_C >= Final_Radius_C):
                print("Confirmed - pair BC is a Detached Binary within an A-BC type triple star system")
 
        roll_for_A_BC_separation_type = _3d6()
        if roll_for_A_BC_separation_type <= 3:
            A_BC_separation_type = "Extremely Close"
            A_BC_separation_base_distance = 0.015
            if BC_separation_type == "Extremely Close":
                A_BC_separation_type = "Very Close"
                A_BC_separation_base_distance = 0.15
        if 4 <= roll_for_A_BC_separation_type <= 5:
            A_BC_separation_type = "Very Close"
            A_BC_separation_base_distance = 0.15
            if BC_separation_type in ["Very Close", "Extremely Close"]:
                A_BC_seperation_type = "Close"
                A_BC_separation_base_distance = 1.5
        if 6 <= roll_for_A_BC_separation_type <= 8:
            A_BC_separation_type = "Close"
            A_BC_separation_base_distance = 1.5
            if BC_separation_type in ["Very Close", "Extremely Close", "Close"]:
                A_BC_separation_type = "Moderate"
                A_BC_separation_base_distance = 15
        if 9 <= roll_for_A_BC_separation_type <= 12:
            A_BC_separation_type = "Moderate"
            A_BC_separation_base_distance = 15
            if BC_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate"]:
                A_BC_separation_type = "Wide"
                A_BC_separation_base_distance = 150
        if 13 <= roll_for_A_BC_separation_type <= 15:
            A_BC_separation_type = "Wide"
            A_BC_separation_base_distance = 150
            if BC_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate", "Wide"]:
                A_BC_separation_type = "Very Wide"
                A_BC_separation_base_distance = 1500
        if 16 <= roll_for_A_BC_separation_type:
            A_BC_separation_type = "Very Wide"
            A_BC_separation_base_distance = 1500
        print(f"Triple Star System with {A_BC_separation_type} Separation Between Star A and Binary Star System BC")
        print(f"Base Distance Between Star A and Binary Star System BC: {A_BC_separation_base_distance} AU")
    
        roll_for_A_BC_average_distance = ((d100())/100)
        A_BC_average_distance = A_BC_separation_base_distance * (10 ** roll_for_A_BC_average_distance)
        A_BC_distance_variance_factor = random.uniform(0.95, 1.05)
        A_BC_average_distance = (A_BC_distance_variance_factor * A_BC_average_distance)
        A_BC_average_distance = round(A_BC_average_distance, 3)
        print(f"Average Distance Between Star A and Binary Star System BC: {A_BC_average_distance} AU")

        if A_BC_separation_type == "Extremely Close":
            A_BC_eccentricity_roll_modifier = -8
        if A_BC_separation_type == "Very Close":
            A_BC_eccentricity_roll_modifier = -6
        if A_BC_separation_type == "Close":
            A_BC_eccentricity_roll_modifier = -4
        if A_BC_separation_type == "Moderate":
            A_BC_eccentricity_roll_modifier = -2
        if A_BC_separation_type == "Wide":
            A_BC_eccentricity_roll_modifier = 0
        if A_BC_separation_type == "Very Wide":
            A_BC_eccentricity_roll_modifier = 0

        roll_for_A_BC_orbital_eccentricity = _3d6() + A_BC_eccentricity_roll_modifier 
        # If at Moderate separation, modify by -2.
        if roll_for_A_BC_orbital_eccentricity <= 3:
            A_BC_eccentricity = 0.0
        if roll_for_A_BC_orbital_eccentricity == 4:
            A_BC_eccentricity = 0.1
        if 5 <= roll_for_A_BC_orbital_eccentricity <= 6:
            A_BC_eccentricity = 0.2
        if 7 <= roll_for_A_BC_orbital_eccentricity <= 8:
            A_BC_eccentricity = 0.3
        if 9 <= roll_for_A_BC_orbital_eccentricity <= 11:
            A_BC_eccentricity = 0.4
        if 12 <= roll_for_A_BC_orbital_eccentricity <= 13:
            A_BC_eccentricity = 0.5
        if 14 <= roll_for_A_BC_orbital_eccentricity <= 15:
            A_BC_eccentricity = 0.6
        if roll_for_A_BC_orbital_eccentricity == 6:
            A_BC_eccentricity = 0.7
        if roll_for_A_BC_orbital_eccentricity == 17:
            A_BC_eccentricity = 0.8
        if roll_for_A_BC_orbital_eccentricity == 18:
            A_BC_eccentricity = 0.9
        print(f"Eccentricity of Binary Pair BC Orbit Around Star A: {A_BC_eccentricity}")
    
        A_BC_minimum_distance = A_BC_average_distance * (1 - A_BC_eccentricity)
        if A_BC_minimum_distance < (3 * BC_maximum_distance):
            A_BC_adjusted_average_distance = (3 * BC_maximum_distance) / (1 - A_BC_eccentricity)
            print(f"Stability Issue Detected - Adjusting Average Distance Between Star A and Binary Star System BC to: {A_BC_adjusted_average_distance} AU")
            A_BC_average_distance = A_BC_adjusted_average_distance
            A_BC_minimum_distance = A_BC_average_distance * (1 - A_BC_eccentricity)       
        A_BC_minimum_distance = round(A_BC_minimum_distance, 3)
        print(f"Minimum Distance Between Star A and Binary Pair BC: {A_BC_minimum_distance} AU")

        A_BC_maximum_distance = A_BC_average_distance * (1 + A_BC_eccentricity)
        A_BC_maximum_distance = round(A_BC_maximum_distance, 3)
        print(f"Maximum Distance Between Star A and Binary Pair BC: {A_BC_maximum_distance} AU")

        A_BC_orbital_period = math.sqrt(( A_BC_average_distance ** 3) / (Final_Mass_A + Final_Mass_B + Final_Mass_C))
        A_BC_orbital_period = round(A_BC_orbital_period,2)
        print(f"Orbital Period of Star A and Binary Pair BC: {A_BC_orbital_period} years")
        A_BC_orbital_period_days = A_BC_orbital_period * 365.26
        A_BC_orbital_period_days = round(A_BC_orbital_period_days,2)
        print(f"which is equivalent to {A_BC_orbital_period_days} days")

    if Stellar_Arrangement == "AB-C":
        roll_for_AB_separation_type = ((_3d6())-3)
        if roll_for_AB_separation_type <= 3:
            AB_separation_type = "Extremely Close"
            AB_separation_base_distance = 0.015
        if 4 <= roll_for_AB_separation_type <= 5:
            AB_separation_type = "Very Close"
            AB_separation_base_distance = 0.15
        if 6 <= roll_for_AB_separation_type <= 8:
            AB_separation_type = "Close"
            AB_separation_base_distance = 1.5
        if 9 <= roll_for_AB_separation_type <= 12:
            AB_separation_type = "Moderate"
            AB_separation_base_distance = 15
        if 13 <= roll_for_AB_separation_type <= 15:
            AB_separation_type = "Wide"
            AB_separation_base_distance = 150
        print(f"AB-C Triple Star System with {AB_separation_type} Separation Between Star A and Star B")
        print(f"Base Distance Between Star A and Star B: {AB_separation_base_distance} AU")

        roll_for_AB_average_distance = ((d100())/100)
        AB_average_distance = AB_separation_base_distance * (10 ** roll_for_AB_average_distance)
        AB_distance_variance_factor = random.uniform(0.95, 1.05)
        AB_average_distance = (AB_distance_variance_factor * AB_average_distance)
        AB_average_distance = round(AB_average_distance, 3)
        print(f"Average Distance Between Star A and Star B: {AB_average_distance} AU")

        if AB_separation_type == "Extremely Close":
            AB_eccentricity_roll_modifier = -8
        if AB_separation_type == "Very Close":
            AB_eccentricity_roll_modifier = -6
        if AB_separation_type == "Close":
            AB_eccentricity_roll_modifier = -4
        if AB_separation_type == "Moderate":
            AB_eccentricity_roll_modifier = -2
        if AB_separation_type == "Wide":
            AB_eccentricity_roll_modifier = 0

        roll_for_AB_orbital_eccentricity = _3d6() + AB_eccentricity_roll_modifier 
        # If at Moderate separation, modify by -2.
        if roll_for_AB_orbital_eccentricity <= 3:
            AB_eccentricity = 0.0
        if roll_for_AB_orbital_eccentricity == 4:
            AB_eccentricity = 0.1
        if 5 <= roll_for_AB_orbital_eccentricity <= 6:
            AB_eccentricity = 0.2
        if 7 <= roll_for_AB_orbital_eccentricity <= 8:
            AB_eccentricity = 0.3
        if 9 <= roll_for_AB_orbital_eccentricity <= 11:
            AB_eccentricity = 0.4
        if 12 <= roll_for_AB_orbital_eccentricity <= 13:
            AB_eccentricity = 0.5
        if 14 <= roll_for_AB_orbital_eccentricity <= 15:
            AB_eccentricity = 0.6
        if roll_for_AB_orbital_eccentricity == 6:
            AB_eccentricity = 0.7
        if roll_for_AB_orbital_eccentricity == 17:
            AB_eccentricity = 0.8
        if roll_for_AB_orbital_eccentricity == 18:
            AB_eccentricity = 0.9
        print(f"Eccentricity of Star C orbit around Star A: {AB_eccentricity}")
    
        AB_minimum_distance = AB_average_distance * (1 - AB_eccentricity)
        AB_minimum_distance = round(AB_minimum_distance, 3)
        print(f"Minimum Distance Between Star A and Star B: {AB_minimum_distance} AU")

        AB_maximum_distance = AB_average_distance * (1 + AB_eccentricity)
        AB_maximum_distance = round(AB_maximum_distance, 3)
        print(f"Maximum Distance Between Star A and Star B: {AB_maximum_distance} AU")

        AB_orbital_period = math.sqrt(( AB_average_distance ** 3) / (Final_Mass_A + Final_Mass_B))
        AB_orbital_period = round(AB_orbital_period,2)
        print(f"Orbital Period of Star A and Star B: {AB_orbital_period} years")
        AB_orbital_period_days = AB_orbital_period * 365.26
        AB_orbital_period_days = round(AB_orbital_period_days,2)
        print(f"which is equivalent to {AB_orbital_period_days} days")

        # Check for Special Case: Close Binary Pairs
        Flag_for_Close_Binary_AB_in_AB_C = "No"
        if AB_separation_type == "Extremely Close":
            Flag_for_Close_Binary_AB_in_AB_C == "Yes"
        if AB_separation_type == "Very Close" or "Close":
            if Evolutionary_Stage_of_Star_A == "Red Giant Branch":
                Flag_for_Close_Binary_AB_in_AB_C == "Yes"            
            if Evolutionary_Stage_of_Star_B == "Red Giant Branch":
                Flag_for_Close_Binary_AB_in_AB_C == "Yes"

        if Flag_for_Close_Binary_AB_in_AB_C == "Yes":
            # Calculate radius of Roche Lobe of Star A
            Roche_Lobe_Radius_A = AB_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_A / Final_Mass_B)))
            # Calculate radius of Roche Lobe of Star B
            Roche_Lobe_Radius_B = AB_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_B / Final_Mass_A)))
            if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
                print("Binary Pair AB in an AB-C type triple star system is a Contact Binary")
                print("Evolution of this star system is out of scope for this model")
            if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
                print("Binary Pair AB in an AB-C type triple star system is Semi-Detached Biniary - Star B is larger than it's Roche Lobe")
                print("Evolution of this star system is out of scope for this model")
                if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                    print("Star A is a candidate to become a recurrent nova")
                if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                    print("Star B is a candidate to become a recurrent nova")
            if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
                print("Binary Pair AB in an AB-C type triple star system is Semi-Detached Biniary - Star A is larger than it's Roche Lobe")
                print("Evolution of this star system is out of scope for this model")
                if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                    print("Star A is a candidate to become a recurrent nova")
                if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                    print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                    print("Star B is a candidate to become a recurrent nova")
            if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
                print("Confirmed - pair AB is a Detached Binary within an AB-C type triple star system")

        roll_for_AB_C_separation_type = _3d6()
        if roll_for_AB_C_separation_type <= 3:
            AB_C_separation_type = "Extremely Close"
            AB_C_separation_base_distance = 0.015
            if AB_separation_type == "Extremely Close":
                AB_C_separation_type = "Very Close"
                AB_C_separation_base_distance = 0.15
        if 4 <= roll_for_AB_C_separation_type <= 5:
            AB_C_separation_type = "Very Close"
            AB_C_separation_base_distance = 0.15
            if AB_separation_type in ["Very Close", "Extremely Close"]:
                AB_C_seperation_type = "Close"
                AB_C_separation_base_distance = 1.5
        if 6 <= roll_for_AB_C_separation_type <= 8:
            AB_C_separation_type = "Close"
            AB_C_separation_base_distance = 1.5
            if AB_separation_type in ["Very Close", "Extremely Close", "Close"]:
                AB_C_separation_type = "Moderate"
                AB_C_separation_base_distance = 15
        if 9 <= roll_for_AB_C_separation_type <= 12:
            AB_C_separation_type = "Moderate"
            AB_C_separation_base_distance = 15
            if AB_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate"]:
                AB_C_separation_type = "Wide"
                AB_C_separation_base_distance = 150
        if 13 <= roll_for_AB_C_separation_type <= 15:
            AB_C_separation_type = "Wide"
            AB_C_separation_base_distance = 150
            if AB_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate", "Wide"]:
                AB_C_separation_type = "Very Wide"
                AB_C_separation_base_distance = 1500
        if 16 <= roll_for_AB_C_separation_type:
            AB_C_separation_type = "Very Wide"
            AB_C_separation_base_distance = 1500
        print(f"Triple Star System with {AB_C_separation_type} Separation Between Star C and Binary Star System AB")
        print(f"Base Distance Between Star C and Binary Star System AB: {AB_C_separation_base_distance} AU")
    
        roll_for_AB_C_average_distance = ((d100())/100)
        AB_C_average_distance = AB_C_separation_base_distance * (10 ** roll_for_AB_C_average_distance)
        AB_C_distance_variance_factor = random.uniform(0.95, 1.05)
        AB_C_average_distance = (AB_C_distance_variance_factor * AB_C_average_distance)
        AB_C_average_distance = round(AB_C_average_distance, 3)
        print(f"Average Distance Between Star C and Binary Star System AB: {AB_C_average_distance} AU")

        if AB_C_separation_type == "Extremely Close":
            AB_C_eccentricity_roll_modifier = -8
        if AB_C_separation_type == "Very Close":
            AB_C_eccentricity_roll_modifier = -6
        if AB_C_separation_type == "Close":
            AB_C_eccentricity_roll_modifier = -4
        if AB_C_separation_type == "Moderate":
            AB_C_eccentricity_roll_modifier = -2
        if AB_C_separation_type == "Wide":
            AB_C_eccentricity_roll_modifier = 0
        if AB_C_separation_type == "Very Wide":
            AB_C_eccentricity_roll_modifier = 0

        roll_for_AB_C_orbital_eccentricity = _3d6() + AB_C_eccentricity_roll_modifier 
        # If at Moderate separation, modify by -2.
        if roll_for_AB_C_orbital_eccentricity <= 3:
            AB_C_eccentricity = 0.0
        if roll_for_AB_C_orbital_eccentricity == 4:
            AB_C_eccentricity = 0.1
        if 5 <= roll_for_AB_C_orbital_eccentricity <= 6:
            AB_C_eccentricity = 0.2
        if 7 <= roll_for_AB_C_orbital_eccentricity <= 8:
            AB_C_eccentricity = 0.3
        if 9 <= roll_for_AB_C_orbital_eccentricity <= 11:
            AB_C_eccentricity = 0.4
        if 12 <= roll_for_AB_C_orbital_eccentricity <= 13:
            AB_C_eccentricity = 0.5
        if 14 <= roll_for_AB_C_orbital_eccentricity <= 15:
            AB_C_eccentricity = 0.6
        if roll_for_AB_C_orbital_eccentricity == 6:
            AB_C_eccentricity = 0.7
        if roll_for_AB_C_orbital_eccentricity == 17:
            AB_C_eccentricity = 0.8
        if roll_for_AB_C_orbital_eccentricity == 18:
            AB_C_eccentricity = 0.9
        print(f"Eccentricity of Star C Orbit Around Binary Pair AB: {AB_C_eccentricity}")
    
        AB_C_minimum_distance = AB_C_average_distance * (1 - AB_C_eccentricity)
        if AB_C_minimum_distance < (3 * AB_maximum_distance):
            AB_C_adjusted_average_distance = (3 * AB_maximum_distance) / (1 - AB_C_eccentricity)
            print(f"Stability Issue Detected - Adjusting Average Distance Between Star C and Binary Star System AB to: {AB_C_adjusted_average_distance} AU")
            AB_C_average_distance = AB_C_adjusted_average_distance
            AB_C_minimum_distance = AB_C_average_distance * (1 - AB_C_eccentricity)       
        AB_C_minimum_distance = round(AB_C_minimum_distance, 3)
        print(f"Minimum Distance Between Star C and Binary Pair AB: {AB_C_minimum_distance} AU")

        AB_C_maximum_distance = AB_C_average_distance * (1 + AB_C_eccentricity)
        AB_C_maximum_distance = round(AB_C_maximum_distance, 3)
        print(f"Maximum Distance Between Star C and Binary Pair AB: {AB_C_maximum_distance} AU")

        AB_C_orbital_period = math.sqrt(( AB_C_average_distance ** 3) / (Final_Mass_A + Final_Mass_B + Final_Mass_C))
        AB_C_orbital_period = round(AB_C_orbital_period,2)
        print(f"Orbital Period of Star C and Binary Pair AB: {AB_C_orbital_period} years")
        AB_C_orbital_period_days = AB_C_orbital_period * 365.26
        AB_C_orbital_period_days = round(AB_C_orbital_period_days,2)
        print(f"which is equivalent to {AB_C_orbital_period_days} days")

if Number_of_Stars == 4:
        
    # prepare mass and radius parameters for orbital calculations (final mass applies - Newton doesn't care if you are a white dwarf or main sequence)
    if Evolutionary_Stage_of_Star_A == "White Dwarf":
        Final_Mass_A = Mass_WDA
        Final_Radius_A = Radius_of_White_Dwarf_A
    if Evolutionary_Stage_of_Star_A != "White Dwarf":
        Final_Mass_A = Mass_A
        Final_Radius_A = Radius_of_Star_A
    if Evolutionary_Stage_of_Star_B == "White Dwarf":
        Final_Mass_B = Mass_WDB
        Final_Radius_B = Radius_of_White_Dwarf_A
    if Evolutionary_Stage_of_Star_B != "White Dwarf":
        Final_Mass_B = Mass_B
        Final_Radius_B = Radius_of_Star_B
    if Evolutionary_Stage_of_Star_C == "White Dwarf":
        Final_Mass_C = Mass_WDC
        Final_Raduis_C = Radius_of_White_Dwarf_C
    if Evolutionary_Stage_of_Star_C != "White Dwarf":
        Final_Mass_C = Mass_C
        Final_Radius_C = Radius_of_Star_C
    if Evolutionary_Stage_of_Star_D == "White Dwarf":
        Final_Mass_D = Mass_WDD
        Final_Raduis_D = Radius_of_White_Dwarf_D
    if Evolutionary_Stage_of_Star_D != "White Dwarf":
        Final_Mass_D = Mass_D
        Final_Radius_D = Radius_of_Star_D

    roll_for_AB_separation_type = ((_3d6())-3)
    if roll_for_AB_separation_type <= 3:
        AB_separation_type = "Extremely Close"
        AB_separation_base_distance = 0.015
    if 4 <= roll_for_AB_separation_type <= 5:
        AB_separation_type = "Very Close"
        AB_separation_base_distance = 0.15
    if 6 <= roll_for_AB_separation_type <= 8:
        AB_separation_type = "Close"
        AB_separation_base_distance = 1.5
    if 9 <= roll_for_AB_separation_type <= 12:
        AB_separation_type = "Moderate"
        AB_separation_base_distance = 15
    if 13 <= roll_for_AB_separation_type <= 15:
        AB_separation_type = "Wide"
        AB_separation_base_distance = 150
    print(f"Quadruple Star System with {AB_separation_type} Separation Between Star A and Star B")
    print(f"Base Distance Between Star A and Star B: {AB_separation_base_distance} AU")

    roll_for_AB_average_distance = ((d100())/100)
    AB_average_distance = AB_separation_base_distance * (10 ** roll_for_AB_average_distance)
    AB_distance_variance_factor = random.uniform(0.95, 1.05)
    AB_average_distance = (AB_distance_variance_factor * AB_average_distance)
    AB_average_distance = round(AB_average_distance, 3)
    print(f"Average Distance Between Star A and Star B: {AB_average_distance} AU")

    if AB_separation_type == "Extremely Close":
        AB_eccentricity_roll_modifier = -8
    if AB_separation_type == "Very Close":
        AB_eccentricity_roll_modifier = -6
    if AB_separation_type == "Close":
        AB_eccentricity_roll_modifier = -4
    if AB_separation_type == "Moderate":
        AB_eccentricity_roll_modifier = -2
    if AB_separation_type == "Wide":
        AB_eccentricity_roll_modifier = 0

    roll_for_AB_orbital_eccentricity = _3d6() + AB_eccentricity_roll_modifier 
    # If at Moderate separation, modify by -2.
    if roll_for_AB_orbital_eccentricity <= 3:
        AB_eccentricity = 0.0
    if roll_for_AB_orbital_eccentricity == 4:
        AB_eccentricity = 0.1
    if 5 <= roll_for_AB_orbital_eccentricity <= 6:
        AB_eccentricity = 0.2
    if 7 <= roll_for_AB_orbital_eccentricity <= 8:
        AB_eccentricity = 0.3
    if 9 <= roll_for_AB_orbital_eccentricity <= 11:
        AB_eccentricity = 0.4
    if 12 <= roll_for_AB_orbital_eccentricity <= 13:
        AB_eccentricity = 0.5
    if 14 <= roll_for_AB_orbital_eccentricity <= 15:
        AB_eccentricity = 0.6
    if roll_for_AB_orbital_eccentricity == 6:
        AB_eccentricity = 0.7
    if roll_for_AB_orbital_eccentricity == 17:
        AB_eccentricity = 0.8
    if roll_for_AB_orbital_eccentricity == 18:
        AB_eccentricity = 0.9
    print(f"Eccentricity of Star C orbit around Star A: {AB_eccentricity}")
    
    AB_minimum_distance = AB_average_distance * (1 - AB_eccentricity)
    AB_minimum_distance = round(AB_minimum_distance, 3)
    print(f"Minimum Distance Between Star A and Star B: {AB_minimum_distance} AU")

    AB_maximum_distance = AB_average_distance * (1 + AB_eccentricity)
    AB_maximum_distance = round(AB_maximum_distance, 3)
    print(f"Maximum Distance Between Star A and Star B: {AB_maximum_distance} AU")

    AB_orbital_period = math.sqrt(( AB_average_distance ** 3) / (Final_Mass_A + Final_Mass_B))
    AB_orbital_period = round(AB_orbital_period,2)
    print(f"Orbital Period of Star A and Star B: {AB_orbital_period} years")
    AB_orbital_period_days = AB_orbital_period * 365.26
    AB_orbital_period_days = round(AB_orbital_period_days,2)
    print(f"which is equivalent to {AB_orbital_period_days} days")

    # Check for Special Case: Close Binary Pairs
    Flag_for_Close_Binary_AB_in_AB_CD = "No"
    if AB_separation_type == "Extremely Close":
        Flag_for_Close_Binary_AB_in_AB_CD == "Yes"
    if AB_separation_type == "Very Close" or "Close":
        if Evolutionary_Stage_of_Star_A == "Red Giant Branch":
            Flag_for_Close_Binary_AB_in_AB_CD == "Yes"            
        if Evolutionary_Stage_of_Star_B == "Red Giant Branch":
            Flag_for_Close_Binary_AB_in_AB_CD == "Yes"

    if Flag_for_Close_Binary_AB_in_AB_CD == "Yes":
        # Calculate radius of Roche Lobe of Star A
        Roche_Lobe_Radius_A = AB_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_A / Final_Mass_B)))
        # Calculate radius of Roche Lobe of Star B
        Roche_Lobe_Radius_B = AB_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_B / Final_Mass_A)))
        if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
            print("Binary Pair AB in a quadruple star system is a Contact Binary")
            print("Evolution of this star system is out of scope for this model")
        if (Roche_Lobe_Radius_A < Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
            print("Binary Pair AB in a quaruple star system is Semi-Detached Biniary - Star B is larger than it's Roche Lobe")
            print("Evolution of this star system is out of scope for this model")
            if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                print("Star A is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                print("Star B is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B < Final_Radius_B):
            print("Binary Pair AB in a quadruple star system is Semi-Detached Biniary - Star A is larger than it's Roche Lobe")
            print("Evolution of this star system is out of scope for this model")
            if Evolutionary_Stage_of_Star_A == "White Dwarf" and Evolutionary_Stage_of_Star_B != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star A) is a White Dwarf")
                print("Star A is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_A != "White Dwarf" and Evolutionary_Stage_of_Star_B == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star B) is a White Dwarf")
                print("Star B is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
            print("Confirmed - pair AB is a Detached Binary within an AB-C type triple star system")

    roll_for_CD_separation_type = ((_3d6())-3)
    if roll_for_CD_separation_type <= 3:
        CD_separation_type = "Extremely Close"
        CD_separation_base_distance = 0.015
    if 4 <= roll_for_CD_separation_type <= 5:
        CD_separation_type = "Very Close"
        CD_separation_base_distance = 0.15
    if 6 <= roll_for_CD_separation_type <= 8:
        CD_separation_type = "Close"
        CD_separation_base_distance = 1.5
    if 9 <= roll_for_CD_separation_type <= 12:
        CD_separation_type = "Moderate"
        CD_separation_base_distance = 15
    if 13 <= roll_for_CD_separation_type <= 15:
        CD_separation_type = "Wide"
        CD_separation_base_distance = 150
    print(f"Quadruple Star System with {CD_separation_type} Separation Between Star C and Star D")
    print(f"Base Distance Between Star C and Star D: {CD_separation_base_distance} AU")

    roll_for_CD_average_distance = ((d100())/100)
    CD_average_distance = CD_separation_base_distance * (10 ** roll_for_CD_average_distance)
    CD_distance_variance_factor = random.uniform(0.95, 1.05)
    CD_average_distance = (CD_distance_variance_factor * CD_average_distance)
    CD_average_distance = round(CD_average_distance, 3)
    print(f"Average Distance Between Star C and Star D: {CD_average_distance} AU")

    if CD_separation_type == "Extremely Close":
        CD_eccentricity_roll_modifier = -8
    if CD_separation_type == "Very Close":
        CD_eccentricity_roll_modifier = -6
    if CD_separation_type == "Close":
        CD_eccentricity_roll_modifier = -4
    if CD_separation_type == "Moderate":
        CD_eccentricity_roll_modifier = -2
    if CD_separation_type == "Wide":
        CD_eccentricity_roll_modifier = 0

    roll_for_CD_orbital_eccentricity = _3d6() + CD_eccentricity_roll_modifier 
    # If at Moderate separation, modify by -2.
    if roll_for_CD_orbital_eccentricity <= 3:
        CD_eccentricity = 0.0
    if roll_for_CD_orbital_eccentricity == 4:
        CD_eccentricity = 0.1
    if 5 <= roll_for_CD_orbital_eccentricity <= 6:
        CD_eccentricity = 0.2
    if 7 <= roll_for_CD_orbital_eccentricity <= 8:
        CD_eccentricity = 0.3
    if 9 <= roll_for_CD_orbital_eccentricity <= 11:
        CD_eccentricity = 0.4
    if 12 <= roll_for_CD_orbital_eccentricity <= 13:
        CD_eccentricity = 0.5
    if 14 <= roll_for_CD_orbital_eccentricity <= 15:
        CD_eccentricity = 0.6
    if roll_for_CD_orbital_eccentricity == 6:
        CD_eccentricity = 0.7
    if roll_for_CD_orbital_eccentricity == 17:
        CD_eccentricity = 0.8
    if roll_for_CD_orbital_eccentricity == 18:
        CD_eccentricity = 0.9
    print(f"Eccentricity of Star C orbit around Star D: {CD_eccentricity}")
    
    CD_minimum_distance = CD_average_distance * (1 - CD_eccentricity)
    CD_minimum_distance = round(CD_minimum_distance, 3)
    print(f"Minimum Distance Between Star C and Star D: {CD_minimum_distance} AU")

    CD_maximum_distance = CD_average_distance * (1 + CD_eccentricity)
    CD_maximum_distance = round(CD_maximum_distance, 3)
    print(f"Maximum Distance Between Star C and Star D: {CD_maximum_distance} AU")

    CD_orbital_period = math.sqrt(( CD_average_distance ** 3) / (Final_Mass_C + Final_Mass_D))
    CD_orbital_period = round(CD_orbital_period,2)
    print(f"Orbital Period of Star C and Star D: {CD_orbital_period} years")
    CD_orbital_period_days = CD_orbital_period * 365.26
    CD_orbital_period_days = round(CD_orbital_period_days,2)
    print(f"which is equivalent to {CD_orbital_period_days} days")

    # Check for Special Case: Close Binary Pairs
    Flag_for_Close_Binary_CD_in_AB_CD = "No"
    if CD_separation_type == "Extremely Close":
        Flag_for_Close_Binary_AB_in_AB_C == "Yes"
    if CD_separation_type == "Very Close" or "Close":
        if Evolutionary_Stage_of_Star_A == "Red Giant Branch":
            Flag_for_Close_Binary_AB_in_AB_CD == "Yes"            
        if Evolutionary_Stage_of_Star_B == "Red Giant Branch":
            Flag_for_Close_Binary_AB_in_AB_CD == "Yes"

    if Flag_for_Close_Binary_AB_in_AB_CD == "Yes":
        # Calculate radius of Roche Lobe of Star C
        Roche_Lobe_Radius_C = CD_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_C / Final_Mass_D)))
        # Calculate radius of Roche Lobe of Star D
        Roche_Lobe_Radius_D = CD_minimum_distance * (0.38 + (0.2 * math.log10(Final_Mass_D / Final_Mass_C)))
        if (Roche_Lobe_Radius_C < Final_Radius_C) and (Roche_Lobe_Radius_D < Final_Radius_D):
            print("Binary Pair CD in a quadruple star system is a Contact Binary")
            print("Evolution of this star system is out of scope for this model")
            if Evolutionary_Stage_of_Star_C == "White Dwarf" and Evolutionary_Stage_of_Star_D != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star C) is a White Dwarf")
                print("Star C is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_C != "White Dwarf" and Evolutionary_Stage_of_Star_D == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star D) is a White Dwarf")
                print("Star D is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_C < Final_Radius_C) and (Roche_Lobe_Radius_D >= Final_Radius_D):
            print("Binary Pair CD in a quadruple star system is a Semi-Detached Biniary - Star C is larger than it's Roche Lobe")
            print("Evolution of this star system is out of scope for this model")
            if Evolutionary_Stage_of_Star_C == "White Dwarf" and Evolutionary_Stage_of_Star_D != "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star C) is a White Dwarf")
                print("Star C is a candidate to become a recurrent nova")
            if Evolutionary_Stage_of_Star_C != "White Dwarf" and Evolutionary_Stage_of_Star_D == "White Dwarf":
                print("However - Criteria Met: Semi-Detached Binary where one star (Star D) is a White Dwarf")
                print("Star D is a candidate to become a recurrent nova")
        if (Roche_Lobe_Radius_C >= Final_Radius_C) and (Roche_Lobe_Radius_D < Final_Radius_D):
            print("Binary Pair CD in a quadruple star system is Semi-Detached Biniary - Star D is larger than it's Roche Lobe")
            print("Evolution of this star system is out of scope for this model")
        if (Roche_Lobe_Radius_A >= Final_Radius_A) and (Roche_Lobe_Radius_B >= Final_Radius_B):
            print("Confirmed - pair CD is a Detached Binary within an quadruple star system")

    roll_for_AB_CD_separation_type = _3d6()
    if roll_for_AB_CD_separation_type <= 3:
        AB_CD_separation_type = "Extremely Close"
        AB_CD_separation_base_distance = 0.015
        if AB_separation_type == "Extremely Close" or CD_separation_type == "Extremely Close":
            AB_CD_separation_type = "Very Close"
            AB_CD_separation_base_distance = 0.15
        if 4 <= roll_for_AB_CD_separation_type <= 5:
            AB_CD_separation_type = "Very Close"
            AB_CD_separation_base_distance = 0.15
        if AB_separation_type in ["Very Close", "Extremely Close"] or CD_separation_type in ["Very Close", "Extremey Close"]:
            AB_CD_seperation_type = "Close"
            AB_CD_separation_base_distance = 1.5
        if 6 <= roll_for_AB_CD_separation_type <= 8:
            AB_CD_separation_type = "Close"
            AB_CD_separation_base_distance = 1.5
        if AB_separation_type in ["Very Close", "Extremely Close", "Close"] or CD_separation_type in ["Very Close", "Extremely Close", "Close"]:
            AB_CD_separation_type = "Moderate"
            AB_CD_separation_base_distance = 15
        if 9 <= roll_for_AB_CD_separation_type <= 12:
            AB_CD_separation_type = "Moderate"
            AB_CD_separation_base_distance = 15
        if AB_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate"]:
            AB_CD_separation_type = "Wide"
            AB_CD_separation_base_distance = 150
        if CD_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate"]:
            AB_CD_separation_type = "Wide"
            AB_CD_separation_base_distance = 150
        if 13 <= roll_for_AB_CD_separation_type <= 15:
            AB_CD_separation_type = "Wide"
            AB_CD_separation_base_distance = 150
        if AB_separation_type in ["Very Close", "Extremely Close", "Close", "Moderate", "Wide"]:
            AB_CD_separation_type = "Very Wide"
            AB_CD_separation_base_distance = 1500
        if CD_separation_type in ["Very Close", "Extremey Close", "Close", "Moderate", "Wide"]:
            AB_CD_separation_type = "Very Wide"
            AB_CD_separation_base_distance = 1500
        if 16 <= roll_for_AB_CD_separation_type:
            AB_CD_separation_type = "Very Wide"
            AB_CD_separation_base_distance = 1500
        print(f"Quadruple Star System with {AB_CD_separation_type} Separation Between Binary Star System AB and Binary Star System CD")
        print(f"Base Distance Between Binary Star System AB and Binary Star System CD: {AB_CD_separation_base_distance} AU")
    
        roll_for_AB_CD_average_distance = ((d100())/100)
        AB_CD_average_distance = AB_CD_separation_base_distance * (10 ** roll_for_AB_CD_average_distance)
        AB_CD_distance_variance_factor = random.uniform(0.95, 1.05)
        AB_CD_average_distance = (AB_CD_distance_variance_factor * AB_CD_average_distance)
        AB_CD_average_distance = round(AB_CD_average_distance, 3)
        print(f"Average Distance Between Binary Pair AB and Binary Pair CD: {AB_CD_average_distance} AU")

        if AB_CD_separation_type == "Extremely Close":
            AB_CD_eccentricity_roll_modifier = -8
        if AB_CD_separation_type == "Very Close":
            AB_CD_eccentricity_roll_modifier = -6
        if AB_CD_separation_type == "Close":
            AB_CD_eccentricity_roll_modifier = -4
        if AB_CD_separation_type == "Moderate":
            AB_CD_eccentricity_roll_modifier = -2
        if AB_CD_separation_type == "Wide":
            AB_CD_eccentricity_roll_modifier = 0
        if AB_CD_separation_type == "Very Wide":
            AB_CD_eccentricity_roll_modifier = 0

        roll_for_AB_CD_orbital_eccentricity = _3d6() + AB_CD_eccentricity_roll_modifier 
        # If at Moderate separation, modify by -2.
        if roll_for_AB_CD_orbital_eccentricity <= 3:
            AB_CD_eccentricity = 0.0
        if roll_for_AB_CD_orbital_eccentricity == 4:
            AB_CD_eccentricity = 0.1
        if 5 <= roll_for_AB_CD_orbital_eccentricity <= 6:
            AB_CD_eccentricity = 0.2
        if 7 <= roll_for_AB_CD_orbital_eccentricity <= 8:
            AB_CD_eccentricity = 0.3
        if 9 <= roll_for_AB_CD_orbital_eccentricity <= 11:
            AB_CD_eccentricity = 0.4
        if 12 <= roll_for_AB_CD_orbital_eccentricity <= 13:
            AB_CD_eccentricity = 0.5
        if 14 <= roll_for_AB_CD_orbital_eccentricity <= 15:
            AB_CD_eccentricity = 0.6
        if roll_for_AB_CD_orbital_eccentricity == 6:
            AB_CD_eccentricity = 0.7
        if roll_for_AB_CD_orbital_eccentricity == 17:
            AB_CD_eccentricity = 0.8
        if roll_for_AB_CD_orbital_eccentricity == 18:
            AB_CD_eccentricity = 0.9
        print(f"Eccentricity of Binary Pair CD Orbit Around Binary Pair AB: {AB_CD_eccentricity}")
    
        AB_CD_minimum_distance = AB_CD_average_distance * (1 - AB_CD_eccentricity)
        Maximum_Binary_Distance = max(AB_maximum_distance, CD_maximum_distance)
        if AB_CD_minimum_distance < (3 * Maximum_Binary_Distance):
            AB_CD_adjusted_average_distance = (3 * Maximum_Binary_Distance) / (1 - AB_CD_eccentricity)
            print(f"Stability Issue Detected - Adjusting Average Distance Between Binary Pair AB and Binary Pair CD to: {AB_CD_adjusted_average_distance} AU")
            AB_CD_average_distance = AB_CD_adjusted_average_distance
            AB_CD_minimum_distance = AB_CD_average_distance * (1 - AB_CD_eccentricity)       
        AB_CD_minimum_distance = round(AB_CD_minimum_distance, 3)
        print(f"Minimum Distance Between Binary Pair AB and Binary Pair CD: {AB_CD_minimum_distance} AU")

        AB_CD_maximum_distance = AB_CD_average_distance * (1 + AB_CD_eccentricity)
        AB_CD_maximum_distance = round(AB_CD_maximum_distance, 3)
        print(f"Maximum Distance Between Binary Pair AB and Binary Pair CD: {AB_CD_maximum_distance} AU")

        # Star A, B, C and D masses have already been prepared for orbital period calculation in previous steps
        AB_CD_orbital_period = math.sqrt(( AB_CD_average_distance ** 3) / (Final_Mass_A + Final_Mass_B + Final_Mass_C + Final_Mass_D))
        AB_CD_orbital_period = round(AB_CD_orbital_period,2)
        print(f"Orbital Period of Binary Pair AB and Binary Pair CD: {AB_CD_orbital_period} years")
        AB_CD_orbital_period_days = AB_CD_orbital_period * 365.26
        AB_CD_orbital_period_days = round(AB_CD_orbital_period_days,2)
        print(f"which is equivalent to {AB_CD_orbital_period_days} days")
