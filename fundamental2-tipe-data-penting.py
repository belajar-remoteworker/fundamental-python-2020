print('\ntipe data skalar => tipe data sederhana')
anak1 = 'elvan'
anak2 = 'tri'
anak3 = 'fadhil'
anak4 = 'faisul'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Elvan', 'Tri', 'Fadhil', 'Faizul']
print(anak)
anak = ['Elvan', 'Tri', 'Fadhil', 'Faizul', 'Limo']
print(anak)
anak.append('Enam')
print(anak)

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nsapa semua anak cara gampang')
for a in anak: # a itu untuk mewakili objek nya, bisa diganti apa saja, hanya jika diganti maka print nya juga diganti
    print(f'Hai {a}')

print('\nsapa anak cara ribet')
for a in range(0,len(anak)):
    print(f'{a+1}.Hai {anak[a]}')





