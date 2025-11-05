#  California House Price Predictor ML APP

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![Powered by Scikit-Learn](https://img.shields.io/badge/ML-Library-Scikit--Learn-f7931e.svg)](https://scikit-learn.org/)
[![Flask Web App](https://img.shields.io/badge/Backend-Flask-lightgreen.svg)](https://flask.palletsprojects.com/)
[![Deployed on Render](https://img.shields.io/badge/Deployed-on%20Render-purple.svg)](https://render.com/)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

---
### Tech Stack
Layer                           Technologies
Frontend         ---->           HTML,CSS,JavaScript

Backend          ---->           Flask(Python)

ML Model         ---->           Scikit-Learn,Ridge-Regression,Polynomial Features

Contanerization  ---->           Docker

Deployment       ---->           Render(Free Tier)

Tools            ---->           Joblib/Pickle,Gunicorn,Numpy,


###  Overview

An **end-to-end Machine Learning web application** that predicts median California house prices using features such as median income, population, latitude, longitude, and housing characteristics.  
Built with **Flask**, trained using **Polynomial Ridge Regression**, and integrated with a HTML/CSS frontend.  

 **Key Highlights**
- End-to-end ML pipeline (data → model → web → deployment)
- Responsive prediction form built with HTML + CSS + JavaScript  
- Trained on the *California Housing Dataset (Sklearn)*  
- Deployed live on **Render** for instant access  
- Fully **Dockerized** for easy container deployment on any platform (AWS, GCP, Railway, etc.)

---

###  Live Demo

🔗 **[Visit Live App on Render](https://california-house-price-predictor-0s0h.onrender.com/)**  
*(Deployed using Render)*

---

###  Docker Deployment

This project also includes a **Dockerfile** for containerized deployment.

Build and run locally:
'''
docker build -t california-house-app .
docker run -p 5000:5000 -e PORT=5000 california-house-app
Access at: http://localhost:5000

---

### Preview

![Homepage](https://raw.githubusercontent.com/Piyush5057/californiaHousePricing/main/static/home.png)
![Prediction Result](https://raw.githubusercontent.com/Piyush5057/californiaHousePricing/main/static/result.png)
