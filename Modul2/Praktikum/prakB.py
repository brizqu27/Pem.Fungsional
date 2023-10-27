import random

# Membuat Fungsi Papan
create_board = lambda panjang, lebar, posisi_awal, posisi_goals: [
    ['A' if (i, j) == posisi_awal else 'O' if (i, j) == posisi_goals else '-' for j in range(lebar)] for i in range(panjang)
]

# Mencetak Papan Permainan
print_board = lambda board: [print(' '.join(row)) for row in board]

generate_random_position = lambda panjang, lebar : (random.randint(0, panjang-1), random.randint(0, lebar-1))

def main():
    while True:
        print("~ Selamat Bermain ~")
        panjang = int(input("Masukkan Panjang board: "))
        lebar = int(input("Masukkan Lebar board: "))

        max_attempts = 3  # Batasan maksimal pengacakan
        userInput = True

        for _ in range(max_attempts):
            posisi_awal = generate_random_position(panjang, lebar)
            posisi_goals = generate_random_position(panjang, lebar)
            board = create_board(panjang, lebar, posisi_awal, posisi_goals)
            print_board(board)
            userInput = True

            while userInput:
               Reset = input("Apakah ingin mengganti Posisi (y/n): ").lower()
               if Reset == 'n':
                    userInput = False
               elif Reset != 'y':
                    print("Salah masukan!")
               else :
                   break
            
            if userInput == False :
                break

        board = create_board(panjang, lebar, posisi_awal, posisi_goals)
        print_board(board)
        
        gerakan = input("Apa gerakanmu? (w = atas, s = bawah, a = kiri, d = kanan): ").lower()
            
        if all(gerakan_char in ['w', 's', 'a', 'd'] for gerakan_char in gerakan):
            x, y = posisi_awal
            for gerakan_char in gerakan:
                if gerakan_char == 'w' and x > 0:
                    x -= 1
                elif gerakan_char == 's' and x < panjang - 1:
                    x += 1
                elif gerakan_char == 'a' and y > 0:
                    y -= 1
                elif gerakan_char == 'd' and y < lebar - 1:
                    y += 1
             
            posisi_awal = x, y
               
            if posisi_awal == posisi_goals:
                print_board(create_board(panjang, lebar, posisi_awal, posisi_goals))
                print("You Win!")
                break
            else : 
                print_board(create_board(panjang, lebar, posisi_awal, posisi_goals))
                print("You Lose!")
                userInput1 = True

                while userInput1:
                    Ulang = input("Apakah ingin Bermain Lagi (y/n)? ")
                    if Ulang == 'n' :
                        print("Sampai Jumpa Lagi....")
                        userInput1 = False;
                    elif Ulang != 'y':
                        print("Salah Input!")
                    else :
                        break
            if userInput1 == False:
                break
        else:
            print("Gerakan tidak valid. Gunakan w, s, a, atau d.")

if __name__== "__main__":
    main()