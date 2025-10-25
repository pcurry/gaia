# this sub-program covers step 5 ("Star System Metallicity") from Zeigler, 2024 - "Architect of Worlds: Comprehensive World Design for Interstellar Fiction"

# currently only randomly generated metallicity - will need to tweak to use Gaia estimate or values from SIMBAD (if available)
Metallicity = None
roll_for_metallicity = _3d6()
Metallicity = (roll_for_metallicity / 10)*(1.2-(system_age/13.5))

if Population == "Halo Population II":
    Metallicity = (Metallicity - 0.2)

if Metallicity < 0:
    Metallicity = 0

Metallicity = round(Metallicity, 2)
print(f"Metallicity: {Metallicity}")