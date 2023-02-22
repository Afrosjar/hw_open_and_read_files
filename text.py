f = open ('text1.txt', encoding = 'utf-8')
a = f.readlines()

# print(f'Длина файла text1 {len(a)}')


q = open ('text2.txt', encoding = 'utf-8')
b = q.readlines()
x = q.readline()
# print(f'Длина файла text2 {len(b)}')

s = open ('text3.txt', encoding = 'utf-8')
c = s.readlines()
# print(f'Длина файла text3 {len(c)}')

d = open ('Final_text.txt','w', encoding = 'utf-8')
# Заходим на проверку по первому IF 
if len(a) < len(b) and len(a) < len(c):
    d.writelines(f"'text1.txt'\n{len(a)}\n")

    with open ('Final_text.txt','a',encoding = 'utf-8') as f:
        counter = 0
        for id, line in enumerate(a,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
            
    if len(b) < len(c):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text2.txt'\n{len(b)}\n")
        counter = 0
        for id, line in enumerate(b,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text3.txt'\n{len(c)}\n")
        counter1 = 0
        for id, line in enumerate(c,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
    if len(c) < len(b):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text2.txt'\n{len(c)}\n")
        counter = 0
        for id, line in enumerate(c,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text3.txt'\n{len(b)}\n")
        counter1 = 0
        for id, line in enumerate(b,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
    
 # Заходим на проверку по второму IF        
if len(b) < len(a) and len(b) < len(c):
    d.writelines(f"'text2.txt'\n{len(b)}\n")

    with open ('Final_text.txt','a',encoding = 'utf-8') as f:
        counter = 0
        for id, line in enumerate(b,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
            
    if len(a) < len(c):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text1.txt'\n{len(a)}\n")
        counter = 0
        for id, line in enumerate(a,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text3.txt'\n{len(c)}\n")
        counter1 = 0
        for id, line in enumerate(c,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
    if len(c) < len(a):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text3.txt'\n{len(c)}\n")
        counter = 0
        for id, line in enumerate(c,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text1.txt'\n{len(a)}\n")
        counter1 = 0
        for id, line in enumerate(a,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
# Заходим на проверку по последнему IF
if len(c) < len(a) and len(c) < len(b):
    d.writelines(f"'text3.txt'\n{len(c)}\n")

    with open ('Final_text.txt','a',encoding = 'utf-8') as f:
        counter = 0
        for id, line in enumerate(c,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
            
    if len(b) < len(a):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text2.txt'\n{len(b)}\n")
        counter = 0
        for id, line in enumerate(b,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text1.txt'\n{len(a)}\n")
        counter1 = 0
        for id, line in enumerate(a,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
    if len(a) < len(b):
        d = open ('Final_text.txt','a', encoding = 'utf-8')
        d.writelines(f"'text1.txt'\n{len(a)}\n")
        counter = 0
        for id, line in enumerate(a,start = 1):
            if counter <= id:
                d.write(f'{line}')
        d.write(f'\n')
        d.writelines(f"'text2.txt'\n{len(b)}\n")
        counter1 = 0
        for id, line in enumerate(b,start = 1):
            if counter1 <= id:
                d.write(f'{line}')
d.close()
f.close()
q.close()
s.close()

























# Необходимо объединить их в один по следующим правилам:

# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Пример Даны файлы: 1.txt

# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt

# Строка номер 1 файла номер 2
# Итоговый файл:

# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 8
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 3.txt
# 9
# строки 1-9 файла номер 3 по очереди