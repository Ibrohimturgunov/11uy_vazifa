class Odam:
    def __init__(self, ismi, pravasi_bormi, yosh):
        self.ismi = ismi
        self.pravasi_bormi = pravasi_bormi
        self.yosh = yosh

class Ota(Odam):
    def __init__(self, ismi, pravasi_bormi, yosh, pul):
        super().__init__(ismi, pravasi_bormi, yosh)
        self.pul = pul

    def pul_ber(self, odam):
        if odam.yosh < 18:
            return f"{odam.ismi}ga {self.pul} so‘m berildi."
        else:
            return f"{odam.ismi} 18 yoshdan katta, unga pul berilmaydi."

ota = Ota("Ota", True, 45, 10000)
ogil_1 = Odam("1-o‘g‘il", True, 17)
ogil_2 = Odam("2-o‘g‘il", False, 19)

print(ota.pul_ber(ogil_1))  # 1-o‘g‘il 18 yoshdan kichik
print(ota.pul_ber(ogil_2))  # 2-o‘g‘il 18 yoshdan katta
