# Fungsi untuk menambahkan peserta baru oleh admin
def tambah_peserta(peserta):
    nama = input("Masukkan nama peserta: ")
    nilai = int(input("Masukkan nilai peserta: "))
    hasil = "Lolos" if nilai >= 75 else "Tidak Lolos"
    peserta.append({"Nama": nama, "Nilai": nilai, "Hasil": hasil})
    print("Data peserta berhasil ditambahkan!")
    return peserta

# Fungsi untuk mengedit nilai peserta oleh admin
def edit_nilai(peserta):
    id_peserta = int(input("Masukkan ID peserta yang ingin diubah nilainya: "))
    if id_peserta < len(peserta):
        new_nilai = int(input("Masukkan nilai baru: "))
        peserta[id_peserta]["Nilai"] = new_nilai
        peserta[id_peserta]["Hasil"] = "Lolos" if new_nilai >= 75 else "Tidak Lolos"
        print("Nilai peserta berhasil diubah!")
    else:
        print("ID peserta tidak valid.")
    return peserta

# Fungsi untuk peserta melihat nilai dan hasil akhir mereka
def lihat_nilai(peserta, id_peserta):
    if id_peserta < len(peserta):
        print(f"Nama: {peserta[id_peserta]['Nama']}")
        print(f"Nilai: {peserta[id_peserta]['Nilai']}")
        print(f"Hasil: {peserta[id_peserta]['Hasil']}")
    else:
        print("ID peserta tidak valid.")

# Fungsi utama yang menjalankan program
def main():
    peserta = []
    
    while True:
        print("\nSistem Informasi Peserta")
        print("1. Admin - Tambah Peserta")
        print("2. Admin - Edit Nilai Peserta")
        print("3. Peserta - Lihat Nilai dan Hasil Akhir")
        print("4. Keluar")
        
        choice = input("Pilih tindakan (1/2/3/4): ")
        
        if choice == "1":
            peserta = tambah_peserta(peserta)
        elif choice == "2":
            peserta = edit_nilai(peserta)
        elif choice == "3":
            id_peserta = int(input("Masukkan ID peserta: "))
            lihat_nilai(peserta, id_peserta)
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()