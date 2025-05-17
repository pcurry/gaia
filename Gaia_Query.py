#pulls Gaia data based on distance from solar system and converts to sol-centric (x,y,z) coordinates
import numpy as np
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.table import Table
import pandas as pd
#query Gaia dataset for galactic longitude, latitude and parallax of nearby stars (within 25 parsecs)
#will need to update to gaia data release 4 (gaiadr4) when it comes out (no earlier than mid-2026) and gaiadr5 (eta 2030)
query = """
SELECT designation, l, b, parallax
FROM gaiadr3.gaia_source
WHERE parallax > 40
"""
job = Gaia.launch_job_async(query)
table = job.get_results()
#%%
df = table.to_pandas()
#create new column and calculate distance to star (in parsecs) based on Gaia parallax
p=df["parallax"]
d=df["distance"]=1/p*1000
l=np.radians(df["l"])
b=np.radians(df["b"])
#create new column with calculated x-coordinates (where positive x is coreward and negative x is rimward)
df["X"]=d*np.cos(b)*np.cos(l)
#create new column with calculated y-coordinates (where positive y is spinward and negative y is trailing in context of the direction of rotaiton of the galactic disk)
df["Y"]=d*np.cos(b)*np.sin(l)
#create new column with calculated z-coordinates (where positive z is "galactic north" and negative z is "galactic south" per arbitrary convention)
df["Z"]=d*np.sin(b)
#add stars which were too bright for Gaia (due to detector saturation)
bright_stars = {'designation': ["Sol", "Alpheratz", "Mirach", "Almach"], 
'l': [0, 111.7322278, 127.1075879, 136.9645847], 
'b': [0, -32.84335675, -27.10282071, -18.55901423], 
'parallax': [8800, 33.62, 16.52, 8.3], 
'distance': [0, 29.74419988, 60.53268765, 120.4819277], 
'X': [0, -9.252949243, -32.50992551, -83.4844413], 
'Y': [0, 23.21361869, 42.9739963, 77.9470326], 
'Z': [0, -16.13159212, -27.57801044, -38.34713907]}
bright_df = pd.DataFrame(bright_stars)
df_combined = pd.concat([df, bright_df], ignore_index=True)
print(df_combined)