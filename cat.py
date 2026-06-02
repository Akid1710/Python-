# Diawali class namaclass
class Cat:
    # self = dirinya sendiri/internal
    #_____Init_____ =constructor=
    #objek yg pertama dipanggil
    def __init__(self, color,weight):
        self.color = color
        self.weight = weight
    # method =fungsi di dalam class
    def sleep(self, duration):
        print(f"Turu {duration} Menit")

# buat objek dari class cat
Belang = Cat("mix", 5)
Oyen = Cat("Orange", 3)
# buat objek dari class cat
Belang = Cat()
Oyen = Cat()
print("obj belang", Belang)
print("obj oyen", Oyen) 
# print("obj belang", Belang)
# print("obj oyen", Oyen) 
Belang.sleep(5)
Oyen.sleep(10)
print(f"warna si oyen: {Oyen.color}")
print(f"berat si oyen: {Oyen.weight} kg")