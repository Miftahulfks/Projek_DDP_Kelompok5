import tkinter as tk
from tkinter import ttk

def prediksi_cuaca(kota):
    prediksi = {
        'Jakarta': {'suhu_min': 25, 'suhu_max': 32, 'kondisi': 'Cerah'},
        'Bogor': {'suhu_min': 20, 'suhu_max': 25, 'kondisi': 'Hujan Sedang'},
        'Depok': {'suhu_min': 22, 'suhu_max': 28, 'kondisi': 'Berawan'},
        'Tangerang': {'suhu_min': 23, 'suhu_max': 30, 'kondisi': 'Cerah'},
        'Bekasi': {'suhu_min': 28, 'suhu_max': 35, 'kondisi': 'Panas'}
    }

    if kota in prediksi:
        return prediksi[kota]
    else:
        return None

def tampilkan_info_cuaca():
    kota_terpilih = combo_kota.get()
    prediksi = prediksi_cuaca(kota_terpilih)

    if prediksi:
        info_cuaca.set(f"Prediksi cuaca di {kota_terpilih}:\n"
                       f"Suhu Minimum: {prediksi['suhu_min']}°C\n"
                       f"Suhu Maksimum: {prediksi['suhu_max']}°C\n"
                       f"Kondisi: {prediksi['kondisi']}")
    else:
        info_cuaca.set("Pilih Dulu Lah!!!")

#GUI Tkinter
root = tk.Tk()
root.title("Aplikasi Ramalan Cuaca")


#Variabel StringVar untuk menyimpan informasi cuaca
info_cuaca = tk.StringVar()

#Label dan Combobox untuk memilih kota
label_kota = tk.Label(root, text="Mau Ramal Kota Mana?:")
label_kota.grid(row=0, column=0, pady=10)

combo_kota = ttk.Combobox(root, values=['Jakarta', 'Bogor', 'Depok', 'Tangerang', 'Bekasi'])
combo_kota.grid(row=0, column=1, pady=10)

#Tombol prediksi cuaca
tombol_ramal = tk.Button(root, text="Ramal Cuaca", command=tampilkan_info_cuaca)
tombol_ramal.grid(row=1, column=0, columnspan=2, pady=10)

#Label untuk menampilkan informasi cuaca
label_info_cuaca = tk.Label(root, textvariable=info_cuaca)
label_info_cuaca.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
