This Docker image is set up to rerun submission 036 in the M4 competition.

The method is called "A Simple Combination of Univariate Models (SCUM)" and is originally written by Petropoulos and Svetunkov from the University of Bath and Lancaster University respectively.

The methods was the 6th best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run -it mariasoleim/m4-reproduction-036"
3. Run the forecasting algorithm with "nohup Rscript M4-FPIS-submission-code-20180525.R". This will take some time. To exit the container without stoping stopping it, press Ctrl + P followed by Ctrl + Q.
4. During the rerun, you can anytime check the status of the running code by checking the progress file. Create a copy of it outside the container with "docker cp container-id:progress.csv ." and read it with "cat progress.csv". This will output two numbers. The first is in range 1 to 6 where 1 is the first yearly series and 6 is hourly series. The second number is the current series within that resolution. The algorithm prosess the series in the same order that they appear in the "M4-info.csv" from the competition's organizers.
5. The forecast will appear as a file called all-ffcs.csv in the root folder of the container. It can be accessed from outside of the container with "docker cp container-id:all-ffcs.csv .".

