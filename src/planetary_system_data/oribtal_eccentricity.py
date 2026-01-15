# this sub-program covers step 15 ("Orbital Eccentricity") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction" 
# starting on page 79

# "The above procedures will generate a stack of planetary orbits which are likely to be stable if all of them are perfectly circular. However, few planets follow such 
# carefully arranged orbital paths. This step assigns eccentricity values to the planetary orbits, in such a way that the whole ensemble remains stable"

# "Recent research seems to indicate that the eccentricity of planetary orbits is strongly correlated with the number of planets in a system. Even if planetary orbits are 
# not tightly stacked, if there are more planets then all of them are likely to have lower eccentricity. We will take advantage of this apparent correlation to assign stable 
# values to eccentricity"

# "Procedure - To begin, count the number of surviving planets in the system (Planetoid Belts do not count) and refer to the System Eccentricity Table"

# Codify the System Ecentricity Table on pg 79

# "Starting with the innermost planet and working outward, select an eccentricity for each planet’s orbit. Planetoid belts will have orbital eccentricity of 0. Planetary 
# orbits will be close to the Typical Eccentricity value from the table for the total number of planets in the system. To determine a value for eccentricity at random, 
# roll 2d6-7, multiply by 0.01, and add the result to the Typical Eccentricity value (minimum 0)"

# "Once the eccentricity of a planet’s orbit has been established, the planet’s minimum distance and maximum distance from the primary star can be computed:"

# Codify the Equations for R(min) and R(max) on pg 79

# "Rmin is the minimum distance, and Rmax is the maximum distance, both in AU. R is the planet’s orbital radius in AU and E is the eccentricity of its orbit."

# "If a planet’s minimum distance gets closer to its primary star than the inner edge of the protoplanetary disk, this is acceptable. If its maximum distance moves out into 
# a forbidden zone, this is not a stable  situation; reduce the planet’s eccentricity to ensure that this does not occur"

# "As a final check, examine the minimum and maximum distance for each pair of adjacent planetary orbits, and apply the following two rules:"
# "Rule 1 - No planet’s minimum distance should be less than the one for the next planet inward"
# "Rule 2 -  No planet’s maximum distance should be greater than the one for the next planet outward"

# "The one exception is that the outermost planet’s minimum distance may violate this rule, implying that its orbit must be significantly inclined from the plane occupied 
# by the rest of the planetary system. Otherwise, adjust any values of eccentricity necessary to prevent violations of the rule."

# "Selecting for an Earthlike world: Human-habitable worlds are not likely to have high orbital eccentricity, although a moderate value (no greater than 0.2) is compatible 
# with Earthlike conditions."