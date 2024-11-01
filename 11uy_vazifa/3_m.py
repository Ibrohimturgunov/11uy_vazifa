class Odam:
    def __init__(self, ismi, pravasi_bormi, yosh, kitoblar=None):
        self.ismi = ismi
        self.pravasi_bormi = pravasi_bormi
        self.yosh = yosh
        self.kitoblar = kitoblar if kitoblar is not None else []

class Ota(Odam):
    def __init__(self, ismi, pravasi_bormi, yosh, pul):
        super().__init__(ismi, pravasi_bormi, yosh)
        self.pul = pul
        self.kitoblar = {}

    def kitob_qosh(self, kitob_nomi, varaqlar_soni):
        bosma_taboq_soni = varaqlar_soni // 15
        self.kitoblar[kitob_nomi] = bosma_taboq_soni

    def pul_ber(self, odam):
        umumiy_bosma_taboq = sum(self.kitoblar.values())
        if umumiy_bosma_taboq > 15:
            if odam.yosh < 18:
                self.pul -= 13000
                return f"{odam.ismi}ga 13 000 so'm berildi. Otaning qolgani: {self.pul} so‘m."
            else:
                return f"{odam.ismi} 18 yoshdan katta, unga pul berilmaydi."
        else:
            return "Kitoblarning umumiy bosma taboqlari yetarli emas."

ogil_1 = Odam("1-o‘g‘il", True, 17)
ogil_2 = Odam("2-o‘g‘il", False, 19)


ota = Ota("Ota", True, 45, 100000)

ota.kitob_qosh("Alpomish", 300)
ota.kitob_qosh("Sariq devni minib", 150)

print(ota.pul_ber(ogil_1))
print(ota.pul_ber(ogil_2))
