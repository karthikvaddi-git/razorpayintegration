from django.shortcuts import render
from decouple import config
from .models import savenature
# Create your views here.
import razorpay
def index(request):
    print(config('RAZOR_KEY_ID'))
    config('RAZOR_KEY_SECRET')

    return render(request,"index.html")

def pay(request):
    if request.method=="POST":
        print(request.POST.get('emailid'))

        client = razorpay.Client(auth=(config('RAZOR_KEY_ID'), config('RAZOR_KEY_SECRET')))
       # payment = client.order.create({'amount': 500, 'currency': 'INR', 'payment_capture': '1'})
      #  saveobj = savenature(phonenumeber=name, amount=amount, paymentid=payment['id'])
       # saveobj.save()
        return render(request, "pay.html")
    else:
        return render(request,"pay.html")



