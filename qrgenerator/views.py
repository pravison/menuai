from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
import mimetypes
import os
from qrcode import *
import time
from wsgiref.util import FileWrapper


# Create your views here.
def qrGenerator(request):
    if request.method == "POST":
        data= request.POST['data']
        img = make(data)
        img_name= 'qr' + str(time.time()) + '.png'
        img.save(settings.MEDIA_ROOT / img_name)
        return render(request, 'qr.html', {'img_name':img_name})
    return render(request, 'qr.html')

def fileDownload(request, filename):
    filepath = os.path.join(settings.MEDIAROOT, filename)
    wrapper = FileWrapper(open(filepath, 'rb'))
    content_type= mimetypes.guess_type(filepath)[0]
    response = HttpResponse(wrapper, mimetype='content_type')
    response['Content-Disposition'] ="attachment; filename= %s" % filename
    return response