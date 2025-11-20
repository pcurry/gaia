# this sub-program covers step 30 ("Average Surface Temperature") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# starting from page 119

# "In this step, we finish estimating the prevalence of various gases in the atmosphere, possibly adjusting the prevalence of carbon dioxide. This will finally lead us 
# to an estimate for the average surface temperature for the world, taking all relevant factors into account."

# "The procedure below is more detailed (and most accurate) for Class 3 through Class 6 worlds, and especially for Class 4 worlds. These are the worlds human visitors 
# are most likely to want to land on and explore. The estimates for surface temperature for Class 1 and Class 2 worlds are designed to be plausible but not precise."

# Procedure

# "Computation of the world’s average surface temperature is somewhat complex and will require several special cases."

# Class 1 (Venus-Type) Worlds

# "To estimate the average surface temperature for a Class 1 world, evaluate the following:"

# Codify Equation on page 119

# "B is the world’s blackbody temperature in kelvins, A is its albedo, MCO2 is the partial atmospheric mass of carbon dioxide as determined in Step Twenty-Seven, 
# and T is the world’s average surface temperature in kelvins. Round T to two significant figures, make a note of the result, and skip ahead to Step Thirty-One"

# Class 2 (Dulcinea-Type) Worlds

# "To estimate the average surface temperature for a Class 2 world, evaluate the following:"

# Codify Equation on page 119

# "B is the world’s blackbody temperature in kelvins, A is its albedo, and MH2 is the partial atmospheric mass of molecular hydrogen as determined in Step Twenty-Seven. 
# K is a constant equal to 180 if no runaway wet greenhouse has taken place, or 500 if one has. T is the world’s resulting average surface temperature in kelvins. Round 
# T to two significant figures, make a note of the result, and skip ahead to Step Thirty-One"

# Class 6 (Luna-Type) Worlds

# "To estimate the average surface temperature for a Class 6 world, evaluate the following:"

# Codify Equation on page 119

# "B is the world's blackbody temperature in kelvins, A is the albedo, and T is the world’s average surface temperature in kelvins. Round T to the nearest kelvin, make 
# a note of the result, and skip ahead to Step Thirty-One"

# Estimate Base Surface Temperature

# "In all other cases, evaluate the base surface temperature as follows:"

# Codify Equation

# "B is the world's blackbody temperature in kelvins, A is the albedo, and T0 is the world’s average surface temperature in kelvins, assuming no greenhouse effect. 
# Round T0 to the nearest kelvin and make a note of the result."

# Methane (CH4)

# "A world’s atmosphere may contain methane (CH4) in trace amounts, if its M-number is no greater than 16 and its blackbody temperature is at least 110 K. If these 
# conditions hold, the world will possess methane if either of the following is true:"
# "The world is Class 3, or"
# "The world is Class 4 and has undergone abiogenesis, either in deep hydrothermal vents or in surface refugia"

# "If methane is not present, set GCH4 equal to 0 and skip ahead to the next sub-step. Methane is a very effective greenhouse gas, so even traces of it can cause 
# measurable warming. To estimate the greenhouse effect caused by methane, evaluate the following:"

# Codify Equation on page 120

# "GCH4 is the greenhouse effect due to methane in kelvins, and R is the atmospheric retention factor. Round GCH4 down to the next kelvin (minimum 0)."

# Ozone (O3)

# "A world’s atmosphere will contain ozone (O3) in trace amounts if it has significant free oxygen. Ozone is formed in the upper atmosphere when molecular oxygen (O2) 
# is exposed to the primary star’s ultraviolet radiation. Ironically, the “ozone layer” then blocks much of that ultraviolet from reaching the world’s surface. The 
# presence of an ozone layer may be a requirement before multicellular life can safely colonize exposed land."

# "A world’s atmosphere will contain ozone if and only if it has undergone an Oxygen Catastrophe. If ozone is not present, set GO3 equal to 0 and skip ahead to the next 
# sub-step."

# "Ozone is an effective greenhouse gas, so even traces of it can cause measurable warming. To estimate the greenhouse effect caused by ozone, evaluate the following:"

# Codify Equation on page 120

# "GO3 is the greenhouse effect due to ozone in kelvins, and R is the atmospheric retention factor. Round GO3 down to the next kelvin (minimum 0)"

# Update Base Surface Temperature

# "At this point, update the estimated average surface temperature to account for any greenhousebwarming due to methane and ozone:"

# Codify Equation on page 121

# "Make a note of T1 and continue to the next sub-step."

# Adjust Level of Carbon Dioxide

# "If the world does not have an active carbonate-silicate cycle, skip ahead to the next sub-step. Otherwise, some (perhaps most) of the carbon dioxide allocated in 
# Step Twenty-Eight will have been drawn out of the atmosphere."

# "To estimate the greenhouse effect due to the remaining carbon dioxide, evaluate the following:"

# Codify Equation on page 121

# "T1 is the surface temperature without accounting for carbon dioxide, as computed just above, and C is the amount of greenhouse effect (in kelvins) necessary to 
# maintain the carbonate-silicate cycle over long periods. Carbon dioxide in the atmosphere will fluctuate over time, but remain close to this level.

# "To estimate GCO2, the greenhouse effect due to carbon dioxide, set it equal to C or to 8 K, whichever is greater. Then add the result of 2d6-7 to get its current 
# value. On most Class 4 worlds, GCO2 will range from 3 K (indicating about 75 parts per million) upward."

# "Estimate the revised partial atmospheric mass of carbon dioxide by evaluating the following:"

# Codify Equation on page 121

# "GCO2 is the greenhouse effect computed above, and MCO2 is the revised partial atmospheric mass of carbon dioxide. Round MCO2 to two significant figures and make a 
# note of it before moving on to the next sub-step."

# "Update Base Surface Temperature"

# "At this point, update the estimated average surface temperature to consider any greenhouse warming due to carbon dioxide. If GCO2 was not computed in the previous 
# sub-step (because there is no active carbonate-silicate cycle), compute it now:"

# Codify Equation on page 121

# "MCO2 is the partial atmospheric mass of carbon dioxide as determined in Step Twenty-Eight, and GCO2 is the greenhouse effect due to carbon dioxide. Round GCO2 to the 
# nearest kelvin."

# "In either case, compute the updated surface temperature as follows:"

# Codify Equation on page 121

# "T2 is the surface temperature after accounting for carbon dioxide, but not water vapor."

# "It’s possible for T2 to be less than 260 K, even if the world has an active-carbonate-silicate cycle. This suggests a world currently in a “snowball” era, with 
# extensive glaciation, due to a recent lack of carbon dioxide causing a temporary interruption in the carbonate-silicate cycle. Worlds in this state are accumulating 
# carbon dioxide in the atmosphere, leading to warming and resumption of the normal cycle. Earth appears to have gone through at least two such periods in its distant 
# past."

# Water Vapor (H2O)

# "Water vapor is an effective greenhouse gas, and may have a profound effect on a world’s climate. The presence of liquid water on a world’s surface may depend on other 
# greenhouse gases, but once it appears, the water vapor it gives off will further amplify the greenhouse effect."

# "Indeed, the effect of water vapor on the greenhouse effect is non-linear: its presence drives up temperatures, but warmer air retains more water vapor, which causes 
# still more warming. This is the process that leads to a runaway greenhouse on Class 1 worlds. Even short of that, water vapor tends to be the strongest contributor to 
# the greenhouse on many worlds."

# "A world’s atmosphere may contain significant amounts of water vapor if its M-number is no greater than 18, its blackbody temperature is at least 260 K, and it has 
# Moderate, Extensive, or Massive prevalence of water. If these conditions do not hold, set GH2O equal to 0 and skip ahead to the next sub-step."

# "Otherwise, to determine GH2O, the greenhouse effect due to water vapor, refer to the Water Vapor Greenhouse Table. Use the row for the value of T2 as computed above 
# to get the base value for GH2O. Then evaluate:"

# Codify Equation on page 122

# "H is the world's hydrographic coverage, as determined in Step Twenty-Three and expressed as a number between 0 and 1. K is an adjustment (in kelvins) to be added
# to the base value of GH2O to determine its final value. In effect, a world with more hydrographic coverage will have more water vapor in its atmosphere and therefore 
# more greenhouse effect."

# "Estimate the partial atmospheric mass of water vapor by evaluating the following:"

# Codify Equation on page 122

# "MH2O is the partial atmospheric mass of water vapor, and GH2O is the greenhouse effect due to water vapor computed above. Round MH2O to two significant figures and 
# make a note of it before moving on to the final sub-step."

# Final Average Surface Temperature

# "At this point, we can complete our estimation of the average surface temperature by considering any greenhouse warming due to water vapor:"

# Codify Equation on page 122

# T is the world’s average surface temperature in kelvins.