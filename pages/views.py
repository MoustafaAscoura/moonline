from django.shortcuts import render,redirect,HttpResponse,get_list_or_404,get_object_or_404
from .models import Product,Order,about
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .cart import Cart
# from .forms import CartAddProductFrom
from django.views.decorators.http import require_POST
# from .forms import CartAddProductFrom
import json
# import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View







def contact(request):
    aboutt =about.objects.all()
    return render(request,'contact.html',{
             'aboutt':aboutt
   })

def app(request):
    produ =Product.objects.all()
    return render(request,'app.html',{
        'produ' : produ
   })

def thanks(request):
   
    return render(request,'thanks.html',{
        
   })

def product_view(request):
    produ =Product.objects.all()
    return render(request,'product_view.html',{
        'produ' : produ
        })


def details(request,pk):
    one_pro =Product.objects.get(id=pk)
    return render(request,'details.html',{
        'one_pro' : one_pro,
        

        })




def form_order(request,pk):
    
    one_pro =Product.objects.get(id=pk)
    # form_del = Orderform(request.POST, request.FILES)
    if request.method == "POST":    
       
       name_customer=request.POST['Full Name']
       length=request.POST['Length']
       
       width=request.POST['width']
       sleeve=request.POST['sleeve']
       shoulders=request.POST['shoulders']
       Phone=request.POST['Phone']
       notes=request.POST['notes']


       amount=(one_pro.PRDPrice*(1-(one_pro.PRDDiscountPrice)/100))+3
    #    payment=request.POST['payment']
       house=request.POST['house']
       street=request.POST['street']
       block=request.POST['block']
       type_address=request.POST['type_address']
       area=request.POST['area']

       Order.objects.create(name_prod=one_pro,name_customer=name_customer,length=length,width=width,
       amount=amount,house=house,street=street,block=block,type_address=type_address,area=area,
       sleeve=sleeve,shoulders=shoulders,Phone=Phone,notes=notes)
       return redirect('pages:thanks')
    return render(request,'form_order.html',{
            'one_pro' : one_pro,

            
            })
    
def kind_view(request,kind):
    one_pro =Product.objects.all()
    one_pro1=one_pro.filter(listt=kind)
    return render(request,'kind.html',{
        'one_pro' : one_pro1,
        
        })


# @require_POST
# def cart_add(request,product_id):
#     cart=Cart(request)
   
#     one_pro =Product.objects.get(id=product_id)
#     # form_del = Orderform(request.POST, request.FILES)
#     if request.method == "POST":    
       
#        name_customer=request.POST['Full Name']
#        length=request.POST['Length']
       
#        width=request.POST['width']
#        sleeve=request.POST['sleeve']
#        shoulders=request.POST['shoulders']
#        Phone=request.POST['Phone']
#        Note=request.POST['note']
#        ord=max_id = Order.objects.aggregate(Max('id'))['id__max']
#        id1=ord.id
#        print(id1)
     
      

#        order1=Order.objects.create(id=id1+1,name_prod=one_pro,name_customer=name_customer,length=length,width=width,sleeve=sleeve,shoulders=shoulders,Phone=Phone,Note=Note)
       
#        form = CartAddProductFrom(request.POST)
#        print(order1.id)
#        if form.is_valid():
#             cd=form.cleaned_data
#             cart.add(product=order1,quantity=cd['quantity'],override_quantity=cd['override_quantity'])
#     return redirect('pages:cart_detail')

# def cart_remove(request,product_id):
#     cart=Cart(request)
#     product = get_object_or_404(Order, id=product_id)
#     # prodect=get_list_or_404(Product,id=product_id)
#     cart.remove(product)
#     return redirect('pages:cart_detail')

# def cart_detail(request):
#     cart=Cart(request)
#     return render(request,'cart_detail.html',{'cart':cart})    
























