# this sub-program covers step 3 ("Arrange Components") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

Mass_Ratio = None
Stellar_Arrangement = None

if Number_of_Stars == 1:
    Stellar_Arrangement = "A"
    print("Single Star System - skipping step #3")
 
elif Number_of_Stars <= 2:
    roll_for_binary_mass_ratio = d100()
    if roll_for_binary_mass_ratio <= 4:
        Mass_Ratio = 0.05
    elif 5 <= roll_for_binary_mass_ratio <= 8:
        Mass_Ratio = 0.10
    elif 9 <= roll_for_binary_mass_ratio <= 12:
        Mass_Ratio = 0.15
    elif 13 <= roll_for_binary_mass_ratio <= 16:
        Mass_Ratio = 0.20
    elif 17 <= roll_for_binary_mass_ratio <= 20:
        Mass_Ratio = 0.25
    elif 21 <= roll_for_binary_mass_ratio <= 24:
        Mass_Ratio = 0.30
    elif 25 <= roll_for_binary_mass_ratio <= 28:
        Mass_Ratio = 0.35
    elif 29 <= roll_for_binary_mass_ratio <= 31:
        Mass_Ratio = 0.40
    elif 32 <= roll_for_binary_mass_ratio <= 34:
        Mass_Ratio = 0.45
    elif 35 <= roll_for_binary_mass_ratio <= 38:
        Mass_Ratio = 0.50
    elif 39 <= roll_for_binary_mass_ratio <= 43:
        Mass_Ratio = 0.55
    elif 44 <= roll_for_binary_mass_ratio <= 48:
        Mass_Ratio = 0.60
    elif 49 <= roll_for_binary_mass_ratio <= 53:
        Mass_Ratio = 0.65
    elif 54 <= roll_for_binary_mass_ratio <= 58:
        Mass_Ratio = 0.70
    elif 59 <= roll_for_binary_mass_ratio <= 63:
        Mass_Ratio = 0.75
    elif 64 <= roll_for_binary_mass_ratio <= 69:
        Mass_Ratio = 0.80
    elif 70 <= roll_for_binary_mass_ratio <= 76:
        Mass_Ratio = 0.85
    elif 77 <= roll_for_binary_mass_ratio <= 86:
        Mass_Ratio = 0.90
    elif 87 <= roll_for_binary_mass_ratio <= 100:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star A and Star B: {Mass_Ratio}")
    Mass_B = Mass_A * Mass_Ratio
    if Mass_B < 0.015:
        Mass_B = 0.015
    Mass_B = round(Mass_B, 3)
    print(f"Mass of Star B: {Mass_B} solar masses")

elif Number_of_Stars == 3:
    random_integer = random.randint(1, 2)
    if random_integer == 1:
        Stellar_Arrangement = "A-BC"
        print("Triple Star System - A star with distant BC pair")
        roll_for_AB_mass_ratio = d100()
        if roll_for_AB_mass_ratio <= 4:
            Mass_Ratio = 0.05
        elif 5 <= roll_for_AB_mass_ratio <= 8:
            Mass_Ratio = 0.10
        elif 9 <= roll_for_AB_mass_ratio <= 12:
            Mass_Ratio = 0.15
        elif 13 <= roll_for_AB_mass_ratio <= 16:
            Mass_Ratio = 0.20
        elif 17 <= roll_for_AB_mass_ratio <= 20:
            Mass_Ratio = 0.25
        elif 21 <= roll_for_AB_mass_ratio <= 24:
            Mass_Ratio = 0.30
        elif 25 <= roll_for_AB_mass_ratio <= 28:
            Mass_Ratio = 0.35
        elif 29 <= roll_for_AB_mass_ratio <= 31:
            Mass_Ratio = 0.40
        elif 32 <= roll_for_AB_mass_ratio <= 34:
            Mass_Ratio = 0.45
        elif 35 <= roll_for_AB_mass_ratio <= 38:
            Mass_Ratio = 0.50
        elif 39 <= roll_for_AB_mass_ratio <= 43:
            Mass_Ratio = 0.55
        elif 44 <= roll_for_AB_mass_ratio <= 48:
            Mass_Ratio = 0.60
        elif 49 <= roll_for_AB_mass_ratio <= 53:
            Mass_Ratio = 0.65
        elif 54 <= roll_for_AB_mass_ratio <= 58:
            Mass_Ratio = 0.70
        elif 59 <= roll_for_AB_mass_ratio <= 63:
            Mass_Ratio = 0.75
        elif 64 <= roll_for_AB_mass_ratio <= 69:
            Mass_Ratio = 0.80
        elif 70 <= roll_for_AB_mass_ratio <= 76:
            Mass_Ratio = 0.85
        elif 77 <= roll_for_AB_mass_ratio <= 86:
            Mass_Ratio = 0.90
        elif roll_for_AB_mass_ratio >= 88:
            Mass_Ratio = 0.95
        print(f"Mass Ratio Between Star A and Star B: {Mass_Ratio}")
        Mass_B = Mass_A * Mass_Ratio
        if Mass_B < 0.015:
            Mass_B = 0.015
        Mass_B = round(Mass_B, 3)
        print(f"Mass of Star B: {Mass_B} solar masses")

        roll_for_BC_mass_ratio = (d100()+30)
        if roll_for_BC_mass_ratio == 31:
            Mass_Ratio = 0.40
        elif 32 <= roll_for_BC_mass_ratio <= 34:
            Mass_Ratio = 0.45
        elif 35 <= roll_for_BC_mass_ratio <= 38:
            Mass_Ratio = 0.50
        elif 39 <= roll_for_BC_mass_ratio <= 43:
            Mass_Ratio = 0.55
        elif 44 <= roll_for_BC_mass_ratio <= 48:
            Mass_Ratio = 0.60
        elif 49 <= roll_for_BC_mass_ratio <= 53:
            Mass_Ratio = 0.65
        elif 54 <= roll_for_BC_mass_ratio <= 58:
            Mass_Ratio = 0.70
        elif 59 <= roll_for_BC_mass_ratio <= 63:
            Mass_Ratio = 0.75
        elif 64 <= roll_for_BC_mass_ratio <= 69:
            Mass_Ratio = 0.80
        elif 70 <= roll_for_BC_mass_ratio <= 76:
            Mass_Ratio = 0.85
        elif 77 <= roll_for_BC_mass_ratio <= 86:
            Mass_Ratio = 0.90
        elif roll_for_BC_mass_ratio >= 88:
            Mass_Ratio = 0.95
        print(f"Mass Ratio Between Star B and Star C: {Mass_Ratio}")
        Mass_C = Mass_B * Mass_Ratio
        if Mass_C < 0.015:
            Mass_C = 0.015
        Mass_C = round(Mass_C, 3)
        print(f"Mass of Star C: {Mass_C} solar masses")

    elif random_integer == 2:
        Stellar_Arrangement = "AB-C"
        print("Triple Star System - AB as close companions with C as distant companion")
        roll_for_AB_mass_ratio = (d100()+30)
        if roll_for_AB_mass_ratio == 31:
            Mass_Ratio = 0.40
        elif 32 <= roll_for_AB_mass_ratio <= 34:
            Mass_Ratio = 0.45
        elif 35 <= roll_for_AB_mass_ratio <= 38:
            Mass_Ratio = 0.50
        elif 39 <= roll_for_AB_mass_ratio <= 43:
            Mass_Ratio = 0.55
        elif 44 <= roll_for_AB_mass_ratio <= 48:
            Mass_Ratio = 0.60
        elif 49 <= roll_for_AB_mass_ratio <= 53:
            Mass_Ratio = 0.65
        elif 54 <= roll_for_AB_mass_ratio <= 58:
            Mass_Ratio = 0.70
        elif 59 <= roll_for_AB_mass_ratio <= 63:
            Mass_Ratio = 0.75
        elif 64 <= roll_for_AB_mass_ratio <= 69:
            Mass_Ratio = 0.80
        elif 70 <= roll_for_AB_mass_ratio <= 76:
            Mass_Ratio = 0.85
        elif 77 <= roll_for_AB_mass_ratio <= 86:
            Mass_Ratio = 0.90
        elif roll_for_AB_mass_ratio >= 88:
            Mass_Ratio = 0.95
        print(f"Mass Ratio Between Star A and Star B: {Mass_Ratio}")
        Mass_B = Mass_A * Mass_Ratio
        if Mass_B < 0.015:
            Mass_B = 0.015
        print(f"Mass of Star B: {Mass_B} solar masses")

        roll_for_AC_mass_ratio = d100()
        if roll_for_AC_mass_ratio <= 4:
            Mass_Ratio = 0.05
        elif 5 <= roll_for_AC_mass_ratio <= 8:
            Mass_Ratio = 0.10
        elif 9 <= roll_for_AC_mass_ratio <= 12:
            Mass_Ratio = 0.15
        elif 13 <= roll_for_AC_mass_ratio <= 16:
            Mass_Ratio = 0.20
        elif 17 <= roll_for_AC_mass_ratio <= 20:
            Mass_Ratio = 0.25
        elif 21 <= roll_for_AC_mass_ratio <= 24:
            Mass_Ratio = 0.30
        elif 25 <= roll_for_AC_mass_ratio <= 28:
            Mass_Ratio = 0.35
        elif 29 <= roll_for_AC_mass_ratio <= 31:
            Mass_Ratio = 0.40
        elif 32 <= roll_for_AC_mass_ratio <= 34:
            Mass_Ratio = 0.45
        elif 35 <= roll_for_AC_mass_ratio <= 38:
            Mass_Ratio = 0.50
        elif 39 <= roll_for_AC_mass_ratio <= 43:
            Mass_Ratio = 0.55
        elif 44 <= roll_for_AC_mass_ratio <= 48:
            Mass_Ratio = 0.60
        elif 49 <= roll_for_AC_mass_ratio <= 53:
            Mass_Ratio = 0.65
        elif 54 <= roll_for_AC_mass_ratio <= 58:
            Mass_Ratio = 0.70
        elif 59 <= roll_for_AC_mass_ratio <= 63:
            Mass_Ratio = 0.75
        elif 64 <= roll_for_AC_mass_ratio <= 69:
            Mass_Ratio = 0.80
        elif 70 <= roll_for_AC_mass_ratio <= 76:
            Mass_Ratio = 0.85
        elif 77 <= roll_for_AC_mass_ratio <= 86:
            Mass_Ratio = 0.90
        elif roll_for_AC_mass_ratio >= 88:
            Mass_Ratio = 0.95
        print(f"Mass Ratio Between Star A and Star C: {Mass_Ratio}")
        Mass_C = Mass_A * Mass_Ratio
        if Mass_C < 0.015:
            Mass_C = 0.015
        Mass_C = round(Mass_C, 3)
        print(f"Mass of Star C: {Mass_C} solar masses")

elif Number_of_Stars == 4:
    Stellar_Arrangement = "AB-CD"
    print("Quadruple Star System - two binary sytems AB and CD with wide separation")

    roll_for_AB_mass_ratio = d100()
    if roll_for_AB_mass_ratio <= 4:
        Mass_Ratio = 0.05
    elif 5 <= roll_for_AB_mass_ratio <= 8:
        Mass_Ratio = 0.10
    elif 9 <= roll_for_AB_mass_ratio <= 12:
        Mass_Ratio = 0.15
    elif 13 <= roll_for_AB_mass_ratio <= 16:
        Mass_Ratio = 0.20
    elif 17 <= roll_for_AB_mass_ratio <= 20:
        Mass_Ratio = 0.25
    elif 21 <= roll_for_AB_mass_ratio <= 24:
        Mass_Ratio = 0.30
    elif 25 <= roll_for_AB_mass_ratio <= 28:
        Mass_Ratio = 0.35
    elif 29 <= roll_for_AB_mass_ratio <= 31:
        Mass_Ratio = 0.40
    elif 32 <= roll_for_AB_mass_ratio <= 34:
        Mass_Ratio = 0.45
    elif 35 <= roll_for_AB_mass_ratio <= 38:
        Mass_Ratio = 0.50
    elif 39 <= roll_for_AB_mass_ratio <= 43:
        Mass_Ratio = 0.55
    elif 44 <= roll_for_AB_mass_ratio <= 48:
        Mass_Ratio = 0.60
    elif 49 <= roll_for_AB_mass_ratio <= 53:
        Mass_Ratio = 0.65
    elif 54 <= roll_for_AB_mass_ratio <= 58:
        Mass_Ratio = 0.70
    elif 59 <= roll_for_AB_mass_ratio <= 63:
        Mass_Ratio = 0.75
    elif 64 <= roll_for_AB_mass_ratio <= 69:
        Mass_Ratio = 0.80
    elif 70 <= roll_for_AB_mass_ratio <= 76:
        Mass_Ratio = 0.85
    elif 77 <= roll_for_AB_mass_ratio <= 86:
        Mass_Ratio = 0.90
    elif roll_for_AB_mass_ratio >= 88:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star A and Star B: {Mass_Ratio}")
    Mass_B = Mass_A * Mass_Ratio
    if Mass_B < 0.015:
        Mass_B = 0.015
    Mass_B = round(Mass_B, 3)
    print(f"Mass of Star B: {Mass_B} solar masses")

    roll_for_AC_mass_ratio = d100()
    if roll_for_AC_mass_ratio <= 4:
        Mass_Ratio = 0.05
    elif 5 <= roll_for_AC_mass_ratio <= 8:
        Mass_Ratio = 0.10
    elif 9 <= roll_for_AC_mass_ratio <= 12:
        Mass_Ratio = 0.15
    elif 13 <= roll_for_AC_mass_ratio <= 16:
        Mass_Ratio = 0.20
    elif 17 <= roll_for_AC_mass_ratio <= 20:
        Mass_Ratio = 0.25
    elif 21 <= roll_for_AC_mass_ratio <= 24:
        Mass_Ratio = 0.30
    elif 25 <= roll_for_AC_mass_ratio <= 28:
        Mass_Ratio = 0.35
    elif 29 <= roll_for_AC_mass_ratio <= 31:
        Mass_Ratio = 0.40
    elif 32 <= roll_for_AC_mass_ratio <= 34:
        Mass_Ratio = 0.45
    elif 35 <= roll_for_AC_mass_ratio <= 38:
        Mass_Ratio = 0.50
    elif 39 <= roll_for_AC_mass_ratio <= 43:
        Mass_Ratio = 0.55
    elif 44 <= roll_for_AC_mass_ratio <= 48:
        Mass_Ratio = 0.60
    elif 49 <= roll_for_AC_mass_ratio <= 53:
        Mass_Ratio = 0.65
    elif 54 <= roll_for_AC_mass_ratio <= 58:
        Mass_Ratio = 0.70
    elif 59 <= roll_for_AC_mass_ratio <= 63:
        Mass_Ratio = 0.75
    elif 64 <= roll_for_AC_mass_ratio <= 69:
        Mass_Ratio = 0.80
    elif 70 <= roll_for_AC_mass_ratio <= 76:
        Mass_Ratio = 0.85
    elif 77 <= roll_for_AC_mass_ratio <= 86:
        Mass_Ratio = 0.90
    elif roll_for_AC_mass_ratio >= 88:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star A and Star C: {Mass_Ratio}")
    Mass_C = Mass_A * Mass_Ratio
    if Mass_C < 0.015:
        Mass_C = 0.015
    Mass_C = round(Mass_C, 3)
    print(f"Mass of Star C: {Mass_C} solar masses")

    roll_for_CD_mass_ratio = (d100()+30)
    if roll_for_CD_mass_ratio == 31:
        Mass_Ratio = 0.40
    elif 32 <= roll_for_CD_mass_ratio <= 34:
        Mass_Ratio = 0.45
    elif 35 <= roll_for_CD_mass_ratio <= 38:
        Mass_Ratio = 0.50
    elif 39 <= roll_for_CD_mass_ratio <= 43:
        Mass_Ratio = 0.55
    elif 44 <= roll_for_CD_mass_ratio <= 48:
        Mass_Ratio = 0.60
    elif 49 <= roll_for_CD_mass_ratio <= 53:
        Mass_Ratio = 0.65
    elif 54 <= roll_for_CD_mass_ratio <= 58:
        Mass_Ratio = 0.70
    elif 59 <= roll_for_CD_mass_ratio <= 63:
        Mass_Ratio = 0.75
    elif 64 <= roll_for_CD_mass_ratio <= 69:
        Mass_Ratio = 0.80
    elif 70 <= roll_for_CD_mass_ratio <= 76:
        Mass_Ratio = 0.85
    elif 77 <= roll_for_CD_mass_ratio <= 86:
        Mass_Ratio = 0.90
    elif 87 <= roll_for_CD_mass_ratio <= 130:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star C and Star D: {Mass_Ratio}")
    Mass_D = Mass_C * Mass_Ratio
    if Mass_D < 0.015:
        Mass_D = 0.015
    Mass_D = round(Mass_D, 3)
    print(f"Mass of Star D: {Mass_D} solar masses")
