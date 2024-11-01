class Odam:
    def __init__(self, ismi, pravasi_bormi):
        self.ismi = ismi
        self.pravasi_bormi = pravasi_bormi

class Mashina:
    def __init__(self, egasi):
        self.egasi = egasi

    def haydashga_ruxsat(self, odam):
        if odam.pravasi_bormi:
            return f"{odam.ismi} mashinani haydashi mumkin."
        else:
            return "Ruxsat yo'q"

ota = Odam("Ota", True)
ogil_1 = Odam("1-o‘g‘il", True)
ogil_2 = Odam("2-o‘g‘il", False)

mashina = Mashina(egasi=ota)

print(mashina.haydashga_ruxsat(ogil_2))
