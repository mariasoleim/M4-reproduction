This Docker image is set up to rerun submission 078 in the M4 competition.

The method is called "THIEF combination" and is originally written by Shaub from Harvard Extension School.

The methods was the 7th best in the M4 competition according to OWA.

To rerun the code:
1. Install Docker
2. Run an instance of the image in detached interactive mode with the command "docker run -it mariasoleim/m4-reproduction-078"
3. Run the forecasting algorithm with "nohup Rscript root/m4/forecastM4.R". This will take some time. To exit the container without stoping stopping it, press Ctrl + P followed by Ctrl + Q.
4. During the rerun, you can anytime check the status of the running code by checking the nohup file. Create a copy of it outside the container with "docker cp container-id:nohup.out ." and read it with "cat nohup.out".
5. The forecast will appear as one file for each resolution in root/m4. It can be accessed from outside of the container with "docker cp container-id:root/m4/mean/resolution-mean.csv .". Change "resolution" with the resolution of your choice.

