# Data Science Salaries Analysis and Dashboard

## Deskripsi
Proyek ini bertujuan untuk menganalisis data gaji profesi di bidang Data Science, memvisualisasikan hasil analisis, dan menyajikan dashboard interaktif menggunakan Streamlit. Dashboard ini memungkinkan pengguna untuk mengeksplorasi berbagai informasi terkait gaji berdasarkan berbagai faktor seperti rasio kerja remote, pengalaman, lokasi perusahaan, dan lainnya.

## Fitur
1. **Analisis Data**
   - Menganalisis hubungan antara pengalaman kerja dengan gaji.
   - Menghitung rata-rata gaji berdasarkan rasio kerja remote, ukuran perusahaan, jenis pekerjaan, dan lokasi perusahaan.
   - Menemukan pola penting dalam data, seperti faktor yang memengaruhi gaji secara signifikan.

2. **Visualisasi Data**
   - Membuat berbagai visualisasi seperti line plot, bar plot, dan box plot untuk menggambarkan hasil analisis.
   - Menyediakan representasi visual yang mudah dipahami oleh pengguna.

3. **Dashboard Interaktif**
   - Mengembangkan dashboard menggunakan Streamlit untuk menyajikan hasil analisis dan visualisasi.
   - Dashboard ini sudah dideploy sehingga dapat diakses secara online.

## Instalasi
### Prasyarat
Pastikan Anda memiliki Python 3.8 atau lebih baru serta virtual environment yang diaktifkan.

1. Clone repositori:
   ```bash
   git clone https://github.com/Adittt17/data_science_salaries.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd dashboard.py
   ```
3. Aktifkan virtual environment:
   ```bash
   source myenv/bin/activate  # Mac/Linux
   myenv\Scripts\activate   # Windows
   ```
4. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Lokally
1. Jalankan dashboard dengan perintah berikut:
   ```bash
   streamlit run dashboard.py
   ```
2. Dashboard akan tersedia di browser Anda di `http://localhost:8501`.

## Akses Dashboard yang Sudah Dideploy
Dashboard sudah dideploy dan dapat diakses melalui link berikut:
[**Data Science Salaries Dashboard**](https://adit-data-science-salaries.streamlit.app/)

## Visualisasi Utama
1. **Rata-rata Gaji Berdasarkan Rasio Remote**:
   - Menunjukkan bahwa pekerjaan onsite memiliki rata-rata gaji tertinggi, diikuti oleh pekerjaan full remote, dan hybrid di posisi terakhir.

2. **Distribusi Gaji Berdasarkan Tahun**:
   - Membandingkan distribusi gaji antar tahun untuk mengidentifikasi tren kenaikan atau penurunan.

3. **Pekerjaan dengan Gaji Tertinggi**:
   - Menampilkan 10 profesi di bidang Data Science dengan rata-rata gaji tertinggi.

4. **Hubungan Pengalaman dengan Gaji**:
   - Visualisasi hubungan langsung antara tingkat pengalaman (junior, mid-level, senior) dengan gaji rata-rata.

## Kontribusi
Kami menyambut kontribusi! Jika Anda memiliki ide atau ingin menambahkan fitur baru, silakan lakukan langkah berikut:
1. Fork repositori ini.
2. Buat branch baru untuk fitur Anda:
   ```bash
   git checkout -b fitur-baru
   ```
3. Commit perubahan Anda:
   ```bash
   git commit -m "Menambahkan fitur baru"
   ```
4. Push ke branch Anda:
   ```bash
   git push origin fitur-baru
   ```
5. Ajukan pull request.

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Anda bebas menggunakan, memodifikasi, dan mendistribusikan proyek ini dengan menyebutkan hak cipta asli.

