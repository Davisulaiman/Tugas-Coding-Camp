import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("./Dashboard/main_data.csv")
    df['date'] = pd.to_datetime(df['date'])  # Konversi kolom date ke datetime
    return df

df = load_data()

# Sidebar
st.sidebar.title("Dashboard Penyewaan Sepeda")
st.sidebar.subheader("Pilih Rentang Tanggal")

# Pastikan hanya memilih tahun 2011 dan 2012
min_date = df['date'].min()
max_date = df['date'].max()
if min_date.year < 2011:
    min_date = pd.Timestamp("2011-01-01")
if max_date.year > 2012:
    max_date = pd.Timestamp("2012-12-31")

start_date = st.sidebar.date_input("Dari Tanggal", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("Sampai Tanggal", max_date, min_value=min_date, max_value=max_date)

# Filter data berdasarkan rentang tanggal
df_filtered = df[(df['date'] >= pd.Timestamp(start_date)) & (df['date'] <= pd.Timestamp(end_date))]
st.sidebar.write(f"Menampilkan data dari {start_date} hingga {end_date}")

section = st.sidebar.radio("Pilih Analisis:", [
    "Waktu Puncak Penyewaan", "Pengaruh Musim", "Pengaruh Suhu, Cuaca & Kelembapan",
    "Performa", "Kategori Pengguna", "Clustering", "RFM Analysis"
])

# Analisis Waktu Puncak Penyewaan
if section == "Waktu Puncak Penyewaan":
    st.header("Analisis Waktu Puncak Penyewaan Sepeda")
    
    # Hari dengan penyewaan terbanyak
    day_rentals = df_filtered.groupby('one_week')['count_rental'].sum().reset_index()
    busiest_day = day_rentals.loc[day_rentals['count_rental'].idxmax()]
    
    st.subheader("📅 Hari dengan Penyewaan Terbanyak")
    st.write(f"Hari dengan penyewaan terbanyak: **{busiest_day['one_week']}** dengan total **{busiest_day['count_rental']:,}** penyewaan.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='one_week', y='count_rental', data=day_rentals, palette='Blues', ax=ax)
    st.pyplot(fig)
    
    # Jam dengan penyewaan terbanyak
    hour_rentals = df_filtered.groupby('hour')['count_rental'].sum().reset_index()
    busiest_hour = hour_rentals.loc[hour_rentals['count_rental'].idxmax()]
    
    st.subheader("⏰ Jam dengan Penyewaan Terbanyak")
    st.write(f"Jam dengan penyewaan terbanyak: **{busiest_hour['hour']}** dengan total **{busiest_hour['count_rental']:,}** penyewaan.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='hour', y='count_rental', data=hour_rentals, palette='Oranges', ax=ax)
    st.pyplot(fig)
    
    # Kombinasi Hari & Jam
    peak_time_df = df_filtered.groupby(['one_week', 'hour'])['count_rental'].sum().reset_index()
    peak_time = peak_time_df.loc[peak_time_df['count_rental'].idxmax()]
    
    st.subheader("📅⏰ Hari & Jam dengan Penyewaan Terbanyak")
    st.write(f"Waktu puncak: **{peak_time['one_week']}** pukul **{peak_time['hour']}** dengan total **{peak_time['count_rental']:,}** penyewaan.")
    pivot_table = peak_time_df.pivot_table(index='one_week', columns='hour', values='count_rental', fill_value=0)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot_table, cmap='YlGnBu', annot=False, linewidths=0.5, ax=ax)
    st.pyplot(fig)

# Analisis Pengaruh Musim
elif section == "Pengaruh Musim":
    st.header("Pengaruh Musim terhadap Penyewaan Sepeda")
    season_rentals = df_filtered.groupby('season')['count_rental'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='season', y='count_rental', data=season_rentals, palette='coolwarm', ax=ax)
    st.pyplot(fig)

# Pengaruh Suhu, Cuaca & Kelembapan
elif section == "Pengaruh Suhu, Cuaca & Kelembapan":
    st.header("Pengaruh Faktor Lingkungan terhadap Penyewaan Sepeda")
    
    # Suhu
    st.subheader("🌡️ Pengaruh Suhu")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df_filtered['temp'], y=df_filtered['count_rental'], alpha=0.6, ax=ax)
    ax.set_xlabel("Suhu (°C)")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
    # Cuaca
    st.subheader("🌦️ Pengaruh Cuaca")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='weather_condition', y='count_rental', data=df_filtered, palette="coolwarm", ax=ax)
    st.pyplot(fig)
    
    # Kelembapan
    st.subheader("💧 Pengaruh Kelembapan")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=df_filtered['humidity'], y=df_filtered['count_rental'], alpha=0.6, ax=ax)
    ax.set_xlabel("Kelembapan (%)")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Performa
elif section == "Performa":
    st.header("📊 Performa Penyewaan Sepeda")
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])
    monthly_counts = df_filtered.groupby(df_filtered['date'].dt.to_period("M"))['count_rental'].sum()
    plt.figure(figsize=(24, 8))
    plt.scatter(monthly_counts.index.astype(str), monthly_counts.values, c="blue", s=10, marker='o')
    plt.plot(monthly_counts.index.astype(str), monthly_counts.values)
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan')
    plt.title('Grafik Performa Penyewaan Sepeda per Bulan')
    st.pyplot(plt)


# Kategori Pengguna
elif section == "Kategori Pengguna":
    st.header("Analisis Kategori Pengguna")
    total_casual = df_filtered['casual'].sum()
    total_registered = df_filtered['registered'].sum()
    fig, ax = plt.subplots()
    ax.pie([total_casual, total_registered], labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=["red", "blue"])
    st.pyplot(fig)

elif section == "Clustering":
    st.header("Analisis Clustering Penyewaan Sepeda")
    bins = [0, 2000, 4000, 6000, 10000]
    labels = ['Low', 'Medium', 'High', 'Very High']
    df_filtered['rental_category'] = pd.cut(df_filtered['count_rental'], bins=bins, labels=labels)
    st.write(df_filtered['rental_category'].value_counts())

    # Clustering manual berdasarkan jumlah peminjaman sepeda
    st.subheader("Clustering Manual Berdasarkan Jumlah Peminjaman Sepeda")
    
    # Total penyewa berdasarkan season
    st.write("### Total Penyewa Berdasarkan Musim")
    st.write(df_filtered.groupby("season")['count_rental'].nunique().sort_values(ascending=False))
    
    # Total penyewa berdasarkan weather_condition
    st.write("### Total Penyewa Berdasarkan Kondisi Cuaca")
    st.write(df_filtered.groupby("weather_condition")['count_rental'].nunique().sort_values(ascending=False))
    
    # Total penyewa berdasarkan category_days (weekdays vs weekend)
    st.write("### Total Penyewa Berdasarkan Weekdays dan Weekend")
    st.write(df_filtered.groupby("category_days").agg({"count_rental": ["count"]}))
    
    # Total penyewa berdasarkan humidity_category
    st.write("### Total Penyewa Berdasarkan Kategori Kelembapan")
    st.write(df_filtered.groupby("humidity_category").agg({"count_rental": ["count"]}))
    
# RFM Analysis Manual
elif section == "RFM Analysis":
    st.header("📊 Analisis RFM Penyewaan Sepeda")
    current_date = df_filtered['date'].max()
    
    rfm_df = df_filtered.groupby('registered').agg({
        'date': lambda x: (current_date - x.max()).days,
        'instant': 'count',
        'count_rental': 'sum'
    }).reset_index()
    
    rfm_df.columns = ['registered', 'recency', 'frequency', 'monetary']
    st.write(rfm_df.head())
    
    rfm_df = df_filtered.groupby('date').agg({
        'count_rental': 'sum'
    }).reset_index()
    
    rfm_df['recency'] = (rfm_df['date'].max() - rfm_df['date']).dt.days
    rfm_df['frequency'] = 1
    rfm_df['monetary'] = rfm_df['count_rental']
    st.write(rfm_df.head())
