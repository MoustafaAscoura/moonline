from django.shortcuts import render
from django.http import HttpResponse
import stripe
from django.shortcuts import redirect
stripe.api_key="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"



def stripePay(request):
    
    if request.method=="POST":
            amount=int(request.POST["amount"])
            try:
                customer=stripe.Customer.create(
                        email=request.POST.get("email"),
                        name=request.POST.get("full_name") ,
                        description="Test donation",
                    source=request.POST['stripeToken']
                )
            except stripe.error.CardError as e:
                return HttpResponse("<h1> There was an error charging your card: </h1>"+str(e))
            except stripe.error.RateLimitError as e:
                return HttpResponse("<h1> Rate Error</h1>")
            except stripe.error.InvalidRequestError as e:
                return HttpResponse("<h1> Invalid requestor</h1>")
            except stripe.error.AuthenticationError as e:
                return HttpResponse("<h1> Invalid API auth</h1>")
            except stripe.error.InvalidRequestError as e:
                return HttpResponse("<h1>stripe error</h1>")

            except Exception as e:
                pass
            
            charge=stripe.Charge.create(
                    customer=customer,
                    amount=int(amount)*100,
                    currency='usd',
                    description="Test donation"
                )
            transRetrive=stripe.Charge.retrieve(
                    charge["id"],
                    api_key="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                )
            charge.save()
            return redirect("templates:pay_success")
            


    return render(request,"index.html")

def paysuccess(request):
    return render(request,"success.html")
