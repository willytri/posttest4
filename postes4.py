def hitung_harga_setelah_diskon(harga, merek):
    if merek.lower() == "tesla":
        diskon_persen = 0.17
    elif merek.lower() == "toyota":
        diskon_persen = 0.21
    elif merek.lower() == "hyundai":
        diskon_persen = 0.23
    else:
        return "Tidak jadi membeli mobil."

    diskon = harga * diskon_persen
    harga_setelah_diskon = harga - diskon
    return harga_setelah_diskon

def login():
    username = "willy"
    password = "120"
    
    print("=== Login ===")
    for _ in range(3):  
        user_input = input("Masukkan username: ")
        pass_input = input("Masukkan password: ")
        
        if user_input == username and pass_input == password:
            print("Login berhasil!")
            return True
        else:
            print("Username atau password salah. Silakan coba lagi.")
    
    print("Terlalu banyak percobaan. Program keluar.")
    return False

def main():
    if not login():
        return  
    
    while True:
        try:
            harga = float(input("Masukkan harga mobil: "))
            if harga < 0:
                raise ValueError("Harga harus positif.")
            
            merek = input("Masukkan merek mobil (tesla/toyota/hyundai): ").strip()
            harga_final = hitung_harga_setelah_diskon(harga, merek)

            if isinstance(harga_final, str):
                print(harga_final)
            else:
                print(f"Harga yang harus dibayar setelah diskon adalah: {harga_final:.2f}")

            pilihan = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").strip().lower()
            if pilihan != "ya":
                print("Terima kasih! Program selesai.")
                break
            
        except ValueError as e:
            print(f"Input tidak valid: {e}")

if __name__ == "__main__":
    main()
