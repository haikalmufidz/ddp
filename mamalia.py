from animal import animal

print('\n==MAMALIA==')
class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernafas, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal()
        print('ukuran_tubuh \t\t\t :', self.ukuran_tubuh,
              '\njenis_kulit \t\t\t :', self.jenis_kulit,
              '\nbernafas \t\t\t :', self.bernafas)
        
mamalia = mamalia ('sapi', 'tumbuhan', 'darat', 'melahirkan', 'paru-paru', 'sangat besar', 'berbulu')
mamalia.info_mamalia()
 