from django.shortcuts import render
from django.utils import timezone   
import os
from django.conf import settings
from .forms import InputForm

def index(request):
    history = []
    if os.path.exists(settings.LOG_FILE_PATH):
        with open(settings.LOG_FILE_PATH, 'r') as f:
            history = f.readlines()
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            timestamp = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"[{timestamp}] {form.cleaned_data['text']}\n"
            with open(settings.LOG_FILE_PATH, 'a') as f:
                f.write(entry)
            history.append(entry)
    else:
        form = InputForm()
    
    return render(request, 'ex02/index.html', {'form': form, 'history': history})   