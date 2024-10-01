import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

all_df = pd.read_csv("./data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
all_df = all_df.interpolate(method='linear')
all_df.dropna(subset=['wd'], inplace=True)

st.sidebar.title("Filter Options")

# Filter by year
year_selected = st.sidebar.selectbox("Select Year", all_df['year'].unique())

# Filter by pollutant
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
pollutant_selected = st.sidebar.selectbox("Select Pollutant", pollutants)

# Filter data based on selected year
filtered_data = all_df[all_df['year'] == year_selected]

# Check if 'hour' column exists
if 'hour' in filtered_data.columns:
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='hour', y=pollutant_selected, ax=ax)
    ax.set_title(f'Trend of {pollutant_selected} in {year_selected}')
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel(f'Average {pollutant_selected}')
    st.pyplot(fig)
else:
    st.error("The 'hour' column is missing from the dataset. Please check the data.")

# Show descriptive statistics
if st.checkbox("Show Descriptive Statistics"):
    st.write(filtered_data.describe())

# Correlation heatmap
st.subheader("Correlation Heatmap")
corr = filtered_data[pollutants].corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax2)
st.pyplot(fig2)
