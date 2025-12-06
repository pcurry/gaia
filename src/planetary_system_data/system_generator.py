# this is a python script to procedurally generate realistic (but fictional) star systems
# primary reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

# will need to build in option to input real parameter values from stars in Gaia DR3 dataset - e.g. in similar manner to what has been done in Sectory_Query.py
# or... take sectors that have been created by Sector_Query.py and generate matching system/planet data for the star systems in that sector

# will also need to develop known_exoplanet.py module to handle cases where exoplanets have been detected / real exoplanet data can be ingested (pg. 176-178)
# e.g. in these cases there will be both IRL known exoplanets in the system + fair to assume that there are other undetected exoplanets for which fictional but realistic stand-ins can be created here

# Step 1: Primary Star Mass

from primary_star_mass import generate_primary_star
Star_A = generate_primary_star()
Mass_A = Star_A.mass
print(f"Mass of Star A: {Star_A.mass} solar masses")

# Step 2: Stellar Multiplicity

from stellar_multiplicity import generate_number_of_stars
Number_of_Stars = generate_number_of_stars(Star_A.mass)
print(f"Number of Stars in System: {Number_of_Stars}")

# Step 3: Arrange Components

from arrange_components import Stellar_Arrangement
print(f"Stellar Arranagement: {Stellar_Arrangement}")

# Step 4: Star System Age

from star_system_age import Population
from star_system_age import system_age

print(f"Stellar Population: {Population}")
system_age = round(system_age, 2)
print(f"System Age: {system_age} Gyr")

# Step 5: Star System Metallicity

from star_system_age import Metallicity

Metallicity = round(Metallicity, 2)
print(f"Metallicity: {Metallicity}")

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

# run planet_generator.py for each planet created by the steps above