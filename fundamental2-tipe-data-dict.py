"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
perbedaannya jika menggunakan dict, yang dipakai kurung kurawal {}
kalo mennggunakan list ( lihat dipelajaran sebelumnya), dia pake kurung siku []
"""

kamus_ind_eng = {}
kamus_ind_eng ['anak'] = 'son'
kamus_ind_eng ['istri'] = 'wife'
kamus_ind_eng ['ayah'] = 'father'
kamus_ind_eng ['ibu'] = 'mother'

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['istri'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dar_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list' : ['Elvan', 'Tri', 'Fadhil', 'Faizul']
}
print(data_dar_server_gojek)
#ini untuk mencetak semua driver
print(f"Driver disekitar sini {data_dar_server_gojek['driver_list']}")
#ini untuk mencetak driver yang dipilih
print(f"Driver #1 {data_dar_server_gojek['driver_list'][0]}")
print(f"Driver #2 {data_dar_server_gojek['driver_list'][1]}")
print(f"Driver #4 {data_dar_server_gojek['driver_list'][3]}")

# data diubah menjadi dictionary semua
data_dar_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list' : [
        {'nama': 'Elvan', 'jarak': 10},
        {'nama':'Tri','jarak': 30},
        {'nama':'Fadhil','jarak':100},
        {'nama':'Faizul', 'jarak':120}
    ]
}

print(f"Jarak driver terdekat berjarak {data_dar_server_gojek['driver_list'][0]['jarak']}meter")
