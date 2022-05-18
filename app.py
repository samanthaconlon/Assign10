###Do I need to just run the one .py file?
###Should I be sorting by population (for map?)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

###slicer code
#is nan supposed to be an option on the side drop down menu
st.title('California Housing Data (1990) by Samantha Conlon')
df = pd.read_csv('housingA10.csv')
st.subheader('See more filters in the sidebar:')
#question: picture has 200,000 but it says to put mean in the notes (198435.7), median (170700.0)
#question: when I did median_house_value.describe() it says type float, but the pic doesnt have float labels ?

value_filter = st.slider(('Median House Price'), 0.00, 500001.00, 200000.00)

###map code
st.map(df)

###sidebar code
prox_filter = st.sidebar.multiselect(
    'Choose location type',
    df.ocean_proximity.unique())

df=df[df.median_house_value <= value_filter]
df=df[df.ocean_proximity.isin(prox_filter)]

income_filter = st.sidebar.radio(
    "Choose income level",
    ("Low", "Medium", "High"))
if income_filter == 'Low':
    df= df[df.median_income<= 2.5]
elif income_filter == 'Medium':
    df=df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]
    
###histogram code
st.subheader('Histogram of the Median House Value')
fig, ax=plt.subplots()
ax.hist([df.median_house_value], bins=30)
st.pyplot(fig)