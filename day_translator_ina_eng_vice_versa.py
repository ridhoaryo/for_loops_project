days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday', 'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday',
    'ahad': 'sunday'
}
day = input('Input hari: ').lower()

for ind, eng in days.items():
    if day == eng:
        print(f'Bahasa Indonesia dari {day.upper()} adalah {ind.upper()}')
    elif day == ind:
        print(f'Bahasa Inggris dari {day.upper()} adalah {eng.upper()}')