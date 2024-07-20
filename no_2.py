class Animal:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def setNama(self, nama):
        self.nama = nama

    def setJenis(self, jenis):
        self.jenis = jenis

    def Information(self):
        return f"Nama: {self.nama}, Jenis: {self.jenis}"

class KuraKura(Animal):
    def __init__(self, nama, jenis, makanan):
        super().__init__(nama, jenis)
        self.makanan = makanan

    def setMakanan(self, makanan):
        self.makanan = makanan

    def Information(self):
        return f"Nama: {self.nama}, Jenis: {self.jenis}, Makanan: {self.makanan}"

# Membuat instance objek dari kelas child (KuraKura)
kura_kura = KuraKura("Shani", "Reptil", "daging")

# Memanggil atribut dan metodenya
print(kura_kura.Information())

# Mengubah nilai atribut menggunakan metode
kura_kura.setNama("rania")
kura_kura.setJenis("Amfibi")
kura_kura.setMakanan("Ikan")

# Memanggil kembali metode untuk melihat perubahan
print(kura_kura.Information())

