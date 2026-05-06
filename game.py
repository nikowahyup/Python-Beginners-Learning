import random
import time


class Game():
    def __init__(self, nama, hp, mana=0):
        self.nama = nama
        self.hp = hp
        self.mana = mana
        self.max_mana = mana
        self.max_hp = hp

    def kondisi(self):

        if self.hp == 0:
            print(f"[STATUS] {self.nama} Telah Mati")
        elif self.hp <= 300:
            print(f'[STATUS] {self.nama} Sedang Sekarat HP : {self.hp} ')
        else:
            print(f"[STATUS] {self.nama} masih sehat HP : {self.hp} | mana : {self.mana}")

    def serang(self, lawan, skill=False):
        if self.hp < 0:
            print(f"{self.nama} sudah mati")
            damage = 0
            return

        if self.mana >= 25 and skill:
            self.mana -= 25
            damage = 200
            print(f"{self.nama} melakukan serangan skill ke {lawan.nama}")
            if self.mana < 25:
                print("Tidak cukup mana")
                damage = 0
                return

        else:
            critical = random.randint(1, 3)
            if critical == 2:
                print(f"Serangan critical dari {self.nama}")
                damage = 160
            else:
                print(f'{self.nama} melakukan serangan')
                damage = 40

        lawan.hp -= damage
        if lawan.hp < 0: lawan.hp = 0
        print(f"Damage masuk: {damage}")
        lawan.kondisi()

    def heal(self):
        if self.hp < 0:
            print(f'{self.nama} tidak bisa heal')
            return

        else:
            print(f"{self.nama} healing...")
            time.sleep(4)
            self.hp += 200
            self.mana += 10
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.mana > self.max_mana:
                self.mana = self.max_mana
        print(f"Healing selesai. HP  : {self.hp} | mana : {self.mana}")

    def bangkit(self):
        if self.hp == 0:
            self.hp += self.max_hp * 0.3
            print(f"{self.nama} telah dibangkitkan dengan HP {self.hp}")


char7 = Game("MINATO", 1500, 150)
char8 = Game("OBITO", 1000, 200)

for x in range(1, 9):
    char7.serang(char8, skill=True)
    time.sleep(3)
    print()
    if char8.hp == 0:
        break
