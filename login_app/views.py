
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Document
from .models import Member


def render_login(request):
    return render(request, 'login.html')


def perform_login(request):
    if request.method != "POST":
        return HttResponse("Method is not allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            next_url = request.GET.get('next', reverse('admin_dashboard'))
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, "Invalid username or password",
                           extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('render_login') + "?next=" + request.GET.get('next', ''))


@login_required
def admin_dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please login first to access this page.")
        return HttpResponseRedirect(reverse('render_login') + "?next=" + request.path)
    else:
        # username = request.user.username
        active_members = Member.objects.filter(status='Active')
        patrons = Member.objects.filter(status='Patron')
        affiliate_members = Member.objects.filter(status='Affiliate')
        male = Member.objects.filter(gender='M')
        female = Member.objects.filter(gender='F')
        context = {
            'active_members': active_members,
            'affiliate_members':affiliate_members,
            'patrons': patrons,
            'male': male,
            'female': female,
        }
        return render(request, "admin_dashboard.html", context)


def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def all_members(request):
    return render(request, 'all_members.html')


# def add_member(request):
#     return render(request, 'add_member.html')


def executive(request):
    return render(request, 'executive.html')


# def active_members(request):
#     return render(request, 'active_members.html')

def active_members(request):
    active_members = Member.objects.filter(status='Active')
    return render(request, 'active_members.html', {'active_members': active_members})


def affiliate_members(request):
    affiliate_members = Member.objects.filter(status='Affiliate')
    return render(request, 'affiliate_members.html', {'affiliate_members': affiliate_members})


def patrons(request):
    patrons = Member.objects.filter(status='Patron')
    return render(request, 'patrons.html',{'patrons':patrons})

# def document(request):
#     if request.method == 'POST':
#         document = Document()
#         document.name = request.POST['document_name']
#         document.image = request.FILES['document_image']
#        document = Document(document_name=document_name, document_image=document_image)
#         document.save()
#         return redirect('document')
#     return render(request, 'document.html')


def document(request):
    success_message = None
    
    if request.method == 'POST':
        document_name = request.POST['document_name']
        document_image = request.FILES['document_image']
        
        document = Document(document_name=document_name, document_image=document_image)
        document.save()

        success_message = 'Document saved successfully.'

    return render(request, 'document.html', {'success_message': success_message})


def add_member(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        surname = request.POST['surname']
        gender = request.POST['gender']
        contact_number = request.POST['contact_number']
        house_number = request.POST['house_number']
        hometown = request.POST['hometown']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        profile_image = request.FILES.get('profile_image')
        previous_school = request.POST['previous_school']
        current_school = request.POST['current_school']
        occupation = request.POST['occupation']
        course = request.POST['course']
        level = request.POST['level']
        field = request.POST['field']
        date_of_joining = request.POST['date_of_joining']
        status = request.POST['status']

        member = Member(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            gender=gender,
            contact_number=contact_number,
            house_number=house_number,
            hometown=hometown,
            email=email,
            date_of_birth=date_of_birth,
            profile_image=profile_image,
            previous_school=previous_school,
            current_school=current_school,
            occupation=occupation,
            course=course,
            level=level,
            field=field,
            date_of_joining=date_of_joining,
            status=status
        )
        member.save()

        # Redirect to a success page or perform any additional actions
        messages.success(request, 'Member added successfully.')
    return render(request, 'add_member.html')
