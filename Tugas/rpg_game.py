class Hero:
    def __init__(self, name, job, hp, damage, hero_type="hero"):
        self.name = name
        self.job = job
        self.max_hp = hp
        self.hp = hp
        self.base_damage = damage
        self.type = hero_type # "hero" / "normal" / "boss"
        self.rage_mode_active = False
        
        # Penyesuaian status berdasarkan Role (TUGAS 4)
        if self.job == "Warrior":
            self.max_hp += 50
            self.hp = self.max_hp
        elif self.job == "Mage":
            self.base_damage += 15
            
    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        if not self.is_alive():
            print(f"❌ {self.name} sudah mati! Tidak bisa menyerang.")
            return

        if not enemy.is_alive():
            print(f"💀 {enemy.name} sudah mati, tidak perlu diserang lagi.")
            return

        current_damage = self.base_damage

        # Logika Boss Rage Mode (TUGAS 5)
        if self.type == "boss" and self.hp <= (self.max_hp / 2):
            if not self.rage_mode_active:
                print(f"\n😈 {self.name} memasuki RAGE MODE!")
                self.rage_mode_active = True
            print("💥 CRITICAL HIT!")
            current_damage = int(self.base_damage * 1.5)

        print(f"\n⚔️ {self.name} menyerang {enemy.name}!")
        enemy.take_damage(current_damage)

    def take_damage(self, damage):
        if damage <= 0:
            print("🛡️ Serangan tidak efektif.")
            return

        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} menerima {damage} damage! (Sisa HP: {self.hp}/{self.max_hp})")

        if self.hp == 0:
            print(f"💀 {self.name} telah gugur di medan perang!")

    def heal(self, target):
        if not self.is_alive():
            print(f"❌ {self.name} sudah mati! Tidak bisa memberikan heal.")
            return

        if not target.is_alive():
            print(f"❌ {target.name} sudah mati! Tidak bisa di-heal.")
            return

        amount = 20
        if self.job == "Healer":
            amount = 50

        target.hp += amount
        if target.hp > target.max_hp:
            target.hp = target.max_hp

        print(f"\n💚 {self.name} memulihkan {target.name} sebesar +{amount} HP! (HP {target.name}: {target.hp}/{target.max_hp})")


# =====================================================================
# 🎮 ENGINE GAME INTERAKTIF (BISA DIMAINKAN)
# =====================================================================

# 1. Inisialisasi Karakter (Kriteria Tugas Tetap Terpenuhi)
party = [
    Hero("Zilong", "Warrior", 100, 25, "hero"),
    Hero("Alice", "Mage", 70, 30, "hero"),
    Hero("Estes", "Healer", 80, 5, "hero")
]

boss = Hero("Raja Iblis", "Boss", 300, 35, "boss")

print("\n==================================================")
print("⚔️ GAME RPG: PARTY HERO VS RAJA IBLIS ⚔️")
print("==================================================")

# Loop Pertarungan (Game Baru Selesai Jika Boss Mati atau Semua Hero Mati)
while boss.is_alive() and any(hero.is_alive() for hero in party):
    
    # --- GILIRAN PLAYER (PARTY HERO) ---
    for hero in party:
        if not boss.is_alive():
            break
            
        if not hero.is_alive():
            continue  # Skip kalau heronya mati
            
        print(f"\n--- GILIRAN: {hero.name} ({hero.job}) [HP: {hero.hp}/{hero.max_hp}] ---")
        print("1. Serang Raja Iblis")
        print("2. Heal Teman (Khusus Healer/Role Lain)")
        
        pilihan = input("Pilih tindakan (1/2): ")
        
        if pilihan == "1":
            hero.attack(boss)
        elif pilihan == "2":
            # Tampilkan daftar teman yang hidup
            print("\nPilih target Heal:")
            for i, h in enumerate(party):
                status = "Hidup" if h.is_alive() else "Mati"
                print(f"{i+1}. {h.name} ({status} | HP: {h.hp})")
            
            try:
                target_idx = int(input("Pilih nomor target: ")) - 1
                if 0 <= target_idx < len(party):
                    hero.heal(party[target_idx])
                else:
                    print("❌ Pilihan salah, giliran hangus!")
            except ValueError:
                print("❌ Input harus angka, giliran hangus!")
        else:
            print("💤 Malah bengong... Giliran dilewati!")
            
    # --- GILIRAN MUSUH (BOSS ATTACK) ---
    if boss.is_alive():
        print("\n==================================================")
        print("😈 GILIRAN RAJA IBLIS MENYERANG!")
        print("==================================================")
        
        # Boss otomatis mengincar Hero yang masih hidup secara acak/berurutan
        hero_hidup = [hero for hero in party if hero.is_alive()]
        if hero_hidup:
            # Mengincar hero pertama yang masih hidup di barisan
            target_boss = hero_hidup[0]
            boss.attack(target_boss)
        print("\n==================================================")

# --- GAME OVER CONDITION ---
print("\n==================================================")
if boss.is_alive():
    print("💀 GAME OVER! Seluruh party kamu dibantai oleh Raja Iblis!")
else:
    print("🎉 SELESAI! Raja Iblis berhasil dikalahkan! Dunia kembali damai!")
print("==================================================")