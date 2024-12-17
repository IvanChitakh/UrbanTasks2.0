def custom_write(file_name, strings):
    opened_file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    number_of_strings = 0
    for item in strings:
        number_of_strings += 1
        cursor = opened_file.tell()
        opened_file.write(f'{item}\n')
        strings_position[number_of_strings, cursor] = item
    opened_file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
