

import math
import random

from planetary_system_data.dice import _3d6, _2d6, d100, percentile_roll
from planetary_system_data.dataclasses_and_enumerations import StarCategory, StellarEvolutionStage, Star, StarSystem, StellarArrangement, StellarPopulation
from planetary_system_data.primary_star import generate_primary_star

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# input user query - option to input real parameter values from stars in Gaia DR3 dataset - e.g. connect with Sectory_Query.py


def star_category_from_mass(mass: float) -> StarCategory:
    if mass < 0.08:
        return StarCategory.BROWN_DWARF
    elif 0.08 <= mass < 0.70:
        return StarCategory.LOW_MASS_STAR
    elif 0.70 <= mass < 1.28:
        return StarCategory.INTERMEDIATE_MASS_STAR
    else:  # mass >= 1.28
        return StarCategory.HIGH_MASS_STAR


# Step 1: Primary Star Mass
Star_A = generate_primary_star()    
Category = Star_A.category
Mass_A = Star_A.mass
    
print(f"Primary Star Type: {Category}")
Mass_A = round(Mass_A, 3)
print(f"Mass of Star A: {Mass_A} solar masses")


# Step 2: Stellar Multiplicity

def generate_number_of_stars(primary_mass: float) -> int:
    """Determine the number of stars in the system based on the mass of the primary star and two rolls."""

    first_roll_for_number_of_stars = _3d6()
    if first_roll_for_number_of_stars < 9:
        return 1
    
    second_roll_for_number_of_stars = d100()
    multiple_stars = 2
    if 76 <= second_roll_for_number_of_stars <= 95:
        multiple_stars = 3
    elif 96 <= second_roll_for_number_of_stars <= 100:
        multiple_stars = 4

    if primary_mass < 0.08:
        return 1 if first_roll_for_number_of_stars <= 13 else multiple_stars
    elif primary_mass < 0.70:
        return 1 if first_roll_for_number_of_stars <= 12 else multiple_stars
    elif primary_mass < 1.00:
        return 1 if first_roll_for_number_of_stars <= 11 else multiple_stars
    elif primary_mass < 1.30:
        return 1 if first_roll_for_number_of_stars <= 10 else multiple_stars
    else: 
        return 1 if first_roll_for_number_of_stars <= 9 else multiple_stars

Number_of_Stars = generate_number_of_stars(Mass_A)
print(f"Number of Stars in System: {Number_of_Stars}")
assert 1 <= Number_of_Stars <= 4

# Step 3: Arrange Components

Mass_Ratio = None
Stellar_Arrangement = None


def binary_system_mass_ratio() -> float:
    roll_for_binary_mass_ratio = d100()
    if roll_for_binary_mass_ratio <= 4:
        return 0.05
    elif 5 <= roll_for_binary_mass_ratio <= 8:
        return 0.10
    elif 9 <= roll_for_binary_mass_ratio <= 12:
        return 0.15
    elif 13 <= roll_for_binary_mass_ratio <= 16:
        return 0.20
    elif 17 <= roll_for_binary_mass_ratio <= 20:
        return 0.25
    elif 21 <= roll_for_binary_mass_ratio <= 24:
        return 0.30
    elif 25 <= roll_for_binary_mass_ratio <= 28:
        return 0.35
    elif 29 <= roll_for_binary_mass_ratio <= 31:
        return 0.40
    elif 32 <= roll_for_binary_mass_ratio <= 34:
        return 0.45
    elif 35 <= roll_for_binary_mass_ratio <= 38:
        return 0.50
    elif 39 <= roll_for_binary_mass_ratio <= 43:
        return 0.55
    elif 44 <= roll_for_binary_mass_ratio <= 48:
        return 0.60
    elif 49 <= roll_for_binary_mass_ratio <= 53:
        return 0.65
    elif 54 <= roll_for_binary_mass_ratio <= 58:
        return 0.70
    elif 59 <= roll_for_binary_mass_ratio <= 63:
        return 0.75
    elif 64 <= roll_for_binary_mass_ratio <= 69:
        return 0.80
    elif 70 <= roll_for_binary_mass_ratio <= 76:
        return 0.85
    elif 77 <= roll_for_binary_mass_ratio <= 86:
        return 0.90
    else: #87-100
        return 0.95

def ternary_system_mass_ratio() -> float:
    roll_for_mass_ratio = (d100() + 30)
    if roll_for_mass_ratio == 31:
        return 0.40
    elif 32 <= roll_for_mass_ratio <= 34:
        return 0.45
    elif 35 <= roll_for_mass_ratio <= 38:
        return 0.50
    elif 39 <= roll_for_mass_ratio <= 43:
        return 0.55
    elif 44 <= roll_for_mass_ratio <= 48:
        return 0.60
    elif 49 <= roll_for_mass_ratio <= 53:
        return 0.65
    elif 54 <= roll_for_mass_ratio <= 58:
        return 0.70
    elif 59 <= roll_for_mass_ratio <= 63:
        return 0.75
    elif 64 <= roll_for_mass_ratio <= 69:
        return 0.80
    elif 70 <= roll_for_mass_ratio <= 76:
        return 0.85
    elif 77 <= roll_for_mass_ratio <= 86:
        return 0.90
    else: #87-130
        return 0.95


def star_mass_from_ratio(primary_mass: float, mass_ratio: float) -> float:
    secondary_mass = primary_mass * mass_ratio
    return max(0.015, round(secondary_mass, 3))


if Number_of_Stars == 1:
    Stellar_Arrangement = StellarArrangement.SINGLE
    Star_System = StarSystem(stars=[Star_A], stellar_arrangement=StellarArrangement.SINGLE)
    print("Single Star System - skipping step #3")

elif Number_of_Stars == 2:
    mass_ratio = binary_system_mass_ratio()

    print(f"Mass Ratio Between Star A and Star B: {mass_ratio}")
    Mass_B = star_mass_from_ratio(Mass_A, mass_ratio)
    print(f"Mass of Star B: {Mass_B} solar masses")
    Stellar_Arrangement = StellarArrangement.BINARY
    Star_B = Star(mass=Mass_B, category=star_category_from_mass(Mass_B))
    Star_System = StarSystem(stars=[Star_A, Star_B], stellar_arrangement=StellarArrangement.BINARY)

elif Number_of_Stars == 3:
    random_integer = random.randint(1, 2)
    if random_integer == 1:
        Stellar_Arrangement = StellarArrangement.TRINARY_DISTANT_PAIR
        print("Triple Star System - A star with distant BC pair")

        a_b_mass_ratio = binary_system_mass_ratio()        
        print(f"Mass Ratio Between Star A and Star B: {a_b_mass_ratio}")
        Mass_B = star_mass_from_ratio(Mass_A, a_b_mass_ratio)
        print(f"Mass of Star B: {Mass_B} solar masses")
        Star_B = Star(mass=Mass_B, category=star_category_from_mass(Mass_B))

        b_c_mass_ratio = ternary_system_mass_ratio()
        print(f"Mass Ratio Between Star B and Star C: {b_c_mass_ratio}")
        Mass_C = star_mass_from_ratio(Mass_B, b_c_mass_ratio)
        print(f"Mass of Star C: {Mass_C} solar masses")
        Star_C = Star(mass=Mass_C, category=star_category_from_mass(Mass_C))
        Star_System = StarSystem(
            stars=[Star_A, Star_B, Star_C], 
            stellar_arrangement=StellarArrangement.TRINARY_DISTANT_PAIR
        )

    else:
        Stellar_Arrangement = StellarArrangement.TRINARY_CLOSE_PAIR
        print("Triple Star System - AB as close companions with C as distant companion")
        a_b_mass_ratio = ternary_system_mass_ratio()
        print(f"Mass Ratio Between Star A and Star B: {a_b_mass_ratio}")
        Mass_B = star_mass_from_ratio(Mass_A, a_b_mass_ratio)
        print(f"Mass of Star B: {Mass_B} solar masses")
        Star_B = Star(mass=Mass_B, category=star_category_from_mass(Mass_B))

        a_c_mass_ratio = binary_system_mass_ratio()
        print(f"Mass Ratio Between Star A and Star C: {a_c_mass_ratio}")
        Mass_C = star_mass_from_ratio(Mass_A, a_c_mass_ratio)
        print(f"Mass of Star C: {Mass_C} solar masses")
        Star_C = Star(mass=Mass_C, category=star_category_from_mass(Mass_C))
        Star_System = StarSystem(
            stars=[Star_A, Star_B, Star_C],
            stellar_arrangement=StellarArrangement.TRINARY_CLOSE_PAIR
        )

elif Number_of_Stars == 4:
    Stellar_Arrangement = "AB-CD"
    print("Quadruple Star System - two binary sytems AB and CD with wide separation")

    a_b_mass_ratio = binary_system_mass_ratio()
    print(f"Mass Ratio Between Star A and Star B: {a_b_mass_ratio}")
    Mass_B = star_mass_from_ratio(Mass_A, a_b_mass_ratio)
    print(f"Mass of Star B: {Mass_B} solar masses")
    Star_B = Star(mass=Mass_B, category=star_category_from_mass(Mass_B))

    a_c_mass_ratio = binary_system_mass_ratio()
    print(f"Mass Ratio Between Star A and Star C: {a_c_mass_ratio}")
    Mass_C = star_mass_from_ratio(Mass_A, a_c_mass_ratio)
    print(f"Mass of Star C: {Mass_C} solar masses")
    Star_C = Star(mass=Mass_C, category=star_category_from_mass(Mass_C))

    c_d_mass_ratio = ternary_system_mass_ratio()    
    print(f"Mass Ratio Between Star C and Star D: {c_d_mass_ratio}")
    Mass_D = star_mass_from_ratio(Mass_C, c_d_mass_ratio)
    print(f"Mass of Star D: {Mass_D} solar masses")
    Star_D = Star(mass=Mass_D, category=star_category_from_mass(Mass_D))
    Star_System = StarSystem(
        stars=[Star_A, Star_B, Star_C, Star_D],
        stellar_arrangement=StellarArrangement.QUATERNARY
    )

# Step 4: Star System Age
Population = None


def generate_stellar_population() -> tuple[str, float]:    
    roll_for_stellar_population = d100()
    if 1 <= roll_for_stellar_population <= 42: 
        population = StellarPopulation.YOUNG_POPULATION_I
        base_age = 0.0
        age_range = 2.0
    elif 43 <= roll_for_stellar_population <= 76: 
        population = StellarPopulation.INTERMEDIATE_POPULATION
        base_age = 2.0
        age_range = 1.0
    elif 77 <= roll_for_stellar_population <= 95: 
        population = StellarPopulation.OLD_POPULATION_I
        base_age = 5.0
        age_range= 3.0
    elif 96 <= roll_for_stellar_population <= 99: 
        population = StellarPopulation.DISK_POPULATION_II
        base_age = 8.0
        age_range = 1.5
    else:  # 100 
        population = StellarPopulation.HALO_POPULATION_II
        base_age = 9.5
        age_range = 3.0

    roll_for_age_range = d100()
    system_age = round(base_age + (age_range * (roll_for_age_range / 100)), 2)

    print(f"Stellar Population: {population}")
    print(f"System Age: {system_age} Gyr")
    return population, system_age

Population, system_age = generate_stellar_population()
Star_System.system_age = system_age


# Step 5: Star System Metallicity

# currently only randomly generated metallicity - will need to tweak to use Gaia estimate or values from SIMBAD (if available)
def generate_metallicity(population, system_age) -> float:
    roll_for_metallicity = _3d6()
    system_age_factor = (1.2 - (system_age / 13.5))
    metallicity = (roll_for_metallicity * system_age_factor) / 10.0
    if population is StellarPopulation.HALO_POPULATION_II:
        metallicity -= 0.2
    return max(0, round(metallicity, 2))


Metallicity = generate_metallicity(Population, system_age)
print(f"Metallicity: {Metallicity}")
Star_System.metallicity = Metallicity



# Step 6: Stellar Evolution
from planetary_system_data.steller_evolution import evolve_star




# Step 7: Stellar Classification

Spectral_Type_of_Star_A = "None"
if Number_of_Stars >= 1:
    if Evolutionary_Stage_of_Star_A == "White Dwarf":
        Spectral_Type_of_Star_A = "D"
    if Evolutionary_Stage_of_Star_A != "White Dwarf":
        if Temperature_Effective_of_Star_A >= 16500:
            Spectral_Type_of_Star_A = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_A < 16500:
            Spectral_Type_of_Star_A = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_A < 15500:
            Spectral_Type_of_Star_A = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_A < 14500:
            Spectral_Type_of_Star_A = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_A < ((13000+14000)/2):
            Spectral_Type_of_Star_A = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_A < ((11900+13000)/2):
            Spectral_Type_of_Star_A = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_A < ((10800+11900)/2):
            Spectral_Type_of_Star_A = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_A < ((9700+10800)/2):
            Spectral_Type_of_Star_A = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_A < ((9450+9700)/2):
            Spectral_Type_of_Star_A = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_A < ((9200+9450)/2):
            Spectral_Type_of_Star_A = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_A < ((8950+9200)/2):
            Spectral_Type_of_Star_A = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_A < ((8700+8950)/2):
            Spectral_Type_of_Star_A = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_A < ((8450+8700)/2):
            Spectral_Type_of_Star_A = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_A < ((8200+8450)/2):
            Spectral_Type_of_Star_A = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_A < ((7950+8200)/2):
            Spectral_Type_of_Star_A = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_A < ((7700+7950)/2):
            Spectral_Type_of_Star_A = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_A < ((7460+7700)/2):
            Spectral_Type_of_Star_A = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_A < ((7720+7460)/2):
            Spectral_Type_of_Star_A = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_A < ((7090+7220)/2):
            Spectral_Type_of_Star_A = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_A < ((6890+7090)/2):
            Spectral_Type_of_Star_A = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_A < ((6760+6890)/2):
            Spectral_Type_of_Star_A = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_A < ((6630+6760)/2):
            Spectral_Type_of_Star_A = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_A < ((6500+6630)/2):
            Spectral_Type_of_Star_A = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_A < ((6370+6500)/2):
            Spectral_Type_of_Star_A = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_A < ((6240+6370)/2):
            Spectral_Type_of_Star_A = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_A < ((6110+6240)/2):
            Spectral_Type_of_Star_A = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_A < ((6020+6110)/2):
            Spectral_Type_of_Star_A = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_A < ((5930+6020)/2):
            Spectral_Type_of_Star_A = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_A < ((5850+5930)/2):
            Spectral_Type_of_Star_A = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_A < ((5770+5850)/2):
            Spectral_Type_of_Star_A = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_A < ((5700+5770)/2):
            Spectral_Type_of_Star_A = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_A < ((5630+5700)/2):
            Spectral_Type_of_Star_A = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_A < ((5570+5630)/2):
            Spectral_Type_of_Star_A = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_A < ((5510+5570)/2):
            Spectral_Type_of_Star_A = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_A < ((5450+5510)/2):
            Spectral_Type_of_Star_A = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_A < ((5390+5450)/2):
            Spectral_Type_of_Star_A = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_A < ((5330+5390)/2):
            Spectral_Type_of_Star_A = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_A < ((5270+5330)/2):
            Spectral_Type_of_Star_A = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_A < ((5130+5270)/2):
            Spectral_Type_of_Star_A = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_A < ((4990+5130)/2):
            Spectral_Type_of_Star_A = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_A < ((4850+4990)/2):
            Spectral_Type_of_Star_A = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_A < ((4710+4850)/2):
            Spectral_Type_of_Star_A = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_A < ((4560+4710)/2):
            Spectral_Type_of_Star_A = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_A < ((4410+4560)/2):
            Spectral_Type_of_Star_A = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_A < ((4270+4410)/2):
            Spectral_Type_of_Star_A = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_A < ((4130+4270)/2):
            Spectral_Type_of_Star_A = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_A < ((3990+4130)/2):
            Spectral_Type_of_Star_A = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_A < ((3850+3990)/2):
            Spectral_Type_of_Star_A = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_A < ((3700+3850)/2):
            Spectral_Type_of_Star_A = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_A < ((3540+3700)/2):
            Spectral_Type_of_Star_A = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_A < ((3380+3540)/2):
            Spectral_Type_of_Star_A = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_A < ((3220+3380)/2):
            Spectral_Type_of_Star_A = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_A < ((3060+3220)/2):
            Spectral_Type_of_Star_A = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_A < ((2900+3060)/2):
            Spectral_Type_of_Star_A = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_A < ((2740+2900)/2):
            Spectral_Type_of_Star_A = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_A < ((2580+2740)/2):
            Spectral_Type_of_Star_A = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_A < ((2420+2580)/2):
            Spectral_Type_of_Star_A = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_A < ((2270+2420)/2):
            Spectral_Type_of_Star_A = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_A < ((2170+2270)/2):
            Spectral_Type_of_Star_A = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_A < ((2070+2170)/2):
            Spectral_Type_of_Star_A = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_A < ((1970+2070)/2):
            Spectral_Type_of_Star_A = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_A < ((1870+1970)/2):
            Spectral_Type_of_Star_A = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_A < ((1770+1870)/2):
            Spectral_Type_of_Star_A = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_A < ((1660+1770)/2):
            Spectral_Type_of_Star_A = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_A < ((1560+1660)/2):
            Spectral_Type_of_Star_A = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_A < ((1460+1560)/2):
            Spectral_Type_of_Star_A = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_A < ((1360+1460)/2):
            Spectral_Type_of_Star_A = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_A < ((1260+1360)/2):
            Spectral_Type_of_Star_A = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_A < ((1190+1260)/2):
            Spectral_Type_of_Star_A = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_A < ((1120+1190)/2):
            Spectral_Type_of_Star_A = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_A < ((1040+1120)/2):
            Spectral_Type_of_Star_A = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_A < ((960+1040)/2):
            Spectral_Type_of_Star_A = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_A < ((880+960)/2):
            Spectral_Type_of_Star_A = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_A < ((800+880)/2):
            Spectral_Type_of_Star_A = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_A < ((720+800)/2):
            Spectral_Type_of_Star_A = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_A < ((640+720)/2):
            Spectral_Type_of_Star_A = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_A < ((570+640)/2):
            Spectral_Type_of_Star_A = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_A < ((500+570)/2):
            Spectral_Type_of_Star_A = "Y0"
    print(f"Spectral Type of Star A: {Spectral_Type_of_Star_A}")

Spectral_Type_of_Star_B = "None"
if Number_of_Stars >= 2:
    Spectral_Type_of_Star_B = "None"
    if Evolutionary_Stage_of_Star_B == "White Dwarf":
        Spectral_Type_of_Star_B = "D"
    if Evolutionary_Stage_of_Star_B != "White Dwarf":
        if Temperature_Effective_of_Star_B >= 16500:
            Spectral_Type_of_Star_B = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_B < 16500:
            Spectral_Type_of_Star_B = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_B < 15500:
            Spectral_Type_of_Star_B = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_B < 14500:
            Spectral_Type_of_Star_B = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_B < ((13000+14000)/2):
            Spectral_Type_of_Star_B = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_B < ((11900+13000)/2):
            Spectral_Type_of_Star_B = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_B < ((10800+11900)/2):
            Spectral_Type_of_Star_B = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_B < ((9700+10800)/2):
            Spectral_Type_of_Star_B = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_B < ((9450+9700)/2):
            Spectral_Type_of_Star_B = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_B < ((9200+9450)/2):
            Spectral_Type_of_Star_B = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_B < ((8950+9200)/2):
            Spectral_Type_of_Star_B = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_B < ((8700+8950)/2):
            Spectral_Type_of_Star_B = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_B < ((8450+8700)/2):
            Spectral_Type_of_Star_B = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_B < ((8200+8450)/2):
            Spectral_Type_of_Star_B = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_B < ((7950+8200)/2):
            Spectral_Type_of_Star_B = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_B < ((7700+7950)/2):
            Spectral_Type_of_Star_B = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_B < ((7460+7700)/2):
            Spectral_Type_of_Star_B = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_B < ((7720+7460)/2):
            Spectral_Type_of_Star_B = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_B < ((7090+7220)/2):
            Spectral_Type_of_Star_B = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_B < ((6890+7090)/2):
            Spectral_Type_of_Star_B = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_B < ((6760+6890)/2):
            Spectral_Type_of_Star_B = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_B < ((6630+6760)/2):
            Spectral_Type_of_Star_B = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_B < ((6500+6630)/2):
            Spectral_Type_of_Star_B = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_B < ((6370+6500)/2):
            Spectral_Type_of_Star_B = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_B < ((6240+6370)/2):
            Spectral_Type_of_Star_B = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_B < ((6110+6240)/2):
            Spectral_Type_of_Star_B = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_B < ((6020+6110)/2):
            Spectral_Type_of_Star_B = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_B < ((5930+6020)/2):
            Spectral_Type_of_Star_B = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_B < ((5850+5930)/2):
            Spectral_Type_of_Star_B = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_B < ((5770+5850)/2):
            Spectral_Type_of_Star_B = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_B < ((5700+5770)/2):
            Spectral_Type_of_Star_B = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_B < ((5630+5700)/2):
            Spectral_Type_of_Star_B = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_B < ((5570+5630)/2):
            Spectral_Type_of_Star_B = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_B < ((5510+5570)/2):
            Spectral_Type_of_Star_B = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_B < ((5450+5510)/2):
            Spectral_Type_of_Star_B = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_B < ((5390+5450)/2):
            Spectral_Type_of_Star_B = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_B < ((5330+5390)/2):
            Spectral_Type_of_Star_B = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_B < ((5270+5330)/2):
            Spectral_Type_of_Star_B = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_B < ((5130+5270)/2):
            Spectral_Type_of_Star_B = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_B < ((4990+5130)/2):
            Spectral_Type_of_Star_B = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_B < ((4850+4990)/2):
            Spectral_Type_of_Star_B = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_B < ((4710+4850)/2):
            Spectral_Type_of_Star_B = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_B < ((4560+4710)/2):
            Spectral_Type_of_Star_B = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_B < ((4410+4560)/2):
            Spectral_Type_of_Star_B = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_B < ((4270+4410)/2):
            Spectral_Type_of_Star_B = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_B < ((4130+4270)/2):
            Spectral_Type_of_Star_B = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_B < ((3990+4130)/2):
            Spectral_Type_of_Star_B = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_B < ((3850+3990)/2):
            Spectral_Type_of_Star_B = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_B < ((3700+3850)/2):
            Spectral_Type_of_Star_B = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_B < ((3540+3700)/2):
            Spectral_Type_of_Star_B = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_B < ((3380+3540)/2):
            Spectral_Type_of_Star_B = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_B < ((3220+3380)/2):
            Spectral_Type_of_Star_B = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_B < ((3060+3220)/2):
            Spectral_Type_of_Star_B = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_B < ((2900+3060)/2):
            Spectral_Type_of_Star_B = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_B < ((2740+2900)/2):
            Spectral_Type_of_Star_B = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_B < ((2580+2740)/2):
            Spectral_Type_of_Star_B = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_B < ((2420+2580)/2):
            Spectral_Type_of_Star_B = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_B < ((2270+2420)/2):
            Spectral_Type_of_Star_B = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_B < ((2170+2270)/2):
            Spectral_Type_of_Star_B = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_B < ((2070+2170)/2):
            Spectral_Type_of_Star_B = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_B < ((1970+2070)/2):
            Spectral_Type_of_Star_B = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_B < ((1870+1970)/2):
            Spectral_Type_of_Star_B = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_B < ((1770+1870)/2):
            Spectral_Type_of_Star_B = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_B < ((1660+1770)/2):
            Spectral_Type_of_Star_B = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_B < ((1560+1660)/2):
            Spectral_Type_of_Star_B = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_B < ((1460+1560)/2):
            Spectral_Type_of_Star_B = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_B < ((1360+1460)/2):
            Spectral_Type_of_Star_B = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_B < ((1260+1360)/2):
            Spectral_Type_of_Star_B = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_B < ((1190+1260)/2):
            Spectral_Type_of_Star_B = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_B < ((1120+1190)/2):
            Spectral_Type_of_Star_B = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_B < ((1040+1120)/2):
            Spectral_Type_of_Star_B = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_B < ((960+1040)/2):
            Spectral_Type_of_Star_B = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_B < ((880+960)/2):
            Spectral_Type_of_Star_B = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_B < ((800+880)/2):
            Spectral_Type_of_Star_B = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_B < ((720+800)/2):
            Spectral_Type_of_Star_B = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_B < ((640+720)/2):
            Spectral_Type_of_Star_B = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_B < ((570+640)/2):
            Spectral_Type_of_Star_B = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_B < ((500+570)/2):
            Spectral_Type_of_Star_B = "Y0"
    print(f"Spectral Type of Star B: {Spectral_Type_of_Star_B}")

Spectral_Type_of_Star_C = "None"
if Number_of_Stars >= 3:
    if Evolutionary_Stage_of_Star_C == "White Dwarf":
        Spectral_Type_of_Star_C = "D"
    if Evolutionary_Stage_of_Star_C != "White Dwarf":
        if Temperature_Effective_of_Star_C >= 16500:
            Spectral_Type_of_Star_C = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_C < 16500:
            Spectral_Type_of_Star_C = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_C < 15500:
            Spectral_Type_of_Star_C = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_C < 14500:
            Spectral_Type_of_Star_C = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_C < ((13000+14000)/2):
            Spectral_Type_of_Star_C = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_C < ((11900+13000)/2):
            Spectral_Type_of_Star_C = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_C < ((10800+11900)/2):
            Spectral_Type_of_Star_C = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_C < ((9700+10800)/2):
            Spectral_Type_of_Star_C = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_C < ((9450+9700)/2):
            Spectral_Type_of_Star_C = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_C < ((9200+9450)/2):
            Spectral_Type_of_Star_C = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_C < ((8950+9200)/2):
            Spectral_Type_of_Star_C = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_C < ((8700+8950)/2):
            Spectral_Type_of_Star_C = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_C < ((8450+8700)/2):
            Spectral_Type_of_Star_C = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_C < ((8200+8450)/2):
            Spectral_Type_of_Star_C = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_C < ((7950+8200)/2):
            Spectral_Type_of_Star_C = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_C < ((7700+7950)/2):
            Spectral_Type_of_Star_C = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_C < ((7460+7700)/2):
            Spectral_Type_of_Star_C = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_C < ((7720+7460)/2):
            Spectral_Type_of_Star_C = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_C < ((7090+7220)/2):
            Spectral_Type_of_Star_C = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_C < ((6890+7090)/2):
            Spectral_Type_of_Star_C = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_C < ((6760+6890)/2):
            Spectral_Type_of_Star_C = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_C < ((6630+6760)/2):
            Spectral_Type_of_Star_C = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_C < ((6500+6630)/2):
            Spectral_Type_of_Star_C = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_C < ((6370+6500)/2):
            Spectral_Type_of_Star_C = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_C < ((6240+6370)/2):
            Spectral_Type_of_Star_C = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_C < ((6110+6240)/2):
            Spectral_Type_of_Star_C = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_C < ((6020+6110)/2):
            Spectral_Type_of_Star_C = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_C < ((5930+6020)/2):
            Spectral_Type_of_Star_C = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_C < ((5850+5930)/2):
            Spectral_Type_of_Star_C = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_C < ((5770+5850)/2):
            Spectral_Type_of_Star_C = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_C < ((5700+5770)/2):
            Spectral_Type_of_Star_C = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_C < ((5630+5700)/2):
            Spectral_Type_of_Star_C = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_C < ((5570+5630)/2):
            Spectral_Type_of_Star_C = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_C < ((5510+5570)/2):
            Spectral_Type_of_Star_C = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_C < ((5450+5510)/2):
            Spectral_Type_of_Star_C = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_C < ((5390+5450)/2):
            Spectral_Type_of_Star_C = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_C < ((5330+5390)/2):
            Spectral_Type_of_Star_C = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_C < ((5270+5330)/2):
            Spectral_Type_of_Star_C = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_C < ((5130+5270)/2):
            Spectral_Type_of_Star_C = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_C < ((4990+5130)/2):
            Spectral_Type_of_Star_C = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_C < ((4850+4990)/2):
            Spectral_Type_of_Star_C = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_C < ((4710+4850)/2):
            Spectral_Type_of_Star_C = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_C < ((4560+4710)/2):
            Spectral_Type_of_Star_C = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_C < ((4410+4560)/2):
            Spectral_Type_of_Star_C = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_C < ((4270+4410)/2):
            Spectral_Type_of_Star_C = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_C < ((4130+4270)/2):
            Spectral_Type_of_Star_C = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_C < ((3990+4130)/2):
            Spectral_Type_of_Star_C = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_C < ((3850+3990)/2):
            Spectral_Type_of_Star_C = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_C < ((3700+3850)/2):
            Spectral_Type_of_Star_C = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_C < ((3540+3700)/2):
            Spectral_Type_of_Star_C = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_C < ((3380+3540)/2):
            Spectral_Type_of_Star_C = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_C < ((3220+3380)/2):
            Spectral_Type_of_Star_C = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_C < ((3060+3220)/2):
            Spectral_Type_of_Star_C = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_C < ((2900+3060)/2):
            Spectral_Type_of_Star_C = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_C < ((2740+2900)/2):
            Spectral_Type_of_Star_C = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_C < ((2580+2740)/2):
            Spectral_Type_of_Star_C = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_C < ((2420+2580)/2):
            Spectral_Type_of_Star_C = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_C < ((2270+2420)/2):
            Spectral_Type_of_Star_C = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_C < ((2170+2270)/2):
            Spectral_Type_of_Star_C = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_C < ((2070+2170)/2):
            Spectral_Type_of_Star_C = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_C < ((1970+2070)/2):
            Spectral_Type_of_Star_C = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_C < ((1870+1970)/2):
            Spectral_Type_of_Star_C = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_C < ((1770+1870)/2):
            Spectral_Type_of_Star_C = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_C < ((1660+1770)/2):
            Spectral_Type_of_Star_C = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_C < ((1560+1660)/2):
            Spectral_Type_of_Star_C = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_C < ((1460+1560)/2):
            Spectral_Type_of_Star_C = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_C < ((1360+1460)/2):
            Spectral_Type_of_Star_C = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_C < ((1260+1360)/2):
            Spectral_Type_of_Star_C = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_C < ((1190+1260)/2):
            Spectral_Type_of_Star_C = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_C < ((1120+1190)/2):
            Spectral_Type_of_Star_C = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_C < ((1040+1120)/2):
            Spectral_Type_of_Star_C = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_C < ((960+1040)/2):
            Spectral_Type_of_Star_C = "T4"
            #median temperature of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_C < ((880+960)/2):
            Spectral_Type_of_Star_C = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_C < ((800+880)/2):
            Spectral_Type_of_Star_C = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_C < ((720+800)/2):
            Spectral_Type_of_Star_C = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_C < ((640+720)/2):
            Spectral_Type_of_Star_C = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_C < ((570+640)/2):
            Spectral_Type_of_Star_C = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_C < ((500+570)/2):
            Spectral_Type_of_Star_C = "Y0"
    print(f"Spectral Type of Star C: {Spectral_Type_of_Star_C}")

Spectral_Type_of_Star_D = "None"
if Number_of_Stars == 4:
    if Evolutionary_Stage_of_Star_D == "White Dwarf":
        Spectral_Type_of_Star_D = "D"
    if Evolutionary_Stage_of_Star_D != "White Dwarf":
        if Temperature_Effective_of_Star_D >= 16500:
            Spectral_Type_of_Star_D = "B3"
            #median temperature of 17000 Kelvin
        if 15500 <= Temperature_Effective_of_Star_D < 16500:
            Spectral_Type_of_Star_D = "B4"
            #median temperature of 16000 Kelvin
        if 14500 <= Temperature_Effective_of_Star_D < 15500:
            Spectral_Type_of_Star_D = "B5"
            #median temeperature of 15000 Kelvin
        if 13500 <= Temperature_Effective_of_Star_D < 14500:
            Spectral_Type_of_Star_D = "B6"
            #median temperature of 14000 Kelvin
        if ((11900+13000)/2) <= Temperature_Effective_of_Star_D < ((13000+14000)/2):
            Spectral_Type_of_Star_D = "B7"
            #median temperature of 13000 Kelvin
        if ((10800+11900)/2) <= Temperature_Effective_of_Star_D < ((11900+13000)/2):
            Spectral_Type_of_Star_D = "B8"
            #median temperature of 11900 Kelvin
        if ((9700+10800)/2) <= Temperature_Effective_of_Star_D < ((10800+11900)/2):
            Spectral_Type_of_Star_D = "B9"
            #median temperature of 10800
        if ((9450+9700)/2) <= Temperature_Effective_of_Star_D < ((9700+10800)/2):
            Spectral_Type_of_Star_D = "A0"
            #median temperaure of 9700
        if ((9200+9450)/2) <= Temperature_Effective_of_Star_D < ((9450+9700)/2):
            Spectral_Type_of_Star_D = "A1"
            #mediuam temperature of 9450
        if ((8950+9200)/2) <= Temperature_Effective_of_Star_D < ((9200+9450)/2):
            Spectral_Type_of_Star_D = "A2"
            #median temperature of 9200 Kelvin
        if ((8700+8950)/2) <= Temperature_Effective_of_Star_D < ((8950+9200)/2):
            Spectral_Type_of_Star_D = "A3"
            #median temperature of 8950 Kelvin
        if ((8450+8700)/2) <= Temperature_Effective_of_Star_D < ((8700+8950)/2):
            Spectral_Type_of_Star_D = "A4"
            #median temperature of 8700 Kelvin
        if ((8200+8450)/2) <= Temperature_Effective_of_Star_D < ((8450+8700)/2):
            Spectral_Type_of_Star_D = "A5"
            #median temperature of 8450 Kelvin
        if ((7950+8200)/2) <= Temperature_Effective_of_Star_D < ((8200+8450)/2):
            Spectral_Type_of_Star_D = "A6"
            #median temperature of 8200 Kelvin
        if ((7700+7950)/2) <= Temperature_Effective_of_Star_D < ((7950+8200)/2):
            Spectral_Type_of_Star_D = "A7"
            #median temperature of 7950 Kelvin
        if ((7460+7700)/2) <= Temperature_Effective_of_Star_D < ((7700+7950)/2):
            Spectral_Type_of_Star_D = "A8"
            #median temperature of 7700 Kelvin
        if ((7220+7460)/2) <= Temperature_Effective_of_Star_D < ((7460+7700)/2):
            Spectral_Type_of_Star_D = "A9"
            #median temperature of 7460 Kelvin
        if ((7090+7220)/2) <= Temperature_Effective_of_Star_D < ((7720+7460)/2):
            Spectral_Type_of_Star_D = "F0"
            #median temperature of 7220 Kelvin
        if ((6890+7090)/2) <= Temperature_Effective_of_Star_D < ((7090+7220)/2):
            Spectral_Type_of_Star_D = "F1"
            #median temperature of 7090 Kelvin
        if ((6760+6890)/2) <= Temperature_Effective_of_Star_D < ((6890+7090)/2):
            Spectral_Type_of_Star_D = "F2"
            #median temperature of 6890 Kelvin
        if ((6630+6760)/2) <= Temperature_Effective_of_Star_D < ((6760+6890)/2):
            Spectral_Type_of_Star_D = "F3"
            #median temperature of 6760 Kelvin
        if ((6500+6630)/2) <= Temperature_Effective_of_Star_D < ((6630+6760)/2):
            Spectral_Type_of_Star_D = "F4"
            #median temperature of 6630 Kelvin
        if ((6370+6500)/2) <= Temperature_Effective_of_Star_D < ((6500+6630)/2):
            Spectral_Type_of_Star_D = "F5"
            #median temperature of 6500 Kelvin
        if ((6240+6370)/2) <= Temperature_Effective_of_Star_D < ((6370+6500)/2):
            Spectral_Type_of_Star_D = "F6"
            #median temperature of 6370 Kelvin
        if ((6110+6240)/2) <= Temperature_Effective_of_Star_D < ((6240+6370)/2):
            Spectral_Type_of_Star_D = "F7"
            #median temperature of 6240 Kelvin
        if ((6020+6110)/2) <= Temperature_Effective_of_Star_D < ((6110+6240)/2):
            Spectral_Type_of_Star_D = "F8"
            #median temperature of 6110 Kelvin
        if ((5930+6020)/2) <= Temperature_Effective_of_Star_D < ((6020+6110)/2):
            Spectral_Type_of_Star_D = "F9"
            #median temperature of 6020 Kelvin
        if ((5850+5930)/2) <= Temperature_Effective_of_Star_D < ((5930+6020)/2):
            Spectral_Type_of_Star_D = "G0"
            #median temperature of 5930 Kelvin
        if ((5770+5850)/2) <= Temperature_Effective_of_Star_D < ((5850+5930)/2):
            Spectral_Type_of_Star_D = "G1"
            #median temperature of 5850 Kelvin
        if ((5700+5770)/2) <= Temperature_Effective_of_Star_D < ((5770+5850)/2):
            Spectral_Type_of_Star_D = "G2"
            #median temperature of 5770 Kelvin
        if ((5630+5700)/2) <= Temperature_Effective_of_Star_D < ((5700+5770)/2):
            Spectral_Type_of_Star_D = "G3"
            #median temperature of 5700 Kelvin
        if ((5570+5630)/2) <= Temperature_Effective_of_Star_D < ((5630+5700)/2):
            Spectral_Type_of_Star_D = "G4"
            #median temperature of 5630 Kelvin
        if ((5510+5570)/2) <= Temperature_Effective_of_Star_D < ((5570+5630)/2):
            Spectral_Type_of_Star_D = "G5"
            #median temperature of 5570 Kelvin
        if ((5450+5510)/2) <= Temperature_Effective_of_Star_D < ((5510+5570)/2):
            Spectral_Type_of_Star_D = "G6"
            #median temperature of 5510 Kelvin
        if ((5390+5450)/2) <= Temperature_Effective_of_Star_D < ((5450+5510)/2):
            Spectral_Type_of_Star_D = "G7"
            #median temperature of 5450 Kelvin
        if ((5330+5390)/2) <= Temperature_Effective_of_Star_D < ((5390+5450)/2):
            Spectral_Type_of_Star_D = "G8"
            #median temperature of 5390 Kelvin
        if ((5270+5330)/2) <= Temperature_Effective_of_Star_D < ((5330+5390)/2):
            Spectral_Type_of_Star_D = "G9"
            #median temperature of 5330 Kelvin
        if ((5130+5270)/2) <= Temperature_Effective_of_Star_D < ((5270+5330)/2):
            Spectral_Type_of_Star_D = "K0"
            #median temperature of 5270 Kelvin
        if ((4990+5130)/2) <= Temperature_Effective_of_Star_D < ((5130+5270)/2):
            Spectral_Type_of_Star_D = "K1"
            #median temperature of 5130 Kelvin
        if ((4850+4990)/2) <= Temperature_Effective_of_Star_D < ((4990+5130)/2):
            Spectral_Type_of_Star_D = "K2"
            #median temperature of 4990 Kelvin
        if ((4710+4850)/2) <= Temperature_Effective_of_Star_D < ((4850+4990)/2):
            Spectral_Type_of_Star_D = "K3"
            #median temperature of 4850 Kelvin
        if ((4560+4710)/2) <= Temperature_Effective_of_Star_D < ((4710+4850)/2):
            Spectral_Type_of_Star_D = "K4"
            #median temperature of 4710 Kelvin
        if ((4410+4560)/2) <= Temperature_Effective_of_Star_D < ((4560+4710)/2):
            Spectral_Type_of_Star_D = "K5"
            #median temperature of 4560 Kelvin
        if ((4270+4410)/2) <= Temperature_Effective_of_Star_D < ((4410+4560)/2):
            Spectral_Type_of_Star_D = "K6"
            #median temperature of 4410 Kelvin
        if ((4130+4270)/2) <= Temperature_Effective_of_Star_D < ((4270+4410)/2):
            Spectral_Type_of_Star_D = "K7"
            #median temperature of 4270 Kelvin
        if ((3990+4130)/2) <= Temperature_Effective_of_Star_D < ((4130+4270)/2):
            Spectral_Type_of_Star_D = "K8"
            #median temperature of 4130 Kelvin
        if ((3850+3990)/2) <= Temperature_Effective_of_Star_D < ((3990+4130)/2):
            Spectral_Type_of_Star_D = "K9"
            #median temperature of 3990 Kelvin
        if ((3700+3850)/2) <= Temperature_Effective_of_Star_D < ((3850+3990)/2):
            Spectral_Type_of_Star_D = "M0"
            #median temperature of 3850 Kelvin
        if ((3540+3700)/2) <= Temperature_Effective_of_Star_D < ((3700+3850)/2):
            Spectral_Type_of_Star_D = "M1"
            #median temperature of 3700 Kelvin
        if ((3380+3540)/2) <= Temperature_Effective_of_Star_D < ((3540+3700)/2):
            Spectral_Type_of_Star_D = "M2"
            #median temperature of 3540 Kelvin
        if ((3220+3380)/2) <= Temperature_Effective_of_Star_D < ((3380+3540)/2):
            Spectral_Type_of_Star_D = "M3"
            #median temperature of 3380 Kelvin
        if ((3060+3220)/2) <= Temperature_Effective_of_Star_D < ((3220+3380)/2):
            Spectral_Type_of_Star_D = "M4"
            #median temperature of 3220 Kelvin
        if ((2900+3060)/2) <= Temperature_Effective_of_Star_D < ((3060+3220)/2):
            Spectral_Type_of_Star_D = "M5"
            #median temperature of 3060 Kelvin
        if ((2740+2900)/2) <= Temperature_Effective_of_Star_D < ((2900+3060)/2):
            Spectral_Type_of_Star_D = "M6"
            #median temperature of 2900 Kelvin
        if ((2580+2740)/2) <= Temperature_Effective_of_Star_D < ((2740+2900)/2):
            Spectral_Type_of_Star_D = "M7"
            #median temperature of 2740 Kelvin
        if ((2420+2580)/2) <= Temperature_Effective_of_Star_D < ((2580+2740)/2):
            Spectral_Type_of_Star_D = "M8"
            #median temperature of 2580 Kelvin
        if ((2270+2420)/2) <= Temperature_Effective_of_Star_D < ((2420+2580)/2):
            Spectral_Type_of_Star_D = "M9"
            #median temperature of 2420 Kelvin
        if ((2170+2270)/2) <= Temperature_Effective_of_Star_D < ((2270+2420)/2):
            Spectral_Type_of_Star_D = "L0"
            #median temperature of 2270 Kelvin
        if ((2070+2170)/2) <= Temperature_Effective_of_Star_D < ((2170+2270)/2):
            Spectral_Type_of_Star_D = "L1"
            #median temperature of 2170 Kelvin
        if ((1970+2070)/2) <= Temperature_Effective_of_Star_D < ((2070+2170)/2):
            Spectral_Type_of_Star_D = "L2"
            #median temperature of 2070 Kelvin
        if ((1870+1970)/2) <= Temperature_Effective_of_Star_D < ((1970+2070)/2):
            Spectral_Type_of_Star_D = "L3"
            #median temperature of 1970 Kelvin
        if ((1770+1870)/2) <= Temperature_Effective_of_Star_D < ((1870+1970)/2):
            Spectral_Type_of_Star_D = "L4"
            #median temperature of 1870 Kelvin
        if ((1660+1770)/2) <= Temperature_Effective_of_Star_D < ((1770+1870)/2):
            Spectral_Type_of_Star_D = "L5"
            #median temperature of 1770 Kelvin
        if ((1560+1660)/2) <= Temperature_Effective_of_Star_D < ((1660+1770)/2):
            Spectral_Type_of_Star_D = "L6"
            #median temperature of 1660 Kelvin
        if ((1460+1560)/2) <= Temperature_Effective_of_Star_D < ((1560+1660)/2):
            Spectral_Type_of_Star_D = "L7"
            #median temperature of 1560 Kelvin
        if ((1360+1460)/2) <= Temperature_Effective_of_Star_D < ((1460+1560)/2):
            Spectral_Type_of_Star_D = "L8"
            #median temperature of 1460 Kelvin
        if ((1260+1360)/2) <= Temperature_Effective_of_Star_D < ((1360+1460)/2):
            Spectral_Type_of_Star_D = "L9"
            #median temperature of 1360 Kelvin
        if ((1190+1260)/2) <= Temperature_Effective_of_Star_D < ((1260+1360)/2):
            Spectral_Type_of_Star_D = "T0"
            #median temperature of 1260 Kelvin
        if ((1120+1190)/2) <= Temperature_Effective_of_Star_D < ((1190+1260)/2):
            Spectral_Type_of_Star_D = "T1"
            #median temperature of 1190 Kelvin
        if ((1040+1120)/2) <= Temperature_Effective_of_Star_D < ((1120+1190)/2):
            Spectral_Type_of_Star_D = "T2"
            #median temperature of 1120 Kelvin
        if ((960+1040)/2) <= Temperature_Effective_of_Star_D < ((1040+1120)/2):
            Spectral_Type_of_Star_D = "T3"
            #median temperature of 1040 Kelvin
        if ((880+960)/2) <= Temperature_Effective_of_Star_D < ((960+1040)/2):
            Spectral_Type_of_Star_D
            #median temperatue of 960 Kelvin
        if ((800+880)/2) <= Temperature_Effective_of_Star_D < ((880+960)/2):
            Spectral_Type_of_Star_D = "T5"
            #median temperature of 880 Kelvin
        if ((720+800)/2) <= Temperature_Effective_of_Star_D < ((800+880)/2):
            Spectral_Type_of_Star_D = "T6"
            #median temperature of 800 Kelvin
        if ((640+720)/2) <= Temperature_Effective_of_Star_D < ((720+800)/2):
            Spectral_Type_of_Star_D = "T7"
            #median temperature of 720 Kelvin
        if ((570+640)/2) <= Temperature_Effective_of_Star_D < ((640+720)/2):
            Spectral_Type_of_Star_D = "T8"
            #median temperature of 640 Kelvin
        if ((500+570)/2) <= Temperature_Effective_of_Star_D < ((570+640)/2):
            Spectral_Type_of_Star_D = "T9"
            #median temperature of 570 Kelvin
        if Temperature_Effective_of_Star_D < ((500+570)/2):
            Spectral_Type_of_Star_D = "Y0"
    print(f"Spectral Type of Star D: {Spectral_Type_of_Star_D}")

# Step 8: Stellar Orbital Parameters

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

# Step 9: Protoplanetary Disk
    # calculate disk density
    if Number_of_Stars >= 1:
        # calculate disk density of Star A
        roll_for_Disk_Density_of_Star_A = _3d6()
        if roll_for_Disk_Density_of_Star_A == 3:
            Disk_Mass_Factor_Star_A = 0.25
            Disk_Mass_Modifier_Star_A = -6
        if roll_for_Disk_Density_of_Star_A == 4:
            Disk_Mass_Factor_Star_A = 0.32
            Disk_Mass_Modifier_Star_A = -5
        if roll_for_Disk_Density_of_Star_A == 5:
            Disk_Mass_Factor_Star_A = 0.4
            Disk_Mass_Modifier_Star_A = -4
        if roll_for_Disk_Density_of_Star_A == 6:
            Disk_Mass_Factor_Star_A = 0.5
            Disk_Mass_Modifier_Star_A = -3
        if roll_for_Disk_Density_of_Star_A == 7:
            Disk_Mass_Factor_Star_A = 0.6
            Disk_Mass_Modifier_Star_A = -2
        if roll_for_Disk_Density_of_Star_A == 8:
            Disk_Mass_Factor_Star_A = 0.7
            Disk_Mass_Modifier_Star_A = -1
        if roll_for_Disk_Density_of_Star_A == 9:
            Disk_Mass_Factor_Star_A = 0.8
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 10:
            Disk_Mass_Factor_Star_A = 1.0
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 11:
            Disk_Mass_Factor_Star_A = 1.0
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 12:
            Disk_Mass_Factor_Star_A = 1.2
            Disk_Mass_Modifier_Star_A = 0
        if roll_for_Disk_Density_of_Star_A == 13:
            Disk_Mass_Factor_Star_A = 1.4
            Disk_Mass_Modifier_Star_A = 1
        if roll_for_Disk_Density_of_Star_A == 14:
            Disk_Mass_Factor_Star_A = 1.7
            Disk_Mass_Modifier_Star_A = 2
        if roll_for_Disk_Density_of_Star_A == 15:
            Disk_Mass_Factor_Star_A = 2.0
            Disk_Mass_Modifier_Star_A = 3
        if roll_for_Disk_Density_of_Star_A == 16:
            Disk_Mass_Factor_Star_A = 2.5
            Disk_Mass_Modifier_Star_A = 4
        if roll_for_Disk_Density_of_Star_A == 17:
            Disk_Mass_Factor_Star_A = 3.2
            Disk_Mass_Modifier_Star_A = 5
        if roll_for_Disk_Density_of_Star_A == 18:
            Disk_Mass_Factor_Star_A = 4.0
            Disk_Mass_Modifier_Star_A = 6
        print(f"Disk Mass Factor for Star A: {Disk_Mass_Factor_Star_A}")
        print(f"Disk Mass Modifier for Star A: {Disk_Mass_Modifier_Star_A}")

    if Number_of_Stars >= 2:
        # calculate disk density of Star B
        roll_for_Disk_Density_of_Star_B = _3d6()
        if roll_for_Disk_Density_of_Star_B == 3:
            Disk_Mass_Factor_Star_B = 0.25
            Disk_Mass_Modifier_Star_B = -6
        if roll_for_Disk_Density_of_Star_B == 4:
            Disk_Mass_Factor_Star_B = 0.32
            Disk_Mass_Modifier_Star_B = -5
        if roll_for_Disk_Density_of_Star_B == 5:
            Disk_Mass_Factor_Star_B = 0.4
            Disk_Mass_Modifier_Star_B = -4
        if roll_for_Disk_Density_of_Star_B == 6:
            Disk_Mass_Factor_Star_B = 0.5
            Disk_Mass_Modifier_Star_B = -3
        if roll_for_Disk_Density_of_Star_B == 7:
            Disk_Mass_Factor_Star_B = 0.6
            Disk_Mass_Modifier_Star_B = -2
        if roll_for_Disk_Density_of_Star_B == 8:
            Disk_Mass_Factor_Star_B = 0.7
            Disk_Mass_Modifier_Star_B = -1
        if roll_for_Disk_Density_of_Star_B == 9:
            Disk_Mass_Factor_Star_B = 0.8
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 10:
            Disk_Mass_Factor_Star_B = 1.0
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 11:
            Disk_Mass_Factor_Star_B = 1.0
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 12:
            Disk_Mass_Factor_Star_B = 1.2
            Disk_Mass_Modifier_Star_B = 0
        if roll_for_Disk_Density_of_Star_B == 13:
            Disk_Mass_Factor_Star_B = 1.4
            Disk_Mass_Modifier_Star_B = 1
        if roll_for_Disk_Density_of_Star_B == 14:
            Disk_Mass_Factor_Star_B = 1.7
            Disk_Mass_Modifier_Star_B = 2
        if roll_for_Disk_Density_of_Star_B == 15:
            Disk_Mass_Factor_Star_B = 2.0
            Disk_Mass_Modifier_Star_B = 3
        if roll_for_Disk_Density_of_Star_B == 16:
            Disk_Mass_Factor_Star_B = 2.5
            Disk_Mass_Modifier_Star_B = 4
        if roll_for_Disk_Density_of_Star_B == 17:
            Disk_Mass_Factor_Star_B = 3.2
            Disk_Mass_Modifier_Star_B = 5
        if roll_for_Disk_Density_of_Star_B == 18:
            Disk_Mass_Factor_Star_B = 4.0
            Disk_Mass_Modifier_Star_B = 6
        print(f"Disk Mass Factor for Star B: {Disk_Mass_Factor_Star_B}")
        print(f"Disk Mass Modifier for Star B: {Disk_Mass_Modifier_Star_B}")

    if Number_of_Stars >= 3:
        # calculate disk density of Star C
        roll_for_Disk_Density_of_Star_C = _3d6()
        if roll_for_Disk_Density_of_Star_C == 3:
            Disk_Mass_Factor_Star_C = 0.25
            Disk_Mass_Modifier_Star_C = -6
        if roll_for_Disk_Density_of_Star_C == 4:
            Disk_Mass_Factor_Star_C = 0.32
            Disk_Mass_Modifier_Star_C = -5
        if roll_for_Disk_Density_of_Star_C == 5:
            Disk_Mass_Factor_Star_C = 0.4
            Disk_Mass_Modifier_Star_C = -4
        if roll_for_Disk_Density_of_Star_C == 6:
            Disk_Mass_Factor_Star_C = 0.5
            Disk_Mass_Modifier_Star_C = -3
        if roll_for_Disk_Density_of_Star_C == 7:
            Disk_Mass_Factor_Star_C = 0.6
            Disk_Mass_Modifier_Star_C = -2
        if roll_for_Disk_Density_of_Star_C == 8:
            Disk_Mass_Factor_Star_C = 0.7
            Disk_Mass_Modifier_Star_C = -1
        if roll_for_Disk_Density_of_Star_C == 9:
            Disk_Mass_Factor_Star_C = 0.8
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 10:
            Disk_Mass_Factor_Star_C = 1.0
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 11:
            Disk_Mass_Factor_Star_C = 1.0
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 12:
            Disk_Mass_Factor_Star_C = 1.2
            Disk_Mass_Modifier_Star_C = 0
        if roll_for_Disk_Density_of_Star_C == 13:
            Disk_Mass_Factor_Star_C = 1.4
            Disk_Mass_Modifier_Star_C = 1
        if roll_for_Disk_Density_of_Star_C == 14:
            Disk_Mass_Factor_Star_C = 1.7
            Disk_Mass_Modifier_Star_C = 2
        if roll_for_Disk_Density_of_Star_C == 15:
            Disk_Mass_Factor_Star_C = 2.0
            Disk_Mass_Modifier_Star_C = 3
        if roll_for_Disk_Density_of_Star_C == 16:
            Disk_Mass_Factor_Star_C = 2.5
            Disk_Mass_Modifier_Star_C = 4
        if roll_for_Disk_Density_of_Star_C == 17:
            Disk_Mass_Factor_Star_C = 3.2
            Disk_Mass_Modifier_Star_C = 5
        if roll_for_Disk_Density_of_Star_C == 18:
            Disk_Mass_Factor_Star_C = 4.0
            Disk_Mass_Modifier_Star_C = 6
        print(f"Disk Mass Factor for Star C: {Disk_Mass_Factor_Star_C}")
        print(f"Disk Mass Modifier for Star C: {Disk_Mass_Modifier_Star_C}")

    if Number_of_Stars == 4:
        roll_for_Disk_Density_of_Star_D = _3d6()
        if roll_for_Disk_Density_of_Star_D == 3:
            Disk_Mass_Factor_Star_D = 0.25
            Disk_Mass_Modifier_Star_D = -6
        if roll_for_Disk_Density_of_Star_D == 4:
            Disk_Mass_Factor_Star_D = 0.32
            Disk_Mass_Modifier_Star_D = -5
        if roll_for_Disk_Density_of_Star_D == 5:
            Disk_Mass_Factor_Star_D = 0.4
            Disk_Mass_Modifier_Star_D = -4
        if roll_for_Disk_Density_of_Star_D == 6:
            Disk_Mass_Factor_Star_D = 0.5
            Disk_Mass_Modifier_Star_D = -3
        if roll_for_Disk_Density_of_Star_D == 7:
            Disk_Mass_Factor_Star_D = 0.6
            Disk_Mass_Modifier_Star_D = -2
        if roll_for_Disk_Density_of_Star_D == 8:
            Disk_Mass_Factor_Star_D = 0.7
            Disk_Mass_Modifier_Star_D = -1
        if roll_for_Disk_Density_of_Star_D == 9:
            Disk_Mass_Factor_Star_D = 0.8
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 10:
            Disk_Mass_Factor_Star_D = 1.0
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 11:
            Disk_Mass_Factor_Star_D = 1.0
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 12:
            Disk_Mass_Factor_Star_D = 1.2
            Disk_Mass_Modifier_Star_D = 0
        if roll_for_Disk_Density_of_Star_D == 13:
            Disk_Mass_Factor_Star_D = 1.4
            Disk_Mass_Modifier_Star_D = 1
        if roll_for_Disk_Density_of_Star_D == 14:
            Disk_Mass_Factor_Star_D = 1.7
            Disk_Mass_Modifier_Star_D = 2
        if roll_for_Disk_Density_of_Star_D == 15:
            Disk_Mass_Factor_Star_D = 2.0
            Disk_Mass_Modifier_Star_D = 3
        if roll_for_Disk_Density_of_Star_D == 16:
            Disk_Mass_Factor_Star_D = 2.5
            Disk_Mass_Modifier_Star_D = 4
        if roll_for_Disk_Density_of_Star_D == 17:
            Disk_Mass_Factor_Star_D = 3.2
            Disk_Mass_Modifier_Star_D = 5
        if roll_for_Disk_Density_of_Star_D == 18:
            Disk_Mass_Factor_Star_D = 4.0
            Disk_Mass_Modifier_Star_D = 6
        print(f"Disk Mass Factor for Star D: {Disk_Mass_Factor_Star_D}")
        print(f"Disk Mass Modifier for Star D: {Disk_Mass_Modifier_Star_D}")

    # calculate planetismal masses
    if Number_of_Stars >= 1:
        Planetismal_Mass_for_Star_A = Disk_Mass_Factor_Star_A * Mass_A * Metallicity
        print(f"Planentismal Mass for Star A: {Planetismal_Mass_for_Star_A}")
    if Number_of_Stars >= 2:
        Planetismal_Mass_for_Star_B = Disk_Mass_Factor_Star_B * Mass_B * Metallicity
        print(f"Planentismal Mass for Star B: {Planetismal_Mass_for_Star_B}")
    if Number_of_Stars >= 3:
        Planetismal_Mass_for_Star_C = Disk_Mass_Factor_Star_C * Mass_C * Metallicity
        print(f"Planentismal Mass for Star C: {Planetismal_Mass_for_Star_C}")
    if Number_of_Stars == 4:
        Planetismal_Mass_for_Star_D = Disk_Mass_Factor_Star_D * Mass_D * Metallicity
        print(f"Planentismal Mass for Star D: {Planetismal_Mass_for_Star_D}")

    # calculate disk inner edges
    if Number_of_Stars >= 1:
        Disk_Inner_Edge_for_Star_A = (_2d6) * 0.005 * (Mass_A ** (1/3))
        Disk_Inner_Edge_for_Star_A = round(Disk_Inner_Edge_for_Star_A,3)
        print(f"Disk Inner Edge for Star A: {Disk_Inner_Edge_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Disk_Inner_Edge_for_Star_B = (_2d6) * 0.005 * (Mass_B ** (1/3))
        Disk_Inner_Edge_for_Star_B = round(Disk_Inner_Edge_for_Star_B,3)
        print(f"Disk Inner Edge for Star B: {Disk_Inner_Edge_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Disk_Inner_Edge_for_Star_C = (_2d6) * 0.005 * (Mass_C ** (1/3))
        Disk_Inner_Edge_for_Star_C = round(Disk_Inner_Edge_for_Star_C,3)
        print(f"Disk Inner Edge for Star C: {Disk_Inner_Edge_for_Star_C} AU")
    if Number_of_Stars == 4:
        Disk_Inner_Edge_for_Star_D = (_2d6) * 0.005 * (Mass_D ** (1/3))
        Disk_Inner_Edge_for_Star_D = round(Disk_Inner_Edge_for_Star_D,3)
        print(f"Disk Inner Edge for Star D: {Disk_Inner_Edge_for_Star_D} AU")

    # calculate ice lines
    if Number_of_Stars >= 1:
        Radius_of_Ice_Line_for_Star_A = 4 * math.sqrt(Initial_Luminosity_of_Star_A)
        Radius_of_Ice_Line_for_Star_A = round(Radius_of_Ice_Line_for_Star_A,3)
        print(f"Ice Line for Star A: {Radius_of_Ice_Line_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Radius_of_Ice_Line_for_Star_B = 4 * math.sqrt(Initial_Luminosity_of_Star_B)
        Radius_of_Ice_Line_for_Star_B = round(Radius_of_Ice_Line_for_Star_B,3)
        print(f"Ice Line for Star B: {Radius_of_Ice_Line_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Radius_of_Ice_Line_for_Star_C = 4 * math.sqrt(Initial_Luminosity_of_Star_C)
        Radius_of_Ice_Line_for_Star_C = round(Radius_of_Ice_Line_for_Star_C,3)
        print(f"Ice Line for Star C: {Radius_of_Ice_Line_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Ice_Line_for_Star_D = 4 * math.sqrt(Initial_Luminosity_of_Star_D)
        Radius_of_Ice_Line_for_Star_D = round(Radius_of_Ice_Line_for_Star_D,3)
        print(f"Ice Line for Star D: {Radius_of_Ice_Line_for_Star_D} AU")

    # calculate slow accretion lines
    if Number_of_Stars >= 1:
        Radius_of_Slow_Accretion_Line_for_Star_A = 20 * (Mass_A ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_A = round(Radius_of_Slow_Accretion_Line_for_Star_A,3)
        print(f"Slow Accretion Line for Star A: {Radius_of_Slow_Accretion_Line_for_Star_A} AU")
    if Number_of_Stars >= 2:
        Radius_of_Slow_Accretion_Line_for_Star_B = 20 * (Mass_B ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_B = round(Radius_of_Slow_Accretion_Line_for_Star_B,3)
        print(f"Slow Accretion Line for Star B: {Radius_of_Slow_Accretion_Line_for_Star_B} AU")
    if Number_of_Stars >= 3:
        Radius_of_Slow_Accretion_Line_for_Star_C = 20 * (Mass_C ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_C = round(Radius_of_Slow_Accretion_Line_for_Star_C,3)
        print(f"Slow Accretion Line for Star C: {Radius_of_Slow_Accretion_Line_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Slow_Accretion_Line_for_Star_D = 20 * (Mass_D ** (1/3))
        Radius_of_Slow_Accretion_Line_for_Star_D = round(Radius_of_Slow_Accretion_Line_for_Star_D,3)
        print(f"Slow Accretion Line for Star D: {Radius_of_Slow_Accretion_Line_for_Star_D} AU")

    # calculate forbidden zones
    if Number_of_Stars == 1:
        print("Single Star System - No Forbidden Zone for Planet Formation")
    if Number_of_Stars == 2:
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * binary_minimum_distance
        print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * binary_minimum_distance
        print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
    if Number_of_Stars == 3:
        if Stellar_Arrangement == "A-BC":
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * A_BC_minimum_distance
            print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * BC_minimum_distance
            print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * BC_minimum_distance
            print(f"Forbidden Zone for Star C begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
        if Stellar_Arrangement == "AB-C":
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * AB_minimum_distance
            print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * AB_minimum_distance
            print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
            Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * AB_C_minimum_distance
            print(f"Forbidden Zone for Star c begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
    if Number_of_Stars == 4:
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A = (1/3) * AB_minimum_distance
        print(f"Forbidden Zone for Star A begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B = (1/3) * AB_minimum_distance
        print(f"Forbidden Zone for Star B begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C = (1/3) * CD_minimum_distance
        print(f"Forbidden Zone for Star C begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C} AU")
        Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D = (1/3) * CD_minimum_distance
        print(f"Forbidden Zone for Star D begins at {Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D} AU")

    # arrange planetary formation orbits
    if Number_of_Stars >= 1:

        Star_A_Protoplanet_1_Flag = "Yes"
        Star_A_Protoplanet_1_Speed_Flag = "Fast"
        Star_A_Protoplanet_2_Flag = "Yes"
        Star_A_Protoplanet_2_Speed_Flag = "Fast"
        Star_A_Protoplanet_3_Flag = "Yes"
        Star_A_Protoplanet_3_Speed_Flag = "Fast"
        Star_A_Protoplanet_4_Flag = "Yes"
        Star_A_Protoplanet_4_Speed_Flag = "Fast"
        Star_A_Protoplanet_5_Flag = "Yes"
        Star_A_Protoplanet_5_Speed_Flag = "Fast"
        Star_A_Protoplanet_6_Flag = "Yes"
        Star_A_Protoplanet_6_Speed_Flag = "Fast"
        Star_A_Protoplanet_7_Flag = "Yes"
        Star_A_Protoplanet_7_Speed_Flag = "Fast"
        Star_A_Protoplanet_8_Flag = "Yes"
        Star_A_Protoplanet_8_Speed_Flag = "Fast"
        Star_A_Protoplanet_9_Flag = "Yes"
        Star_A_Protoplanet_9_Speed_Flag = "Fast"
        Star_A_Protoplanet_10_Flag = "Yes"
        Star_A_Protoplanet_10_Speed_Flag = "Fast"
        Star_A_Protoplanet_11_Flag = "Yes"
        Star_A_Protoplanet_11_Speed_Flag = "Fast"
        Star_A_Protoplanet_12_Flag = "Yes"
        Star_A_Protoplanet_12_Speed_Flag = "Fast"
        Star_A_Protoplanet_13_Flag = "Yes"
        Star_A_Protoplanet_13_Speed_Flag = "Fast"
        Star_A_Protoplanet_14_Flag = "Yes"
        Star_A_Protoplanet_14_Speed_Flag = "Fast"
        Star_A_Protoplanet_15_Flag = "Yes"
        Star_A_Protoplanet_15_Speed_Flag = "Fast"
        Star_A_Protoplanet_16_Flag = "Yes"
        Star_A_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_A = Disk_Inner_Edge_for_Star_A

        formation_orbit_1_for_Star_A = 0.6 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_1_for_Star_A:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_A_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_A = 0.8 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_2_for_Star_A:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_A_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_A = 1.2 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_3_for_Star_A:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_A_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_A_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_A = 1.8 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_4_for_Star_A:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_A_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_A = 2.7 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_5_for_Star_A:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_A_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_A = 4.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_6_for_Star_A:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_A_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_A = 6.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_7_for_Star_A:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_A_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_A = 9.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_8_for_Star_A:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_A_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_A = 13.5 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_9_for_Star_A:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_A_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_A = 20.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_10_for_Star_A:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_A_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_A = 30.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_10_for_Star_A:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_A_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_A = 45.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_12_for_Star_A:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_A_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_A = 68.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_13_for_Star_A:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_A_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_A = 100.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_14_for_Star_A:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_A_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_A = 150.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_15_for_Star_A:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_A_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_A = 222.0 * math.sqrt(Initial_Luminosity_of_Star_A)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_A} AU")
        if formation_orbit_0_for_Star_A >= formation_orbit_16_for_Star_A:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_A_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_A >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_A:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_A_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_A >= Radius_of_Slow_Accretion_Line_for_Star_A:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_A_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars >= 2:
        Star_B_Protoplanet_1_Flag = "Yes"
        Star_B_Protoplanet_1_Speed_Flag = "Fast"
        Star_B_Protoplanet_2_Flag = "Yes"
        Star_B_Protoplanet_2_Speed_Flag = "Fast"
        Star_B_Protoplanet_3_Flag = "Yes"
        Star_B_Protoplanet_3_Speed_Flag = "Fast"
        Star_B_Protoplanet_4_Flag = "Yes"
        Star_B_Protoplanet_4_Speed_Flag = "Fast"
        Star_B_Protoplanet_5_Flag = "Yes"
        Star_B_Protoplanet_5_Speed_Flag = "Fast"
        Star_B_Protoplanet_6_Flag = "Yes"
        Star_B_Protoplanet_6_Speed_Flag = "Fast"
        Star_B_Protoplanet_7_Flag = "Yes"
        Star_B_Protoplanet_7_Speed_Flag = "Fast"
        Star_B_Protoplanet_8_Flag = "Yes"
        Star_B_Protoplanet_8_Speed_Flag = "Fast"
        Star_B_Protoplanet_9_Flag = "Yes"
        Star_B_Protoplanet_9_Speed_Flag = "Fast"
        Star_B_Protoplanet_10_Flag = "Yes"
        Star_B_Protoplanet_10_Speed_Flag = "Fast"
        Star_B_Protoplanet_11_Flag = "Yes"
        Star_B_Protoplanet_11_Speed_Flag = "Fast"
        Star_B_Protoplanet_12_Flag = "Yes"
        Star_B_Protoplanet_12_Speed_Flag = "Fast"
        Star_B_Protoplanet_13_Flag = "Yes"
        Star_B_Protoplanet_13_Speed_Flag = "Fast"
        Star_B_Protoplanet_14_Flag = "Yes"
        Star_B_Protoplanet_14_Speed_Flag = "Fast"
        Star_B_Protoplanet_15_Flag = "Yes"
        Star_B_Protoplanet_15_Speed_Flag = "Fast"
        Star_B_Protoplanet_16_Flag = "Yes"
        Star_B_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_B = Disk_Inner_Edge_for_Star_B

        formation_orbit_1_for_Star_B = 0.6 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_1_for_Star_B:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_B_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_B = 0.8 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_2_for_Star_B:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_B_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_B = 1.2 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_3_for_Star_B:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_B_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_B_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_B = 1.8 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_4_for_Star_B:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_B_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_B = 2.7 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_5_for_Star_B:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_B_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_B = 4.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_6_for_Star_B:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_B_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_B = 6.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_7_for_Star_B:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_B_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_B = 9.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_8_for_Star_B:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_B_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_B = 13.5 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_9_for_Star_B:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_B_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_B = 20.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_10_for_Star_B:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_B_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_B = 30.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_10_for_Star_B:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_B_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_B = 45.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_12_for_Star_B:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_B_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_B = 68.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_13_for_Star_B:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_B_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_B = 100.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_14_for_Star_B:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_B_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_B = 150.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_15_for_Star_B:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_B_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_B = 222.0 * math.sqrt(Initial_Luminosity_of_Star_B)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_B} AU")
        if formation_orbit_0_for_Star_B >= formation_orbit_16_for_Star_B:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_B_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_B >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_B:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_B_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_B >= Radius_of_Slow_Accretion_Line_for_Star_B:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_B_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars >= 3:
        Star_C_Protoplanet_1_Flag = "Yes"
        Star_C_Protoplanet_1_Speed_Flag = "Fast"
        Star_C_Protoplanet_2_Flag = "Yes"
        Star_C_Protoplanet_2_Speed_Flag = "Fast"
        Star_C_Protoplanet_3_Flag = "Yes"
        Star_C_Protoplanet_3_Speed_Flag = "Fast"
        Star_C_Protoplanet_4_Flag = "Yes"
        Star_C_Protoplanet_4_Speed_Flag = "Fast"
        Star_C_Protoplanet_5_Flag = "Yes"
        Star_C_Protoplanet_5_Speed_Flag = "Fast"
        Star_C_Protoplanet_6_Flag = "Yes"
        Star_C_Protoplanet_6_Speed_Flag = "Fast"
        Star_C_Protoplanet_7_Flag = "Yes"
        Star_C_Protoplanet_7_Speed_Flag = "Fast"
        Star_C_Protoplanet_8_Flag = "Yes"
        Star_C_Protoplanet_8_Speed_Flag = "Fast"
        Star_C_Protoplanet_9_Flag = "Yes"
        Star_C_Protoplanet_9_Speed_Flag = "Fast"
        Star_C_Protoplanet_10_Flag = "Yes"
        Star_C_Protoplanet_10_Speed_Flag = "Fast"
        Star_C_Protoplanet_11_Flag = "Yes"
        Star_C_Protoplanet_11_Speed_Flag = "Fast"
        Star_C_Protoplanet_12_Flag = "Yes"
        Star_C_Protoplanet_12_Speed_Flag = "Fast"
        Star_C_Protoplanet_13_Flag = "Yes"
        Star_C_Protoplanet_13_Speed_Flag = "Fast"
        Star_C_Protoplanet_14_Flag = "Yes"
        Star_C_Protoplanet_14_Speed_Flag = "Fast"
        Star_C_Protoplanet_15_Flag = "Yes"
        Star_C_Protoplanet_15_Speed_Flag = "Fast"
        Star_C_Protoplanet_16_Flag = "Yes"
        Star_C_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_C = Disk_Inner_Edge_for_Star_C

        formation_orbit_1_for_Star_C = 0.6 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_1_for_Star_C:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_C_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_C = 0.8 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_2_for_Star_C:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_C_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_C = 1.2 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_3_for_Star_C:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_C_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_C_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_C = 1.8 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_4_for_Star_C:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_C_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_C = 2.7 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_5_for_Star_C:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_C_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_C = 4.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_6_for_Star_C:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_C_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_C = 6.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_7_for_Star_C:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_C_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_C = 9.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_8_for_Star_C:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_C_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_C = 13.5 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_9_for_Star_C:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_C_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_C = 20.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_10_for_Star_C:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_C_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_C = 30.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_10_for_Star_C:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_C_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_C = 45.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_12_for_Star_C:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_C_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_C = 68.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_13_for_Star_C:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_C_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_C = 100.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_14_for_Star_C:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_C_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_C = 150.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_15_for_Star_C:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_C_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_C = 222.0 * math.sqrt(Initial_Luminosity_of_Star_C)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_C} AU")
        if formation_orbit_0_for_Star_C >= formation_orbit_16_for_Star_C:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_C_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_C >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_C:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_C_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_C >= Radius_of_Slow_Accretion_Line_for_Star_C:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_C_Protoplanet_16_Speed_Flag = "Slow"

    if Number_of_Stars == 4:
        Star_D_Protoplanet_1_Flag = "Yes"
        Star_D_Protoplanet_1_Speed_Flag = "Fast"
        Star_D_Protoplanet_2_Flag = "Yes"
        Star_D_Protoplanet_2_Speed_Flag = "Fast"
        Star_D_Protoplanet_3_Flag = "Yes"
        Star_D_Protoplanet_3_Speed_Flag = "Fast"
        Star_D_Protoplanet_4_Flag = "Yes"
        Star_D_Protoplanet_4_Speed_Flag = "Fast"
        Star_D_Protoplanet_5_Flag = "Yes"
        Star_D_Protoplanet_5_Speed_Flag = "Fast"
        Star_D_Protoplanet_6_Flag = "Yes"
        Star_D_Protoplanet_6_Speed_Flag = "Fast"
        Star_D_Protoplanet_7_Flag = "Yes"
        Star_D_Protoplanet_7_Speed_Flag = "Fast"
        Star_D_Protoplanet_8_Flag = "Yes"
        Star_D_Protoplanet_8_Speed_Flag = "Fast"
        Star_D_Protoplanet_9_Flag = "Yes"
        Star_D_Protoplanet_9_Speed_Flag = "Fast"
        Star_D_Protoplanet_10_Flag = "Yes"
        Star_D_Protoplanet_10_Speed_Flag = "Fast"
        Star_D_Protoplanet_11_Flag = "Yes"
        Star_D_Protoplanet_11_Speed_Flag = "Fast"
        Star_D_Protoplanet_12_Flag = "Yes"
        Star_D_Protoplanet_12_Speed_Flag = "Fast"
        Star_D_Protoplanet_13_Flag = "Yes"
        Star_D_Protoplanet_13_Speed_Flag = "Fast"
        Star_D_Protoplanet_14_Flag = "Yes"
        Star_D_Protoplanet_14_Speed_Flag = "Fast"
        Star_D_Protoplanet_15_Flag = "Yes"
        Star_D_Protoplanet_15_Speed_Flag = "Fast"
        Star_D_Protoplanet_16_Flag = "Yes"
        Star_D_Protoplanet_16_Speed_Flag = "Fast"

        formation_orbit_0_for_Star_D = Disk_Inner_Edge_for_Star_D

        formation_orbit_1_for_Star_D = 0.6 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 1 for Star A is at {formation_orbit_1_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_1_for_Star_D:
            print("Formation Orbit 1 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 1 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_1_Flag = "No"
        if formation_orbit_1_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 1 is outisde the slow accretion line")
            Star_D_Protoplanet_1_Speed_Flag = "Slow"

        formation_orbit_2_for_Star_D = 0.8 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 2 for Star A is at {formation_orbit_2_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_2_for_Star_D:
            print("Formation Orbit 2 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 2 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_2_Flag = "No"
        if formation_orbit_2_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 2 is outisde the slow accretion line")
            Star_D_Protoplanet_2_Speed_Flag = "Slow"

        formation_orbit_3_for_Star_D = 1.2 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 3 for Star A is at {formation_orbit_3_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_3_for_Star_D:
            print("Formation Orbit 3 is within the inner edge - no protoplanet formed") 
            Star_D_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 3 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_3_Flag = "No"
        if formation_orbit_3_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 3 is outisde the slow accretion line")
            Star_D_Protoplanet_3_Speed_Flag = "Slow"

        formation_orbit_4_for_Star_D = 1.8 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 4 for Star A is at {formation_orbit_4_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_4_for_Star_D:
            print("Formation Orbit 4 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 4 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_4_Flag = "No"
        if formation_orbit_4_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 4 is outisde the slow accretion line")
            Star_D_Protoplanet_4_Speed_Flag = "Slow"

        formation_orbit_5_for_Star_D = 2.7 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 5 for Star A is at {formation_orbit_5_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_5_for_Star_D:
            print("Formation Orbit 5 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 5 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_5_Flag = "No"
        if formation_orbit_5_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 5 is outisde the slow accretion line")
            Star_D_Protoplanet_5_Speed_Flag = "Slow"

        formation_orbit_6_for_Star_D = 4.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 6 for Star A is at {formation_orbit_6_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_6_for_Star_D:
            print("Formation Orbit 6 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 6 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_6_Flag = "No"
        if formation_orbit_6_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 6 is outisde the slow accretion line")
            Star_D_Protoplanet_6_Speed_Flag = "Slow"

        formation_orbit_7_for_Star_D = 6.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 7 for Star A is at {formation_orbit_7_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_7_for_Star_D:
            print("Formation Orbit 7 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 7 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_7_Flag = "No"
        if formation_orbit_7_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 7 is outisde the slow accretion line")
            Star_D_Protoplanet_7_Speed_Flag = "Slow"

        formation_orbit_8_for_Star_D = 9.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 8 for Star A is at {formation_orbit_8_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_8_for_Star_D:
            print("Formation Orbit 8 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 8 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_8_Flag = "No"
        if formation_orbit_8_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 8 is outisde the slow accretion line")
            Star_D_Protoplanet_8_Speed_Flag = "Slow"

        formation_orbit_9_for_Star_D = 13.5 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 9 for Star A is at {formation_orbit_9_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_9_for_Star_D:
            print("Formation Orbit 9 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 9 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_9_Flag = "No"
        if formation_orbit_9_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 9 is outisde the slow accretion line")
            Star_D_Protoplanet_9_Speed_Flag = "Slow"

        formation_orbit_10_for_Star_D = 20.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 10 for Star A is at {formation_orbit_10_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_10_for_Star_D:
            print("Formation Orbit 10 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 10 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_10_Flag = "No"
        if formation_orbit_10_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 10 is outisde the slow accretion line")
            Star_D_Protoplanet_10_Speed_Flag = "Slow"

        formation_orbit_11_for_Star_D = 30.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 11 for Star A is at {formation_orbit_11_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_10_for_Star_D:
            print("Formation Orbit 11 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 11 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_11_Flag = "No"
        if formation_orbit_11_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 11 is outisde the slow accretion line")
            Star_D_Protoplanet_11_Speed_Flag = "Slow"

        formation_orbit_12_for_Star_D = 45.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 12 for Star A is at {formation_orbit_12_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_12_for_Star_D:
            print("Formation Orbit 12 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 12 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_12_Flag = "No"
        if formation_orbit_12_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 12 is outisde the slow accretion line")
            Star_D_Protoplanet_12_Speed_Flag = "Slow"

        formation_orbit_13_for_Star_D = 68.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 13 for Star A is at {formation_orbit_13_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_13_for_Star_D:
            print("Formation Orbit 13 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 13 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_13_Flag = "No"
        if formation_orbit_13_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 13 is outisde the slow accretion line")
            Star_D_Protoplanet_13_Speed_Flag = "Slow"

        formation_orbit_14_for_Star_D = 100.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 14 for Star A is at {formation_orbit_14_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_14_for_Star_D:
            print("Formation Orbit 14 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_14_Flag = "No"
        if formation_orbit_14_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 14 is outisde the slow accretion line")
            Star_D_Protoplanet_14_Speed_Flag = "Slow"

        formation_orbit_15_for_Star_D = 150.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 15 for Star A is at {formation_orbit_15_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_15_for_Star_D:
            print("Formation Orbit 15 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 15 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_15_Flag = "No"
        if formation_orbit_15_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 15 is outisde the slow accretion line")
            Star_D_Protoplanet_15_Speed_Flag = "Slow"

        formation_orbit_16_for_Star_D = 222.0 * math.sqrt(Initial_Luminosity_of_Star_D)
        print("Formation Orbit 16 for Star A is at {formation_orbit_16_for_Star_D} AU")
        if formation_orbit_0_for_Star_D >= formation_orbit_16_for_Star_D:
            print("Formation Orbit 16 is within the inner edge - no protoplanet formed")
            Star_D_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_D >= Radius_of_Inner_Edge_of_Forbidden_Zone_for_Star_D:
            print("Formation Orbit 14 is in the Forbidden Zone - no protoplanet formed")
            Star_D_Protoplanet_16_Flag = "No"
        if formation_orbit_16_for_Star_D >= Radius_of_Slow_Accretion_Line_for_Star_D:
            print("Formation Orbit 16 is outisde the slow accretion line")
            Star_D_Protoplanet_16_Speed_Flag = "Slow"

# Step 10: Disk Instability
    # "Very early in the process of planetary formation, the first gas giant planets may form due to disk instability in the protoplanetary disk
    # Here, the outer protoplanetary disk is perturbed by the gravitation of nearby stars, or due to the formation of large clumps of material by random chance.
    # The disk then forms spiral-arm structures, which can quickly give rise to unusually massive gas giant planets. Disk instability is more likely to occur if the protoplanetary disk is denser
    # (that is, if its disk mass factor, determined in Step Nine, is high)."

    # "To determine at random whether disk instability took place, roll 3d6 and add the disk mass modifier determined in Step Nine. If the result is 12 or higher, one or more planets may form
    # due to disk instability. Otherwise, skip forward to Step Eleven."

    if Number_of_Stars >= 1:
        Disk_Stability_for_Star_A = "Stable"
        roll_for_Disk_Stability_Star_A = _3d6()        
        if (roll_for_Disk_Density_of_Star_A + Disk_Mass_Modifier_Star_A) >= 12:
            Disk_Stability_for_Star_A = "Unstable"

    if Number_of_Stars >= 2:
        Disk_Stability_for_Star_B = "Stable"
        roll_for_Disk_Stability_Star_B = _3d6()
        if (roll_for_Disk_Density_of_Star_B + Disk_Mass_Modifier_Star_B) >= 12:
            Disk_Stability_for_Star_B = "Unstable"

    if Number_of_Stars >= 3:
        Disk_Stability_for_Star_C = "Stable"
        roll_for_Disk_Stability_Star_C = _3d6()        
        if (roll_for_Disk_Density_of_Star_C + Disk_Mass_Modifier_Star_C) >= 12:
            Disk_Stability_for_Star_C = "Unstable"

    if Number_of_Stars == 4:
        Disk_Stability_for_Star_D = "Stable"
        roll_for_Disk_Stability_Star_D = _3d6()        
        if (roll_for_Disk_Density_of_Star_D + Disk_Mass_Modifier_Star_D) >= 12:
            Disk_Stability_for_Star_D = "Unstable"

    if Disk_Stability_for_Star_A == "Unstable":

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