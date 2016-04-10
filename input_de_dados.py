# -*- coding: utf-8 -*-


# http://stackoverflow.com/questions/27394879/python-open-file-readline-list-convert-to-string


import sys

arquivo = open('texto1.txt', 'r')
arquivo_str = arquivo.readline()
arquivo.close()

arquivo_str = arquivo_str.rstrip('\n')
print arquivo_str

# http://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python
# with open('data.txt', 'r') as myfile:
#     data=myfile.read().replace('\n', '')
