class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / interval
    def __init__(self, name, job, hp):
        self.name = name
        self.job = job
        self.hp = hp
        print(f"Hero {self.name} telah di summon")

    def heal(self):
        print(f"{self.name} meminum Posion......")
        heal_amount = 20
        self.hp += heal_amount
        print(f"HP {self.name} bertambah +{heal_amount}")

    def teke_damage(self,damage):
        self.hp -= damage
        print(f"{self.name} terkena {damage} Damage!!")
        print(f" Sisa HP: {self.hp}")
        if self.hp == 0:
            print(f" {self.name} Tereliminasi dari Lane!!!")


    def attack(self, enemy, damage):
        print(f"{self.name} menyerang {enemy.name}!")
        enemy.teke_damage(damage)

    def __str__(self):
        status = "$ Hidup"
        if self.hp == 0:
            status = "* Matii!!"

        return f"[{self.job}] {self.name} | HP: {self.hp} | {status}"


# buat objek / summon hero" ke lobby
zilong = Hero("Zilong", "Warrior", 100)
Aurora = Hero("Aurora", "Mage", 100)
zilong.attack(Aurora, 30)
print(Aurora)
Aurora.attack(zilong, 10)
Aurora.attack(zilong, 10)
Aurora.attack(zilong, 10)
Aurora.heal()
print(zilong)
print('SKILL 1: Congkel Bang')
zilong.attack(Aurora, 70)
print(Aurora)
print(zilong)