# =========================
# CETAKAN ORANG
# =========================
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self.role = role

    def cek_password(self, password):
        return self.__password == password


# =========================
# CETAKAN SANTRI
# =========================
class Santri(User):
    def __init__(self, username, password, nis):
        super().__init__(username, password, "santri")
        self.nis = nis


# =========================
# CETAKAN MUSYRIF
# =========================
class Musyrif(User):
    def __init__(self, username, password):
        super().__init__(username, password, "musyrif")


# =========================
# CETAKAN IZIN
# =========================
class Izin:
    def __init__(self, nama, alasan, tanggal, jam):
        self.nama = nama
        self.alasan = alasan
        self.tanggal = tanggal
        self.jam = jam
        self.status = "Pending"


# =========================
# PROGRAM UTAMA (BISA INPUT)
# =========================
print("=== LOGIN ===")
username = input("Username: ")
password = input("Password: ")

# DATA CONTOH
santri = Santri("ahmad", "123", "S001")
musyrif = Musyrif("ustadz", "admin")

user = None

if username == santri.username and santri.cek_password(password):
    user = santri
elif username == musyrif.username and musyrif.cek_password(password):
    user = musyrif
else:
    print("Login gagal")

# JIKA LOGIN BERHASIL
if user:
    print("Login berhasil sebagai", user.role)
