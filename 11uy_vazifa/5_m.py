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

    def pul_ber(self, odam):
        if odam.yosh < 18:
            return f"{odam.ismi}ga {self.pul} so‘m berildi."
        else:
            return f"{odam.ismi} 18 yoshdan katta, unga pul berilmaydi."

    def kitob_qidir(self, kitob_nomi, bolalar):
        oqiganlar = [bola.ismi for bola in bolalar if kitob_nomi in bola.kitoblar]
        if oqiganlar:
            return f"{kitob_nomi} kitobini o‘qiganlar: {', '.join(oqiganlar)}"
        else:
            return f"{kitob_nomi} kitobi hech kim tomonidan oqilmagan."

ota = Ota("Ota", True, 45, 10000)
ogil_1 = Odam("1-o‘g‘il", True, 17, kitoblar=["Alpomish", "Sariq devni minib"])
ogil_2 = Odam("2-o‘g‘il", False, 19, kitoblar=["O‘tgan kunlar", "Alpomish"])

bolalar = [ogil_1, ogil_2]
print(ota.kitob_qidir("Alpomish", bolalar))
print(ota.kitob_qidir("O‘tgan kunlar", bolalar))
print(ota.kitob_qidir("Yulduzli tunlar", bolalar))
