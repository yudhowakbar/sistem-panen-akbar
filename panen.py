# Program sederhana menghitung total hasil panen
data_panen = [120, 95, 150, 80, 110] # dalam kilogram

total_panen = sum(data_panen)
print(f"Total hasil panen saat ini adalah: {total_panen} kg")

# Fitur diskon (Soal 2b)
diskon = total_panen * 0.10 # diskon 10%
print(f"Diskon yang diberikan seberat: {diskon} kg")