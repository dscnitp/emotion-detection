from django.http import HttpResponse
from django.shortcuts import render
from tensorflow.keras.models import Sequential
from nltk.tokenize import word_tokenize,sent_tokenize
import joblib
import nltk
nltk.download('punkt')
import numpy as np
def home(request):
    return render(request,'home.html')


def count(request):
    s=request.GET['a']
    s=word_tokenize(s)
    for i in range(100-len(s)):
        s.append('<pad>')
    embedded_arr=[]
    embedded_arr.append([])
    vocab_f=open('glove.6B.50d.txt', encoding="utf-8")
    word_to_emb={}
    for line in vocab_f:
      word_to_emb[line.split()[0]]=[float(i) for i in line.split()[1:]] 
    word_to_emb['<pad>']=[0]*50
    for word in s:
        if word.lower() in word_to_emb:
            embedded_arr[-1].append(word_to_emb[word.lower()])
        else:
            embedded_arr[-1].append([0]*50)
    #x_input=np.array(embedded_arr)
    x_input=np.array(embedded_arr)
    cls=joblib.load('final_model.sav')
    ans=cls.predict(x_input)
    #return arr.argmax()    
    return render(request,'count.html',{'ans':ans})