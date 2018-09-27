import hashlib
import matplotlib
from termcolor import colored, cprint


def menu():
    print("=============================================")
    print("888888 e    e      8   8                    =")
    print("8    8 e    e      8   8 eeeee eeeee ee  8   =")
    print(colored("8eeee8 8    8 <==> 8eee8 8   8 8     88  8    ======>", 'red', attrs=['bold']))
    print(colored("88     8eeee8 <==> 88  8 8eee8 8eeee 8eee8    ======>", 'red', attrs=['bold']))
    print("88       88        88  8 88  8    88 88  8   =")            #Don't change it, Noob!
    print("88       88        88  8 88  8 8ee88 88  8  = \t ",(colored("Author:naufalrivaille   [v1.0]", "red", attrs=['bold', 'blink'])))
    print("=============================================")
    print("\n")


    print("=====> Menu Pilihan <=====")
    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("\n")

menu()
def md5():
    kode = input("Masukkan String ke hash :")
    hash_inp = hashlib.md5(kode.encode())
    print("Hasil dari String", "[", kode, "]", "adalah = ", hash_inp.hexdigest())

def sha1():
    kode = input("Masukkan String ke hash :")
    hash_inp = hashlib.sha1(kode.encode())
    print("Hasil dari String", "[", kode, "]", "adalah = ", hash_inp.hexdigest())

def sha256():
    kode = input("Masukkan String ke hash :")
    hash_inp = hashlib.sha256(kode.encode())
    print("Hasil dari String", "[", kode, "]", "adalah = ", hash_inp.hexdigest())
User_input = int(input("Masukkan pilihan anda : "))
blocklist = ("Pilihan tidak ada dalam daftar :(")

if User_input == 1:
    print("Anda memilih hash[md5] .. \n")
    md5()
elif User_input == 2:
    print("Anda memilih hash[sha1] .. \n")
    sha1()
elif User_input == 3:
    print("Anda memilih hash[sha256] .. \n")
    sha256()
else:
    print(blocklist)

