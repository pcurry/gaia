import random

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# next step: optional conectivity to Sector_Query.py (e.g. input real parameter values from stars in Gaia DR3 dataset)

# Step 1: Primary Star Mass

Category = None

random_integer = random.randint(1,100)

if 1 <= random_integer <= 3: 
    Category = "Brown Dwarf"
    #input routine for calculating mass of this category of stars
elif 4 <= random_integer <=77:
    Category = "Low Mass Star"
    #input routine for calculating mass of this category of stars
elif 78 <= random_integer <=90:
    Category = "Intermediate Mass Star"
    #input routine for calculating mass of this category of stars
elif 91 <= random_integer <=100:
    Category = "High Mass Star"
    #input routine for calculating mass of this category of stars
print(f"Star Type: {Category}")

# Step 2: Stellar Multiplicity
# Step 3: Arrange Components
# Step 4: Star System Age

Population = None
base_age = None
age_range = None
random_integer = random.randint(1, 100)

if 1 <= random_integer <= 42: 
    Population = "Young Population I"
    Base_Age = 0.0
    Age_Range = 2.0
elif 43 <= random_integer <= 76: 
    Population = "Intermediate Population"
    Base_Age = 2.0
    Age_Range = 1.0
elif 77 <= random_integer <= 95: 
    Population = "Old Population I"
    Base_Age = 5.0
    Age_Range= 3.0
elif 96 <= random_integer <= 99: 
    Population = "Disk Population II"
    Base_Age = 8.0
    Age_Range = 1.5
elif 100 == random_integer: 
    Population = "Halo Population II"
    Base_Age = 9.5
    Age_Range = 3.0

random_integer = random.randint(1, 100)
star_age = Base_Age + (Age_Range*(random_integer/100))

print(f"Stellar Population: {Population}")
print(f"Star Age: {star_age} Gyr")

# Step 5: Star System Metallicity

# currently only randomly generated metallicity - will need to tweak to use Gaia estimate or values from SIMBAD (if available)
Metallicity = None
random_integer3 = random.randint(3, 18)
Metallicity = (random_integer3 / 10)*(1.2-(star_age/13.5))

if Population == "Halo Population II":
    Metallicity = (Metallacity - 0.2)

if Metallicity < 0:
    Metallicity = 0

print(f"Metallicity: {Metallicity}")

# Step 6: Stellar Evolution



# Step 7: Stellar Classification
# Step 8: Stellar Orbital Parameters
# Step 9: Protoplanetary Disk
# Step 10: Disk Instability
# Step 11: Core Accretion
# Step 12: Oligarchic Collision
# Step 13: Planetary Orbital Radii
# Step 14: Planetary Mass
# Step 15: Orbital Eccentricity
# Step 16: Physical Parameters
# Step 17: Natural Satellites
# Step 18: Orbital Period
# Step 19: Rotation Period
# Step 20: Obliquity
# Step 21: Local Calendar
# Step 22: Blackbody Temperature
# Step 23: Water
# Step 24: Geophysics
# Step 25: Magnetic Field
# Step 26: Early Atmosphere
# Step 27: Albedo
# Step 28: Carbon Dioxide
# Step 29: Presence of Life
# Step 30: Average Surface Temperature
# Step 31: Finalize Atmosphere