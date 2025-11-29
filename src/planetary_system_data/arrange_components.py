# this sub-program covers step 3 ("Arrange Components") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

import random
from dice import d100
from primary_star_mass import primary_mass
from stellar_multiplicity import Number_of_Stars

Mass_Ratio = None
Stellar_Arrangement = None

# "This step determines how the components of a multiple star system are arranged into a hierarchy of pairs, and the initial mass of each companion star in the system. 
# Skip this step for singleton star systems"

if Number_of_Stars == 1:
    Stellar_Arrangement = "A"
    print("Single Star System - skipping step #3")
 
# "Astronomers normally tag the various stellar components in a multiple star system with capital letters in the Latin alphabet: A, B, C, and so on. So, for example, 
# the famous trinary star Alpha Centauri has three components: the bright yellow-white star Alpha Centauri A, its relatively close orange companion Alpha Centauri B, 
# and a distant red dwarf companion Alpha Centauri C (also called Proxima Centauri, since it is noticeably closer to Sol than the A-B pair)."

# "Unfortunately, astronomers are not always consistent about which component is given which alphabetic tag. This book always tags the primary star, the star with the
# highest initial mass in the system, as the A-component. The other components are tagged in order of their distance from the primary star."

# Procedure

# "The procedure for arranging stars in a system varies, depending on the multiplicity of the system."

# "Stars other than the primary are called companion stars. These stars can have any mass, from tiny brown dwarfs up to stars almost as massive as the primary, 
# although there is a clear tendency toward the latter"

# Binary Star Systems

# "There is only one possible arrangement for the two stars of a binary system. There are two components, A and B, and the primary star or A-component is in a 
# gravitationally bound pair with the B-component."

# Select the mass for the companion star. To generate its mass at random, roll d100 on the Companion Star Mass Table to determine a mass ratio for the companion."

# "In each case, you may select a mass ratio between the next lower and next higher results on the table. For example, if the result on the table indicates a mass ratio 
# of 0.60, it would be appropriate to select an actual ratio greater than 0.55 but less than 0.65. The mass ratio cannot be lower than 0.05 or higher than 1.00."

# "In a binary star system, the companion star’s mass will be equal to the mass of the primary star, multiplied by the companion’s mass ratio. Round the companion’s 
# mass to the nearest hundredth of a solar mass unit. You may wish to round the companion’s mass off further, to match one of the entries in the Stellar Mass Table 
# (see Step One). In no case will the mass of a companion star be less than 0.015 solar masses; round any such result up to that number."

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

# Trinary Star Systems

# "There are two possible configurations for the three stars (components A, B, and C) of a trinary system."

# "One possibility is that the primary star (the A-component) has no close companion, but the B and C components move some distance away as a gravitationally bound pair 
# of close companions (A and B-C)."

# "The other is that the primary star and the B-component move as a bound pair of close companions, with the C-component moving alone at a greater distance (A-B and C).

# "Both arrangements appear to be about equally common. When designing a trinary star system, select either one. To select one at random, flip a coin."

# "In a trinary star system composed of a single A-component and a close B-C pair, the mass of the B component is computed using the Companion Star Mass Table, based on 
# the mass of the primary star. The mass of the C-component is computed based on the mass of the B-component. When rolling on the Companion Star Mass Table, add 30 to 
# the roll for the C component."

# "In a trinary star system composed of an A-B close pair and a C distant companion, the mass of each of the B and C components is computed using the Companion Star Mass 
# Table, based on the mass of the primary star. When rolling on the table, add 30 to the roll for the B component"

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

# Quaternary System

# "There are many possible arrangements for the four stars (components A, B, C, and D) of a quaternary system. However, by far the most common arrangement, and the most 
# stable over long periods of time, is one in which two binary pairs (A-B and C-D) orbit one another at a wide separation."

# "In a quaternary star system, the mass of each of the B and C components is computed using the Companion Star Mass Table, based on the mass of the primary star. 
# The mass of the D-component is computed based on the mass of the C-component. When rolling on the Companion Star Mass Table, add 30 to the roll for both the 
# B component and the D component"

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