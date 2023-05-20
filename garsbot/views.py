# views.py
from django.shortcuts import render
from .forms import AskGarsbotForm
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from django.conf import settings
import os

def get_answer(query):
    data_file_path = os.path.join(settings.BASE_DIR, 'garsbot', 'data', 'grape.txt')
    loader = TextLoader(data_file_path, encoding='utf-8')
    index = VectorstoreIndexCreator().from_loaders([loader])
    output = index.query(query)
    return output


def ask_garsbot(request):
    if request.method == "POST":
        form = AskGarsbotForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            # your function goes here, make sure to replace it with your actual function
            answer = get_answer(question)
            return render(request, 'garsbot/answer.html', {'answer': answer})
    else:
        form = AskGarsbotForm()

    return render(request, 'garsbot/ask.html', {'form': form})
