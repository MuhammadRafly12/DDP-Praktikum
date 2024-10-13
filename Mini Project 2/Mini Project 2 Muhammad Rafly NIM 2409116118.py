from prettytable import PrettyTable
import os
import time

# Warna
BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' 




# Variabel
# Dictionary
ayam = [
    {'nama': 'Ayam Goreng Original', 'harga': 15000},
    {'nama': 'Ayam Goreng Spicy', 'harga': 16000}
]

keranjang = []


# List tapi Nested List
akun = [['rafly', '123', 'admin'], ['Fadil', '123', 'alomani jawa']]

def bersih():
    os.system("cls || clear")

def tunggu(angka):
    time.sleep(angka)
    
    
def loadingMenuUtama():
    bersih()
    print(BOLD+RED+'''                                                                                 
            ⠀⠀⠀⠀⢀⣸⣷⣼⠿⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣰⣯⠹⠟⠁⢀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢠⠋⠉⣻⠶⠚⠿⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⢀⣸⣷⡋⠀⠺⠷⣆⡀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠶⠛⠋⠉⠉⠉⠓⠒⠦⣄⡀⠀⠀⠀⠀⠀
            ⠀⠘⠋⢙⠏⠀⢰⠖⠋⣹⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀
            ⠀⠀⠀⢯⡀⠀⢸⠦⡴⠃⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⣀⡤⠤⠒⠒⠦⢤⡀⠀⠙⣆⠀⠀
            ⠀⠀⠀⣠⠟⠶⠞⠀⠀⠈⢣⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⣠⣞⣭⡤⠤⣄⡀⠀⠀⠙⢷⡀⠘⡆⠀
            ⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⡇⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⢠⠞⠋⠁⢀⣀⣀⣀⡈⠑⢦⡀⠀⢻⡄⢹⠀
            ⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⣧⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠴⠚⠛⠒⠢⢄⡉⠳⣆⠹⣄⠀⢷⢸⡇
            ⠀⡿⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⢿⣦⣀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⣤⣀⠑⡄⠘⢷⣿⡄⢸⣾⡇
            ⢸⡇⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠉⠛⠛⠲⠶⠤⠬⣄⡀⠀⠀⠀⠀⢀⣈⡉⠙⠢⡀⠈⠻⣿⡀⠈⣿⡇⠀⣿⠃
            ⢸⡇⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠐⢶⣤⣉⢿⠓⢦⣸⡆⠀⢹⡇⠀⢸⡇⢀⡟⠀
            ⠈⣷⠀⠀⠀⠀⢰⠁⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠙⣄⠈⣷⡙⢧⡇⠀⢿⠇⠀⠘⠀⠀⠀⠁⠈⠀⠀
            ⠀⢹⣆⠀⠀⠀⠘⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠸⣄⢧⡇⠈⣿⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠻⣦⠀⠀⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⡟⣸⠃⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠙⢷⣄⡀⣀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣤⣀⠠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠉⠳⣤⡑⢦⡈⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠘⣦⠀⠙⣦⠈⠙⠓⠶⠦⠤⠤⠤⠄⠠⠤⣴⡶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⢷⠀⠀⠀⢀⣴⠶⠒⠒⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠘⣧⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠶⢒⠺⣧⡤⢾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢸⠀⠀⠆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⡤⠏⢸⣦⠀⣸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠚⠛⠛⠛⢛⣫⣴⣿⣶⣶⠋⣸⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠉⠉⠉⠉⡿⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                FRIED CHICKEN INDONESIA
'''+RESET)
    tunggu(1)
    loading()
    

def cek_validasi_huruf(nama):
    for char in nama:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

def cek_validasi_angka(angka):
    return angka.isdigit()

    # CRUD ADMIN
    # Create
def AdminTambahMenu():
    bersih()
    print("=== Tambah Menu Baru ===")  
    while True:
        try:
            nama = str(input("Masukkan nama menu: ")).strip()
            if not nama:
                raise ValueError("Nama menu tidak boleh kosong.")
            if not cek_validasi_huruf(nama):
                raise ValueError("Nama menu hanya boleh berisi huruf.")
            harga_input = input("Masukkan harga menu: ").strip()
            if not harga_input:
                raise ValueError("Harga menu tidak boleh kosong.")
            if not cek_validasi_angka(harga_input):
                raise ValueError("Harga menu hanya boleh berisi angka.")
            harga = int(harga_input)
            if harga <= 0:
                raise ValueError("Harga menu tidak boleh mines.")
            ayam.append({'nama': nama, 'harga': harga})
            print(f"Menu '{nama}' dengan harga 'Rp{harga}' berhasil ditambahkan.\n")
            break  
        
        except ValueError as e:
            print(f"Input tidak valid: {e} Silakan coba lagi.")


    # Read
def LihatMenu():
    bersih()
    print("=== Lihat Semua Menu ===")
    if not ayam:
        print("Belum ada menu yang tersedia.\n")
    else: 
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Menu", "Harga"]
        iterasi= 1
        for ayams in ayam:
            tabel.add_row([iterasi, ayams['nama'], f"Rp{ayams['harga']}"])
            iterasi+= 1
        
        print(tabel)
    print()

    # Update
def AdminUpdateMenu():
    bersih()
    print("=== Update Menu ===")
    LihatMenu()
    if not ayam:
        return
    try:
        pilihan = int(input("Pilih nomor menu yang akan diupdate: "))
        if 1 <= pilihan <= len(ayam):
            nama_baru = input("Masukkan nama menu baru: ").strip()
            if not nama_baru:
                raise ValueError("Nama menu tidak boleh kosong.")
            if not cek_validasi_huruf(nama_baru):
                raise ValueError("Nama menu hanya boleh berisi huruf dan spasi.")
            
            harga_baru_input = input("Masukkan harga menu baru: ").strip()
            if not harga_baru_input:
                raise ValueError("Harga menu tidak boleh kosong.")
            if not cek_validasi_angka(harga_baru_input):
                raise ValueError("Harga menu hanya boleh berisi angka.")
            
            harga_baru = int(harga_baru_input)
            if harga_baru <= 0:
                raise ValueError("Harga menu harus lebih besar dari nol.")
            
            ayam[pilihan - 1] = {'nama': nama_baru, 'harga': harga_baru}
            print("Menu berhasil diupdate.\n")
        else:
            print("Pilihan tidak valid.\n")
    except ValueError as e:
        print(f"Input tidak valid: {e} Silakan coba lagi.\n")

def AdminHapusMenu():
    bersih()
    print("=== Hapus Menu ===")
    LihatMenu()
    if not ayam:
        return
    try:
        pilihan = int(input("Pilih nomor menu yang akan dihapus: "))
        if 1 <= pilihan <= len(ayam):
            removed_item = ayam.pop(pilihan - 1)
            print(f"Menu '{removed_item['nama']}' berhasil dihapus.\n")
        else:
            print("Pilihan tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

    
def menuAdmin():
    while True:
        bersih()
        print(GREEN+'''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗████╗░████║██║████╗░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ███████║██║░░██║██╔████╔██║██║██╔██╗██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝
''')
        print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    
        print(BOLD+"\u2022 Tambah Menu Baru (1)")
        print("\u2022 Lihat Semua Menu (2)")
        print("\u2022 Update Menu (3)")
        print("\u2022 Hapus Menu (4)")
        print("\u2022 Keluar (5)"+GREEN)
        print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    

        menu_admin = input("Masukkan Pilihan (1-5) > ")
        if menu_admin == '1':
            AdminTambahMenu()
        elif menu_admin == '2':
            LihatMenu()
            loading()
        elif menu_admin == '3':
            AdminUpdateMenu()
        elif menu_admin == '4':
            AdminHapusMenu()
        elif menu_admin == '5':
            print("Keluar dari menu admin.\n")
            menuUtama()
        else:
            print("Pilihan tidak valid.\n")
            loading()
    

def pesanFriedChicken():
    LihatMenu()
    try:
        pilihan = int(input("Pilih nomor menu yang ingin dipesan: "))
        if 1 <= pilihan <= len(ayam):
            keranjang.append(ayam[pilihan - 1])
            print(f"'{ayam[pilihan - 1]['nama']}' telah ditambahkan ke keranjang.\n")
        else:
            print("Pilihan tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

def lihatKeranjang():
    bersih()
    print("=== Keranjang Anda ===")
    if not keranjang:
        print("Keranjang kosong.\n")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Menu", "Harga"]
        idx = 1
        for item in keranjang:
            tabel.add_row([idx, item['nama'], f"Rp{item['harga']}"])
            idx += 1
        
        print(tabel)
    print()
    
def checkout():
    if not keranjang:
        print("Keranjang kosong. Tidak ada yang bisa di-checkout.\n")
    else:
        total = sum(item['harga'] for item in keranjang)
        print("=== Checkout ===")
        lihatKeranjang()
        print(f"Total harga: Rp{total}")
        keranjang.clear()
        print("Terima kasih sudah berbelanja!\n")

def menuUser():
    while True:
        bersih()
        print(GREEN+'''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██╗░░░██╗░██████╗███████╗██████╗░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██║░░░██║██╔════╝██╔════╝██╔══██╗
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██║░░░██║╚█████╗░█████╗░░██████╔╝
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ╚██████╔╝██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
''')
        print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    
        print(BOLD+"\u2022 Lihat Menu Fried Chicken (1)")
        print("\u2022 Pesan Fried Chicken (2)")
        print("\u2022 Lihat Keranjang (3)")  
        print("\u2022 Checkout (4)")
        print("\u2022 Keluar (5)"+GREEN)
        print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    


        menu_user = input("Masukkan Pilihan (1-5) > ")
        if menu_user == '1':
            LihatMenu()
            loading()
        elif menu_user == '2':
            pesanFriedChicken()
            loading()
        elif menu_user == '3':
            lihatKeranjang()
            loading()
        elif menu_user == '4':
            checkout()
            loading()
            
        elif menu_user == '5':
            print("Keluar dari menu user.")
            menuUtama()
        else:
            print("Pilihan tidak valid.\n")
            loading()

    
def login():
    bersih() 
    print(GREEN+'''
                ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
                ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
                ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
                ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
                ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
                ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
''')
    print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    
    while True:
        username = input("Masukkan Username > ")
        password = input("Masukkan Password > ")
        berhasil_login_cek = False
        for akuns in akun:
            if akuns[0] == username and akuns[1] == password:
                berhasil_login_cek = True
                if akuns[2] == 'admin':
                    print("Berhasil login, tunggu sebentar.")
                    loading()
                    bersih()
                    menuAdmin()
                elif akuns[2] == 'user':
                    print("Berhasil login, tunggu sebentar.")
                    loading()
                    bersih()
                    menuUser()
                else:
                    print("Mohon maaf, kamu adalah anomali.")
                    menuUtama()
                break  
        if berhasil_login_cek:
            break
        else:
            print("Username atau Password kamu salah.")
    
def register():
    bersih()
    print(GREEN + '''
    ██████╗░███████╗░██████╗░██╗░██████╗████████╗███████╗██████╗░
    ██╔══██╗██╔════╝██╔════╝░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██████╔╝█████╗░░██║░░██╗░██║╚█████╗░░░░██║░░░█████╗░░██████╔╝
    ██╔══██╗██╔══╝░░██║░░╚██╗██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
    ██║░░██║███████╗╚██████╔╝██║██████╔╝░░░██║░░░███████╗██║░░██║
    ╚═╝░░╚═╝╚══════╝░╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
''')
    print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)    
    while True:
        try:
            username = input("Masukkan Username > ").strip()
            password = input("Masukkan Password > ").strip()

            if username == "":
                raise ValueError("Username tidak boleh kosong.")
            if password == "":
                raise ValueError("Password tidak boleh kosong.")

            role = 'user'
            akuns = [username, password, role]
            akun.append(akuns)
            print("-" * 25)
            print("Kamu ingin melanjutkan ke menu login? (ya/tidak)")

            while True:
                konfirmasi = input("Masukkan Pilihan > ").strip().lower()
                if konfirmasi == "ya":
                    login()
                    return  
                elif konfirmasi == "tidak":
                    menuUtama()
                    return
                    
                else:
                    print('Perbaiki pilihan kamu, hanya "Ya / Tidak"')

        except ValueError as ve:
            print(f"Error: {ve}")
            print("Silakan coba lagi.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            print("Silakan coba lagi.")
    
    
def loading():
    print("="*30)
    print(BOLD+"Pencet ENTER Untuk Melanjutkan..."+RESET)
    print("="*30) 
    print()
    input()

def menuUtama():
    loadingMenuUtama()
    bersih()
    print(GREEN+'''
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██║░░░██║░░░██║░░░███████║██╔████╔██║███████║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██║░░░██║░░░██║░░░██╔══██║██║╚██╔╝██║██╔══██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ╚██████╔╝░░░██║░░░██║░░██║██║░╚═╝░██║██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝   
''')
    print("Selamat Datang di Toko Fried Chicken")
    print(RESET+BOLD+BLUE+"Do not count your chickens before they are hatched. - Aesop"+RESET+GREEN)
    print("─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)
    print(BOLD+"\u2022 Login (1)"+RESET)
    print(BOLD+"\u2022 Register (2)"+RESET)
    print(BOLD+"\u2022 Keluar Program (0)"+RESET)
    print(GREEN+"─────────────────────────────────⊱⁜⊰─────────────────────────────────"+RESET)
    while True:
        try :
            pilihMenu = int(input("Masukkan Pilihan Menu Utama > "))
            if pilihMenu == 1:
                print("Menu Login")
                login()
                break
            elif pilihMenu == 2:
                print("Menu Register")
                register()
                break
            elif pilihMenu == 0:
                exit(0)
            else:
                print("Mohon maaf, pilihan kamu diluar dari menu.")
        except ValueError:
            print("Hanya bisa menerima inputan angka.")
    
menuUtama()