from django.shortcuts import render
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def ask_me(request):
    #query = request.POST.get('prompt')
    loader = TextLoader('data/grape.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    query = "ايش اقدر ارزع في شهر اكتوبر؟"
    output = index.query(query)
    print(output)
    return render(request, 'askme.html', {})

