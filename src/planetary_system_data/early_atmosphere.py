# this sub-program covers step 26 ("Early Atmosphere") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction" 
# starting from page 108

# "This step begins the process of designing the world’s atmosphere, starting with the presence of hydrogen, helium, and nitrogen."

# "In this and later steps, we will use the concept of atmospheric mass. This is equivalent to the mass of a standard-sized column of the atmosphere, stretching 
# from the world’s surface to the margins of space. A world with total atmospheric mass of 1 has an atmosphere whose mass in such a column is equal to that of 
# Earth."

# "We will also refer to the partial atmospheric mass of specific components of the atmosphere. These represent the atmospheric mass due to that specific substance. 
# The sum of all the partial atmospheric masses will, by definition, be equal to the world’s total atmospheric mass."

# "After determining the prevalence of these atmospheric components, we cano classify the world under development into one of six world classes. These overall types 
# will have an impact on several of the remaining steps in the design sequence. The available classes are:"
# "Class 1 (Venus-type): An extremely hot world whose dense atmosphere is dominated by carbon dioxide as the result of a runaway dry greenhouse."
# "Class 2 (Dulcinea-type): A “super-Earth” whose dense atmosphere is dominated by retained primordial hydrogen, possibly also by water vapor after a 
# runaway wet greenhouse. Named after the planet Dulcinea (Mu Arae C), the first such planet to be discovered."
# "Class 3 (Titan-type): A cold world with a substantial atmosphere dominated by nitrogen."
# "Class 4 (Earth-type): A world with moderate temperatures, whose substantial atmosphere is dominated by nitrogen but can have other significant components as 
# well (such as carbon dioxide or free oxygen)."
# "Class 5 (Mars-type): A world with a very thin atmosphere, dominated by carbon dioxide, which is just substantial enough to raise dust storms and other forms of
# weather."
# "Class 6 (Luna-type): A world with no significant atmosphere"

# Procedure

# "Carry out the following steps for the world under consideration."

# Atmosphere Retention Factor

# "Assign an atmosphere retention factor to the world. This is a measure of the world’s ability to generate and retain an atmosphere. A world with more volcanic 
# activity will have a higher atmosphere retention factor, since active vulcanism replenishes the atmosphere. On the other hand, a world with a weak magnetic field 
# will have a lower atmosphere retention factor, because stellar wind will strip the atmosphere away."

# "The atmosphere retention factor is a relative measure. A value of 1 indicates that the world is about as efficient as Earth at generating and retaining its 
# atmosphere."

# "Select an atmosphere retention factor between 0 and 3.0. To generate an atmosphere retention factor at random, roll 3d6 and modify the result as follows:"

# "+6 if the world has Massive prevalence of water or has undergone a runaway greenhouse event (dry or wet)"
# "+6 if the world has a Molten Lithosphere"
# "+4 if the world has a Soft Lithosphere"
# "+2 if the world has an Early Plate Lithosphere"
# "-2 if the world has an Ancient Plate Lithosphere"
# "-4 if the world has a Solid Lithosphere"
# "-2 if the world has a Moderate Magnetic Field"
# "-4 if the world has a Weak Magnetic Field"
# "-6 if the world has no Magnetic Field"

# "Multiply the modified roll by 0.1 and note the result as the atmosphere retention factor."

# Atmospheric Components

# "For each of the following possible volatile compounds, check to see whether the world can retain that volatile as a component of its atmosphere."
# "In each case, there will be a maximum M-number and possibly a minimum blackbody temperature that must hold for that component. If the world’s M-number is too high, 
# that potential component of the atmosphere will undergo EUV-driven or thermal escape in a relatively short time. If the world’s blackbody temperature is too low, 
# that component will tend to “freeze out” and form liquid or solid layers on the surface. Either way, that volatile will not be available to make up a substantial 
# atmosphere."
 
# If all given conditions hold, then the world will have a substantial amount of that component in its atmosphere. Estimate the partial atmospheric mass for that 
# component as described. In each case, vary the partial atmospheric mass by up to 10%."

# Molecular Hydrogen (H2)
# "The world will retain molecular hydrogen if it has atmosphere retention factor greater than 0, and its (corrected) M-number is no greater than 2, no matter what its 
# blackbody temperature. If this is the case, estimate the partial atmospheric mass of molecular hydrogen (MH2) as equal to 7.5 times the atmosphere retention factor. 
# Vary this value by up to 10%, and round it to two significant figures."

# Helium (He)
# "The world will retain helium if it has atmosphere retention factor greater than 0, and its (corrected) M-number is no greater than 4, no matter what its blackbody 
# temperature. If this is the case, estimate the partial atmospheric mass of helium (MHe) as equal to 2.5 times the atmosphere retention factor. Vary this value by up 
# to 10%, and round it to two significant figures.

# Nitrogen (N2)
# "The world will retain molecular nitrogen if it has atmosphere retention factor greater than 0, its M-number is no greater than 28, and its blackbody temperature is 
# at least 80 K. If this is the case, estimate the partial atmospheric mass of molecular nitrogen (MN2) as equal to 0.7 times the atmosphere retention factor."

# "Multiply MN2 by an additional factor of 15 if the world’s blackbody temperature is no greater than 125 K and it has Massive prevalence of water."

# "Vary the final value of MN2 by up to 10%, and round it to two significant figures."

# Assigning a World Class

# "At this point, the world can be assigned one of the six world classes. Check the following cases and assign the world class that best fits."

# "First Case: If the world has undergone a runaway dry greenhouse, it is Class 1 (Venus-type)."

# "Second Case: If the world retains molecular hydrogen, it is Class 2 (Dulcinea-type), whether it has undergone a runaway wet greenhouse or not."

# "Third Case: If all the following conditions hold:"
# "The world does not retain molecular hydrogen,"
# "The world does retain molecular nitrogen, and"
# "The blackbody temperature is between 80 K and 125 K inclusive."
# "Then the world is Class 3 (Titan-type)."

# "Fourth Case: If all the following conditions hold:"
# "The world does not retain molecular hydrogen,"
# "The world does retain molecular nitrogen, and"
# "The blackbody temperature is greater than 125 K."
# "Then the world is Class 4 (Earth-type)."

# "Fifth Case: If all the following conditions hold:"
# "The world does not retain molecular hydrogen, helium, or molecular nitrogen,"
# "The M-number is 44 or less, and"
# "The blackbody temperature is greater than 195 K."
# "Then the world is Class 5 (Mars-type)."
# "A world with atmosphere retention factor of 0 can be Class 5 (it may still be capable of retaining a very thin carbon-dioxide atmosphere). Mars itself
# is an example of this case."

# "Sixth Case: If the world cannot be placed in any of world classes 1 through 5, then it is Class 6 (Luna-type)"