import json
import os
from typing import Dict, List, Any

# =====================================================================
# 👥 INHERITANCE: CLASS USER -> PENGURUS & SANTRI
# =====================================================================
class User:
    def __init__(self, username: str, nama: str, role: str) -> None:
        self.username: str = username
        self.nama: str = nama
        self.role: str = role
        self.__password: str = "pondok123" # Encapsulation: Private Attribute

    # Getter untuk password
    def cek_password(self, input_pass: str) -> bool:
        return self.__password == input_pass

    # Setter untuk password baru
    def ganti_password(self, pass_lama: str, pass_baru: str) -> None:
        if self.cek_password(pass_lama):
            self.__password = pass_baru
            print("✅ Password berhasil diubah!")
        else:
            print("❌ Password lama salah!")


class Pengurus(User):
    def __init__(self, username: str, nama: str) -> None:
        super().__init__(username, nama, "Pengurus")


class Santri(User):
    def __init__(self, username: str, nama: str, nis: str, saldo_awal: int = 0) -> None:
        super().__init__(username, nama, "Santri")
        self.nis: str = nis
        # Encapsulation: Saldo disembunyikan agar tidak bisa diubah ilegal dari luar class
        self.__saldo: int = saldo_awal 

    # PROPERTY (GETTER) untuk membaca saldo secara aman
    @property
    def saldo(self) -> int:
        return self.__saldo

    # METHOD untuk tambah saldo (Setor)
    def setor_tunai(self, jumlah: int) -> bool:
        if jumlah > 0:
            self.__saldo += jumlah
            return True
        return False

    # METHOD untuk kurangi saldo (Tarik)
    def tarik_tunai(self, jumlah: int) -> bool:
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False


# =====================================================================
# 🗄️ ENGINE SISTEM: MANAJEMEN DATABASE DATA (SAVE/LOAD JSON)
# =====================================================================
class BankSantriSystem:
    def __init__(self, file_path: str = "data_tabungan.json") -> None:
        self.file_path: str = file_path
        self.users: Dict[str, User] = {}
        self.load_data()

    def tambah_santri_baru(self, username: str, nama: str, nis: str, saldo_awal: int) -> None:
        if username in self.users:
            print("❌ Username sudah terdaftar!")
            return
        
        self.users[username] = Santri(username, nama, nis, saldo_awal)
        self.save_data()
        print(f"✅ Akun Tabungan Santri {nama} (NIS: {nis}) berhasil dibuat!")

    def save_data(self) -> None:
        # Mengubah object OOP menjadi bentuk teks JSON
        data_to_save: Dict[str, Any] = {}
        for username, obj in self.users.items():
            if isinstance(obj, Santri):
                data_to_save[username] = {
                    "role": "Santri", "nama": obj.nama, "nis": obj.nis, "saldo": obj.saldo
                }
            elif isinstance(obj, Pengurus):
                data_to_save[username] = {"role": "Pengurus", "nama": obj.nama}
        
        with open(self.file_path, "w") as f:
            json.dump(data_to_save, f, indent=4)

    def load_data(self) -> None:
        # Default Akun Pengurus jika file belum ada
        self.users["admin"] = Pengurus("admin", "Ustadz Admin")
        
        if not os.path.exists(self.file_path):
            return
            
        with open(self.file_path, "r") as f:
            try:
                data_terload = json.load(f)
                for username, info in data_terload.items():
                    if info["role"] == "Santri":
                        self.users[username] = Santri(username, info["nama"], info["nis"], info["saldo"])
                    elif info["role"] == "Pengurus" and username != "admin":
                        self.users[username] = Pengurus(username, info["nama"])
            except json.JSONDecodeError:
                pass


# =====================================================================
# 📋 INTERFACE: MAIN MENU CLI
# =====================================================================
def main() -> None:
    sys = BankSantriSystem()
    
    while True:
        print("\n======================================")
        print("   💻 SISTEM TABUNGAN DIGITAL PONDOK  ")
        print("======================================")
        print("1. Login")
        print("0. Keluar Aplikasi")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "0":
            print("👋 Syukron! Program selesai.")
            break
            
        if pilihan == "1":
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            
            if username in sys.users and sys.users[username].cek_password(password):
                user_aktif = sys.users[username]
                print(f"\n🟢 Login Berhasil! Selamat datang, {user_aktif.nama} ({user_aktif.role})")
                
                # MENU PENGURUS
                if isinstance(user_aktif, Pengurus):
                    while True:
                        print("\n--- MENU PENGURUS PONDOK ---")
                        print("1. Buka Rekening Santri Baru")
                        print("2. Lihat Semua Rekening")
                        print("0. Logout")
                        
                        sub_pilih = input("Pilih aksi: ")
                        if sub_pilih == "0": break
                        elif sub_pilih == "1":
                            u_baru = input("Masukkan Username Baru: ")
                            n_baru = input("Masukkan Nama Santri   : ")
                            nis_baru = input("Masukkan NIS Santri    : ")
                            try:
                                s_awal = int(input("Masukkan Saldo Awal    : Rp"))
                                sys.tambah_santri_baru(u_baru, n_baru, nis_baru, s_awal)
                            except ValueError:
                                print("❌ Error: Saldo awal harus berupa angka!")
                        elif sub_pilih == "2":
                            print("\n=== DAFTAR TABUNGAN SANTRI ===")
                            for u, obj in sys.users.items():
                                if isinstance(obj, Santri):
                                    print(f"👤 {obj.nama} (NIS: {obj.nis}) | Saldo: Rp{obj.saldo}")
                
                # MENU SANTRI
                elif isinstance(user_aktif, Santri):
                    while True:
                        print(f"\n--- MENU TABUNGAN SANTRI ({user_aktif.nama}) ---")
                        print(f"💰 Sisa Saldo Anda: Rp{user_aktif.saldo}")
                        print("1. Setor Tunai")
                        print("2. Tarik Tunai")
                        print("0. Logout")
                        
                        sub_pilih = input("Pilih aksi: ")
                        if sub_pilih == "0": break
                        elif sub_pilih == "1":
                            try:
                                nominal = int(input("Masukkan nominal setor: Rp"))
                                if user_aktif.setor_tunai(nominal):
                                    sys.save_data()
                                    print("✅ Setor tunai berhasil!")
                                else:
                                    print("❌ Nominal tidak valid!")
                            except ValueError:
                                print("❌ Input harus angka!")
                        elif sub_pilih == "2":
                            try:
                                nominal = int(input("Masukkan nominal tarik: Rp"))
                                if user_aktif.tarik_tunai(nominal):
                                    sys.save_data()
                                    print("✅ Tarik tunai berhasil!")
                                else:
                                    print("❌ Tarik gagal! Saldo tidak cukup atau input salah.")
                            except ValueError:
                                print("❌ Input harus angka!")
            else:
                print("❌ Username atau Password salah!")

if __name__ == "__main__":
    main()