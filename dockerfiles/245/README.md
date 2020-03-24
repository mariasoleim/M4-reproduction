This Docker image is set up to rerun submission 245 in the M4 competition.

The method is called "M4metalearning" and is originally written by Montero-Manso, Talagala, Hyndman and Athanasopoulos from the University of A Coruña & Monash University.

The methods was the 2nd best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run -it mariasoleim/m4-reproduction-245"
3. Run the code with "nohup Rscript run.R". This may take a while.
4. The forecast will appear as a file called y_hat.csv in the root folder of the container. It can be accessed from outside of the container with "docker cp container-id:/y_hat.csv .". Due to problems with some of the time series, there will be no forecasts for "Y12146", "Y21168", "Y22801", "Q5619", "M16993" or "D2085".

