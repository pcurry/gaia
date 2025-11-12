# this sub-program covers step 22 ("Blackbody Temperature") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction" starting from page 96

# "The blackbody temperature of a world is the average surface temperature it would have if it were an ideal blackbody, a perfect absorber and radiator of heat. Real planets are not
# ideal blackbodies, so their surface temperatures will vary from this ideal, but the blackbody temperature is a useful tool for determining a variety of other surface conditions."

# "In particular, the blackbody temperature helps to determine what atmospheric gases the world can retain over billion-year timescales. We need to compare the average velocity of a gas of
# given molecular weight at a specific average temperature, and the escape velocity for a given planetary body. In effect, if the average molecular velocity is not significantly less than escape
# velocity, that gas is likely to escape from the planet’s atmosphere on a time-scale of tens to hundreds of thousands of years. Such thermal escape is also called Jeans escape."

# "The simple Jeans-escape model is not adequate for some cases. In particular, non-gas-giant worlds that nonetheless possess thick atmospheres dominated by light gases (hydrogen and
# helium) are likely to lose some or all of that envelope to a related mechanism. High-energy radiation from the primary star, notably extreme ultraviolet (EUV) light and stellar wind, will
# heat gases in the outer shell of the atmosphere. This EUV-driven escape can drive off such light gases even if the planet’s surface temperature is relatively low."

# "This step computes the blackbody temperature and the M-number for the world under development. The M-number is equal to a minimum molecular weight that can be retained against thermal escape over 
# long timescales. We will also apply a correction to the M-number in cases where it is low (4 or less) to account for EUV-driven escape"

# Procedure

# "To determine the blackbody temperature for a world, evaluate the following:"

# Codify equation at bottom on page 96

# "T is the blackbody temperature in kelvins, L is the current luminosity of the primary star in solar units, and R is the orbital radius of a planet (or the planet that a satellite orbits) in AU.
# Blackbody temperature will be the same for a planet and all its satellites. Round the blackbody temperature to the nearest kelvin"

# "In the (very rare) case in which a world’s blackbody temperature is greater than 3,000 K, eliminate that planet from the planetary system. At these temperatures, rock itself vaporizes
# and the world will be destroyed by stellar heat"

# "To estimate the M-number for a world, evaluate the following:"

# Codify the equation on page 97

# "M is the M-number and T is the blackbody temperature. K is the world’s density compared to Earth, and R is the world’s radius in kilometers, both as determined in Steps Sixteen or
# Seventeen"

# "If the M-number as computed above is greater than 1 but no greater than 4, and the world’s primary star is not a brown dwarf, then set the M-number to be equal to exactly 5. This
# represents cases in which EUV-driven escape has stripped away the world’s primordial hydrogen atmosphere."

# "Otherwise round the result up to the next integer."