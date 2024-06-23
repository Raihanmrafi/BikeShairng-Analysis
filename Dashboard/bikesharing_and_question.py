import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project Information
st.title('Proyek Akhir Belajar Analisis Data dengan Python (Bike Sharing)')
st.write("""
- **Nama:** Raihan Muhammad Rafi
- **Email:** [raihanmuhammad3073@gmail.com]
- **ID Dicoding:** ggraihan
""")

## Menentukan Pertanyaan Bisnis
st.header('Menentukan Pertanyaan Bisnis')

st.write("""
- What is the comparison of the number of bike renters with casual status and bike renters with registered status in each month?
- Does windspeed level influence the usage of bike rentals?
""")

## Melakukan Import Pada Semua Packages/Library yang Digunakan
st.header('Melakukan Import Pada Semua Packages/Library yang Digunakan')

# Load data
@st.cache
def load_data():
    day_df = pd.read_csv('day.csv')
    hour_df = pd.read_csv('hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Data Wrangling
st.subheader('Data Wrangling')

# Assessing Data
st.subheader('Assessing Data')
st.write("Missing values in day data:")
st.write(day_df.isnull().sum())
st.write("\nMissing values in hour data:")
st.write(hour_df.isnull().sum())

st.write("\nDuplicated rows in day data:")
st.write(day_df.duplicated().sum())
st.write("\nDuplicated rows in hour data:")
st.write(hour_df.duplicated().sum())

# Exploratory Data Analysis (EDA)
st.subheader('Exploratory Data Analysis (EDA)')

# Explore ...
st.write("Statistics for day_df:")
st.write(day_df.describe())

st.write("Statistics for hour_df:")
st.write(hour_df.describe())

# Visualization & Explanatory Analysis
st.subheader('Visualization & Explanatory Analysis')

# Comparison of the number of bike renters with casual status and bike renters with registered status in each month
st.subheader('Comparison of Casual and Registered Users Monthly')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['month'] = day_df['dteday'].dt.month
monthly_data = day_df.groupby('month')[['casual', 'registered']].sum()

plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data['casual'], label='Casual Users', marker='o')
plt.plot(monthly_data.index, monthly_data['registered'], label='Registered Users', marker='o')
plt.title('Comparison of Casual and Registered Users Monthly')
plt.xlabel('Month')
plt.ylabel('Total Count of Users')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
st.pyplot()

# Does windspeed affect the number of bike rentals
st.subheader('Wind Speed vs. Bike Rentals')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='cnt', data=day_df, alpha=0.6)
plt.title('Wind Speed vs. Bike Rentals')
plt.xlabel('Wind Speed')
plt.ylabel('Count of Total Bike Rentals')
plt.grid(True)
st.pyplot()

# Conclusion
st.header('Conclusion')
st.write("""
1. The conclusion of question 1 is that the number of registered bike renters is always higher than casual bike renters. However, towards the end of the year, there is a decreasing trend in the number of both casual and registered renters.
2. The conclusion of question 2 is that wind speed affects the number of bike renters. The higher the wind speed, the fewer bike renters there are.
""")
