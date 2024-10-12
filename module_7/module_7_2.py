def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    strings_position = {}
    string_number = 0
    byte = file.seek(0)
    for string in strings:
        file.write(string + "\n")
        string_number +=1
        key = (string_number, byte)
        strings_position[key] = string
        byte = file.tell()
    file.close()
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




