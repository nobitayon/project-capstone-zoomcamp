# project-capstone-zoomcamp

## Problem Description

classify whether the person in the photo is wearing glasses or not .Dataset from https://www.kaggle.com/aniruddha123/glasses-data . I make two deep learning model ,model_v1 and model_v2.The difference just in number of convolutional layer. 

File in repository :
* model_v1.ipynb : Model selection process
* model_v2.ipynb : 
* predict-test.py : to try web service that deployed locally
* deploy-test.py  : to try web service that deployed on pythonanywhere
* prep.py : Module that needed on predict.py 
* Dockerfile : to running the service on docker
* Summary-model.xlsx : summary of model selection process
* Data.csv : Data i used to train and test on this project
* 
# How to run project

## Install dependencies
1. Create new environment with `conda create -n myenv python=3.8`
2. Activate new environment with `conda activate myenv`
3. Install dependencies with `pip install - r requirements.txt`

## To run notebook.ipynb
1. Activate myenv
2. Open model_v1.ipynb or model_v2.ipynb . I put EDA and problem description in model_v1.ipynb


## Deploy locally using docker
1. Build docker image using `docker build -t glass-model .`
2. run docker image using `docker run -it --rm -p 8080:8080 glass-model:latest`
3. run `python predict-test.py` on another command prompt 

Thank you for reviewing my project , sorry for the many shortcomings

