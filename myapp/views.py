from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def cases(request):
    return render(request, 'cases.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')

def services(request):
    try:
        data = serviceCategories.objects.all()
        context = {"data":data}
        return render(request, 'services.html', context)
    except:
        pass
    return render(request, 'services.html')

def service(request):
    if request.method == "POST":
        cateid = request.POST.get("cateid")
        try:
            data = Services.objects.filter(cate=serviceCategories(id=cateid))
            return render(request, "Service.html", {"data":data})
        except:
            pass


def serviceDetails(request):
    if request.method == "POST":
        serviceid = request.POST.get("serviceid")
        try:
            servicedetails = Services.objects.get(id=serviceid)
            print(servicedetails)
            context = {"data": servicedetails}
            return render(request, "servicesDetails.html", context)
        except:
            print('sdjisdfokdso')

        return render(request, "servicesDetails.html")

def loginpage(request):
    return render(request, 'login.html')



def verifyuser(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("password")

        try:
            userdata = User.objects.get(email=email, password=pwd)
            request.session["login_id"] = userdata.id
            request.session.save()
            messages.success(request, "Login Successfull!!")
            return redirect(index)

        except User.DoesNotExist:
            messages.error(request, "Invalid Details")
            return redirect(loginpage)
    else:
        messages.info(request, "Some Error Occurs")
    return render(request, "login.html")

def signuppage(request):
    return render(request, 'signup.html')


def registeruser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        profile = request.FILES["dp"]
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please choose a different email.")
            return redirect(loginpage)
        else:
            try:
                if password1 == password2:
                    insertuser = User(name=name, email=email, phone=phone, password=password1, dp=profile, timestamp="")
                    insertuser.save()
                    messages.success(request, "Account created now you can login !!!")
                    return redirect(loginpage)
            except:
                pass
        return redirect(loginpage)


def forgotpwdpage(request):
    return render(request, "forgotpassword.html")


def forgotpwd(request):
    if request.method == 'POST':
        username = request.POST.get('email')

        try:
            user = User.objects.get(email=username)

        except user.DoesNotExist:
            user = None

        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = f'''Subject: Your Password Reset:
A Fresh Start for You !

Great news! We've enhanced your experience with a secure password reset. 

Your temporary password is [  {password}  ]  for easy access. 

Thank you for trusting 

Best Regards,
Our Team
'''
            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                '#',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = User.objects.get(email=username)
            cuser.password = password
            cuser.save(update_fields=['password'])

            messages.info(request, 'mail is sent successfully to your registered email')
            return redirect(index)
        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)


def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        insertcontact = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        insertcontact.save()
        messages.success(request, "Response Recorded !")
        return redirect(index)
    return render(request, 'contact.html')



def logout(request):
    try:
        del request.session["login_id"]
        messages.info(request, "Logut Successful!!")
        return redirect(loginpage)
    except:
        pass



def feedbakcpage(request):
    return render(request, "feedback.html")



def storefeedback(request):
    if request.method == "POST":
        uid = request.session["login_id"]
        rating = request.POST.get("rating")
        message = request.POST.get("message")

        insert = Feedback(user=User(id=uid), rating=rating, comments=message, timestamp="")
        insert.save()

        messages.info(request, "Your Feedback Has Been Submitted")
        return redirect(feedbakcpage)
    return render(request, "feedback.html")


def profile(request):
    try:
        userdata = User.objects.get(id=request.session["login_id"])
        return render(request, "profile.html", {"userdata":userdata})
    except:
        pass

    return render(request, "profile.html")



def storeInquiry(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        user = request.session["login_id"]
        service = request.POST.get("serviceid")
        try:
            inquiry = serviceInquiry(user=User(id=user), serviceId=Services(id=service), subject=subject,message=message, timestamp="")
            inquiry.save()
            messages.success(request, "Your Response Recorded Successful! ")
            return redirect(index)
        except:
            pass
    return render(request, "services.html")


def courcesCategoriesPage(request):
    try:
        data = courcesCategories.objects.all()
        context = {"data": data}
        return render(request, 'courceCategories.html', context)
    except:
        pass
    return render(request, "courceCategories.html")


def cources(request):
    if request.method == "POST":
        cateid = request.POST.get("cateid")
        print(cateid)
        try:
            data = Cource.objects.filter(cate=courcesCategories(id=cateid))
            return render(request, "cources.html", {"data":data})
        except:
            pass


def courceDetails(request):
    if request.method == "POST":
        courceid = request.POST.get("courceid")
        try:
            courceDetail = Cource.objects.get(id=courceid)
            context = {"data": courceDetail}
            return render(request, "courceDetails.html", context)
        except:
            pass
        return render(request, "courceDetails.html")



def storeCourceInquiry(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        user = request.session["login_id"]
        cource = request.POST.get("courceid")
        try:
            inquiry = courceInquiry(user=User(id=user), courceId=Cource(id=cource), subject=subject,message=message, timestamp="")
            inquiry.save()
            messages.success(request, "Your Response Recorded Successful! ")
            return redirect(index)
        except:
            pass
    return render(request, "index.html")

