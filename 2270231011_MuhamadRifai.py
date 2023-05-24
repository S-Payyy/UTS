dataDiri = ["Muhamad Rifai", 2270231011 ,"A1"]
print("Name : {}\nClass : {}\nNim : {}\n".format(dataDiri[0],dataDiri[1],dataDiri[2])+"="*40)
for i in range(1,4):
  print(f"{i}. Jawaban Soal No {i}")
print("="*40)

jawaban1 = """
Dalam struktur data queue linear dengan array satu dimensi, pembacaan dan pelepasan informasi dilakukan menggunakan operasi enqueue (penambahan elemen) dan dequeue (penghapusan elemen).

Karena queue ini memiliki prinsip FIFO maka Pembacaan Informasi:
1. Baca elemen pada posisi "front" dalam queue.
2. Jika ada elemen lain dalam queue, baca elemen pada posisi berikutnya (front+1), dan seterusnya hingga mencapai posisi "end".
3. Urutan pembacaan informasi harus mengikuti urutan masuknya elemen ke dalam queue.

Pelepasan Informasi:
1. Hapus elemen pada posisi "front" dalam queue.
2. Jika ada elemen lain dalam queue, hapus elemen pada posisi berikutnya (front+1), dan seterusnya hingga mencapai posisi "end".
3. Setelah elemen terdepan dihapus, perbarui posisi "front" dengan menambahkan 1.
4. Periksa apakah "front" sudah mencapai posisi "end". Jika ya, artinya queue kosong. Dalam hal ini, atur "front" dan "end" kembali ke nilai -1.

Berikut ilustrasinya:
[Loket] B C D
index : 0 1 2

informasi yang pertama keluar adalah B, dan index selanjutnya menjadi n-1. (index 1 menjadi index 0, index 2 menjadi index 1)

[Loket] C D 
index : 0 1

informasi yang kedua keluar adalah C, dan index selanjutnya menjadi n-1. (index 1 menjadi index 0, index 2 menjadi index 1)

[Loket] D 
index : 0

Lalu informasi yang terakhir keluar adalah D, karena ini adalah informasi terahir maka Loket menjadi Empty.
"""

jawaban2 = """
Dalam struktur data stack, urutan pembacaan informasi dan pelepasan informasi mengikuti prinsip LIFO (Last-In-First-Out), yang berarti elemen yang terakhir dimasukkan ke dalam stack akan menjadi elemen pertama yang dikeluarkan.

Berikut adalah urutan pembacaan informasi dan pelepasan informasi dalam struktur data stack:

Pembacaan Informasi:

1. Baca elemen paling atas (top) dari stack.
2. Jika ada elemen lain dalam stack, baca elemen di bawahnya (elemen kedua dari atas), dan seterusnya hingga mencapai elemen terbawah (bottom) dari stack.
3. Urutan pembacaan informasi akan terbalik dari urutan masuknya elemen ke dalam stack.

Pelepasan Informasi:

1. Hapus elemen paling atas (top) dari stack.
2. Setelah elemen paling atas dihapus, perbarui posisi top dengan menggesernya ke elemen di bawahnya.
3. Periksa apakah stack kosong setelah penghapusan. Jika top bernilai -1, artinya stack kosong.

ilustrasinya gampangnya menggunakan tumpukan baju: 

[         ]
[  ember  ]
[         ]

lalu kita tambahkan dengan metode PUSH, 3 baju dengan urutan: merah, kuning, hijau.

index 2 [  Hijau ]
index 1 [ Kuning ]
index 0 [  Merah ]

dalam pembacaan informasi Stack yaitu LIFO maka elemen terakhir yang kita tambahkan akan dikeluarkan terlebih dahulu dengan metode POP.

index 2 [ Kosong ]
index 1 [ Kuning ]
index 0 [ Merah  ]

apabila di lakukan POP kembali maka element Kuning akan dikeluarkan : 

index 2 [ Kosong ]
index 1 [ Kosong ]
index 0 [ Merah  ]

lalu di lakukan POP kembali maka element Merah juga dikeluarkan dari Stack:

index 2 [ Kosong ]
index 1 [ Kosong ]
index 0 [ kosong ]

apabila Stack tidak terdapat element apapun maka akan menjadi Tumpukan Kosong.
"""

def jawaban3():
  import os
  from collections import deque
  os.system("cls")
  queue = deque()

  def tambah():
    queue.append(input("\nMasukan element: "))
    print("Isi Queue:", queue)
  
  def keluar():
    def is_queue_empty(queue):
      return len(queue) == 0

    if is_queue_empty(queue) == True:
      print("Antrian Kosong. tidak dapat melakukan Poping")
    else:
      data = queue.popleft()
      print("\nData yang dikeluarkan:", data)
      
  def ngecek():
    print("Isi queue saat ini:", queue)

  while True:
    print()
    work = input("Menu Queue\n1. Push Item\n2. Pop Item\n3. Melihat isi Queue\nPilih Menu: ")
    match work:
      case "1": tambah()
      case "2": keluar() # Sekaligus mengecek apakah antrian kosong atau tidak
      case "3": ngecek()
      case _: print("Menu tidak tersedia")

while True:
  coices = input("Pilih No Soal 1 - 3 : ")
  match coices:
    case "1" : print(jawaban1)
    case "2" : print(jawaban2)
    case "3" : jawaban3()
    case _: print("Soal tidak ditemukan.")
    