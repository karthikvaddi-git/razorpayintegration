from django.shortcuts import render
from decouple import config
from .models import savenature
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import razorpay
def index(request):
    print(config('RAZOR_KEY_ID'))
    config('RAZOR_KEY_SECRET')

    return render(request,"index.html")

def pay(request):
    if request.method=="POST":

        name=request.POST.get('nameid')
        email=request.POST.get('emailid')
        amount=request.POST.get('amountid')


        client = razorpay.Client(auth=(config('RAZOR_KEY_ID'), config('RAZOR_KEY_SECRET')))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)

        print(payment)

        saveobj = savenature(name=name, email=email, paymentid=payment['id'],amount=amount)
        saveobj.save()
        context={'payment':payment}

        return render(request, "pay.html",{'payment':payment})

    else:
        return render(request,"pay.html")


@csrf_exempt
def success(request):
    if request.method == "POST":
        a = (request.POST)
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        user = savenature.objects.filter(paymentid=order_id).first()
        user.paid = True
        user.save()

    return render(request, "success.html")


def rz(request):
    return render(request,"rz.html")



