# Buffalo Crime Dynamics

![Screenshot 2024-05-03 213047](https://github.com/user-attachments/assets/73e4fb4f-58b9-4757-b03a-8ccbc1cf157a)



A Machine Learning-powered application for crime prediction in Buffalo, NY, using real-time data scraping and advanced modeling techniques. This tool helps the public by forecasting crime hotspots based on historical data.

![Build Status](https://img.shields.io/badge/build-passing-blue)
![Python Version](https://img.shields.io/badge/python-3.8%2B-orange)
![License](https://img.shields.io/github/license/dianagudinho/BuffaloCrimeDynamics)

## Features
:white_check_mark: Real-time Crime Data: Uses real-time data scraping from the Socrata Open Data API.  

:white_check_mark: Predictive Modeling: Uses Logistic Regression and Random Forest classifiers to predict high and low crime areas.  

:white_check_mark:Interactive Visualizations: Displays crime trends and hotspots using visual tools like Streamlit, Matplotlib, and Seaborn.   

:white_check_mark: Accuracy: Achieved an accuracy of 94.66% with Random Forest on 300k crime records.  

:white_check_mark: User-friendly Interface: Built using Streamlit for easy interaction and data exploration.  

:white_check_mark: Technologies: Pandas, Sodapy, Scikit-Learn, Matplotlib, Seaborn  

## Installation
Prerequisites: `Python 3.8` or higher

### Setup Instructions  

> Dataset from Open Data Buffalo: <a href="https://data.buffalony.gov/Public-Safety/Crime-Incidents/d6g9-xbgu/data_preview">Data</a> (It also has API endpoint link)

> Link for the trained model can be downloded from here(`random_forest_model.pkl` file): <a href="https://drive.google.com/file/d/1Vn41YcJ9SgeZmqWflmDFlvRhMbj65jEN/view?usp=sharing">Download here</a>

Directory:
```
  . src
    ├── app.py                    
    ├── random_forest_model.pkl                   
    ├── buff_crime.ipynb                        
    └── requirements.txt
```
Clone the Repository:  
```bash

git clone https://github.com/dianagudinho/BuffaloCrimeDynamics.git
cd BuffaloCrimeDynamics

```
Install Dependencies: Make sure you are in the project directory and run:  

```bash

pip install -r requirements.txt

```
Run the App: Start the Streamlit app by running:  

```bash

streamlit run app.py

```

## Usage  
After installation, open the browser at `http://localhost:8501`. You will see the interface with options to:  

- Select Crime Type: Choose which crime category to predict.  

- Adjust Timeframe: Set the time window for predictions.  

- View Predictions: Interactive visualizations of crime trends, prediction accuracy, and mapped crime hotspots.  


## Technologies Used  
- Languages: `Python`
- Libraries:
  - Data Handling: `pandas`, `numpy` 
  - Visualization: `matplotlib`, `seaborn`  
  - Machine Learning: `scikit-learn`, `joblib`  
  - Data Scraping: `sodapy`, `Socrata Open Data API`  
  - UI: `Streamlit`  
- Machine Learning Models:  
  - Logistic Regression  
  - Random Forest  

## Project Architecture  

:page_facing_up: Data Scraping Module: Fetches real-time crime data from the Buffalo open data API.  

:chart_with_upwards_trend: Data Preprocessing: Cleans and processes crime data.  

:desktop_computer: Modeling Module: Trains ML models (Logistic Regression, Random Forest) to predict crime levels.  

:bar_chart:Visualization: Uses Streamlit and Seaborn for real-time crime mapping and trend visualization.  

### Contributing  
Contributions are welcome! To contribute:  

1. Fork the repository.
   
2. Create a new branch (`git checkout -b feature-name`).
   
3. Commit your changes (`git commit -m 'Add some feature'`).

4. Push to the branch (`git push origin feature-name`).
  
5. Create a Pull Request.  

## License
This project is licensed under the MIT License - see the LICENSE file for details.  

## Contact

Created by <a href="mailto:diagudinho@gmail.com">Diana Minine Gudinho</a> - feel free to contact me!  





