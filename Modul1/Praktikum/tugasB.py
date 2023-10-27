list_buku = []
pelanggan = {}
user_log = [{"Username": "user1", "Password": "user123"},
            {"Username": "user2", "Password": "user123"},
            {"Username": "user3", "Password": "user123"}]


def login_admin():
    useradmin = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if useradmin == "admin" and password == "admin123":
        print("Login admin berhasil")
        return True
    else:
        print("Gagal Login. Username atau Password salah.")
        return False


def login_pengunjung():
    username = input("Username: ")
    password = input("Password: ")
    user_auth = next((user for user in user_log if user["Username"] == username and user["Password"] == password), None)
    if user_auth:
        print(f"Login Pengunjung berhasil sebagai {username}")
        return username
    else:
        print("Gagal Login pengunjung. Username atau Password salah.")
        return None


def tambah_buku():
    judul = input("Judul Buku    : ")
    penulis = input("Nama Penulis  : ")
    buku = {"Judul": judul, "Penulis": penulis, "Tersedia": True}
    list_buku.append(buku)
    print("\nBerhasil Ditambahkan!")


def pinjam_buku(id_user):
    if id_user not in pelanggan:
        pelanggan[id_user] = []

    print("Daftar Buku Tersedia : ")
    for i, buku in enumerate(list_buku):
        if buku["Tersedia"]:
            print(f"{i}. {buku['Judul']} oleh {buku['Penulis']}")

    pilihan = int(input("Pilihan buku yang ingin dipinjam (masukkan nomor buku): "))
    if 0 <= pilihan < len(list_buku) and list_buku[pilihan]["Tersedia"]:
        list_buku[pilihan]["Tersedia"] = False
        pelanggan[id_user].append(list_buku[pilihan])
        print("Buku berhasil dipinjam")
    else:
        print("Pilihan buku tidak valid / Buku tidak tersedia!")


def pengembalian_buku(id_user):
    if id_user in pelanggan and pelanggan[id_user]:
        print("Buku yang Anda Pinajm")
        print("\n")
        for i, buku in enumerate(pelanggan[id_user]):
            print(f"{i}. {buku['Judul']} oleh {buku['Penulis']}")

        if pelanggan[id_user]:
            pilihan = int(input("Masukkan No Buku : "))

            if 0 <= pilihan < len(pelanggan[id_user]):
                buku_dikembalikan = pelanggan[id_user].pop(pilihan)
                buku_dikembalikan["Tersedia"] = True
                print("Buku Telah Dikembalikan!")
                print("\n")
            else:
                print("Nomor Buku tidak valid")
                print("\n")
        else:
            print("Anda tidak memiliki buku yang dipinjam.")
            print("\n")
    else:
        print("Anda tidak memiliki buku yang dipinjam.")
        print("\n")


def list_buku_pinjam():
    print("Buku yang Sedang Dipinjam oleh Pengunjung : ")
    for pengunjung, buku_dipinjam in pelanggan.items():
        if buku_dipinjam:
            print(f"Pengunjung : {pengunjung}")
            for i, buku in enumerate(buku_dipinjam):
                print(f"{i}. {buku['Judul']} oleh {buku['Penulis']}")


def list_buku_dikembalikan():
    print("Buku yang Telah Dikembalikan oleh Pengunjung : ")
    for pengunjung, buku_dikembalikan in pelanggan.items():
        if not buku_dikembalikan:
            continue
        print(f"Pengunjung : {pengunjung}")
        for buku in buku_dikembalikan:
            print(f"- {buku['Judul']} oleh {buku['Penulis']}")


def menu_admin():
    print("\nMenu Admin")
    print("1. Input Buku")
    print("2. List Buku Dipinjam")
    print("3. List Buku Kembali")
    print("4. Kembali ke Menu Login")
    pilihan_admin = input("Pilih: ")
    if pilihan_admin == "1":
        tambah_buku()
    elif pilihan_admin == "2":
        list_buku_pinjam()
    elif pilihan_admin == "3":
        list_buku_dikembalikan()
    elif pilihan_admin == "4":
        return
    menu_admin()


def menu_pengunjung(username_pengunjung):
    print("\nMenu Pengunjung")
    print("1. Pinjam Buku")
    print("2. Pengembalian Buku")
    print("3. Kembali ke Menu")
    pilihan_pengunjung = input("Pilih: ")
    if pilihan_pengunjung == "1":
        pinjam_buku(username_pengunjung)
    elif pilihan_pengunjung == "2":
        pengembalian_buku(username_pengunjung)
    elif pilihan_pengunjung == "3":
        return
    menu_pengunjung(username_pengunjung)


pengunjung_terlogin = None

while True:
    print("\nLogin")
    print("1. Login Admin")
    print("2. Login Pengunjung")
    print("3. Keluar")

    choice = input("Pilih: ")
    if choice == "1":
        if login_admin():
            menu_admin()
    elif choice == "2":
        if pengunjung_terlogin is None:
            username_pengunjung = login_pengunjung()
            if username_pengunjung:
                pengunjung_terlogin = username_pengunjung
                menu_pengunjung(pengunjung_terlogin)
        else:
            menu_pengunjung(pengunjung_terlogin)
    elif choice == "3":
        exit(0)