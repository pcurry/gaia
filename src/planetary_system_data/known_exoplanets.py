# reference: Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction" - pg. 176-178

# "Several factors need to be kept in mind when reviewing exoplanetary data."

# "First, it’s entirely possible for exoplanets to escape detection, even in orbit around stars for which other exoplanets 
# have been found. Planets with low mass, 
# or long orbital periods, or whose orbits are steeply inclined from our point of view, may all go undetected."

# "Second, it’s also entirely possible for an exoplanet candidate to be a “false positive.” The signal in the data which suggests 
# the presence of a planet may also be caused by the star’s natural variability, or by some other object, or simply by error in 
# the astronomical instruments or observational methods. The scientific community doesn’t consider a candidate to be “confirmed” 
# until it’s been verified by a second set of observations using a different instrument... and even then, some candidates have 
# later been found to be in error."

# "All of this means that when developing an interstellar setting, it’s reasonable to limit which exoplanet candidates are to be 
# included, based on the scientific community’s current level of confidence in each detection. Meanwhile, it’s also plausible to 
# add additional exoplanets beyond those that are already known to exist, especially if these are specifically designed to be 
# difficult to detect (relatively low mass, long orbital period, and so on)."

# "For the rest of this section, we will discuss how to work with data about confirmed exoplanet candidates. The best and most 
# convenient source for this data is the NASA Exoplanet Archive, although references provided for a star by SIMBAD will also 
# discuss candidates."

# Orbital Parameters

# "Nearly every exoplanet candidate has defined orbital parameters defined. For example, the NASA Exoplanet Archive lists the 
# following parameters for most candidates:
# "The semimajor axis (what Architect of Worlds calls the “orbital radius”) a, listed in AU."
# "The eccentricity e."

# "These should be sufficient to place a candidate exoplanet in a star system under development."
# "These figures are given with a confidence interval, using a notation that looks like this:"
# (example - a = 11.55 with superscript +0.98 and subscript -0.86)

# "This means that given the available observations, the most likely value for the planet’s orbital radius is 11.55 AU. However, 
# the actual value could be up to 0.86 AU lower, or 0.98 AU higher, than this value. When placing a candidate exoplanet in a star 
# system, feel free to vary the given parameters within the confidence interval."

# "The transit detection method makes it difficult to estimate an exoplanet's orbital eccentricity. The Exoplanet Archive may 
# give an eccentricity of 0, or have no listing at all. In these cases, generating a random eccentricity will be necessary."

# Mass

# "The Exoplanet Archive will often list the mass of an exoplanet candidate as MP. This is done in two different units:"
# "Mass in Earth-masses (M⊕), as used by Architect of Worlds."
# "Mass in Jupiter-masses (MJup), where one Jupiter-mass is equal to 317.94 Earth-masses."

# "In many cases, especially when the exoplanet candidate was detected by the radial velocity method, the figure given is a 
# minimum mass. This is marked by the mass being given not simply as MP, but as the more complex formulation MP sin i, where i is 
# the (unknown) inclination of the exoplanet’s orbital plane to our line of sight.  This is because we can only infer the 
# exoplanet’s mass by the component of its primary star’s movement that is directly toward and away from us. If the exoplanet’s 
# orbital plane is closer to being face-on to us, it takes more planetary mass to generate the observed movement of the primary 
# star."

# "When dealing with exoplanet candidates whose true mass is unknown, it’s worth selecting a value for sin i, between 0 and 1 but 
# with a strong preference for higher values. One way to generate a value at random might be to roll percentile dice twice to 
# generate values between 0 and 1, and taking the larger of the two. If there is more than one exoplanet candidate in the target 
# planetary system, the same value of sin i should be used for all of them.

# "Once the value of sin i has been selected, the true mass of any exoplanet candidate in that system can be estimated by 
# dividing its minimum mass MP sin i by sin i."

# Radius and Density

# "In some cases, especially when an exoplanet candidate was detected using the transit method, the Exoplanet Archive may list 
# its radius as RP. As with a planet’s mass, this will be listed in terms of the radii of Earth and Jupiter:
# Radius in Earth-radii (R⊕), where one Earth-radius is equal to 6,371.0 km.
# Radius in Jupiter-radii (RJup), where one Jupiter-radius is equal to 71,450 km.

# "It’s quite rare for an exoplanet candidate to have both known mass and radius. If the exoplanet was discovered by the transit 
# method, its radius can be measured directly, but its mass can only be estimated. Likewise, if the planet was discovered by the 
# radial velocity method, its mass can be measured, but its radius can only be estimated."

# "The Exoplanet Archive uses a specific empirical relationship to estimate mass given radius, or to estimate radius given mass. 
# Feel free to accept these estimates as given, or you may prefer to use the procedures in Step Sixteen of the design sequence to 
# generate your own estimates."

# Inferring Undetected Exoplanets

# "Once any confirmed exoplanet candidates have been placed in the system under development, there are two ways to infer whether 
# there it would be plausible to add one or more “undetected” exoplanets.

# "First, if detection was by the radial velocity method and so the eccentricity of exoplanetary candidate orbits is available, 
# take the average eccentricity of all confirmed candidates. Compare the result to the System Eccentricity Table (p. 79). If the 
# average eccentricity is lower than the value on the table for the number of confirmed exoplanet candidates, it’s plausible to 
# assume that the difference indicates the presence of one or more undetected planets."

# "Second, if there are at least three confirmed exoplanet candidates in the system, compute the ratios between adjacent orbital 
# radii. If one of the ratios is significantly larger than the average, this indicates a “gap” into which at least one undetected 
# exoplanet might be placed.

# "It’s always plausible to place additional undetected exoplanets beyond the orbit of the outermost confirmed exoplanet 
# candidate, toward the outer edge of a planetary system. The methods currently in use are biased toward detection of planets 
# close to their primary stars, so the outer region of a planetary system is always a likely place for undetected exoplanets to 
# lurk"