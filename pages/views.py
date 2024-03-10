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
        district = request.POST['district']
        piece = request.POST['piece']

        Order.objects.create(name_prod=one_pro, name_customer=name_customer, length=length, width=width,
                             amount=amount, house=house, street=street, block=block, type_address=type_address,
                             area=area, district=district, piece=piece,
                             sleeve=sleeve, shoulders=shoulders, Phone=Phone, notes=notes)
        return redirect('pages:thanks')
    
    cities = ["القبلة","الصالحية","الوطية","بنيد القار","كيفان","الدوحة","الدسمة","الدعية","المنصورية","ضاحية عبد الله السالم","النزهة","الفيحاء","الشامية","الروضة","العديلية","الخالدية","القادسية","قرطبة","السرة","اليرموك","الشويخ","الري","غرناطة","الصليبيخات والدوحة","النهضة","مدينة جابر الأحمد","القيروان","شمال غرب الصليبيخات","جزيرة فيلكا","جزيرة كبر","جزيرة عوهة","جزيرة أم المرادم","جزيرة مسكان","جزيرة قاروه","جزيرة أم النمل","جزيرة الشويخ","الفنطاس","العقيلة","الظهر","المقوع","المهبولة","الرقة","هدية","أبو حليفة","الصباحية","المنقف","الفحيحيل","الأحمدي","الوفرة","الزور","الخيران","ميناء عبد الله","الوفرة الزراعية","بنيدر","الجليعة","الضباعية","ضاحية جابر العلي","ضاحية فهد الأحمد","الشعيبة","واره","مدينة صباح الأحمد","النويصيب","مدينة الخيران","مدينة صباح الأحمد البحرية","أبرق خيطان","الأندلس","اشبيلية","جليب الشيوخ","خيطان","خيطان الجديدة","العمرية","العارضية","العارضية الصناعية","العباسية","الفردوس","الفروانية","الحساوي","الشدادية","الرابية","الرحاب","الرقعي","الري الصناعية","ضاحية صباح الناصر","ضاحية عبد الله المبارك","الضجيج","الصليبية","أمغرة","النعيم","القصر","الواحة","تيماء","النسيم","العيون","القيصرية","العبدلي","الجهراء القديمة","الجهراء الجديدة","كاظمة","مدينة سعد العبد الله","السالمي","المطلاع","مدينة الحرير","كبد","الروضتين","الصبية","جزيرة بوبيان","جزيرة وربة","حولي","الشعب","السالمية","الرميثية","الجابرية","مشرف","بيان","آلبدع","النقرة","ميدان حولي","سلوى","جنوب السرة","الزهراء","الصديق","حطين","السلام","الشهداء","العدان","القصور","القرين","ضاحية صباح السالم","المسيلة","المسايل","أبو فطيرة","أبو الحصانية"]
    return render(request, 'form_order.html', context={'cities': cities})


def kind_view(request, kind):
    one_pro = Product.objects.all()
    one_pro1 = one_pro.filter(listt=kind)
    return render(request, 'kind.html', {
        'one_pro': one_pro1,

    })
