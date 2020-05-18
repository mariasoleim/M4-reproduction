This Docker image is set up to rerun submission 260 in the M4 competition.

The method is called "Theta - BoxCox" and is originally written by Legaki and Koutsouri from National Technical University of Athens.

The methods was the 8th best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run -it mariasoleim/m4-reproduction-260"
3. Run the forecasting algorithm with "nohup Rscript final_M4.R". This will take some time. To exit the container without stoping stopping it, press Ctrl + P followed by Ctrl + Q.
4. The forecast will appear as a file called final_dataset.csv in the root folder of the container. It can be accessed from outside of the container with "docker cp container-id:/final_dataset.csv .".

