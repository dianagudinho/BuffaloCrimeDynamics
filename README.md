# BuffaloCrimeDynamics

A machine learning-powered application for crime prediction in Buffalo, NY, using real-time data scraping and advanced modeling techniques. This tool helps law enforcement and the public by forecasting crime hotspots based on historical data.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technologies](#technologies)
5. [Project Architecture](#project-architecture)
6. [Screenshots](#screenshots)
7. [License](#license)
8. [Contact](#contact)


Features
Real-time Crime Data: Uses real-time data scraping from the Socrata Open Data API.
Predictive Modeling: Uses Logistic Regression and Random Forest classifiers to predict high and low crime areas.
Interactive Visualizations: Displays crime trends and hotspots using visual tools like Streamlit, Matplotlib, and Seaborn.
Accuracy: Achieved an accuracy of 94.66% with Random Forest on 300k crime records.
User-friendly Interface: Built using Streamlit for easy interaction and data exploration.
Technologies: Pandas, Sodapy, Scikit-Learn, Matplotlib, Seaborn

Technologies Used
Languages: Python
Libraries:
Data Handling: pandas, numpy
Visualization: matplotlib, seaborn
Machine Learning: scikit-learn, joblib
Data Scraping: sodapy, Socrata Open Data API
UI: Streamlit
Machine Learning Models:
Logistic Regression
Random Forest

Project Architecture
Provide an architectural overview of the project, describing how the different components interact.

Data Scraping Module: Fetches real-time crime data from the Buffalo open data API.
Data Preprocessing: Cleans and processes crime data.
Modeling Module: Trains ML models (Logistic Regression, Random Forest) to predict crime levels.
Visualization: Uses Streamlit and Seaborn for real-time crime mapping and trend visualization.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Create a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Created by Diana Minine Gudinho - feel free to contact me!





