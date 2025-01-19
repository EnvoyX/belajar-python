# Multithread = melakukan multiple task concurrently (multitasking)

import threading
import time

def jalan_kaki(durasi):
    time.sleep(durasi) # 6 detik
    print(f"Telah berjalan sendirian")

def jalan_bersama(orang1, orang2, durasi):
    time.sleep(durasi) # 8 detik
    print(f"Kamu telah berjalan bersama {orang1} & {orang2}")

def buang_sampah():
    time.sleep(2)
    print("Kamu telah membuang sampah")

def ambil_paket():
    time.sleep(4)
    print("Kamu telah mengambil paket")

def pulangKeRumah():
    time.sleep(10)
    print("Kamu telah kembali pulang")

# Jika dijalan dalam satu thread

# jalan_kaki(durasi = 8)    
# jalan_bersama(orang1= "Momo Ayase", orang2= "Aira Shiratori", durasi= 10)
# buang_sampah()
# ambil_paket()
# pulangKeRumah()

# Jika dijalankan dalam multiple thread

thread1 = threading.Thread(target=jalan_kaki, args=(6,))
thread1.start()

thread2 = threading.Thread(target=jalan_bersama, args=("Momo Ayase", "Aira Shiratori", 8))
thread2.start()

thread3 = threading.Thread(target=ambil_paket)
thread3.start()

thread4 = threading.Thread(target=buang_sampah)
thread4.start()

thread5 = threading.Thread(target=pulangKeRumah)
thread5.start()

# .join() memastikan semua task telah selesai sebelum dilanjutkan ke proses
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

# Multi-threading memungkinan untuk menyelesaikan
# suatu task secara simultan dan efisien
# dengan masing-masing thread mengerjakan tugas masing-masing

print("All task are done!")