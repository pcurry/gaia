# this sub-program covers step 23 ("Water") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"  - starting from page 98

# "Water is one of the most common substances in the universe. Its special properties will have a profound effect on the surface conditions of any world, from its 
# initial geological development to its eventual climate, and finally to the evolution of life. Some worlds may never have much water, others will tend to lose whatever 
# water they begin with, and still others will retain significant amounts of water throughout their lives."

# "If a world is to have plenty of water, it needs to (somehow) have considerable input of material from outside the formation ice line in the protoplanetary disk. 
# “Dry” terrestrial planets forming in the inner system are unlikely to have much water, unless some event sends a large supply of icy planetesimals inward to impact 
# on the young planets. Gas giants moving outside the formation ice line or into the Kuiper belt at the fringes of the system are the most likely trigger for this. 
# Earth and Mars in our own planetary system seem to have benefited from both of these sources, but otherwise-Earthlike exoplanets may not have been so fortunate."

# "This step estimates how much water can be found on a given world. The possible cases will be sorted into five categories: Trace, Minimal, Moderate, Extensive, and 
# Massive. These categories are defined as follows."

# "Trace: No liquid water remains on the surface. If there is a substantial atmosphere, it may carry traces of water vapor. Small pockets of water ice may remain on the 
# surface, in permanently shadowed craters or valleys, or on the night face of a world tide-locked to its primary star. Small deposits of water may be locked in hydrated 
# minerals deep below the surface. Examples: Mercury, Venus, Earth’s moon, or Io."

# "Minimal: Liquid water is vanishingly rare on the surface, but large deposits of water ice may exist in the form of polar caps, in sheltered craters or valleys, or on 
# the night face of a tide-locked world. Substantial aquifers or ice deposits may exist close beneath the surface. Hydrated minerals can be found in the world’s 
# interior. Examples: Mars."

# "Moderate: A substantial portion of the world’s surface, but not a majority, is covered by some combination of liquid-water seas and water ice, depending on local 
# temperature. The liquid-water oceans or ice deposits are up to a few kilometers in depth. Far away from the oceans or ice deposits, water becomes vanishingly rare. 
# Hydrated minerals are common in the world’s interior. Examples: Mars a few billion years ago"

# "Extensive: Most of the world’s surface is covered by some combination of liquid-water oceans and water ice, up to several kilometers in depth. Water is common in 
# most areas of the surface, even away from  the oceans or ice deposits. Hydrated minerals are plentiful far into the world’s interior. Examples: Earth, Venus a few 
# billion years ago"

# "Massive: The entire surface is covered by some combination of liquid-water oceans and water ice, up to hundreds of kilometers deep. Deeper layers of this world-ocean 
# may be composed of higher-level crystalline forms of water (Ice II and up). Hydrated minerals are plentiful far into the world’s interior. Examples: Europa, Ganymede, 
# Callisto, Titan, some “super-Earth” exoplanets."

# "While classifying the prevalence of water, we can also begin to estimate how much of the world’s surface is covered by water, either as liquid-water seas and oceans, 
# or as a layer of ice. We will express this hydrographic coverage in terms of a percentage. A world with 0% hydrographic coverage has no significant surface water or 
# ice, while a world with 100% hydrographic coverage has no exposed dry land."

# "The amount of water available on a given world will depend upon its M-number (Step Twenty-Two), its blackbody temperature (Step Twenty-Two), its location with 
# respect to the protoplanetary disk (Step Nine), and (in some cases) the arrangement of any planets elsewhere in the planetary system (Steps Ten through Thirteen)."

# Procedure

# "Begin by noting which of the following three cases the world being developed falls under, based on its M-number."


# "First Case: M-number is 2 or less"

# "In this case, the world’s prevalence of water is automatically Massive. Its hydrographic coverage is automatically 100%"


# "Second Case: M-number is between 3 and 28"

# "In this case, determine whether the world is outside or inside the protoplanetary nebula’s formation ice line, as determined in Step Nine. If the world’s orbital 
# radius (or that of its planet, in the case of a major satellite) is exactly on the formation ice line, assume that it is outside"

# "If the world in this case is outside the formation ice line, then its prevalence of water is automatically Massive, and its hydrographic coverage is automatically 
# 100%."

# "If the world in this case is inside the formation ice line, then roll 3d6, modified as follows:"
# "Subtract the world’s M-number."
# "Add +6 if at least one core-accretion planet (which may be a gas giant or failed core) is currently outside the protoplanetary nebula’s formation ice line, and the 
# planetary system experienced a Grand Tack event."
# "Add +3 if at least one planet is currently outside the protoplanetary nebula’s slow-accretion line."

# "Take the modified 3d6 roll and refer to the Initial Water Prevalence Table."

# Codify the Initial Water Prevelance Table on Page 99


# "Third Case: M-number is 29 or greater"

# "In this case, determine whether either of the two following cases is true:"
# "The world’s blackbody temperature is 125 K or greater"
# "The world is the major satellite of a gas giant, and it was designated as a rocky satellite in Step Seventeen."

# "If either of these two conditions are true, then the world’s prevalence of water is Trace and its hydrographic coverage is automatically 0%. Otherwise, its 
# prevalence of water is Massive, and its hydrographic coverage is automatically 100%"

# "Special Case: Loss of Primordial Water and Runaway Greenhouses"

# "Worlds which retain water over billion-year timescales will possess a so-called cold trap. That is, the world’s surface is cold enough that water typically remains 
# in a liquid or even a solid state, and little water vapor escapes to the upper atmosphere. This is important because water molecules in the outer atmosphere are 
# subject to photodissociation. This process causes water to break apart into hydrogen and oxygen under the impact of direct sunlight, after which the hydrogen is 
# likely to escape to space."

# "Worlds which are warm enough to lack a cold trap are likely to lose most or all their water. This can be a slow and relatively gentle process if there was relatively 
# little water to begin with. On the other hand, if enough water vapor rises into the atmosphere at once, the results can be catastrophic. Water vapor is an efficient 
# greenhouse gas, so a world with a great deal of it in the atmosphere is likely to continue warming quickly. The result may be a runaway greenhouse."

# "In this case, smaller worlds which are unable to retain thick hydrogen atmospheres are likely to experience a dry greenhouse. In this case, the world’s entire ocean 
# will eventually boil away and be lost to photodissociation. The remaining atmosphere will be dominated by carbon dioxide at very high temperatures and pressures, with 
# almost no water remaining."

# "On the other hand, “super-Earths” that retain thick hydrogen atmospheres are more likely to experience a wet greenhouse. Such worlds may retain liquid-water oceans 
# even if their surface temperatures are very high, since the dense atmosphere will mean the local boiling point of water is also high. At even higher temperatures and 
# pressures, water exceeds its critical point and becomes a fluid bearing properties of both the liquid and gaseous states. In either case, since such a world can retain 
# molecular hydrogen, it will not tend to lose water to photodissociation. Water molecules which break up in the upper atmosphere will simply return, as free oxygen 
# chemically recombines with the plentiful atmospheric hydrogen. The result will be a hot, dense atmosphere dominated by hydrogen and water vapor."

# "To account for these possibilities, apply the following rules."

# "If a world whose M-number is greater than 2 has Minimal prevalence of water, and its blackbody temperature is 300 K or greater, then the world’s water may have been 
# lost to space."
# "Roll 3d6 and add the blackbody temperature in kelvins. If the result is 318 or greater, then reduce the prevalence of water to Trace. The world’s hydrographic 
# coverage will automatically be 0%."

# "If a world whose M-number is greater than 2 has Moderate or higher prevalence of water, and the world’s blackbody temperature is 300 K or greater, then a runaway 
# greenhouse event may have occurred. As above, roll 3d6 and add the world’s blackbody temperature in kelvins. If the result is 318 or greater, a runaway greenhouse 
# has taken place. Make a note of this event for later steps in the design sequence and reduce the prevalence of water to Trace. The world’s hydrographic coverage will 
# automatically be 0%. Make a note that the world has undergone a dry greenhouse."

# "Finally, if a world whose M-number is 2 or less has a blackbody temperature is 140 K or greater, then a runaway greenhouse event may have occurred. Roll 3d6 and add 
# the world’s blackbody temperature in kelvins. If the result is 158 or greater, a runaway greenhouse has taken place. Make a note of this event for later steps in the 
# design sequence, but do not alter the world's prevalence of water (which should be Massive). Make a note that the world has undergone a wet greenhouse"