import random
import math

# script to procedurally generate realistic (but fictional) star systems
# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# input user query - option to input real parameter values from stars in Gaia DR3 dataset - e.g. connect with Sectory_Query.py

# run different pathway if star system known exoplanets (or planets, e.g. the solar system)
# e.g. will have to create separate code to handle systems with mix of known exoplanets and interpolating additional fictional exoplanets

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

# Step 9: Protoplanetary Disk
# run protoplanetary_disk.py here

# Step 10: Disk Instability
# run disk_instability.py here

# Step 11: Core Accretion
# run core_accretion.py here

# Step 12: Oligarchic Collision
# run oligarchic_collison.py here
# input Step 12 elements - starting from pg. 67

# run planet_generator.py for each planet created by the steps above