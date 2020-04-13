This Docker image is set up to rerun submission 118 in the M4 competition.

The method is called "ES-RNN" and is originally written by Smyl from Uber Technologies.

The methods was the best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run --name=m4-reproduction-118 -it mariasoleim/m4-reproduction-118". If you get a permission error, run all the command and all the following commands with sudo in front. E.g. "sudo docker run --name=m4-reproduction-118 -it mariasoleim/m4-reproduction-118"
3. Run the code with "source linux_example_scripts/run_resolution", but change resolution to hourly, daily, weekly, monthly, quarterly or yearly. E.g. "source linux_example_scripts/run_weekly" for predicting the weekly time series. This will take some time. You can quit the container without stopping it with Ctrl + P followed by Ctrl + Q. A folder is generated in ../output. The folder will contain a number of forecasts that could have been used as individual forecasts. However, since part of the method is to merge these, we are gonna do that. 
4. Attach to the container again with "docker attach m4-reproduction-118".
5. Reveal the name of the generated folder with "ls ../output"
6. Merge the different files in ../output/folder_name by running the command "Rscript ../R/merge_resolution.R folder_name", but change resolution to hourly, daily, weekly, monthly, quarterly or yearly, and change the folder_name to the name of the newly generated folder. E.g. "Rscript ../R/merge_weekly.R Weekly2020-03-16_11_29Final".
7. The script is finished when the total number of forecasts with the given resolution is printed. Use Ctrl + Z to exit the script. 
8. The forecast is found in ../output/folder_name/ResolutionForec.csv. Exit the Docker container with the command Ctrl + P followed by Ctrl + Q. Extract the forecast from the container with "docker cp m4-reproduction-118:home/es-rnn/output/folder_name/ResolutionForec.csv ." Change "Resolution" with the resolution you are working with. E.g. "docker cp m4-reproduction-118:home/es-rnn/output/folder_name/WeeklyForec.csv ."

