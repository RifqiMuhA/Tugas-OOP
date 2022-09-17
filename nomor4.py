# Fungsi untuk mencetak space antar pola
def printSpasi(spasiAwal, indeks):
    for i in range(1, spasiAwal+indeks):
        # Print spasi tanpa new line
        print(" ", end='')

def forLoopAscending(baris, indeks):
    for i in range(0, baris-indeks+1):
        print("*", end='')
    
def forLoopDescending(baris, indeks):
    for i in range(0, indeks):
        print("*", end='')

def forLoopPola(baris):
    # Looping sebanyak baris dari 1
    for i in range (1, baris+1):
        print(str(i) + ".", end='')
        forLoopAscending(baris, i)

        printSpasi(baris*3, i)

        print(str(i) + ".", end='')
        forLoopDescending(baris, i)
        print('')
    
def whileLoopAscending(baris, indeks):
    while baris >= indeks:
        print('*', end='')
        baris -= 1

def whileLoopDescending(baris, indeks):
    while indeks > 0:
        print('*', end='')
        indeks -= 1

def whileLoopPola(baris):
    i = 1
    while(i <= baris):
        print(str(i) + ".", end='')
        whileLoopAscending(baris, i)

        printSpasi(baris*3, i)

        print(str(i) + ".", end='')
        whileLoopDescending(baris, i)

        print('')
        i += 1

# main program
baris = int(input("Masukkan Banyak Baris  : "))
print("Susunan angka dan bintang (Dengan for loop)")
forLoopPola(baris)
print("\nSusunan angka dan bintang (Dengan while loop)")
whileLoopPola(baris)