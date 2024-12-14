from animal import animal

print('\n==AMPHIBI==')
class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak,)
        self.habitat = habitat
        self.bernafas = bernafas

    def info_amphibi(self):
        super().info_animal(),
        print('habitat \t\t\t :', self.habitat,
              '\nbernafas \t\t\t :', self.bernafas)
        
amphibi = amphibi('buaya', 'daging', 'air', 'bertelur', 'air tawar', 'bernapas dengan paru-paru')
amphibi.info_amphibi()