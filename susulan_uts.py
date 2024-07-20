def mahasiswa():
    data = []
    while True:
        nama = input("Masukkan Nama: ")
        nilai_algoritma = float(input("Masukkan Nilai Algoritma: "))
        nilai_matematika = float(input("Masukkan Nilai Matematika: "))
        
        data.append({
            'Nama': nama,
            'Nilai Algoritma': nilai_algoritma,
            'Nilai Matematika': nilai_matematika,
            'Rata-rata': (nilai_algoritma + nilai_matematika) / 2
        })
        
        tambah_lagi = input("Ingin Tambah Lagi? (YA/TIDAK): ").strip().upper()
        if tambah_lagi != 'YA':
            break
    
    print("\nData yang dimasukkan:")
    for entry in data:
        print(f"Nama: {entry['Nama']}, Nilai Algoritma: {entry['Nilai Algoritma']}, Nilai Matematika: {entry['Nilai Matematika']}, Rata-rata: {entry['Rata-rata']:.2f}")

mahasiswa()