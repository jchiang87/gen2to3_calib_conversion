old_calib_dir=/global/cscratch1/sd/jchiang8/desc/gen3_tests/repo/CALIB
new_repo=repo
new_calib_dir=${new_repo}/CALIB
mode=copy

# bias
ingestCalibs.py ${new_repo} ${old_calib_dir}/bias/2022-01-01/bias-R* --calib ${new_calib_dir}/ --output ${new_calib_dir}/bias --longlog  --mode=${mode} --validity 9999 --create

# dark
ingestCalibs.py ${new_repo} ${old_calib_dir}/dark/2022-01-01/dark-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/dark --longlog  --mode=${mode} --validity 9999

# flat
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/u_sim_1.4/2022-08-06/flat_u_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/g_sim_1.4/2022-08-06/flat_g_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/r_sim_1.4/2022-08-06/flat_r_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/i_sim_1.4/2022-08-06/flat_i_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/z_sim_1.4/2022-08-06/flat_z_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/flat/y_sim_1.4/2022-08-06/flat_y_sim_1.4-R*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/flat --longlog  --mode=${mode} --validity 9999

# SKY
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/u_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/g_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/r_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/i_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/z_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999
ingestCalibs.py ${new_repo} ${old_calib_dir}/SKY/2023-12-01/y_sim_1.4/SKY-*  --calib ${new_calib_dir}/ --output ${new_calib_dir}/sky --longlog  --mode=${mode} --validity 9999

# bfk
