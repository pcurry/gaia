#this script pulls Gaia data based on distance from the solar system and converts to sol-centric (x,y,z) coordinates

print("Initializing...")
import os
import random
import numpy as np
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.table import Table
import pandas as pd
import re
import math
import sys

cached_file = "xmatched_cached.csv"

# %%

def get_random_quote():

    quotes = [
        "'My God, it's full of stars.' ~ final transmission of Commander David Bowman during EVA from Discovery One",
        "'We are all in the gutter, but some of us are looking at the stars.' ~ Oscar Wilde",
        "'The wonder is, not that the field of stars is so vast, but that man has measured it.' ~ Anatole France",
	    "'Nay, I swear by the places of the stars - and lo! that is verily a tremendous oath, if ye but knew' ~ Sura 56:75-76"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_random_quote())

# %%

if not os.path.exists(cached_file):
    print("No Cached File Found - Gaia and SIMBAD Queries Required - Please Define Parallax Range You Wish To Sample")
    pmin = input("Enter inner parallax in milliarcseconds - e.g. set to 770 or higher to include Proxima Centauri: ")
    pmax = input("Enter outer parallax in milliarcseconds - e.g. set to 40 to reach out to 25 parsecs from Sol: ")
    print(f"Querying Gaia DR3 for all stars with parallaxes between {pmin} and {pmax} milliarcseconds")
    #query Gaia dataset for galactic longitude, latitude and parallax of stars within user-defined parallaxes
    #will need to update to gaia data release 4 (gaiadr4) when it comes out (no earlier than mid-2026) and gaiadr5 (eta 2030)
    query = f"""
    SELECT designation, l, b, parallax, phot_g_mean_mag, bp_rp, bp_g, g_rp, teff_gspphot, mh_gspphot, logg_gspphot
    FROM gaiadr3.gaia_source
    WHERE parallax > {pmax} AND parallax < {pmin}
    """
    job = Gaia.launch_job_async(query)
    table = job.get_results()
    print("GAIA done")
    #%%
    gaia_DR3_df = table.to_pandas()
    
    print("Preparing to Query SIMBAD for Star Names and Spectral Types")
    Simbad.add_votable_fields('main_id', 'sp_type', 'otype')
    #prepare lists to store the results from Simbad
    star_names = []
    spectral_types = []
    object_types = []
    
    #memo to self: tweak to submit arrays to SIMBAD / improve speed

    print("just to let you you know, this may take a while...")
    print("also, SIMBAD will likely return a warning message that the request executed correctly, but there was no data corresponding to these criteria")
    print("(this is due to fraction of Gaia designations with no matching entries in SIMBAD and not a failure to find any matches)")
    print("(it is safe to ignore this warning and allow the script to continue to run)")
    print("okay, querying SIMBAD now...")
    #iteratively query SIMBAD from the designation row
    for index, row in gaia_DR3_df.iterrows():
        designation = row["designation"]
        simbad_result = Simbad.query_object(designation)
        if simbad_result is not None and len(simbad_result)>0:
            simbad_1 = simbad_result['main_id'][0] if 'main_id' in simbad_result.colnames else 'N/A'
            simbad_2 = simbad_result['sp_type'][0] if 'sp_type' in simbad_result.colnames else 'N/A'
            simbad_3 = simbad_result['otype'][0] if 'otype' in simbad_result.colnames else 'N/A'
            star_names.append(simbad_1)
            spectral_types.append(simbad_2)
            object_types.append(simbad_3)
        else:
            star_names.append("")
            spectral_types.append("")
            object_types.append("")
    print("SIMBAD Query Completed")
    # %%
    print ("Merging SIMBAD and Gaia Results")
    gaia_DR3_df["SIMBAD_ID"]=star_names
    gaia_DR3_df["Spectral_Type"]=spectral_types
    gaia_DR3_df["Object_Type"]= object_types
    print(f"Writing to cached {cached_file}")    
    gaia_DR3_df.to_csv(cached_file, index=False)
else:
    print(f"Loading from cached {cached_file}")
    gaia_DR3_df = pd.read_csv(cached_file)

print("Calculating Distances and Magnitudes")
#prepare columns that will be used in further calculations
p=gaia_DR3_df["parallax"]
m=gaia_DR3_df["phot_g_mean_mag"]
#create new column and calculate distance to star (in parsecs) based on Gaia parallax
gaia_DR3_df["distance"]=1/p*1000
#prepare column that will be used in further calculation
d=gaia_DR3_df["distance"]
#create a new column that normalizes Gaia G-Mag to a distance of 10 parsecs
gaia_DR3_df["adjusted_mag"]=m-5*(np.log(d/10))

print("Calculating Cartesian Coordinates")

#convert galactic coordinates from degrees to radians in preparation for xyz coordinate calculations
l=np.radians(gaia_DR3_df["l"])
b=np.radians(gaia_DR3_df["b"])

#create new column with calculated x-coordinates (where positive x is coreward and negative x is rimward)
gaia_DR3_df["X"]=d*np.cos(b)*np.cos(l)
#create new column with calculated y-coordinates (where positive y is spinward and negative y is trailing in context of the direction of rotaiton of the galactic disk)
gaia_DR3_df["Y"]=d*np.cos(b)*np.sin(l)
#create new column with calculated z-coordinates (where positive z is "galactic north" and negative z is "galactic south" per arbitrary convention)
gaia_DR3_df["Z"]=d*np.sin(b)

# %%

print("Assigning Stars To Sectors")
original_x_values = gaia_DR3_df["X"]
original_y_values = gaia_DR3_df["Y"]
original_z_values = gaia_DR3_df["Z"]

x_prefix = original_x_values.apply(lambda val: "C" if val >= 0 else "R")
y_prefix = original_y_values.apply(lambda val: "S" if val >= 0 else "T")
z_prefix = original_z_values.apply(lambda val: "U" if val >= 0 else "D")

x_rounded = (gaia_DR3_df["X"].abs() / 10).apply(math.ceil).astype(int)
y_rounded = (gaia_DR3_df["Y"].abs() / 10).apply(math.ceil).astype(int)
z_rounded = (gaia_DR3_df["Z"].abs() / 10).apply(math.ceil).astype(int)

gaia_DR3_df["Sector_Reference"] = x_prefix.astype(str) + \
                                   x_rounded.astype(str) + "-" + \
                                   y_prefix.astype(str) + \
                                   y_rounded.astype(str) + "-" + \
                                   z_prefix.astype(str) + \
                                   z_rounded.astype(str)

# %%
print("Generating Star Names from SIMBAD IDs")

#rename datadframe to reflect it will now include more data sources than just Gaia DR3
xmatched_df = gaia_DR3_df

#create a duplicate of the SIMBAD ID column
xmatched_df["label_name"] = xmatched_df["SIMBAD_ID"]
xmatched_df["label_name"] = xmatched_df["label_name"].fillna(xmatched_df["designation"])
column_to_clean="label_name"

#remove unwanted prefixes and other nonsense from SIMBAD ID format

xmatched_df[column_to_clean]= (
    xmatched_df[column_to_clean]
    .astype(str)
    .str.replace(r'star', 'Star', regex=True) #fix 'Baranrd's star' and similar occurences from SIMBAD
    .str.replace(r'NAME ', '', regex=True) #remove SIMBAD prefix to proper star names
    .str.replace(r'GR\*', 'GR', regex=True) #
    .str.replace(r'.*?\*', '', regex=True) #remove prefixes to star names
    .str.lstrip() #remove whitespace to left of any star name
    .str.replace(r'\s{2,}', ' ', regex=True) #remove double/triple spaces
)
# %%

#replace simbad abbreviations with full greek letters

simbad_greek_letters = {
    'alf ': 'Alpha ',
    'bet ': 'Beta ',
    'gam ': 'Gamma ',
    'del ': 'Delta ',
    'eps ': 'Epsilon ',
    'zet ': 'Zeta ',
    'eta ': 'Eta ',
    'tet ': 'Theta ',
    'iot ': 'Iota ',
    'kap ': 'Kappa ',
    'lam ': 'Lambda ',
    'mu.': 'Mu',
    'nu.': 'Nu',
    'ksi ': 'Xi ',
    'omi ': 'Omicron ',
    'pi.': 'Pi',
    'rho ': 'Rho ',
    'sig ': 'Sigma ',
    'tau ': 'Tau ',
    'ups ': 'Upsilon ',
    'phi ': 'Phi ',
    'chi ': 'Chi ',
    'psi ': 'Psi ',
    'ome ': 'Omega ',
    'alf0': 'Alpha-',
    'bet0': 'Beta-',
    'gam0': 'Gamma-',
    'del0': 'Delta-',
    'eps0': 'Epsilon-',
    'zet0': 'Zeta-',
    'eta0': 'Eta-',
    'tet0': 'Theta-',
    'iot0': 'Iota-',
    'kap0': 'Kappa-',
    'lam0': 'Lambda-',
    'ksi0': 'Xi-',
    'omi0': 'Omicron-',
    'rho0': 'Rho-',
    'sig0': 'Sigma-',
    'tau0': 'Tau-',
    'ups0': 'Upsilon-',
    'phi0': 'Phi-',
    'chi0': 'Chi-',
    'psi0': 'Psi-',
    'ome0': 'Omega-'}

for key, value in simbad_greek_letters.items():    
    xmatched_df['label_name'] = xmatched_df['label_name'].str.replace(key, value, regex=False)

# %%

#replace SIMBAD constellation abbreviations with genitive forms of constellation names

simbad_const_abbrv = {
    ' And': ' Andromedae',
    ' Ant': ' Antliae',
    ' Aps': ' Apodis',
    ' Aqr': ' Aquarii',
    ' Aql': ' Aquilae',
    ' Ara': ' Arae',
    ' Ari': ' Arietis',
    ' Aur': ' Aurigae',
    ' Boo': ' Bootis',
    ' Cae': ' Caeli',
    ' Cam': ' Camelopardalis',
    ' Cnc': ' Cancri',
    ' CVn': ' Canum Venaticorum',
    ' CMa': ' Canis Majoris',
    ' CMi': ' Canis Minoris',
    ' Cap': ' Capricorni',
    ' Car': ' Carinae',
    ' Cas': ' Cassiopeiae',
    ' Cen': ' Centauri',
    ' Cep': ' Cephei',
    ' Cet': ' Ceti',
    ' Cha': ' Chamaeleontis',
    ' Cir': ' Circini',
    ' Col': ' Columbae',
    ' Com': ' Comae Berenices',
    ' CrA': ' Coronae Australis',
    ' CrB': ' Coronae Borealis',
    ' Crv': ' Corvi',
    ' Crt': ' Crateris',
    ' Cru': ' Crucis',
    ' Cyg': ' Cygni',
    ' Del': ' Delphini',
    ' Dor': ' Doradus',
    ' Dra': ' Draconis',
    ' Eql': ' Equulei',
    ' Eri': ' Eridani',
    ' For': ' Fornacis',
    ' Gem': ' Geminorum',
    ' Gru': ' Gruis',
    ' Her': ' Herculis',
    ' Hor': ' Horologii',
    ' Hya': ' Hydrae',
    ' Hyi': ' Hydri',
    ' Ind': ' Indi',
    ' Lac': ' Lacertae',
    ' Leo': ' Leonis',
    ' LMi': ' Leonis Minoris',
    ' Lep': ' Leporis',
    ' Lib': ' Librae',
    ' Lup': ' Lupi',
    ' Lyn': ' Lyncis',
    ' Lyr': ' Lyrae',
    ' Men': ' Mensae',
    ' Mic': ' Microscopii',
    ' Mon': ' Monocerotis',
    ' Mus': ' Muscae',
    ' Nor': ' Normae',
    ' Oct': ' Octantis',
    ' Oph': ' Ophiuchi',
    ' Ori': ' Orionis',
    ' Pav': ' Pavonis',
    ' Peg': ' Pegasi',
    ' Per': ' Persei',
    ' Phe': ' Phoenicis',
    ' Pic': ' Pictoris',
    ' Psc': ' Piscium',
    ' PsA': ' Piscis Austrini',
    ' Pup': ' Puppis',
    ' Pyx': ' Pyxidis',
    ' Ret': ' Reticulii',
    ' Sge': ' Sagittae',
    ' Sgr': ' Sagittarii',
    ' Sco': ' Scorpii',
    ' Scl': ' Sculptoris',
    ' Sct': ' Scuti',
    ' Ser': ' Serpentis',
    ' Sex': ' Sextantis',
    ' Tau': ' Tauri',
    ' Tel': ' Telescopii',
    ' Tri': ' Trianguli',
    ' TrA': ' Trianguli Australis',
    ' Tuc': ' Tucanae',
    ' UMa': ' Ursae Majoris',
    ' UMi': ' Ursae Minoris',
    ' Vel': ' Velorum',
    ' Vir': ' Virginis',
    ' Vol': ' Volantis',
    ' Vul': ' Vulpeculae'}

for key, value in simbad_const_abbrv.items():
    xmatched_df['label_name'] = xmatched_df['label_name'].str.replace(key, value, regex=False)
# %%

#clean up remaining artifacts

def add_space_before_letter(text):
    text = str(text)
    return re.sub(r'(?<! )([A-Z])$', r' \1', text)

xmatched_df[column_to_clean]= (
    xmatched_df[column_to_clean]
    .astype(str)
    .str.replace(r'Mu0', 'Mu-', regex=True)
    .str.replace(r'Nu0', 'Nu-', regex=True)
    .str.replace(r'Pi0', 'Pi-', regex=True)
    .str.replace(r'BEta', 'Beta', regex=True)
    .str.replace(r'ZEta', 'Zeta', regex=True)
    .str.replace(r'Centauritauri', 'Centauri', regex=True) #fix Proxima Centauri
    .apply(add_space_before_letter)
)

# %%
user_query = input("Do you want to add stars which were not present in Gaia DR3? (yes/no): ").lower()

if user_query == "yes":
    print("Adding Stars Outside of Gaia DR3")
    #add stars which do not appear in any Gaia data release or do not appear in DR3
    csv_file_path = 'not_in_Gaia_DR3.csv'
    not_in_Gaia_DR3_df = pd.read_csv(csv_file_path)
    df_merged = pd.concat([xmatched_df, not_in_Gaia_DR3_df], ignore_index=True)
else:
    print("ok - no additional stars added")

# %%
#sort panda dataframe by Sector Designations
df_sorted = df_merged.sort_values(by='Sector_Reference')

#export a master csv with all of the Gaia/SIMBAD crossmatches sorted by sector
df_sorted.to_csv('all_results_sorted_by_sector.csv', index=False)
print("All Stars Within The Designated Parallax Range Have Been Crossmatched In SIMBAD, Parsed Into 10pc x 10 pc x 10 pc Sectors and Exported as all_results_sorted_by_sector.csv")

# %%
print("Parsing Into Indivual Sector Files")

unique_sectors = df_sorted['Sector_Reference'].unique()

for sector in unique_sectors:
    # Filter df_sorted to include only rows with a particular sector
    sector_df = df_sorted[df_sorted['Sector_Reference'] == sector]
    # create a filename based on the sector
    filename = f"sector_{sector.replace(' ', '_')}.csv"
    # Export the filtered DataFrame to a CSV file
    sector_df.to_csv(filename, index=False)
    print(f"Exported Data for Sector '{sector}' to '{filename}'")

print("Finished Exporting All Data")