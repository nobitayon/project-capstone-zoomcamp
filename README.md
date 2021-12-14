# project-capstone-zoomcamp

## Problem Description

classify whether the person in the photo is wearing glasses or not .Dataset from https://www.kaggle.com/aniruddha123/glasses-data . I make two deep learning model ,model_v1 and model_v2.The difference just in number of convolutional layer. 

File in repository :
* model_v1.ipynb : Model selection process
* model_v2.ipynb : 
* predict-test.py : to try web service that deployed locally
* deploy-test.py  : to try web service that deployed on pythonanywhere
* Dockerfile : to running the service on docker
* model_v1_10_0.948.h5 : Model that i save from training
* model_v1_10_0.982.h5 : Model that i save from training
* requirements.txt : requirement to run model_v1.ipynb or model_v2.ipynb
* make_folder.ipynb : To make train,validation,and test folder

For EDA , i referenced from this source :
* https://medium.com/geekculture/eda-for-image-classification-dcada9f2567a
* https://towardsdatascience.com/exploratory-data-analysis-ideas-for-image-classification-d3fc6bbfb2d2

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

