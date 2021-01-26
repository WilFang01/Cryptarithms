# NIM : 13519025
# Nama : Wilbert Fangderson
# Tugas Kecil Stima 1

# Cryptarithmetic
# ===============
# Contoh :
#  SEND
#  MORE+
# ------
# MONEY
# Output : S = 9, E = 5, N = 6, D = 7, M = 1, O = 0, R = 8, Y = 2
#================

# Fungsi
def IsExist(x,array):
    # Mengecek apakah huruf yang muncul sudah ada dalam array variabel
    # True jika ada, False jika belum
    if x in array : 
        return True
    else : 
        return False


def register_first_letter(file):
    # Melakukan register kata pertama ke dalam array_first_letter
    array_first_letter = [0 for i in range(10)]
    j = 0
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        for i in range (1):
            # Mengecek apakah variabel berupa huruf
            if ((ord(line[i]) >= 65) and (ord(line[i])<=90)):
                if not IsExist(line[i],array_first_letter):
                    array_first_letter[j] = line[i]
                    j += 1
    return array_first_letter


def count_var(file):
    # Menghitung jumlah huruf dalam file
    array_var = [0 for i in range(10)]
    j = 0
    count = 0
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        # Mendaftarkan huruf yang muncul ke dalam array variabel
        for i in range(len(line)) :
            # Mengecek apakah variabel berupa huruf
            if ((ord(line[i]) >= 65) and (ord(line[i])<=90)):
                if not IsExist(line[i],array_var):
                    array_var[j] = line[i]
                    j += 1
                    count += 1
    return count


def register_var(file,count):
    # Melakukan register variabel file ke dalam array_var
    j = 0
    array_var = [0 for i in range(count)]
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        # Mendaftarkan huruf yang muncul ke dalam array variabel
        for i in range(len(line)) :
            # Mengecek apakah variabel berupa huruf
            if ((ord(line[i]) >= 65) and (ord(line[i]) <= 90)):
                if not IsExist(line[i],array_var):
                    array_var[j] = line[i]
                    j += 1
    return array_var


def count_word(file):
    # Menghitung jumlah kata dalam file
    array_word = [0 for i in range(10)]
    j = 0
    count = 0
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        # Mengecek apakah variabel berupa huruf
        if ((ord(line[1]) >= 65) and (ord(line[1])<=90)):
            array_word[j] = line.strip(' ').strip('+')
            j += 1
            count += 1
    return count


def register_word(file,total_word):
    # Melakukan register kata file per line dalam array_word
    array_word = [0 for i in range(total_word)]
    j = 0
    for line in file :
        # Menghapus spasi pada kepala dan ekor baris
        line = line.strip()
        # Mendaftarkan kata yang muncul ke dalam array variabel
        # Mengecek apakah variabel berupa huruf
        if ((ord(line[1]) >= 65) and (ord(line[1]) <= 90)):
            array_word[j] = line.strip(' ').strip('+')
            j += 1
    return array_word


def initiate_value(count):
    # Melakukan register value awal
    array_value = [-1 for i in range(count)]
    value = 0
    for i in range(count):
        array_value[i] = value
        value += 1
    return array_value


def increment_value(array_value,count):
    # Melakukan increment 1 kepada value
    num = 0
    dup = 10**(count-1)
    for i in range(count):
        num = num + array_value[i]*dup
        dup = dup // 10
    
    # Value +1
    num += 1

    dup2 = 10**(count-1)
    for i in range(count):
        array_value[i] = num//dup2
        num = num % dup2
        dup2 = dup2 // 10

    return array_value


def word_value(word,array_var,array_value):
    # Menghitung value dari sebuah kata
    value = 0
    dup = 10**(len(word)-1)
    for i in range(len(word)):
        j = 0
        match = False
        while not match :
            if (word[i] != array_var[j]):
                j += 1
            else :
                value = value + array_value[j]*dup
                dup = dup // 10
                match = True
    return value

def array_unique(array_value):
    # Mengecek apakah tidak ada value yang sama dalam sebuah array
    check = True
    for i in range(len(array_value)):
        for j in range(len(array_value)):
            if (array_value[i] == array_value[j]) and (i != j):
                check = False
    return check

def check_value(array_var,array_value,array_word,count,array_first_letter):
    # Mengecek apakah value yang sudah di set terpenuhi
    check = True
    total_left = 0
    total_right = word_value(array_word[len(array_word)-1],array_var,array_value)
    for i in range(len(array_word)-1):
        if (array_unique(array_value)):
            a = list(array_word[i])
            if (a[0] in array_first_letter):
                for j in range(count):
                    if (a[0] == array_var[j]):
                        if (array_value[j] == 0) :
                            check = False
                        else :
                            total_left = total_left + word_value(array_word[i],array_var,array_value)
            else:
                total_left = total_left + word_value(array_word[i],array_var,array_value)
        else :
            check = False

    if(total_left != total_right):
        check = False

    return check

def count_line(file):
    # Menghitung jumlah line pada file
    total_line = 0
    testfile = open("testfile.txt","r")
    line = testfile.read()
    line_split = line.split("\n")

    for i in line_split :
        if i :
            total_line += 1

    return total_line

def longest_word(array_word,total_word):
    maks = 0
    for i in range(total_word):
        if (len(array_word[i]) > maks):
            maks = len(array_word[i])
    return maks


# Program Utama
with open("testfile.txt","r") as file :
    count = count_var(file)
with open("testfile.txt","r") as file :
    total_line = count_line(file)
with open("testfile.txt","r") as file :
    total_word = count_word(file)
with open("testfile.txt","r") as file :
    main_array_var = register_var(file,count)
with open("testfile.txt","r") as file :
    main_array_word = register_word(file,total_word) 
with open("testfile.txt","r") as file :
    main_array_first_letter = register_first_letter(file)

main_array_value = initiate_value(count)

# Untuk menghitung Total Test
total_test = 0

# Algoritma
while (check_value(main_array_var,main_array_value,main_array_word,count,main_array_first_letter) == False ) :
    increment_value(main_array_value,count)
    total_test+=1

print(main_array_value)
print(main_array_var)

# Output
for i in range(len(main_array_word)-1):
    if (len(main_array_word[i]) < longest_word(main_array_word,total_word)) :
        space = longest_word(main_array_word,total_word) - len(main_array_word[i])
        print(' '*space,end='')
    print(word_value(main_array_word[i],main_array_var,main_array_value),end='')
    if (i == (len(main_array_word)-2)):
        print('+')
    else:
        print()
print("------")
print(word_value(main_array_word[len(main_array_word)-1],main_array_var,main_array_value))
print("Total Test : ",total_test)