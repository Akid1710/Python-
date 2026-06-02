# =========================
# CLASS USER
# =========================
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password  # dikunci
        self.role = role

    def cek_password(self, password):
        return self.__password == password


# =========================
# CLASS SANTRI
# =========================
class Santri(User):
    def __init__(self, username, password, nis):
        super().__init__(username, password, "santri")
        self.nis = nis

    def ajukan_izin(self):
        print("\n--- FORM IZIN ---")
        alasan = input("Alasan izin   : ")
        tanggal = input("Tanggal izin  : ")
        jam = input("Jam keluar    : ")

        izin = Izin(self.username, alasan, tanggal, jam)
        return izin


# =========================
# CLASS MUSYRIF
# =========================
class Musyrif(User):
    def __init__(self, username, password):
        super().__init__(username, password, "musyrif")

    def proses_izin(self, izin):
        print("\n--- PROSES IZIN ---")
        print("Nama   :", izin.nama)
        print("Alasan :", izin.alasan)
        print("Tanggal:", izin.tanggal)
        print("Jam    :", izin.jam)
        print("Status :", izin.status)

        print("\n1. Setujui")
        print("2. Tolak")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            izin.setujui()
        elif pilihan == "2":
            izin.tolak()


# =========================
# CLASS IZIN
# =========================
class Izin:
    def __init__(self, nama, alasan, tanggal, jam):
        self.nama = nama
        self.alasan = alasan
        self.tanggal = tanggal
        self.jam = jam
        self.status = "Pending"

    def setujui(self):
        self.status = "Disetujui"

    def tolak(self):
        self.status = "Ditolak"


# =========================
# PROGRAM UTAMA
# =========================
santri = Santri("ahmad", "123", "S001")
musyrif = Musyrif("ustadz", "admin")

izin_list = []

print("=== SISTEM PERIZINAN KELUAR ===")
username = input("Username: ")
password = input("Password: ")

user = None

if username == santri.username and santri.cek_password(password):
    user = santri
elif username == musyrif.username and musyrif.cek_password(password):
    user = musyrif
else:
    print("Login gagal!")

# JIKA LOGIN BERHASIL
if user:
    print("\nLogin sebagai:", user.role)

    if user.role == "santri":
        izin = user.ajukan_izin()
        izin_list.append(izin)
        print("\nIzin berhasil diajukan")
        print("Status:", izin.status)

    elif user.role == "musyrif":
        if not izin_list:
            print("Belum ada izin masuk.")import json
import os

# =========================
# CLASS USER
# =========================
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self.role = role

    def cek_password(self, password):
        return self.__password == password


# =========================
# CLASS SANTRI
# =========================
class Santri(User):
    def __init__(self, username, password, nis):
        super().__init__(username, password, "santri")
        self.nis = nis

    def ajukan_izin(self):
        alasan = input("Alasan izin  : ")
        tanggal = input("Tanggal     : ")
        jam = input("Jam keluar  : ")

        return Izin(self.username, alasan, tanggal, jam)


# =========================
# CLASS MUSYRIF
# =========================
class Musyrif(User):
    def __init__(self, username, password):
        super().__init__(username, password, "musyrif")

    def proses_izin(self, izin):
        print("\n--- DETAIL IZIN ---")
        print("Nama   :", izin.nama)
        print("Alasan :", izin.alasan)
        print("Tanggal:", izin.tanggal)
        print("Jam    :", izin.jam)
        print("Status :", izin.status)

        print("\n1. Setujui")
        print("2. Tolak")
        pilih = input("Pilih: ")

        if pilih == "1":
            izin.status = "Disetujui"
        elif pilih == "2":
            izin.status = "Ditolak"


# =========================
# CLASS IZIN
# =========================
class Izin:
    def __init__(self, nama, alasan, tanggal, jam, status="Pending"):
        self.nama = nama
        self.alasan = alasan
        self.tanggal = tanggal
        self.jam = jam
        self.status = status

    def to_dict(self):
        return {
            "nama": self.nama,
            "alasan": self.alasan,
            "tanggal": self.tanggal,
            "jam": self.jam,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Izin(
            data["nama"],
            data["alasan"],
            data["tanggal"],
            data["jam"],
            data["status"]
        )


# =========================
# SAVE & LOAD FILE
# =========================
FILE = "izin.json"

def load_izin():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        data = json.load(f)
        return [Izin.from_dict(i) for i in data]

def save_izin(izin_list):
    with open(FILE, "w") as f:
        json.dump([i.to_dict() for i in izin_list], f, indent=4)


# =========================
# PROGRAM UTAMA
# =========================
santri = Santri("ahmad", "123", "S001")
musyrif = Musyrif("ustadz", "admin")

izin_list = load_izin()

while True:
    print("\n=== SISTEM PERIZINAN KELUAR ===")
    print("1. Login")
    print("2. Keluar")
    menu = input("Pilih: ")

    if menu == "2":
        save_izin(izin_list)
        print("Data disimpan. Selesai.")
        break

    username = input("Username: ")
    password = input("Password: ")

    user = None
    if username == santri.username and santri.cek_password(password):
        user = santri
    elif username == musyrif.username and musyrif.cek_password(password):
        user = musyrif
    else:
        print("Login gagal!")
        continue

    print("Login sebagai:", user.role)

    if user.role == "santri":
        izin = user.ajukan_izin()
        izin_list.append(izin)
        save_izin(izin_list)
        print("Izin diajukan. Status:", izin.status)

    elif user.role == "musyrif":
        if not izin_list:
            print("Belum ada izin.")
        else:
            izin = izin_list[-1]
            user.proses_izin(izin)
            save_izin(izin_list)
            print("Status sekarang:", izin.status)

        else:
            izin = izin_list[0]
            user.proses_izin(izin)
            print("\nStatus terbaru:", izin.status)
