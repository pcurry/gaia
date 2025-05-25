#this script pulls Gaia data based on distance from the solar system and converts to sol-centric (x,y,z) coordinates

print("Initializing...")
import os
import random
import numpy as np
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.table import Table
import pandas as pd

cached_file = "gaia_cached.csv"

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
    SELECT designation, l, b, parallax, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE parallax > {pmax} AND parallax < {pmin}
    """
    job = Gaia.launch_job_async(query)
    table = job.get_results()
    print("GAIA done")
    #%%
    gaia_DR3_df = table.to_pandas()
    
    print("Preparing to Query SIMBAD for Star Names and Spectral Types")
    Simbad.add_votable_fields('main_id', 'sp_type')
    #prepare lists to store the results from Simbad
    star_names = []
    spectral_types = []
    
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
            star_names.append(simbad_1)
            spectral_types.append(simbad_2)
        else:
            star_names.append("")
            spectral_types.append("")
    print("SIMBAD Query Completed")
    # %%
    print ("Merging SIMBAD and Gaia Results")
    gaia_DR3_df["SIMBAD_ID"]=star_names
    gaia_DR3_df["Spectral_Type"]=spectral_types
    print(f"Writing to cached {cached_file}")    
    gaia_DR3_df.to_csv(cached_file)
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

print("Converting SIMBAD IDs to proper star names")

#create duplicate of SIMBAD ID column
gaia_DR3_df["interim_ID"] = gaia_DR3_df["SIMBAD_ID"]
column_to_clean="interim_ID"

#remove unwanted prefixes from SIMBAD ID format
string_1_to_remove="V* "
string_2_to_remove="** "
string_3_to_remove="* "
string_4_to_remove="NAME "
string_5_to_remove="  "
gaia_DR3_df[column_to_clean]= (
    gaia_DR3_df[column_to_clean]
    .astype(str)
    .str.replace(string_1_to_remove, '', regex=False)
    .str.replace(string_2_to_remove, '', regex=False)
    .str.replace(string_3_to_remove, '', regex=False)
    .str.replace(string_4_to_remove, '', regex=False)
    #remove annoying double spaces
    .str.replace(string_5_to_remove, ' ', regex=False)
    #and again to get rid of those very annoying triple spaces
    .str.replace(string_5_to_remove, ' ', regex=False)
)
# %%

#replace simbad abbreviations with full greek letters

simbad_greek_letters = {
    'alf': 'Alpha',
    'bet': 'Beta',
    'gam': 'Gamma',
    'del': 'Delta',
    'eps': 'Epsilon',
    'zet': 'Zeta',
    'eta': 'Eta',
    'tet': 'Theta',
    'iot': 'Iota',
    'lap': 'Kappa',
    'lam': 'Lambda',
    'mu.': 'Mu',
    'nu.': 'Nu',
    'ksi': 'Xi',
    'omi': 'Omicron',
    'pi.': 'Pi',
    'rho': 'Rho',
    'sig': 'Sigma',
    'tau': 'Tau',
    'ups': 'Upsilon',
    'phi': 'Phi',
    'khi': 'Chi',
    'psi': 'Psi',
    'ome': 'Omega'}

#need to insert code to edit interim_ID column based on above dictionary

# %%

#replace SIMBAD constellation abbreviations with genitive forms of constellation names

simbad_constellation_abbreviations = {
    'And': 'Andromedae',
    'Ant': 'Antliae',
    'Aps': 'Apodis',
    'Aqr': 'Aquarii',
    'Aql': 'Aquilae',
    'Ara': 'Arae',
    'Ari': 'Arietis',
    'Aur': 'Aurigae',
    'Boo': 'Boötis',
    'Cae': 'Caeli',
    'Cam': 'Camelopardalis',
    'Cnc': 'Cancri',
    'CVn': 'Canum Venaticorum',
    'CMa': 'Canis Majoris',
    'CMi': 'Canis Minoris',
    'Cap': 'Capricorni',
    'Car': 'Carinae',
    'Cas': 'Cassiopeiae',
    'Cen': 'Centauri',
    'Cep': 'Cephei',
    'Cet': 'Ceti',
    'Cha': 'Chamaeleontis',
    'Cir': 'Circini',
    'Col': 'Columbae',
    'Com': 'Comae Berenices',
    'CrA': 'Coronae Australis',
    'CrB': 'Coronae Borealis',
    'Crv': 'Corvi',
    'Crt': 'Crateris',
    'Cru': 'Crucis',
    'Cyg': 'Cygni',
    'Del': 'Delphini',
    'Dor': 'Doradus',
    'Dra': 'Draconis',
    'Eql': 'Equulei',
    'Eri': 'Eridani',
    'For': 'Fornacis',
    'Gem': 'Geminorum',
    'Gru': 'Gruis',
    'Her': 'Herculis',
    'Hor': 'Horologii',
    'Hya': 'Hydrae',
    'Hyi': 'Hydri',
    'Ind': 'Indi',
    'Lac': 'Lacertae',
    'Leo': 'Leonis',
    'LMi': 'Leonis Minoris',
    'Lep': 'Leporis',
    'Lib': 'Librae',
    'Lup': 'Lupi',
    'Lyn': 'Lyncis',
    'Lyr': 'Lyrae',
    'Men': 'Mensae',
    'Mic': 'Microscopii',
    'Mon': 'Monocerotis',
    'Mus': 'Muscae',
    'Nor': 'Normae',
    'Oct': 'Octantis',
    'Oph': 'Ophiuchi',
    'Ori': 'Orionis',
    'Pav': 'Pavonis',
    'Peg': 'Pegasi',
    'Per': 'Persei',
    'Phe': 'Phoenicis',
    'Pic': 'Pictoris',
    'Psc': 'Piscium',
    'PsA': 'Piscis Austrini',
    'Pup': 'Puppis',
    'Pyx': 'Pyxidis',
    'Ret': 'Reticulii',
    'Sge': 'Sagittae',
    'Sgr': 'Sagittarii',
    'Sco': 'Scorpii',
    'Scl': 'Sculptoris',
    'Sct': 'Scuti',
    'Ser': 'Serpentis',
    'Sex': 'Sextantis',
    'Tau': 'Tauri',
    'Tel': 'Telescopii',
    'Tri': 'Trianguli',
    'TrA': 'Trianguli Australis',
    'Tuc': 'Tucanae',
    'UMa': 'Ursae Majoris',
    'UMi': 'Ursae Minoris',
    'Vel': 'Velorum',
    'Vir': 'Virginis',
    'Vol': 'Volantis',
    'Vul': 'Vulpeculae'}

#need to insert code to edit interim_ID column based on above dictionary

# %%

print("Adding Stars Outside of Gaia DR3")
#add stars which do not appear in any Gaia data release or do not appear in DR3
csv_file_path = 'not_in_Gaia_DR3.csv'
not_in_Gaia_DR3_df = pd.read_csv(csv_file_path)
df_final = pd.concat([gaia_DR3_df, not_in_Gaia_DR3_df], ignore_index=True)
# %%
df_final.to_csv('gaia_query_result.csv', index=False)
print("Results Exported to 'gaia_query.result.csv'")