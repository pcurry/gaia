# this sub-program covers step 17 ("Natural Satellites") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction" - starting from pg. 83

# "This step determines the number and placement of major satellites. We define a major satellite as a natural satellite which is large enough to have formed a sphere under its own gravitation.
# A major satellite will be at least 200 kilometers in radius if it is mostly made of ice, or at least 300 kilometers in radius if it is mostly stone."

# "In general, the rocky planets close to a star are unlikely to form major satellites during the process of planetary accretion. A terrestrial planet which suffers a specific kind of massive
# impact event may form one major satellite, as the planetary material scattered into orbit coalesces. Gas giant planets are likely to have several major satellites. For example, planets
# with major satellites in our own system include Earth (1), Jupiter (4), Saturn (7), Uranus (5), and Neptune (1)."

# " Many planets will also have moonlets, much smaller satellites that are often irregular in shape. Some moonlets may be remnants of the process of planetary formation. Others are likely to
# be captured asteroids or comets. Even small objects may have moonlets of their own. In our system, the planet Mars has two moonlets, and many asteroids and Kuiper Belt objects have been found 
# to have moonlets of their own. A gas giant planet will often have dozens or even hundreds of moonlets in a wide variety of orbits."

# Procedure

# "To determine the number and arrangement of natural satellites for a given planet, begin by computing the planet’s Hill radius. This is the distance from the planet within which its
# gravitation dominates over that of the primary star. The Hill radius defines the region of space where a satellite is likely to form or be captured, and where it can maintain a stable orbit
# around the planet for long periods of time"

# "Compute the planet’s Hill radius using:"

# Codify equation on page 84

# "H is the Hill radius in kilometers, R<sub>min</sub> is the minimum distance from the planet to the primary star (in AUs), M<sub>P</sub> is the mass of the planet (in Earth-masses), and M<sub>S</sub> is 
# the mass of the primary star (in solar masses). Round off to three significant figures."

# First Case: Satellites Forming via Natural Accretion

# "To estimate how many major satellites will form with the planet, as part of the original accretion process, evaluate the following formula:"

# Codify Equation on Page 84

# "H is the Hill radius in kilometers, and R is the average distance from the planet to its primary star in AU. Round N down to the next integer. If the result is greater than 0, then the planet
# will have one or more major satellites that formed with the planet itself. No planet is likely to have more than about 8 major satellites."

# "If N is greater than 0, feel free to adjust it upward or downward by up to 2, so long as the result is still greater than 0 and no greater than 8. To make this adjustment at random, roll 1d6:
# subtract 2 from N (minimum 1) on a result of 1, subtract 1 from N (minimum 1) on a result of 2, add 1 to N (maximum 8) on a result of 5, and add 2 to N (maximum 8) on a result of 6.

# "The innermost major satellite will have an orbital radius equal to about 1d+2 times the radius of the planet. Vary this result by up to 10%."

# "Major satellites after the innermost can be placed using the Major Satellite Orbital Ratio Table. For each major satellite proceeding outward, make a roll on the table and multiply the previous orbital
# radius by the indicated ratio. If a result on the table does not yield an orbital resonance, feel free to select any value for the ratio between the next lower and next higher entries. If a result on the table
# does yield an orbital resonance, apply exactly that ratio between satellite orbits. As when placing planets, 2:1 Laplace resonances must occur in stacks of at least two. If this is not possible, adjust the 
# last ratio to be exactly 1.60."

# Codify Major Satellite Orbital Ratio Table

# "The eccentricity of major satellite orbits will be small (less than 0.01)."

# "The total mass of all major satellites formed during planetary accretion will be about one ten-thousandth of the mass of the planet. The mass of each major satellite can be generated at
# random with a 3d6 roll"

# Codify Equation of page 85

# "M<sub>s</sub> is the mass of a major satellite in Earth-masses, M<sub>p</sub> is the mass of the planet in Earth- masses, and N is the number of major satellites. Round the satellite’s mass off to two significant
# figures."

# "To determine the density of any of these major satellites, begin by determining whether the satellite will be rocky or icy. A satellite will be rocky if its primary planet orbits inside the
# formation ice line, or it orbits a gas giant with a mass of at least 200 Earth-masses, and the satellite’s orbital radius around the gas giant is no more than 600,000 km. Otherwise, the
# satellite will be icy. Make a note of the satellite’s rocky or icy status for possible use in later steps of the design sequence."

# "Next, apply the following:"

# Codify Equation of page 85

# "D is the satellite’s estimated density, and M is its mass in Earth-masses. Round the estimated density off to the nearest hundredth. To determine the exact density, roll 3d6+10 (for a rocky
# satellite) or 3d6-20 (for an icy satellite). Multiply the result by 0.01, and add to the estimated density to determine the actual density. A satellite’s density can be no less than 0.18 or greater
# than 1.43. If necessary, adjust its density to be within this range."

# "As with a planet, compute a satellite’s radius using:"

# Codify Equation of page 85

# "R is the satellite’s radius in kilometers, M is its mass in Earth-masses, and D is its density. Round off to three significant figures."

# "Use the following to compute a satellite’s surface gravity:"

# Codify Equation on page 85

# "G is the satellite’s surface gravity in standard g, M is its mass in Earth-masses, and D is itsbdensity. Round to the nearest hundredth of a gravity."
 
# "If a planet has one or more major satellites formed during planetary accretion, it may also have many moonlets. We will not generate these in detail, but they may be of interest in general.
# Close to the planet will be a family of inner moonlets. These can range in number from a handful up to dozens. Their orbital radii range from about 1.8 times the planet’s radius, out to
# just inside the radius of the innermost major satellite. In some cases, inner moonlets can be interspersed between the orbits of the first few major satellites as well."

# "If there are inner moonlets, the planet is also likely to have a ring system. A few inner moonlets mean a thin system of rings, not easily visible from any distance. More inner moonlets imply
# a thicker and more visible set of rings. Ring systems hug close to the planet, reaching out to about twice the planet’s radius."

# "To generate the ring system at random, roll 3d6. On a result of 6-9, the planet will have a thin, wispy ring system comparable to that of Jupiter or Neptune, barely visible even at close range.
# On a result of 10-13, the ring system will be moderate, comparable to that of Uranus, visible from a distance through a telescope. On a result of 14 or higher, the planet will have many
# inner moonlets, supporting a dense ring system comparable to Saturn’s, easily visible from anywhere in the star system through a telescope, and spectacular at close range.

# "Beyond the major satellites will be one or more families of outer moonlets. As with the inner moonlets, these can range in number from a handful up to dozens. They are captured planetoids or other debris, 
# following orbits that are eccentric, strongly inclined to the planet’s equator, or even retrograde. Their orbital radii begin at over 100 times the planet’s radius and continue outward to about 
# one-fifth to one-third of the planet’s Hill radius"

# Second Case: Satellites Forming via Major Impact

# "Leftover oligarchs and terrestrial planets, late in their formation process, are subject to repeated massive impact events. The planetary material scattered into orbit by such impacts
# will, in some cases, form a large natural satellite. However, that satellite is in turn likely to spiral back into collision with the parent planet, or to migrate outward and escape the planet’s
# Hill radius entirely. In our own planetary system, only Earth still has a major satellite because of this process. While Mercury, Venus, and Mars all appear to have suffered similar massive
# impacts, none of them have retained any resulting major satellite."

# "To determine whether a leftover oligarch or terrestrial planet can have a large natural satellite, divide the planet’s Hill radius by its own radius. If the result is 300 or greater, then the planet
# can retain a large natural satellite over the long term. In this case, roll 1d: on a 5 or 6 the planet will have exactly one large natural satellite."

# "If it exists, the major satellite will form quite close to the planet but will quickly move outward due to tidal interactions. Its current orbital radius will be between 40 and 100 times the
# planet’s radius. To generate an orbital radius at random, roll 3d6+7 and multiply by 4 times the planet’s radius. The eccentricity of the major satellite’s orbit will be small (no more than about
# 0.05)."

# "The major satellite formed by a massive impact event will have a mass about one hundredth of the mass of the planet. The mass of the major satellite can be generated at random with a 3d6
# roll:"

# Codity Equation on Page 86

# "M<sub>S</sub> is the mass of the major satellite, and M<sub>P</sub> is the mass of the planet, both in Earth-masses. Round the satellite’s mass off to two significant figures."

# "To determine the density, radius, and surface gravity of the major satellite, apply the procedures from the First Case above. Satellites of leftover oligarchs or terrestrial planets will
# almost certainly be rocky."

# Third Case: Terrestrial Planet Moonlets

# "If a leftover oligarch or terrestrial planet has no major satellite, it may acquire one or more moonlets through a variety of means. For example, in our own planetary system, Mars has two
# moonlets."

# "A leftover oligarch or terrestrial planet may have moonlets if it can have a major satellite (that is, its Hill radius is at least 300 times the planet’s own radius) but it has no such satellite. In
# this case, roll 1d: on a 4-6 the planet will have at least one moonlet. Roll 1d-3 (minimum 1) for the number of moonlets"

# "The innermost moonlet will have an orbital radius equal to about 1d+2 times the radius of the planet (feel free to adjust this by up to half the planet’s radius). Moonlets after the first
# can be placed using the Major Satellite Orbital Ratio Table under the First Case above. The eccentricity of moonlet orbits will be very small (less than 0.02)."