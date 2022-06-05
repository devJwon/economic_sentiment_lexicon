import os
from pdfminer.high_level import extract_text

path_dir = '/Users/jwon/lab/paper/crawling/pdf'
file_list = os.listdir(path_dir)

for i in range(20):
    text = extract_text(path_dir + '/' + file_list[i])
    with open(f'/Users/jwon/lab/paper/crawling/txt/{file_list[i][:6]}.txt', mode='w', encoding='UTF-8') as output:
        output.write(text)