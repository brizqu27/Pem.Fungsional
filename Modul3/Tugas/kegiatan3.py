# Data list seperti pada kegiatan 1 modul 1
random_list = [3.1, 2.7, 5.5, 19, 753, 412, 'Hello', 'Python', 'world', 'AI']

# Filter untuk memisahkan nilai float, int, dan string
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_to_digits(num):
    return {
        'ratusan': num // 100,
        'puluhan': (num % 100) // 10,
        'satuan': num % 10
    }

data_int_mapped = list(map(map_to_digits, data_int))

# Output
print("Data Float:", data_float)
print("Data Int:")
for item in data_int_mapped:
    print(item)
print("Data String:", data_string)
