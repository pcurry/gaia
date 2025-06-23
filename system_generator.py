# script to procedurally generate realistic (but fictional) star systems using outputs from sector_querry.py
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

# Step 1: Primary Star Mass
# Step 2: Stellar Multiplicity
# Step 3: Arrange Components
# Step 4: Star System Age

# Roll (d100) / Population / Base Age / Age Range
# 01-42 / Young Population I / 0.0 / 2.0
# 43-76 / Intermediate Population I / 2.0 / 3.0
# 77-95 / Old Population I / 5.0 / 3.0
# 96-99 / Disk Population II / 8.0 / 1.5
# 00 / Halo Population II / 9.5 / 3.0
random_integer = random.randint(1, 100)
if 1 <= random_integer <= 42, then Population="Young Population I"
if 43 <= random_integer <= 76, then Population="Intermediate Population"
if 77 <= random_integer <= 95, then Population="Old Population I"
if 96 <= random_integer <= 99, then Population="Disk Population II"
if 100 = random_integer, then Populattion="Halo Population II"

# Step 5: Star System Metallicity
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