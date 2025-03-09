# Bike Sharing Dashboard

## Deskripsi
Project ini merupakan project Analisis Data menggunakan dataset Bike Sharing. Hasil analisis tersebut dibuat dalam bentuk Dashboard dengan platform Streamlit.

## Directory
- `/dashboard`: Berisikan file yang ditampilkan untuk dashboard dan 1 dataset yang telah dibersihkan
- `/data` : Menyimpan dataset yang digunakan untuk analisis (Bike Sharing Dataset)
- `Proyek_Analisis_Data (1).ipynb` : file jupyter notebook yang berisikan analisis data yang dilakukan
- `README.md` : file informasi tentang proyek ini
- `requirements.txt` : file yang berisikan library apa saja yang digunakan pada proyek ini
- `url.txt` : tautan untuk dashboard

## Menjalankan Dashboard (Instalasi)

Untuk menjalankan proyek ini, ikuti langkah-langkah berikut:

1. **Buat dan Aktifkan Virtual Environment**  
   Jalankan perintah berikut untuk membuat virtual environment:
   ```sh
   python -m venv venv
   ```
   
   Kemudian aktifkan virtual environment:
   - **Windows**:  
     ```sh
     venv\Scripts\activate
     ```
   - **Mac/Linux**:  
     ```sh
     source venv/bin/activate
     ```

2. **Instal Dependensi**  
   Setelah virtual environment aktif, instal semua dependensi yang diperlukan dengan menjalankan:
   ```sh
   pip install -r requirements.txt
   ```

3. **Menjalankan Dashboard**  
   Jalankan perintah berikut untuk memulai dashboard:
   ```sh
   streamlit run dashboard.py
   ```

4. **Keluar dari Virtual Environment**  
   Jika ingin keluar dari virtual environment, jalankan:
   ```sh
   deactivate
   ```

## Cara Menjalankan Projek

### Menjalankan Dashboard Streamlit
Untuk menjalankan dashboard interaktif, jalankan perintah berikut di direktori root:

```sh
streamlit run dashboard/dashboard.py
```
Dashboard akan terbuka secara otomatis di browser Anda.

### Menjalankan Jupyter Notebook
Untuk melihat analisis data secara lebih mendalam, jalankan Jupyter Notebook dengan perintah:


```sh
jupyter notebook Proyek_Analisis_Data (1).ipynb
```
Kemudian, buka file `Proyek_Analisis_Data (1).ipynb` melalui antarmuka web Jupyter Notebook yang terbuka.

