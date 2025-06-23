import streamlit as st
import joblib
import numpy as np

model = joblib.load("model_pip.pkl")

pekerjaan_options = ['Buruh Harian Lepas', 'Nelayan', 'Petani', 'Pedagang', 'PNS', 'lainnya',
                     'TNI/Polisi', 'Guru', 'Wiraswasta', 'Tidak Bekerja', 'Sudah Meninggal']

pendidikan_options = ['Tidak Sekolah', 'SD', 'SMP', 'SMA', 'D1', 'D2', 'D3', 'S1', 'S2']

transportasi_options = ['Jalan Kaki', 'Motor', 'Mobil', 'Angkutan Umum', 'Perahu', 'Sepeda']

# Ganti dengan frekuensi sebenarnya dari data kamu
kecamatan_freq_map = {
    'Kambu': 0.12, 'Mandonga': 0.10, 'Puuwatu': 0.08, 'Kadia': 0.07, 'Wua-Wua': 0.05
    # tambah kecamatan lain sesuai frekuensi dari dataset
}

st.title("Prediksi Kerentanan Putus Sekolah")

Penerima_KIP = st.selectbox("Penerima KIP", ['Ya', 'Tidak'])
Penerima_KPS = st.selectbox("Penerima KPS", ['Ya', 'Tidak'])
Pekerjaan_Ibu = st.selectbox("Pekerjaan Ibu", pekerjaan_options)
Jenjang_Pendidikan_Ayah = st.selectbox("Jenjang Pendidikan Ayah", pendidikan_options)
Penghasilan_Ibu = st.number_input("Penghasilan Ibu (dalam rupiah)", step=100000)
Jenjang_Pendidikan_Ibu = st.selectbox("Jenjang Pendidikan Ibu", pendidikan_options)
Pekerjaan_Ayah = st.selectbox("Pekerjaan Ayah", pekerjaan_options)
Jarak = st.number_input("Jarak Rumah ke Sekolah (KM)", step=0.1)
Penghasilan_Ayah = st.number_input("Penghasilan Ayah (dalam rupiah)", step=100000)
Alat_Transportasi = st.selectbox("Alat Transportasi", transportasi_options)
Kecamatan = st.selectbox("Kecamatan", list(kecamatan_freq_map.keys()))

if st.button("Prediksi"):
    input_data = np.array([[
        1 if Penerima_KIP == 'Ya' else 0,
        1 if Penerima_KPS == 'Ya' else 0,
        pekerjaan_options.index(Pekerjaan_Ibu),
        pendidikan_options.index(Jenjang_Pendidikan_Ayah),
        Penghasilan_Ibu,
        pendidikan_options.index(Jenjang_Pendidikan_Ibu),
        pekerjaan_options.index(Pekerjaan_Ayah),
        Jarak,
        Penghasilan_Ayah,
        transportasi_options.index(Alat_Transportasi),
        kecamatan_freq_map[Kecamatan]
    ]])

    prediction = model.predict(input_data)[0]
    label = "Rentan" if prediction == 1 else "Tidak Rentan"
    st.success(f"Hasil Prediksi: {label}")
