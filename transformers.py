# -*- coding: utf-8 -*-
"""Transformers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ACQSXrGWkcnZdvbQHI7ZR8voCoJYQ03x
"""

! pip install transformers
print('done')
! pip install transformers[sentencepiece]
print('done')
! pip install sentencepiece
print('done')
! pip install gtts
print('done')

from transformers import pipeline

classifier = pipeline("automatic-speech-recognition",model='fractalego/personal-speech-to-text-model')
translation = pipeline('translation_XX_to_YY',model='Helsinki-NLP/opus-mt-en-ar')

from google.colab import files
uploaded = files.upload()

file ="/content/One Minute English #1 - Learn Vocabulary Fast.mp3"
file1 = '/content/WhatsApp Ptt 2022-03-05 at 5.45.21 PM.mp3'
file2='/content/11.ogg'

speech2text = classifier(file1)
text= list(speech2text.values())
text2text = translation(text)
text2 =list(text2text[0].values())

print('English Translation is ',text)
print("Arabic translation is ",text2)

from gtts import gTTS
mytext =' '.join([str(elem) for elem in text2])
language = 'ar'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")

from IPython.display import Audio
Audio("welcome.mp3")

