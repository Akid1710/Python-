# Import library prettytable untuk nilai plus (pastikan sudah install: pip install prettytable)
from prettytable import PrettyTable

# 🧩 STRUKTUR DATA (WAJIB)
data_siswa = []

# Fungsi Otomatis untuk generate ID biar tidak bentrok
def generate_id():
    if not data_siswa:
        return 1
    return max(siswa['id'] for siswa in data_siswa) + 1

# 🛠️ FUNGSI 1: Tambah Data
def tambah_data():
    print("\n--- TAMBAH DATA SISWA ---")
    nama = input("Masukkan Nama  : ")
    kelas = input("Masukkan Kelas : ")
    
    # Bungkus dalam dictionary sesuai instruksi
    siswa_baru = {
        "id": generate_id(),
        "nama": nama,
        "kelas": kelas
    }
    
    data_siswa.append(siswa_baru)
    print(f"✅ Data {nama} berhasil ditambahkan!")

# 🛠️ FUNGSI 2: Tampilkan Data
def tampil_data():
    print("\n--- DATA SISWA ---")
    if not data_siswa:
        print("❌ Belum ada data tersimpan.")
        return
    
    # Menggunakan PrettyTable untuk nilai plus
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Kelas"]
    
    for siswa in data_siswa:
        tabel.add_row([siswa["id"], siswa["nama"], siswa["kelas"]])
        
    print(tabel)

# 🛠️ FUNGSI 3: Ubah Data
def ubah_data():
    print("\n--- UBAH DATA SISWA ---")
    tampil_data()
    if not data_siswa:
        return
        
    try:
        id_cari = int(input("Masukkan ID siswa yang ingin diubah: "))
    except ValueError:
        print("❌ ID harus berupa angka!")
        return
        
    for siswa in data_siswa:
        if siswa["id"] == id_cari:
            print(f"Data ditemukan: {siswa['nama']} ({siswa['kelas']})")
            nama_baru = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            kelas_baru = input("Masukkan Kelas baru (kosongkan jika tidak diubah): ")
            
            if nama_baru:
                siswa["nama"] = nama_baru
            if kelas_baru:
                siswa["kelas"] = kelas_baru
                
            print("✅ Data berhasil diperbarui!")
            return
            
    print("❌ ID tidak ditemukan.")

# 🛠️ FUNGSI 4: Hapus Data
def hapus_data():
    print("\n--- HAPUS DATA SISWA ---")
    tampil_data()
    if not data_siswa:
        return
        
    try:
        id_cari = int(input("Masukkan ID siswa yang ingin dihapus: "))
    except ValueError:
        print("❌ ID harus berupa angka!")
        return
        
    for siswa in data_siswa:
        if siswa["id"] == id_cari:
            data_siswa.remove(siswa)
            print(f"✅ Data siswa dengan ID {id_cari} berhasil dihapus!")
            return
            
    print("❌ ID tidak ditemukan.")

# 📋 MENU UTAMA (Menggunakan WHILE dan IF)
while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")
    
    pilihan = input("Pilih menu (0-4): ")
    
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("👋 Terima kasih! Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid! Silakan pilih 0-4.")