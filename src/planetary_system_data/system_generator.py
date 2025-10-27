import random
import math

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# input user query - option to input real parameter values from stars in Gaia DR3 dataset - e.g. connect with Sectory_Query.py

# define dice rolling functions
def d100() -> int:
  return random.randint(1, 100)
def _3d6() -> int:
  return (random.randint(1, 6) + random.randint (1, 6) + random.randint (1, 6))
def _2d6() -> int:
  return (random.randint(1, 6) + random.randint (1, 6))

# Step 1: Primary Star Mass
# run primary_star_mass.py
# only run if don't have star mass (or spectral type) from Gaia / SIMBAD
# reverse engineer mass from spectral type (if available from Gaia / SIMBAD)

# Step 2: Stellar Multiplicity
# run stellar_multiplcity.py
# only run if don't have number of stars in system from Gaia / SIMBAD

# Step 3: Arrange Components
# run arrange_components.py

# Step 4: Star System Age
# only run if don't have star system age from SIMBAD
# run star_system_age.py

# Step 5: Star System Metallicity
# run star_system_metallicity.py
# only run if don't have metallicity from Gaia / SIMBAD

# Step 6: Stellar Evolution
# run stellar_evolution.py

# Step 7: Stellar Classification
# run stellar_classification.py

# Step 8: Stellar Orbital Parameters
# run stellar_orbital_parameters.py

# skip all following steps if known exoplanets (will have to create separate code to handle systems with mix of known exoplanets and interpolating additional fictional exoplanets)

# Step 9: Protoplanetary Disk
# run protoplanetary_disk.py here

# Step 10: Disk Instability
# run disk_instability.py here

# Step 11: Core Accretion
# run core_accretion.py here

# Step 12: Oligarchic Collision
# run oligarchic_collison.py here
# input Step 12 elements - starting from pg. 67

# Step 13: Planetary Orbital Radii
# run planetary_orbital_radii.py here
# input Step 13 elements - starting from pg. 69

# Step 14: Planetary Mass
# run planetary_mass.py here
# input Step 14 elements - starting from pg. 75

# Step 15: Orbital Eccentricity
# run orbtal_eccrenricity.py here
# input Step 15 elements - starting from pg. 79

# Step 16: Physical Parameters
# run physical_parameters.py here
# input Step 16 elements - starting from pg. 81

# Step 17: Natural Satellites
# run natural_satellites.py here
# input Step 17 elements - starting from pg. 83

# Step 18: Orbital Period
# run orbital_period.py here
# input Step 18 elements - starting from pg. 89

# Step 19: Rotation Period
# run rotation_period.py here
# input Step 19 elements - starting from page 90

# Step 20: Obliquity
# run obliquity.py here
# input Step 20 elements - starting from page 93

# Step 21: Local Calendar
# run local_calendar.py here
# input Step 21 elements - starting from page 95

# Step 22: Blackbody Temperature
# run blackobdy_temperature.py here
# input Step 22 elements - starting from page 96

# Step 23: Water
# run water.py here
# input Step 23 elements - starting from page 98

# Step 24: Geophysics
# run geophysics.py here
# input Step 24 elements - starting from page 101

# Step 25: Magnetic Field
# run magnetic_field.py here
# input Step 25 elements - starting from page 107

# Step 26: Early Atmosphere
# run early_atmosphere.py here
# input Step 26 elements - starting from page 108

# Step 27: Albedo
# run albedo.py here
# input Step 27 elements - starting from page 111

# Step 28: Carbon Dioxide
# run carbon_dioxide.py here
# input Step 28 elements - starting from page 112

# Step 29: Presence of Life
# run life.py here
# input Step 29 elements - starting from page 114

# Step 30: Average Surface Temperature
# run surface_temperature.py here
# input Step 30 elements - starting from page 119

# Step 31: Finalize Atmosphere
# run atmosphere.py here
# input Step 31 elements - starting from page 124