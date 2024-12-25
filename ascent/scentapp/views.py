from django.shortcuts import render , redirect
from .models import *
from .models import Item
from .models import Reservation
from .models import TopNote
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# .all merr te gjithe elementet e modelit: ketu pedoret for in ne html
# .get merr vetem elementin qe ploteson kushtin
# .filter merr te gjithe elementet qe plotesojne kushtin: ketu pedoret for in ne html
# Create your views here.
def home(request):
    items = Item.objects.all()
    
    context = {"infoItems": items, }
    return render(request, "home.html")

def about(request):
   
    context = {""}
    return render(request, "about.html")
def workshops(request):
    
    context = {""}
    return render(request, "workshops.html")

def contact(request):
    
    context = {""}
    if request.method == "POST":
        emri = request.POST["firstName"]
        mbiemri = request.POST["lastName"]
        email = request.POST["email"]
        koment = request.POST["comment"]
        if emri == "" and mbiemri == "" and email == "" and koment == "":
            messages.error(request, "Ploteso fushat")
        else:
            Contact(
                contact_name=emri,
                contact_surname=mbiemri,
                contact_email=email,
                contact_comment=koment,
            ).save()
            messages.success(request, "Faleminderit")
    return render(request, "contact.html")

 # Funksioni i regjistrimit
def register(request):
    categories = Category.objects.all()
    context = {"cat": categories}
    # Marrja e informacioneve
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        # Kontrollohet nese fushat jane bosh
        if (
            first_name == ""
            and last_name == ""
            and username == ""
            and email == ""
            and password == ""
            and confirm_password == ""
        ):
            return redirect("../register/")
        else:
            # Kontrolli i password-it
            if password == confirm_password:
                # Kontrollohet nese useri eshte regjistruar me pare
                # User importohet ne fillim eshte e djangos
                if User.objects.filter(username=username).exists():
                    # nese po behet rifresh faqja e regjister
                    return redirect("/")
                else:
                    # Krijohet nje user i ri
                    # User importohet ne fillim eshte e djangos
                    user = User.objects.create_user(
                        email=email,
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.set_password(password)
                    # Ruhet useri
                    user.save()
                    # kalon tek faqja e login
                    return redirect("../login/")
    else:
        return render(request, "register.html", context)


def login(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    # marrja e te dhenave nga forma
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Kontrollo i te dhenave
        # auth importohet ne fillim eshte e djangos
        user = auth.authenticate(username=username, password=password)
        # Nese logohet kalon tek faqja e homh
        if user is not None:
            # metode e djangos
            auth.login(request, user)
            return redirect("/")
        else:
            # nese nuk perputhen informacionet behet refresh faqja
            return redirect("login/")
    else:
        return render(request, "login.html", context)



# Nuk e akseson faqen nese nuk je i log-uar
# Importohet ne fillim eshte pjese e djangos
@login_required(login_url="/login/")
def accessLogin(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "accessLogin.html", context)    


def detailItems(request, id):
    categories = Category.objects.all()
    detail = Item.objects.get(pk=id)
    context = {"detail":detail, "infoCategories": categories}
    return render(request, "detailItems.html", context)

def make_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = request.POST.get('date')
        

        reservation = Reservation(
            name=name,
            email=email,
            phone=phone,
            date=date,
            message=message
        )
        reservation.save()
        return redirect('reservation_success') 

    return render(request, 'reservation_form.html')

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            TopNote.objects.create(title=title, description=description)
            return redirect('home')
    
    top_notes = TopNote.objects.all()
    return render(request, 'home.html', {'top_notes': top_notes})