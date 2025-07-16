import random
import math

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# next step: optional conectivity to Sector_Query.py (e.g. input real parameter values from stars in Gaia DR3 dataset)

# define dice rolling functions
def d100() -> int:
  return random.randint(1, 100)
def _3d6() -> int:
  return (random.randint(1, 6) + random.randint (1, 6) + random.randint (1, 6))

# Step 1: Primary Star Mass

Category = None
Mass = None

roll_for_star_type = d100()

if 1 <= roll_for_star_type <= 3: 
    Category = "Brown Dwarf"
    roll_for_brown_dwarf_mass = d100()
    if 1 <= roll_for_brown_dwarf_mass <= 10: 
        Mass = 0.015
    elif 11 <= roll_for_brown_dwarf_mass <= 29:
        Mass = 0.02
    elif 30 <= roll_for_brown_dwarf_mass <= 45:
        Mass = 0.03
    elif 46 <= roll_for_brown_dwarf_mass <= 60:
        Mass = 0.04
    elif 61 <= roll_for_brown_dwarf_mass <= 74:
        Mass = 0.05
    elif 75 <= roll_for_brown_dwarf_mass <= 87:
        Mass = 0.06
    elif 88 <= roll_for_brown_dwarf_mass <= 100:
        Mass = 0.07
elif 4 <= roll_for_star_type <= 77:
    Category = "Low Mass Star"
    roll_for_low_mass_star_mass = d100()
    if 1 <= roll_for_low_mass_star_mass <= 13:
        Mass = 0.08
    elif 14 <= roll_for_low_mass_star_mass <= 23:
        Mass = 0.10
    elif 24 <= roll_for_low_mass_star_mass <= 34:
        Mass = 0.12
    elif 35 <= roll_for_low_mass_star_mass <= 43:
        Mass = 0.15
    elif 44 <= roll_for_low_mass_star_mass <= 52:
        Mass = 0.18
    elif 53 <= roll_for_low_mass_star_mass <= 59:
        Mass = 0.22
    elif 60 <= roll_for_low_mass_star_mass <= 65:
        Mass = 0.26
    elif 66 <= roll_for_low_mass_star_mass <= 70:
        Mass = 0.30
    elif 71 <= roll_for_low_mass_star_mass <= 74:
        Mass = 0.34
    elif 75 <= roll_for_low_mass_star_mass <= 77:
        Mass = 0.38
    elif 78 <= roll_for_low_mass_star_mass <= 80:
        Mass = 0.42
    elif 81 <= roll_for_low_mass_star_mass <= 83:
        Mass = 0.46
    elif 84 <= roll_for_low_mass_star_mass <= 86:
        Mass = 0.50
    elif 87 <= roll_for_low_mass_star_mass <= 89:
        Mass = 0.53
    elif 90 <= roll_for_low_mass_star_mass <= 92:
        Mass = 0.56
    elif 93 <= roll_for_low_mass_star_mass <= 95:
        Mass = 0.59
    elif 96 <= roll_for_low_mass_star_mass <= 97:
        Mass = 0.62
    elif 98 <= roll_for_low_mass_star_mass <= 99:
        Mass = 0.65
    elif 100 == roll_for_low_mass_star_mass:
        Mass = 0.68
elif 78 <= roll_for_star_type <=90:
    Category = "Intermediate Mass Star"
    roll_for_intermediate_mass_star_mass = d100()
    if 1 <= roll_for_intermediate_mass_star_mass <= 7:
        Mass = 0.70
    elif 8 <= roll_for_intermediate_mass_star_mass <= 13:
        Mass = 0.72
    elif 14 <= roll_for_intermediate_mass_star_mass <= 19:
        Mass = 0.74
    elif 20 <= roll_for_intermediate_mass_star_mass <= 24:
        Mass = 0.76
    elif 25 <= roll_for_intermediate_mass_star_mass <= 29:
        Mass = 0.78
    elif 30 <= roll_for_intermediate_mass_star_mass <= 34:
        Mass = 0.80
    elif 35 <= roll_for_intermediate_mass_star_mass <= 39:
        Mass = 0.82
    elif 40 <= roll_for_intermediate_mass_star_mass <= 43:
        Mass = 0.84
    elif 44 <= roll_for_intermediate_mass_star_mass <= 47:
        Mass = 0.86
    elif 48 <= roll_for_intermediate_mass_star_mass <= 51:
        Mass = 0.88
    elif 52 <= roll_for_intermediate_mass_star_mass <= 55:
        Mass = 0.90
    elif 56 <= roll_for_intermediate_mass_star_mass <= 59:
        Mass = 0.92
    elif 60 <= roll_for_intermediate_mass_star_mass <= 62:
        Mass = 0.94
    elif 63 <= roll_for_intermediate_mass_star_mass <= 65:
        Mass = 0.96
    elif 66 <= roll_for_intermediate_mass_star_mass <= 68:
        Mass = 0.98
    elif 69 <= roll_for_intermediate_mass_star_mass <= 71:
        Mass = 1.00
    elif 72 <= roll_for_intermediate_mass_star_mass <= 74:
        Mass = 1.02
    elif 75 <= roll_for_intermediate_mass_star_mass <= 78:
        Mass = 1.04
    elif 79 <= roll_for_intermediate_mass_star_mass <= 82:
        Mass = 1.07
    elif 83 <= roll_for_intermediate_mass_star_mass <= 85:
        Mass = 1.10
    elif 86 <= roll_for_intermediate_mass_star_mass <= 89:
        Mass = 1.13
    elif 90 <= roll_for_intermediate_mass_star_mass <= 92:
        Mass = 1.16
    elif 93 <= roll_for_intermediate_mass_star_mass <= 95:
        Mass = 1.19
    elif 96 <= roll_for_intermediate_mass_star_mass <= 97:
        Mass = 1.22
    elif 98 <= roll_for_intermediate_mass_star_mass <= 100:
        Mass = 1.25
elif 91 <= roll_for_star_type <=100:
    Category = "High Mass Star"
    roll_for_high_mass_star_mass = d100()
    if 1 <= roll_for_high_mass_star_mass <= 3:
        Mass = 1.28
    elif 4 <= roll_for_high_mass_star_mass <= 6:
        Mass = 1.31
    elif 7 <= roll_for_high_mass_star_mass <= 9:
        Mass = 1.34
    elif 10 <= roll_for_high_mass_star_mass <= 12:
        Mass = 1.37
    elif 13 <= roll_for_high_mass_star_mass <= 16:
        Mass = 1.40
    elif 17 <= roll_for_high_mass_star_mass <= 19:
        Mass = 1.44
    elif 20 <= roll_for_high_mass_star_mass <= 23:
        Mass = 1.48
    elif 24 <= roll_for_high_mass_star_mass <= 27:
        Mass = 1.53
    elif 28 <= roll_for_high_mass_star_mass <= 31:
        Mass = 1.58
    elif 32 <= roll_for_high_mass_star_mass <= 35:
        Mass = 1.64
    elif 36 <= roll_for_high_mass_star_mass <= 38:
        Mass = 1.70
    elif 39 <= roll_for_high_mass_star_mass <= 41:
        Mass = 1.76
    elif 42 <= roll_for_high_mass_star_mass <= 45:
        Mass = 1.82
    elif 46 <= roll_for_high_mass_star_mass <= 49:
        Mass = 1.90
    elif 50 <= roll_for_high_mass_star_mass <= 53:
        Mass = 2.00
    elif 54 <= roll_for_high_mass_star_mass <= 56:
        Mass = 2.10
    elif 57 <= roll_for_high_mass_star_mass <= 59:
        Mass = 2.20
    elif 60 <= roll_for_high_mass_star_mass <= 62:
        Mass = 2.30
    elif 63 <= roll_for_high_mass_star_mass <= 67:
        Mass = 2.40
    elif 68 <= roll_for_high_mass_star_mass <= 71:
        Mass = 2.60
    elif 72 <= roll_for_high_mass_star_mass <= 75:
        Mass = 2.80
    elif 76 <= roll_for_high_mass_star_mass <= 78:
        Mass = 3.00
    elif 79 <= roll_for_high_mass_star_mass <= 82:
        Mass = 3.20
    elif 83 <= roll_for_high_mass_star_mass <= 87:
        Mass = 3.50
    elif 88 <= roll_for_high_mass_star_mass <= 91:
        Mass = 4.00
    elif 92 <= roll_for_high_mass_star_mass <= 94:
        Mass = 4.50
    elif 95 <= roll_for_high_mass_star_mass <= 96:
        Mass = 5.00
    elif 97 <= roll_for_high_mass_star_mass <= 98:
        Mass = 5.50
    elif 99 <= roll_for_high_mass_star_mass <= 100:
        Mass = 6.00
print(f"Star Type: {Category}")
print(f"Mass of Star A: {Mass} solar masses")

# Step 2: Stellar Multiplicity

Number_of_Stars = 0
first_roll_for_number_of_stars = _3d6()
second_roll_for_number_of_stars = d100()

if Mass < 0.08:
    if 1 <= first_roll_for_number_of_stars <= 13:
        Number_of_Stars = 1
    elif 14 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 0.08 <= Mass < 0.70:
    if 1 <= first_roll_for_number_of_stars <= 12:
        Number_of_Stars = 1
    elif 13 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 0.7 <= Mass < 1.00:
    if 1 <= first_roll_for_number_of_stars <= 11:
        Number_of_Stars = 1
    elif 12 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 1.00 <= Mass < 1.30:
    if 1 <= first_roll_for_number_of_stars <= 10:
        Number_of_Stars = 1
    elif 11 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4
elif 1.30 <= Mass: 
    if 1 <= first_roll_for_number_of_stars <= 9:
        Number_of_Stars = 1
    elif 10 <= first_roll_for_number_of_stars <= 18:
        if 1 <= second_roll_for_number_of_stars <= 75:
            Number_of_Stars = 2
        elif 76 <= second_roll_for_number_of_stars <= 95:
            Number_of_Stars = 3
        elif 96 <= second_roll_for_number_of_stars <= 100:
            Number_of_Stars = 4

print(f"Number of Stars in System: {Number_of_Stars}")

# Step 3: Arrange Components

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
    Mass_B = Mass * Mass_Ratio
    if Mass_B < 0.015:
        Mass_B = 0.015
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
        Mass_B = Mass * Mass_Ratio
        if Mass_B < 0.015:
            Mass_B = 0.015
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
        Mass_B = Mass * Mass_Ratio
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
        Mass_C = Mass * Mass_Ratio
        if Mass_C < 0.015:
            Mass_C = 0.015
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
    Mass_B = Mass * Mass_Ratio
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
    elif roll_for_AB_mass_ratio >= 88:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star A and Star C: {Mass_Ratio}")
    Mass_C = Mass * Mass_Ratio
    if Mass_C < 0.015:
        Mass_C = 0.015
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
    elif 87 <= roll_for_AB_mass_ratio <= 130:
        Mass_Ratio = 0.95
    print(f"Mass Ratio Between Star C and Star D: {Mass_Ratio}")
    Mass_D = Mass_C * Mass_Ratio
    if Mass_D < 0.015:
        Mass_D = 0.015
    print(f"Mass of Star D: {Mass_D} solar masses")

# Step 4: Star System Age

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
star_age = Base_Age + (Age_Range*(roll_for_age_range/100))

print(f"Stellar Population: {Population}")
print(f"Star Age: {star_age} Gyr")

# Step 5: Star System Metallicity

# currently only randomly generated metallicity - will need to tweak to use Gaia estimate or values from SIMBAD (if available)
Metallicity = None
roll_for_metallicity = _3d6()
Metallicity = (roll_for_metallicity / 10)*(1.2-(star_age/13.5))

if Population == "Halo Population II":
    Metallicity = (Metallicity - 0.2)

if Metallicity < 0:
    Metallicity = 0

Metallicity = round(Metallicity, 2)
print(f"Metallicity: {Metallicity}")

# Step 6: Stellar Evolution

Temperature_Effective = None
Luminosity = None
Radius = None

if Mass < 0.08:
    Temperature_Effective = 18600 * ((Mass ** 0.8) / (star_age ** 0.3))
    Luminosity = (Temperature_Effective ** 4) / (1.1e+17)

elif 0.08 <= Mass <= 0.5:
    # need to come back and redo as linear interpolation
    if 0.08 <= Mass <= 0.09:
        Temperature_Effective = 2500
        Luminosity = 0.00047
    elif 0.09 < Mass <= 0.11:
        Temperature_Effective = 2710
        Luminosity = 0.00087
    elif 0.11 < Mass <= 0.135:
        Temperature_Effective = 2930
        Luminosity = 0.0016
    elif 0.135 < Mass <= 0.2:
        Temperature_Effective = 3090
        Luminosity = 0.0029
    elif 0.2 < Mass <= 0.24:
        Temperature_Effective = 3370
        Luminosity = 0.007
    elif 0.24 < Mass <= 0.28:
        Temperature_Effective = 3480
        Luminosity = 0.01
    elif 0.28 < Mass <= 0.32:
        Temperature_Effective = 3550
        Luminosity = 0.013
    elif 0.32 < Mass <= 0.36:
        Temperature_Effective = 3600
        Luminosity = 0.017
    elif 0.36 < Mass <= 0.4:
        Temperature_Effective = 3640
        Luminosity = 0.02
    elif 0.4 < Mass <= 0.44:
        Temperature_Effective = 3680
        Luminosity = 0.025
    elif 0.44 < Mass <= 0.48:
        Temperature_Effective = 3730
        Luminosity = 0.031
    elif 0.48 < Mass <= 0.5:
        Temperature_Effective = 3780
        Luminosity = 0.039

elif 0.5 < Mass:
    Initial_Effective_Temperature = None
    Final_Effective_Temperature = None
    Initial_Luminosity = None
    Luminosity_Growth_Rate = None
    Main_Sequence_Lifespan = None

    if 0.5 < Mass <= 0.515:
        Initial_Effective_Temperature = 3780
        Final_Effective_Temperature = 4330
        Initial_Luminosity = 0.039
        Luminosity_Growth_Rate = 1.01
        Main_Sequence_Lifespan = 131
    elif 0.515 < Mass <= N.NN:
        Initial_Effective_Temperature = 
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = NNN
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.436
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.362
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.305
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.241
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.171
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.127
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.0987
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.0789
    elif N.NN < Mass <= N.NN:
        Initial_Effective_Temperature = NNN
        Final_Effective_Temperature = NNN
        Initial_Luminosity = NNN
        Luminosity_Growth_Rate = NNN
        Main_Sequence_Lifespan = 0.0647

if 0.08 <= Mass:
    Radius = 155000 * ((sqrt(Luminosity))/(Temperature_Effective * Temperature_Effective))

print(f"Effective Temperature of Star A: {Temperature_Effective} Kelvin")
print(f"Luminosity of Star A: {Luminosity} solar luminosities")
print(f"Radius of Star A: {Radius} AU")

# Step 7: Stellar Classification
    # input Step 7 elements

# Step 8: Stellar Orbital Parameters
    # input Step 8 elements

# Step 9: Protoplanetary Disk
    # input Step 9 elements

# Step 10: Disk Instability
    # input Step 10 elements

# Step 11: Core Accretion
    # input Step 11 elements

# Step 12: Oligarchic Collision
    # input Step 12 elements

# Step 13: Planetary Orbital Radii
    # input Step 13 elements

# Step 14: Planetary Mass
    # input Step 14 elements

# Step 15: Orbital Eccentricity
    # input Step 15 elements

# Step 16: Physical Parameters
    # input Step 16 elements

# Step 17: Natural Satellites
    # input Step 17 elements

# Step 18: Orbital Period
    # input Step 18 elements

# Step 19: Rotation Period
    # input Step 19 elements

# Step 20: Obliquity
# input Step 20 elements

# Step 21: Local Calendar
    # input Step 21 elements

# Step 22: Blackbody Temperature
    # input Step 22 elements

# Step 23: Water
    # input Step 23 elements

# Step 24: Geophysics
    # input Step 24 elements

# Step 25: Magnetic Field
    # input Step 25 elements

# Step 26: Early Atmosphere
    # input Step 26 elements

# Step 27: Albedo
    # input Step 27 elements

# Step 28: Carbon Dioxide
    # input Step 28 elements

# Step 29: Presence of Life
    # input Step 29 elements

# Step 30: Average Surface Temperature
    # input Step 30 elements

# Step 31: Finalize Atmosphere
    # input Step 31 elements