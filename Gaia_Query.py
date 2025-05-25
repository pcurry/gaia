#this script pulls Gaia data based on distance from the solar system and converts to sol-centric (x,y,z) coordinates

print("Initializing...")
import os
import numpy as np
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.table import Table
import pandas as pd
Simbad.add_votable_fields('main_id', 'sp_type')

cached_file = "gaia_cached.csv"

pmax = 40

if not os.path.exists(cached_file):
    print(f"Querying Gaia DR3 for all stars with parallax greater than pmax={pmax} mas")
    #query Gaia dataset for galactic longitude, latitude and parallax of nearby stars (within 25 parsecs)
    #will need to update to gaia data release 4 (gaiadr4) when it comes out (no earlier than mid-2026) and gaiadr5 (eta 2030)
    query = f"""
    SELECT designation, l, b, parallax, phot_g_mean_mag
    FROM gaiadr3.gaia_source
    WHERE parallax > {pmax}
    """
    job = Gaia.launch_job_async(query)
    table = job.get_results()
    print("GAIA done")
    #%%
    gaia_DR3_df = table.to_pandas()

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
    
    print("Querying SIMBAD for Star Names and Spectral Types")
    #prepare lists to store the results from Simbad
    star_names = []
    spectral_types = []
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
    # %%
    print ("Merging SIMBAD and Gaia Results")
    gaia_DR3_df["SIMBAD_ID"]=star_names
    gaia_DR3_df["Spectral_Type"]=spectral_types
    print(f"Writing to cached {cached_file}")    
    gaia_DR3_df.to_csv(cached_file)
else:
    print(f"Loading from cached {cached_file}")
    gaia_DR3_df = pd.read_csv(cached_file)

print("Calculating Cartesian Coordinates")

#convert galactic coordinates from degrees to radians in preparation for xyz coordinate calculations
l=np.radians(gaia_DR3_df["l"])
b=np.radians(gaia_DR3_df["b"])

#prepare existing distance column for xzy coordinate calculations
d=gaia_DR3_df["distance"]

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
    .str.replace(string_5_to_remove, ' ', regex=False)
    #and again to get rid of annoying triple spaces
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