import random

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# next step: optional conectivity to Sector_Query.py (e.g. input real parameter values from stars in Gaia DR3 dataset)

# Step 1: Primary Star Mass

Category = None
Mass = None

random_integer = random.randint(1,100)

if 1 <= random_integer <= 3: 
    Category = "Brown Dwarf"
    random_integer = random.randint(1,100)
    if 1 <= random_integer <= 10: 
        Mass = 0.015
    elif 11 <= random_integer <= 29:
        Mass = 0.02
    elif 30 <= random_integer <= 45:
        Mass = 0.03
    elif 46 <= random_integer <= 60:
        Mass = 0.04
    elif 61 <= random_integer <= 74:
        Mass = 0.05
    elif 75 <= random_integer <= 87:
        Mass = 0.06
    elif 88 <= random_integer <= 100:
        Mass = 0.07
elif 4 <= random_integer <=77:
    Category = "Low Mass Star"
    random_integer = random.randint(1,100)
    if 1 <= random_integer <= 13:
        Mass = 0.08
    elif 14 <= random_integer <= 23:
        Mass = 0.10
    elif 24 <= random_integer <= 34:
        Mass = 0.12
    elif 35 <= random_integer <= 43:
        Mass = 0.15
    elif 44 <= random_integer <= 52:
        Mass = 0.18
    elif 53 <= random_integer <= 59:
        Mass = 0.22
    elif 60 <= random_integer <= 65:
        Mass = 0.26
    elif 66 <= random_integer <= 70:
        Mass = 0.30
    elif 71 <= random_integer <= 74:
        Mass = 0.34
    elif 75 <= random_integer <= 77:
        Mass = 0.38
    elif 78 <= random_integer <= 80:
        Mass = 0.42
    elif 81 <= random_integer <= 83:
        Mass = 0.46
    elif 84 <= random_integer <= 86:
        Mass = 0.50
    elif 87 <= random_integer <= 89:
        Mass = 0.53
    elif 90 <= random_integer <= 92:
        Mass = 0.56
    elif 93 <= random_integer <= 95:
        Mass = 0.59
    elif 96 <= random_integer <= 97:
        Mass = 0.62
    elif 98 <= random_integer <= 99:
        Mass = 0.65
    elif 100 == random_integer:
        Mass = 0.68
elif 78 <= random_integer <=90:
    Category = "Intermediate Mass Star"
    random_integer = random.randint(1,100)
    if 1 <= random_integer <= 7:
        Mass = 0.70
    elif 8 <= random_integer <= 13:
        Mass = 0.72
    elif 14 <= random_integer <= 19:
        Mass = 0.74
    elif 20 <= random_integer <= 24:
        Mass = 0.76
    elif 25 <= random_integer <= 29:
        Mass = 0.78
    elif 30 <= random_integer <= 34:
        Mass = 0.80
    elif 35 <= random_integer <= 39:
        Mass = 0.82
    elif 40 <= random_integer <= 43:
        Mass = 0.84
    elif 44 <= random_integer <= 47:
        Mass = 0.86
    elif 48 <= random_integer <= 51:
        Mass = 0.88
    elif 52 <= random_integer <= 55:
        Mass = 0.90
    elif 56 <= random_integer <= 59:
        Mass = 0.92
    elif 60 <= random_integer <= 62:
        Mass = 0.94
    elif 63 <= random_integer <= 65:
        Mass = 0.96
    elif 66 <= random_integer <= 68:
        Mass = 0.98
    elif 69 <= random_integer <= 71:
        Mass = 1.00
    elif 72 <= random_integer <= 74:
        Mass = 1.02
    elif 75 <= random_integer <= 78:
        Mass = 1.04
    elif 79 <= random_integer <= 82:
        Mass = 1.07
    elif 83 <= random_integer <= 85:
        Mass = 1.10
    elif 86 <= random_integer <= 89:
        Mass = 1.13
    elif 90 <= random_integer <= 92:
        Mass = 1.16
    elif 93 <= random_integer <= 95:
        Mass = 1.19
    elif 96 <= random_integer <= 97:
        Mass = 1.22
    elif 98 <= random_integer <= 100:
        Mass = 1.25
elif 91 <= random_integer <=100:
    Category = "High Mass Star"
    random_integer = random.randint(1,100)
    if 1 <= random_integer <= 3:
        Mass = 1.28
    elif 4 <= random_integer <= 6:
        Mass = 1.31
    elif 7 <= random_integer <= 9:
        Mass = 1.34
    elif 10 <= random_integer <= 12:
        Mass = 1.37
    elif 13 <= random_integer <= 16:
        Mass = 1.40
    elif 17 <= random_integer <= 19:
        Mass = 1.44
    elif 20 <= random_integer <= 23:
        Mass = 1.48
    elif 24 <= random_integer <= 27:
        Mass = 1.53
    elif 28 <= random_integer <= 31:
        Mass = 1.58
    elif 32 <= random_integer <= 35:
        Mass = 1.64
    elif 36 <= random_integer <= 38:
        Mass = 1.70
    elif 39 <= random_integer <= 41:
        Mass = 1.76
    elif 42 <= random_integer <= 45:
        Mass = 1.82
    elif 46 <= random_integer <= 49:
        Mass = 1.90
    elif 50 <= random_integer <= 53:
        Mass = 2.00
    elif 54 <= random_integer <= 56:
        Mass = 2.10
    elif 57 <= random_integer <= 59:
        Mass = 2.20
    elif 60 <= random_integer <= 62:
        Mass = 2.30
    elif 63 <= random_integer <= 67:
        Mass = 2.40
    elif 68 <= random_integer <= 71:
        Mass = 2.60
    elif 72 <= random_integer <= 75:
        Mass = 2.80
    elif 76 <= random_integer <= 78:
        Mass = 3.00
    elif 79 <= random_integer <= 82:
        Mass = 3.20
    elif 83 <= random_integer <= 87:
        Mass = 3.50
    elif 88 <= random_integer <= 91:
        Mass = 4.00
    elif 92 <= random_integer <= 94:
        Mass = 4.50
    elif 95 <= random_integer <= 96:
        Mass = 5.00
    elif 97 <= random_integer <= 98:
        Mass = 5.50
    elif 99 <= random_integer <= 100:
        Mass = 6.00
print(f"Star Type: {Category}")
print(f"Mass: {Mass} solar masses")

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