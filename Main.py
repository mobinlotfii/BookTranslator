import fitz
import googletrans
from datetime import datetime as dt
from nltk.tokenize import sent_tokenize

fname = "test.pdf"
doc = fitz.open(fname)
out = open(fname.split('.')[0] + ".txt", "wb")
pcount = doc.page_count
start = dt.now()

for page in doc.pages(130,150):  
    text = page.get_text()
    text = page.get_text()
    text = str(text.replace('  ', ' '))
    text = str(text.replace('\n', ' '))
    text = str(text.replace(' :', ':'))
    text = str(text.replace(' ,', ','))
    #text = str(text.replace('.', '.\n'))

    out.write(bytes(f"""{text}
    
    """, 'utf-8'))

    text = sent_tokenize(text)
    
    for idx in range(len(text)):
        sent_ = text[idx]

        translator = googletrans.Translator()
        translated = translator.translate(sent_, dest='fa').text
        out.write(bytes(translated, 'utf-8'))

finished = dt.now()
delta = (finished - start).seconds
print(f'Elapsed time: {delta} sec, velocity: {delta/pcount} per page')
out.close()
