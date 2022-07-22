from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
from .forms import FileForm


def index(request):
    return render(request, 'index.html')


def model_form_upload(request):
    initial_data = {
        'uploader': request.user,
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileForm(initial=initial_data)
    return render(request, 'upload_file.html', {
        'form': form
    })


def account_profile(request):
    return render(request, 'profile_details.html')
