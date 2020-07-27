from django.shortcuts import render
from .forms import ImageForm
from django.shortcuts import redirect
from django.contrib import messages
from pdf2image import convert_from_path
from django.http import HttpResponse

def create_dailyfeed(request):

    if request.method == 'POST' :

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            pages1 = convert_from_path('{}'.format(inst.page1.path), 50)
            for page1 in pages1:
                page1.save('{}'.format(inst.page1.path)[:-4] +".jpg", 'JPEG')
            return redirect('/', messages.success(request, 'Image is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form.errors)
    else:
        form = ImageForm()
        return render(request,'newspaper.htm',{'form' : form})