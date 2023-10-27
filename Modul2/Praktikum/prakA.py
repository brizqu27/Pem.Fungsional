def inputData(data_peserta, id, nama, nilai):
    peserta = {
        "id": id,
        "nama": nama,
        "nilai": nilai,
    }
    data_peserta.append(peserta)
    return data_peserta

def editData(data_peserta, inputId, new_nilai):
    peserta = next((data for data in data_peserta if data["id"] == inputId), None)
    if peserta:
        peserta["nilai"] = new_nilai
    return data_peserta

hitung_hasil_akhir = lambda nilai: sum(nilai) / len(nilai)

def showNilaiAdmin(peserta):
    if peserta:
        hasil_akhir = hitung_hasil_akhir(peserta["nilai"])
        return {
            "ID": peserta["id"],
            "Nama": peserta["nama"],
            "Nilai": peserta["nilai"],
            "Hasil Akhir": hasil_akhir
        }
    else:
        return "ID yang Anda masukkan tidak ditemukan."

def showNilai(peserta):
    if peserta:
        hasil_akhir = hitung_hasil_akhir(peserta["nilai"])
        pesan = "Selamat, anda lulus!" if hasil_akhir >= 75 else "Maaf, anda tidak lulus. Silakan perbaiki nilai anda."
        return {
            "ID": peserta["id"],
            "Nama": peserta["nama"],
            "Nilai": peserta["nilai"],
            "Hasil Akhir": hasil_akhir,
            "Pesan": pesan
        }
    else:
        return "ID yang Anda masukkan tidak ditemukan."

def findData(data_peserta, inputId):
    peserta = next((p for p in data_peserta if p["id"] == inputId), None)
    if peserta:
        return peserta
    return None

def main():
    data_peserta = []
    while True:
        print("Masukkan apakah kamu seorang admin atau peserta:")
        user = input()
        if user == "admin":
            print("1. Input Data")
            print("2. Edit Data")
            print("3. Find Data")
            pilih = int(input("Masukkan Pilihan: "))
            if pilih == 1:
                id = int(input("ID: "))
                nama = input("Nama: ")
                nilai = [float(x.strip()) for x in input("Nilai: ").split(",")]
                data_peserta = inputData(data_peserta, id, nama, nilai)
            elif pilih == 2:
                inputId = int(input("Masukkan ID yang ingin diedit: "))
                new_nilai = [float(x.strip()) for x in input("Nilai yang ingin dirubah: ").split(",")]
                peserta = findData(data_peserta, inputId)
                if peserta:
                    data_peserta = editData(data_peserta, inputId, new_nilai)
                else:
                    print("ID yang Anda masukkan tidak ditemukan.")
            elif pilih == 3:
                inputId = int(input("Masukkan ID yang ingin ditemukan: "))
                peserta = findData(data_peserta, inputId)
                if peserta:
                    data = showNilaiAdmin(peserta)
                    if isinstance(data, dict):
                        print("Data Peserta:")
                        print("ID:", data["ID"])
                        print("Nama:", data["Nama"])
                        print("nilai:", data["Nilai"])
                        print("hasil_akhir:", data["Hasil Akhir"])
                    else:
                        print(data)
                else:
                    print("ID yang Anda masukkan tidak ditemukan.")
            else:
                print("Salah input")
        elif user == "peserta":
            inputId = int(input("Masukkan ID Anda: "))
            peserta = findData(data_peserta, inputId)
            result = showNilai(peserta)
            if isinstance(result, dict):
                print("Data Peserta:")
                print("ID:", result["ID"])
                print("Nama:", result["Nama"])
                print("nilai:", result["Nilai"])
                print("hasil_akhir:", result["Hasil Akhir"])
                if "Pesan" in result:
                    print(result["Pesan"])
            else:
                print(result)
        elif user == "exit":
            break
        else:
            print("Yang Anda masukkan salah.")

if __name__ == "__main__":
    main()