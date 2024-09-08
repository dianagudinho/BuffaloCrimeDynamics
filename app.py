import streamlit as st
import pandas as pd
import joblib
import base64
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
original_title = '<h1 style="font-family: serif; color:white; font-size: 50px;">Buffalo Crime Dynamics </h1>'

st.markdown(original_title, unsafe_allow_html=True)

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://www.shutterstock.com/image-photo/january-9th-2021-buffalo-ny-600nw-1898837020.jpg");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
    
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# Load the model
model = joblib.load('random_forest_model.pkl')

def calculate_weekday(day, month, year):
    input_date = datetime(year, month, day)
    return input_date.weekday()

def calculate_is_weekend(weekday):
    return int(weekday >= 5)

def calculate_week_of_year(day, month, year):
    input_date = datetime(year, month, day)
    return input_date.isocalendar()[1]

def predict_crime_level(input_data):
    input_df = pd.DataFrame([input_data])
    
    input_df['lat'] = 42.897 
    input_df['long'] = -78.879

    input_df['Weekday'] = calculate_weekday(input_data['Day'], input_data['Month'], input_data['Year'])
    input_df['IsWeekend'] = calculate_is_weekend(input_df['Weekday'])
    input_df['WeekOfYear'] = calculate_week_of_year(input_data['Day'], input_data['Month'], input_data['Year'])

    # Map incident type and district to encoded values
    incident_type_mapping = {
        'Agg Assault on Police Officer': 0, 'Aggr Assault': 1, 'Assault': 2, 'Breaking and Entering': 3, 'Bulgary': 4,
        'Crime Negligent Homicide': 5, 'Homicide': 6, 'Larcency/Theft': 7, 'Manslaughter': 8, 'Murder': 9,
        'Other Sexual Offense': 10, 'Rape': 11, 'Robbery': 12, 'Sexual Abuse': 13, 'Sexual Assulat': 14,
        'Theft': 15, 'Theft Of Services': 16, 'Theft Of Vehicle': 17, 'Uuv': 18
    }
    district_mapping = {
        'Delaware': 0, 'Ellicott': 1, 'Fillmore': 2, 'LoveJoy': 3, 'Masten': 4, 'Niagara': 5, 'North': 6,
        'South': 7, 'University': 8, 'Unknown': 9, 'None': 10
    }

    # Encode incident type and district
    input_df['incidentType'] = input_df['incidentType'].map(incident_type_mapping)
    input_df['district'] = input_df['district'].map(district_mapping)

    # Make prediction
    prediction = model.predict(input_df)
    return "High Crime" if prediction[0] == 1 else "Low Crime"

def main():

    zip_code = st.text_input("Zip Code", key="zip_code_input")
    
    date_selected = st.date_input("Select Date", key="date_input")
    year = date_selected.year
    month = date_selected.month
    day = date_selected.day
    
    hour = st.number_input("Hour", min_value=0, max_value=23, step=1, key="hour_input")

    incident_types = [ 'Agg Assault on Police Officer', 'Aggr Assault', 'Assault', 'Breaking and Entering', 'Bulgary',
        'Crime Negligent Homicide', 'Homicide', 'Larcency/Theft', 'Manslaughter', 'Murder',
        'Other Sexual Offense', 'Rape', 'Robbery', 'Sexual Abuse', 'Sexual Assulat',
        'Theft', 'Theft Of Services', 'Theft Of Vehicle', 'Uuv']
    incident_type = st.selectbox("Incident Type", incident_types, key="incident_type_select")

    district_options = ['Delaware', 'Ellicott', 'Fillmore', 'LoveJoy', 'Masten', 'Niagara', 'North',
        'South', 'University', 'Unknown', 'None']
    district = st.selectbox('Select District', district_options)

    if st.button('Predict Crime Level', key="predict_button"):
        input_data = {
            'zipCode': zip_code,
            'Year': year,
            'Month': month,
            'Day': day,
            'Hour': hour,
            'incidentType': incident_type,
            'district': district
        }
        result = predict_crime_level(input_data)
        st.success(f"The predicted crime level for ZIP {zip_code} on {year}-{month}-{day} at {hour}:00 with incident type {incident_type} is: {result}")

    st.write("<span style='color:white'>Crime Data Insights</span>", unsafe_allow_html=True)

    @st.cache_data
    def load_data():
        return pd.read_csv('file.csv')

    data = load_data()
    
    # Filter data for last year
    last_year_data = data[data['year'] == (year - 1)]

    st.write(f"<span style='color:white'>Number of crimes in the last year: {len(last_year_data)}</span>", unsafe_allow_html=True)

    # Plotting graphs
    st.write("<span style='color:white'>Crime Type Distribution</span>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.countplot(data['parentIncidentType'], ax=ax)
    st.pyplot(fig)

    st.write("<span style='color:white'>Crime Occurrence by District</span>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data['councilDistrict'], ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write("<span style='color:white'>Crime Occurrences by Hour of the Day</span>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots()
    sns.histplot(data['hour'], bins=24, kde=False, ax=ax3)
    ax3.set_title('Crime Occurrences by Hour')
    ax3.set_xlabel('Hour of the Day')
    ax3.set_ylabel('Crime Count')
    st.pyplot(fig3)

if __name__ == '__main__':
    main()
