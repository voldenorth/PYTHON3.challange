import numpy as np


def pilihan(*args):
  for i in args:
    if i == 1:
      pilih = int(input('pilih 1=besar,2=kecil,3=sama:'))
      if pilih == 1:
        pilih = 'besar'
      if pilih == 2:
        pilih = 'kecil'
      if pilih == 3:
        pilih = 'sama'
    if i == 0:
      pilih = int(input('masukan angka1-12:'))
  return pilih


def result(x, y):
  if x & y >= 4:
    hasil = 'besar'
  if x & y <= 3:
    hasil = 'kecil'
  if x == y:
    hasil = 'sama'
  return hasil


while True:
  dadu_1 = np.random.randint(1, 6)
  dadu_2 = np.random.randint(1, 6)
  dadu = []
  dadu.append(dadu_1)
  dadu.append(dadu_2)
  hasil = dadu_1 + dadu_2
  x = int(input("silahkan pilih 0=angka atau 1=pilihan:"))
  a = pilihan(x)
  b = result(dadu_1, dadu_2)
  if x == 0:
    if hasil == a:
      print('SELAMAT ANDA MENANG')
    else:
      print('ANDA KALAH, SILAHKAN COBA LAGI')
  if x == 1:
    if a == b:
      print('SELAMAT ANDA MENANG')
    else:
      print('ANDA KALAH, SILAHKAN COBA LAGI')
  print(hasil)
  print(dadu)
  lanjut = input('apakah ingin lanjut?(y/n)')
  if lanjut == 'y':
    continue
  if lanjut == 'n':
    break
  else:
    ValueError
