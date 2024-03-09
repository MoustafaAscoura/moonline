from django.shortcuts import render, redirect
from .models import Product, Order, about

def contact(request):
    return render(request, 'contact.html', {
        'aboutt': about.objects.all()
    })


def app(request):
    produ = Product.objects.all()
    return render(request, 'app.html', {
        'produ': produ
    })


def thanks(request):
    return render(request, 'thanks.html', {

    })


def details(request, pk):
    one_pro = Product.objects.get(id=pk)
    return render(request, 'details.html', {
        'one_pro': one_pro,

    })


def form_order(request, pk):
    one_pro = Product.objects.get(id=pk)
    # form_del = Orderform(request.POST, request.FILES)
    if request.method == "POST":
        name_customer = request.POST['Full Name']
        length = request.POST['Length']

        width = request.POST['width']
        sleeve = request.POST['sleeve']
        shoulders = request.POST['shoulders']
        Phone = request.POST['Phone']
        notes = request.POST['notes']

        amount = (one_pro.PRDPrice * (1 - (one_pro.PRDDiscountPrice) / 100)) + 3
        #    payment=request.POST['payment']
        house = request.POST['house']
        street = request.POST['street']
        block = request.POST['block']
        type_address = request.POST['type_address']
        area = request.POST['area']

        Order.objects.create(name_prod=one_pro, name_customer=name_customer, length=length, width=width,
                             amount=amount, house=house, street=street, block=block, type_address=type_address,
                             area=area,
                             sleeve=sleeve, shoulders=shoulders, Phone=Phone, notes=notes)
        return redirect('pages:thanks')
    return render(request, 'form_order.html', {
        'one_pro': one_pro,

    })


def kind_view(request, kind):
    one_pro = Product.objects.all()
    one_pro1 = one_pro.filter(listt=kind)
    return render(request, 'kind.html', {
        'one_pro': one_pro1,

    })
