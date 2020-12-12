import os
import shutil
import glob
import sqlite3

os.chdir('repo/CALIB')

# Rename i-band directory and flats
calib_dir = os.path.abspath('.')
shutil.move(os.path.join(calib_dir, 'flat', 'i'),
            os.path.join(calib_dir, 'flat', 'i_sim_1.4'))
files = sorted(glob.glob(os.path.join(calib_dir, 'flat', 'i_sim_1.4',
                                      '2022-08-06', 'flat_i*')))
for src in files:
    dest = src.replace('_i-R', '_i_sim_1.4-R')
    shutil.move(src, dest)

# Create symlinks between i-band flat calib files and flats for ugrzy bands.
iband_flats = sorted(glob.glob(os.path.join(calib_dir, 'flat', 'i_sim_1.4',
                                            '2022-08-06', 'flat_i_sim_1.4-R*')))
for band in 'ugrzy':
    flat_dir = os.path.join(calib_dir, 'flat', f'{band}_sim_1.4', '2022-08-06')
    os.makedirs(flat_dir, exist_ok=True)
    os.chdir(flat_dir)
    for flat in iband_flats:
        basename = os.path.basename(flat)
        src = os.path.join('../../i_sim_1.4/2022-08-06', basename)
        assert(os.path.isfile(src))
        dest = basename.replace('i_sim_1.4-R', f'{band}_sim_1.4-R')
        try:
            os.symlink(src, dest)
        except FileExistsError as eobj:
            print(outfile, eobj)
            #pass

os.chdir(calib_dir)
# Update the calibRegistry.sqlite3 file with entries for the flats
# in the ugrzy bands.
conn = sqlite3.connect('calibRegistry.sqlite3')
curs = conn.cursor()

# Get the entries for the i-band flats.
query = 'select raftName, detectorName, detector, calibDate, validStart, validEnd from flat where filter="i"'
curs.execute(query)
entries = [x for x in curs]

for band in 'ugrizy':
    for row in entries:
        my_row = [f'{band}_sim_1.4'] + list(row)
        query = "insert into flat (filter, raftName, detectorName, detector, calibDate, validStart, validEnd) values ('{}', '{}', '{}', {}, '{}', '{}', '{}')".format(*my_row)
        try:
            curs.execute(query)
        except sqlite3.IntegrityError:
            pass
    conn.commit()

# Delete original i-band rows:
query = 'delete from flat where filter="i"'
curs.execute(query)
conn.commit()
