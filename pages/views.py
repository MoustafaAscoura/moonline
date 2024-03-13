from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView


def contact(request):
    about_info = about.objects.first()
    return render(request, 'contact.html', {
        'aboutt': about_info,
        'theme_color': about_info.theme_color
    })

def app(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    about_info = about.objects.first()
    return render(request, 'app.html', {
        'products': products,
        'categories': categories,
        'landing_image': about_info.landing_image,
        'theme_color': about_info.theme_color
    })


def thanks(request):
    about_info = about.objects.first()
    return render(request, 'thanks.html', {
        'theme_color': about_info.theme_color
    })


def details(request, pk):
    one_pro = Product.objects.get(id=pk)
    about_info = about.objects.first()
    return render(request, 'details.html', {
        'one_pro': one_pro,
        'theme_color': about_info.theme_color
    })


def form_order(request, pk):
    one_pro = Product.objects.get(id=pk)
    about_info = about.objects.first()
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
    return render(request, 'form_order.html', context={
        'cities': cities,
        'theme_color': about_info.theme_color})

class CategoryListView(ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories'
    
    def get_context_data(self, *args, **kwargs):
        about_info = about.objects.first()
        context = super().get_context_data(*args, **kwargs)
        context['theme_color'] = about_info.theme_color
        return context
    
class CategoryView(DetailView):
    template_name = 'category.html'
    model = Category
    context_object_name = 'category'
    def get_context_data(self, *args, **kwargs):
        about_info = about.objects.first()
        context = super().get_context_data(*args, **kwargs)
        context['theme_color'] = about_info.theme_color
        return context
