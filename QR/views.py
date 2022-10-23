from django.shortcuts import render, redirect
import qrcode
from .models import QRCode
import random
from django.http import HttpResponse

# Create your views here.
def QR_Generator(request, path=None):

    return render(request, "QR/QRGenerator.html",{
        'Title':'Generador de código QR',
        'Image':path
    })


def QR_Generator_Img(request):

    if request.method == "GET":
        
        # Getting the data request
        data = request.GET['Data']

        # Creating image name.
        name = data.strip().replace("/", "").replace(".","").replace(":","").replace("-","")
        length = int(len(name)/3)
        name = ''.join(random.choice(name) for i in range(length))

        # Making QR CODE
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        path = f"Media\QRCodes\{name}.png"
        img.save(path)

        try:
            # Saving QR CODE
            QR = QRCode(
                name = data,
                image = path
            )
            QR.save()
        
            # Redirect
            QR = QRCode.objects.latest('id')
            path = getattr(QR, 'image')
            return redirect(QR_Generator, path=path)
    
        except:
            return HttpResponse("Hubo algun error")
        

