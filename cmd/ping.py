def execute(*args):
    """
    Menjalankan perintah ping. 
    Jika ada argumen, tampilkan argumen tersebut. Jika tidak, tampilkan 'Pong!'.
    """
    if args:
        # Jika ada argumen, cetak argumen tersebut
        # Di masa depan, ini bisa digunakan untuk mem-ping host tertentu
        print(f"Ping ke: {' '.join(args)}")
        # Di sini Anda bisa menambahkan logika untuk memanggil sistem ping yang sebenarnya
        # import os
        # os.system(f"ping {' '.join(args)}")
    else:
        # Jika tidak ada argumen, cetak Pong!
        print("Pong!")
