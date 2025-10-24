# this sub-program covers step 1 ("Primary Star Mass") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

Category = None
Mass_A = None

roll_for_star_type = d100()

if 1 <= roll_for_star_type <= 3: 
    Category = "Brown Dwarf"
    roll_for_brown_dwarf_mass = d100()
    if 1 <= roll_for_brown_dwarf_mass <= 10: 
        Mass_A = 0.015
    elif 11 <= roll_for_brown_dwarf_mass <= 29:
        Mass_A = 0.02
    elif 30 <= roll_for_brown_dwarf_mass <= 45:
        Mass_A = 0.03
    elif 46 <= roll_for_brown_dwarf_mass <= 60:
        Mass_A = 0.04
    elif 61 <= roll_for_brown_dwarf_mass <= 74:
        Mass_A = 0.05
    elif 75 <= roll_for_brown_dwarf_mass <= 87:
        Mass_A = 0.06
    elif 88 <= roll_for_brown_dwarf_mass <= 100:
        Mass_A = 0.07
elif 4 <= roll_for_star_type <= 77:
    Category = "Low Mass Star"
    roll_for_low_mass_star_mass = d100()
    if 1 <= roll_for_low_mass_star_mass <= 13:
        Mass_A = 0.08
    elif 14 <= roll_for_low_mass_star_mass <= 23:
        Mass_A = 0.10
    elif 24 <= roll_for_low_mass_star_mass <= 34:
        Mass_A = 0.12
    elif 35 <= roll_for_low_mass_star_mass <= 43:
        Mass_A = 0.15
    elif 44 <= roll_for_low_mass_star_mass <= 52:
        Mass_A = 0.18
    elif 53 <= roll_for_low_mass_star_mass <= 59:
        Mass_A = 0.22
    elif 60 <= roll_for_low_mass_star_mass <= 65:
        Mass_A = 0.26
    elif 66 <= roll_for_low_mass_star_mass <= 70:
        Mass_A = 0.30
    elif 71 <= roll_for_low_mass_star_mass <= 74:
        Mass_A = 0.34
    elif 75 <= roll_for_low_mass_star_mass <= 77:
        Mass_A = 0.38
    elif 78 <= roll_for_low_mass_star_mass <= 80:
        Mass_A = 0.42
    elif 81 <= roll_for_low_mass_star_mass <= 83:
        Mass_A = 0.46
    elif 84 <= roll_for_low_mass_star_mass <= 86:
        Mass_A = 0.50
    elif 87 <= roll_for_low_mass_star_mass <= 89:
        Mass_A = 0.53
    elif 90 <= roll_for_low_mass_star_mass <= 92:
        Mass_A = 0.56
    elif 93 <= roll_for_low_mass_star_mass <= 95:
        Mass_A = 0.59
    elif 96 <= roll_for_low_mass_star_mass <= 97:
        Mass_A = 0.62
    elif 98 <= roll_for_low_mass_star_mass <= 99:
        Mass_A = 0.65
    elif 100 == roll_for_low_mass_star_mass:
        Mass_A = 0.68
elif 78 <= roll_for_star_type <=90:
    Category = "Intermediate Mass Star"
    roll_for_intermediate_mass_star_mass = d100()
    if 1 <= roll_for_intermediate_mass_star_mass <= 7:
        Mass_A = 0.70
    elif 8 <= roll_for_intermediate_mass_star_mass <= 13:
        Mass_A = 0.72
    elif 14 <= roll_for_intermediate_mass_star_mass <= 19:
        Mass_A = 0.74
    elif 20 <= roll_for_intermediate_mass_star_mass <= 24:
        Mass_A = 0.76
    elif 25 <= roll_for_intermediate_mass_star_mass <= 29:
        Mass_A = 0.78
    elif 30 <= roll_for_intermediate_mass_star_mass <= 34:
        Mass_A = 0.80
    elif 35 <= roll_for_intermediate_mass_star_mass <= 39:
        Mass_A = 0.82
    elif 40 <= roll_for_intermediate_mass_star_mass <= 43:
        Mass_A = 0.84
    elif 44 <= roll_for_intermediate_mass_star_mass <= 47:
        Mass_A = 0.86
    elif 48 <= roll_for_intermediate_mass_star_mass <= 51:
        Mass_A = 0.88
    elif 52 <= roll_for_intermediate_mass_star_mass <= 55:
        Mass_A = 0.90
    elif 56 <= roll_for_intermediate_mass_star_mass <= 59:
        Mass_A = 0.92
    elif 60 <= roll_for_intermediate_mass_star_mass <= 62:
        Mass_A = 0.94
    elif 63 <= roll_for_intermediate_mass_star_mass <= 65:
        Mass_A = 0.96
    elif 66 <= roll_for_intermediate_mass_star_mass <= 68:
        Mass_A = 0.98
    elif 69 <= roll_for_intermediate_mass_star_mass <= 71:
        Mass_A = 1.00
    elif 72 <= roll_for_intermediate_mass_star_mass <= 74:
        Mass_A = 1.02
    elif 75 <= roll_for_intermediate_mass_star_mass <= 78:
        Mass_A = 1.04
    elif 79 <= roll_for_intermediate_mass_star_mass <= 82:
        Mass_A = 1.07
    elif 83 <= roll_for_intermediate_mass_star_mass <= 85:
        Mass_A = 1.10
    elif 86 <= roll_for_intermediate_mass_star_mass <= 89:
        Mass_A = 1.13
    elif 90 <= roll_for_intermediate_mass_star_mass <= 92:
        Mass_A = 1.16
    elif 93 <= roll_for_intermediate_mass_star_mass <= 95:
        Mass_A = 1.19
    elif 96 <= roll_for_intermediate_mass_star_mass <= 97:
        Mass_A = 1.22
    elif 98 <= roll_for_intermediate_mass_star_mass <= 100:
        Mass_A = 1.25
elif 91 <= roll_for_star_type <=100:
    Category = "High Mass Star"
    roll_for_high_mass_star_mass = d100()
    if 1 <= roll_for_high_mass_star_mass <= 3:
        Mass_A = 1.28
    elif 4 <= roll_for_high_mass_star_mass <= 6:
        Mass_A = 1.31
    elif 7 <= roll_for_high_mass_star_mass <= 9:
        Mass_A = 1.34
    elif 10 <= roll_for_high_mass_star_mass <= 12:
        Mass_A = 1.37
    elif 13 <= roll_for_high_mass_star_mass <= 16:
        Mass_A = 1.40
    elif 17 <= roll_for_high_mass_star_mass <= 19:
        Mass_A = 1.44
    elif 20 <= roll_for_high_mass_star_mass <= 23:
        Mass_A = 1.48
    elif 24 <= roll_for_high_mass_star_mass <= 27:
        Mass_A = 1.53
    elif 28 <= roll_for_high_mass_star_mass <= 31:
        Mass_A = 1.58
    elif 32 <= roll_for_high_mass_star_mass <= 35:
        Mass_A = 1.64
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
        Mass_A = 2.10
    elif 57 <= roll_for_high_mass_star_mass <= 59:
        Mass_A = 2.20
    elif 60 <= roll_for_high_mass_star_mass <= 62:
        Mass_A = 2.30
    elif 63 <= roll_for_high_mass_star_mass <= 67:
        Mass_A = 2.40
    elif 68 <= roll_for_high_mass_star_mass <= 71:
        Mass_A = 2.60
    elif 72 <= roll_for_high_mass_star_mass <= 75:
        Mass = 2.80
    elif 76 <= roll_for_high_mass_star_mass <= 78:
        Mass_A = 3.00
    elif 79 <= roll_for_high_mass_star_mass <= 82:
        Mass_A = 3.20
    elif 83 <= roll_for_high_mass_star_mass <= 87:
        Mass_A = 3.50
    elif 88 <= roll_for_high_mass_star_mass <= 91:
        Mass_A = 4.00
    elif 92 <= roll_for_high_mass_star_mass <= 94:
        Mass_A = 4.50
    elif 95 <= roll_for_high_mass_star_mass <= 96:
        Mass_A = 5.00
    elif 97 <= roll_for_high_mass_star_mass <= 98:
        Mass_A = 5.50
    elif 99 <= roll_for_high_mass_star_mass <= 100:
        Mass_A = 6.00
print(f"Primary Star Type: {Category}")
Mass_A = round(Mass_A, 3)
print(f"Mass of Star A: {Mass_A} solar masses")
