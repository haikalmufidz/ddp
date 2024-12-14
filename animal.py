print('==ANIMAL==')
class animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print('nama hewan \t\t\t :', self.name,
              '\nmakanan \t\t\t :', self.makanan,
              '\nhidup \t\t\t\t :', self.hidup,
              '\nberkembang_biak \t\t :', self.berkembang_biak)


hewan = animal('kucing oren','daging','darat','melahirkan')
hewan.info_animal()