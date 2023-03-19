# Introduction
This Flask app displays data from a dataset of parking violations in the city of Los Angeles.

## Requirements
To run the app, you need to have Docker installed on your machine and the parking-citations.csv file in the current directory.
You can download the dataset from: https://www.kaggle.com/datasets/cityofLA/los-angeles-parking-citations?resource=download&select=parking-citations.csv

Create a data folder and save this file into the data folder

In the terminal, navigate to the root directory of the project.

Run the following command to build the Docker container:
```
docker build -t elastacloud-app .
```
Once the container is built, run the following command to start the app:
```
docker run -p 5000:5000 elastacloud-app
```
Open a web browser and go to http://localhost:5000 to see the app
