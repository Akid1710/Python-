from colorama import Fore, Back, Style, init

# auto reset warna (biar gk bocor)
init(autoreset=True)
# Fore (Foreground) = warna teks
# Back (background) = warna background
print(Fore.CYAN + Back.WHITE + "M. Dika Kurniawan")
# Style = ganti style teks (BRIGHT, DIM, NORMAL, RESET_ALL)
print(Style.BRIGHT + Fore.BLACK + Back.YELLOW + "Ganteng")










# print = output data ke terminal
print("hello world")
print("=" * 116)
# tips data python
Name = "Made Suryana" #string (text)
Age = 28 #integer (number)
Married = False #boolean (true/false)
print(f"{Name}, umur {Age} tahun")
NamaBali= ('Wayan' , 'Made' , 'Kadek' , 'Putu' )
print(NamaBali)
# fungsi diawali kata 'def'
# def nama fungsi (Parameter-parameter)
def hallo(nama , city):
    print(f"hallo bali {nama}, asal {city}")
    print("=" * 30)
# panggil nama fungsi diluar def
hallo("Wayan Coster", "Singaraja")
hallo("Nyoman Sureca", "Denpasar")