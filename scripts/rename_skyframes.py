import os
import shutil
import glob
import sqlite3
import pandas as pd

bands = 'ugrizy'

os.chdir('repo/CALIB')

# Rename the sky frame files
sky_dir = os.path.join('sky', '2023-12-01')
for band in bands:
    src = os.path.join(sky_dir, band)
    dest = src + '_sim_1.4'
    shutil.move(src, dest)

    pattern = os.path.join(dest, f'sky-{band}-R*')
    print(pattern)
    files = glob.glob(pattern)
    print(band, len(files))
    for src in files:
        dest = src.replace(f'sky-{band}-R', f'sky-{band}_sim_1.4-R')
        shutil.move(src, dest)

# Update the calibRegistry.sqlite3 file
with sqlite3.connect('calibRegistry.sqlite3') as conn:
    df = pd.read_sql('select * from sky', conn)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        i = row['id']
        band = row['filter']
        cmd = f'update sky set filter="{band}_sim_1.4" where id={i}'
        cursor.execute(cmd)
    conn.commit()
