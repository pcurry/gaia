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
            star_names.append("No Match in SIMBAD")
            spectral_types.append("Unknown")
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

d=gaia_DR3_df["distance"]

#create new column with calculated x-coordinates (where positive x is coreward and negative x is rimward)
gaia_DR3_df["X"]=d*np.cos(b)*np.cos(l)
#create new column with calculated y-coordinates (where positive y is spinward and negative y is trailing in context of the direction of rotaiton of the galactic disk)
gaia_DR3_df["Y"]=d*np.cos(b)*np.sin(l)
#create new column with calculated z-coordinates (where positive z is "galactic north" and negative z is "galactic south" per arbitrary convention)
gaia_DR3_df["Z"]=d*np.sin(b)
# %%
print("Adding Stars Outside of Gaia DR3")
#add stars which do not appear in any Gaia data release or do not appear in DR3
csv_file_path = 'not_in_Gaia_DR3.csv'
not_in_Gaia_DR3_df = pd.read_csv(csv_file_path)
df_final = pd.concat([gaia_DR3_df, not_in_Gaia_DR3_df], ignore_index=True)
# %%
df_final.to_csv('gaia_query_result.csv', index=False)
print("Results Exported to 'gaia_query.result.csv'")


