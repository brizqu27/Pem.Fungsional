def konversi_menit(minggu, hari, jam, menit):
    total_menit = (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
    return total_menit

def konversi_waktu(data):
    # Membagi string data menjadi komponen minggu, hari, jam, dan menit
    komponen = data.split()
    minggu = int(komponen[0])
    hari = int(komponen[2])
    jam = int(komponen[4])
    menit = int(komponen[6])
    
    # Menggunakan fungsi konversi_menit untuk mengkonversi ke menit
    total_menit = konversi_menit(minggu, hari, jam, menit)
    return total_menit

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk memeriksa apakah suatu karakter adalah angka
def is_integer(char):
    return char.isdigit()

# Menggunakan list comprehension untuk memisahkan dan menyaring nilai integer
data_integer = [list(filter(is_integer, item.split())) for item in data]

print()
print("=== HASIL INTERGER ===")
print()
# Menampilkan data masukan dan hasil yang telah diambil
for i in range(len(data)):
    print("Data inputan:", data[i])
    print("Data yang diambil:", data_integer[i])
    print()
