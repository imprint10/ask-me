import os
from django.shortcuts import render
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "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"

def ask_me(request):
    #query = request.POST.get('prompt')
    #with open('C:/Users/impab/OneDrive/Desktop/GAIA hakthon/ask-me/data/grape.txt', 'r', encoding='utf-8') as file:
    #    content = file.read()
    
    #loader = TextLoader(content)
    #index = VectorstoreIndexCreator().from_loaders([loader])
    query = "ايش اقدر ارزع في شهر اكتوبر؟"
    #output = index.query(query)
    #print(output)
    return render(request, 'index.html', {'output': query})