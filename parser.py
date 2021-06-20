import docx
import os
from glob import glob


# for i in glob('*.docx'):  #В директории ищет нужный документ
#     print(i)

doc = docx.Document('pars3.docx')  #Открываю вордовский документ

text = []

for paragraph in doc.paragraphs:  #Считываю тект по параграфам
    text.append(paragraph.text)

# print('\n'.join(text))

yestext = '\n'.join(text)  # Объединяю весь текст в один

# if 'Петров' in yestext:
#     print('Петров есть')

print(yestext)
for i in range(100):
    if str(i) in yestext:
        print(i)
print(yestext)

# if 'Начальное' in yestext:
#     os.rename("C://Users/user/Desktop/Parse/pars4.docx", "C://Users/user/Desktop/Parse/Sorted/pars7777.docx")

# a = os.listdir('Users\user\Desktop\Parse')
# print(a)

# os.mkdir("Sorted")  # Создаёт новую папку

# os.rename("C://Users/user/Desktop/Parse/pars.docx", "C://Users/user/Desktop/Parse/Sorted/pars7777.docx")  # Перемещает документ в другую директорию



