# this sub-program covers step 19 ("Rotation Period") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"
# starting from page 90

# "The next three steps in the sequence all have to do with planetary rotation. Every object in the cosmos appears to rotate, and in fact some objects 
# appear to “tumble” by rotating around a changing axis."

# "Planets and their major satellites usually have simple rotation, spinning in the same direction as their orbital motion, around an axis that is 
# approximately perpendicular to the plane of their orbital motion. There are, of course, a variety of exceptions to this general rule."

# "This step determines the rotation period of a given world. In this case, we will be dealing with what’s called the sidereal period of rotation—the 
# time it takes for a world to rotate once with respect to the distant stars."

# "Worlds appear to form with wildly varying rotation periods, the legacy of the chaotic processes of planetary formation. However, many worlds will have 
# been affected by tidal deceleration applied by the gravitational influence of nearby objects. Tidal deceleration may cause a world to be captured into a 
# special status called a spin-orbital resonance, in which the world’s orbital period and its rotational period form a small-integer ratio."

# "One special case of a spin-orbital resonance is the case where the resonance is 1:1 (that is, the orbital period and rotational period are exactly equal). 
# This case is sometimes called tide-locking"

# Procedure

# "A world will fall into one of three categories: a major satellite of a planet, a planet with its own major satellite, or a planet without major satellites"

# "First Case: Major Satellites of Planets"

# "Major satellites of planets, as placed in Step Seventeen, will almost invariably be in a spin-orbital resonance state. Most models of the formation of such 
# satellites suggest that they are captured into such a state almost immediately after their formation."

# "Since a major satellite’s orbit normally has very small eccentricity, the spin-orbital resonance will be 1:1 (that is, it will be tide-locked). The satellite’s 
# rotation period will be exactly equal to its orbital period."

# "Second Case: Planets with Major Satellites"

# "A leftover oligarch, terrestrial planet, or failed core which has a major satellite may be captured into a spin resonance with the satellite’s orbit. This is 
# somewhat unlikely unless the system is very old. For example, Earth is not likely to become tide-locked to its own moon within the lifetime of the sun. However, 
# a satellite’s tidal effects on the primary planet will tend to slow its rotation rate.

# "To estimate the probability that a planet has become tide-locked to its satellite, and to estimate its rotation rate if this is not the case, begin by evaluating 
# the following:"

# Codify Equation on page 91

# "A is the age of the star system in billions of years. MS and MP are the mass of the satellite and the planet, respectively, in Earth-masses. R is the radius of the 
# planet, and D is the radius of the satellite’s orbit, both in kilometers."

# "If T is equal to or greater than 2, the planet is almost certainly tide-locked to its satellite. Its rotation period will be exactly equal to the
# orbital period of the satellite."

# "Otherwise, to generate a rotation period for the planet at random, multiply T by 12, round the result to the nearest integer, add the result to a roll of 3d6, and 
# refer to the Rotation Period Table."

# Codify the Rotiaon Period Table on page 91

# "The planet will be tide-locked to its satellite on a result of 24 or higher, or in any case where the randomly generated rotation rate is longer than the satellite’s 
# orbital period. In these cases, again, its rotation period will be exactly equal to the orbital period of the satellite."

# "If the plamet is not tide-locked to its satellite, feel free to adjust the rotation period to any value between the next lower and next higher rows on the table."

# "Third Case: Planets Without Major Satellites"

# "A leftover oligarch, terrestrial planet, or failed core which has no major satellite may be captured into a spin-orbital resonance with respect to its primary star. 
# Even if this does not occur, solar tides will tend to slow the planet’s rotation rate."

# "To estimate the probability that such a planet has been captured into a spin-orbital resonance, and to estimate its rotation rate if this is not the case, 
# begin by evaluating the following:"

# Codify Equation on page 91

# "A is the age of the star system in billions of years, MS is the mass of the primary star in solar masses, MP is the mass of the planet in Earth-masses, 
# R is the radius of the planet in kilometers, and D is the radius of the planet’s orbit in AU."

# "Again, if T is equal to or greater than 2, the planet has almost certainly been captured in a spin-orbital resonance. Otherwise, to generate a rotation period for 
# the planet at random, multiply T by 12, round the result to the nearest integer, add the result to a roll of 3d6, and refer to the Rotation Period Table. The planet 
# will be in a spin-orbital resonance on a result of 24 or higher, or in any case where the randomly generated rotation rate is longer than the planet’s orbital
# period."

# "Planets captured into a spin-orbital resonance are not necessarily tide-locked to their primary star (in other words, the resonance is not necessarily 1:1). 
# Tidal deceleration tends to match a planet’s rotation rate to its rate of revolution during its periastron passage. If the planet’s orbit is eccentric, this match 
# may be approximated more closely by a different resonance. To determine the most likely resonance, refer to the Planetary Spin-Orbit Resonance Table."

# Codify the Planetary Spin-Orbit Resonance Table on page 92

# "On this table, the “most probable resonance” is the status that the planet is most likely to be captured into over a long period of time. It’s possible for 
# a planet to be captured into a higher resonance (that is, a resonance from a lower line on the table) but this situation is unlikely to be stable over billions 
# of years."