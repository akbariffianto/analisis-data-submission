# Dicoding Collection Dashboard ✨

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```

# Proyek Analisis Kualitas Udara 🌍

## Setup Environment - Anaconda
```
conda create --name air-quality-analysis python=3.9
conda activate air-quality-analysis
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_kualitas_udara
cd proyek_analisis_kualitas_udara
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit
```
streamlit run app.py
```

## Deskripsi Proyek
### Proyek ini adalah analisis kualitas udara yang menggunakan data polutan dari berbagai stasiun. 
### Aplikasi ini memungkinkan pengguna untuk:
- Melihat tren kualitas udara sepanjang waktu.
- Menganalisis pengaruh hujan dan suhu terhadap polutan.
- Menggunakan clustering untuk memahami hubungan antara kecepatan angin dan PM2.5.

### Fitur Utama
- Visualisasi tren tahunan dan bulanan dari polutan.
- Analisis waktu berdasarkan jam untuk melihat kualitas udara.
- Pengaruh hujan terhadap kadar polutan.
- Korelasi antara suhu dan konsentrasi polutan.
- Clustering berdasarkan kecepatan angin dan PM2.5.
