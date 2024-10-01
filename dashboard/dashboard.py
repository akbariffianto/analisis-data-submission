import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("https://raw.githubusercontent.com/akbariffianto/analisis-data-submission/refs/heads/main/dashboard/main_data.csv")

st.title("Proyek Analisis Kualitas Udara")

st.sidebar.header('Pilihan Stasiun')

station_choice = st.sidebar.selectbox('Pilih Stasiun', df['station'].unique())
df = df[df['station'] == station_choice]

df['year'] = pd.to_datetime(df['year'], format='%Y').dt.year
df['month'] = pd.to_datetime(df['month'], format='%m').dt.month

pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

st.subheader('Distribusi polutan tiap bulan pada stasiun '+ station_choice)
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i, pollutant in enumerate(pollutants):
    monthly_avg = df.groupby('month')[pollutant].mean().reset_index()
    sns.lineplot(data=monthly_avg, x='month', y=pollutant, marker='o', ax=axs[i])
    axs[i].set_title(f'Distribusi {pollutant} Tiap Bulan')
    axs[i].set_xlabel('Bulan')
    axs[i].set_ylabel(f'Nilai Rata-rata {pollutant}')
    axs[i].set_xticks(range(1, 13))
    axs[i].set_xticklabels(month_names)

plt.tight_layout()
st.pyplot(fig)
st.subheader('Fluktuasi polutan di setiap jam pada satu hari')
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

for i, pollutant in enumerate(pollutants):
    hourly_avg = df.groupby('hour')[pollutant].mean().reset_index()
    sns.lineplot(data=hourly_avg, x='hour', y=pollutant, ax=axs[i])
    axs[i].set_title(f'Tren Rata-rata {pollutant} per Jam dalam Sehari')
    axs[i].set_xlabel('Jam')
    axs[i].set_ylabel(f'Rata-rata {pollutant}')

plt.tight_layout()
st.pyplot(fig)

st.subheader('Dampak tingkat hujan terhadap polutan')
rain_mean = df['RAIN'].mean()
df['rain_category'] = df['RAIN'].apply(lambda x: 'rendah' if x <= rain_mean else 'tinggi')

fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

for i, pollutant in enumerate(pollutants):
    sns.boxplot(x='rain_category', y=pollutant, data=df, ax=axs[i])
    axs[i].set_title(f'Pengaruh Hujan terhadap {pollutant}')
    axs[i].set_xlabel('Kategori Hujan')
    axs[i].set_ylabel(f'Nilai {pollutant}')

plt.tight_layout()
st.pyplot(fig)

st.subheader('Korelasi antara suhu tinggi dan peningkatan polutan')
fig, axs = plt.subplots(3, 2, figsize=(12, 12))
axs = axs.flatten()

for i, pollutant in enumerate(pollutants):
    sns.scatterplot(x='TEMP', y=pollutant, data=df, ax=axs[i])
    correlation = df['TEMP'].corr(df[pollutant])
    axs[i].set_title(f'Korelasi antara Suhu dan {pollutant} (Korelasi: {correlation:.2f})')
    axs[i].set_xlabel('Suhu (°C)')
    axs[i].set_ylabel(f'Konsentrasi {pollutant}')

plt.tight_layout()
st.pyplot(fig)

st.subheader('Clustering Hubungan Kecepatan Angin dengan Polutan PM2.5')

X = df[['WSPM', 'PM2.5']]
X = X.fillna(X.mean())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)
df['cluster'] = kmeans.labels_

fig, ax = plt.subplots()
sns.scatterplot(x='WSPM', y='PM2.5', hue='cluster', data=df, palette='viridis', ax=ax)
ax.set_title('Clustering PM2.5 dan Kecepatan Angin')
ax.set_xlabel('Kecepatan Angin')
ax.set_ylabel('PM2.5')
st.pyplot(fig)
