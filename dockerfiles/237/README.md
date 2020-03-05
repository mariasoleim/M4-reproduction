This Docker image is set up to rerun submission 237 in the M4 competition.

The method is called "Weighted Ensemble of Statistical Models" and is originally written by Pawlikowski, Chorowska, and Yanchuk from the company ProLogistica Soft.

The methods was the 3. best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run -it mariasoleim/m4-reproduction-237"
3. Change directory into the M4 folder with "cd M4"
4. Choose a resolution by commenting out the corresponding line in run.R. Nano is preinsalled in the container for this purpose. Edit the file with "nano run.R". For example, if you want to make a forecast for monthly series, uncomment the line "indices = 47001:95000 # monthly". Yearly series are commented out by default.
5. Run the code with "nohup Rscript run.R". This may take a while.
6. The forecast will appear as a file called y_hat.csv in the root folder of the container. It can be accessed from outside of the container with "docker cp container-id:/y_hat.csv .".

