from animal import animal

print('\n==KARNIVORA==')
class karnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_makanan, jenis_gigi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_gigi = jenis_gigi                     
        self.jenis_makanan = jenis_makanan

    def info_karnivora(self):
        super().info_animal()
        print('jenis_makanan \t\t\t :', self.jenis_makanan,
              '\njenis_gigi \t\t\t :', self.jenis_gigi)
        
karnivora = karnivora ('singa', 'rusa', 'darat', 'melahirkan', 'daging', 'bertaring')
karnivora.info_karnivora()
 