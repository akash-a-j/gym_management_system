from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance,Category,Product
from .forms import TrainerForm, GalleryForm, ProductForm

# Create your views here.
def Home(request):
    return render(request,"index.html")

def product_list(request, category_id=None):
    try:
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            products = Product.objects.filter(category=category, is_available=True)
            context = {'category': category, 'products': products}
        else:
            products = Product.objects.filter(is_available=True)
            categories = Category.objects.all()
            context = {
                'products': products,
                'categories': categories
            }
        
        # Add debug information
        print(f"Number of products found: {products.count()}")
        return render(request, 'product_list.html', context)
    except Exception as e:
        print(f"Error in product_list view: {str(e)}")
        messages.error(request, "An error occurred while loading products.")
        return render(request, 'product_list.html', {'products': []})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def trainer(request):
    posts=Trainer.objects.all()
    context={"posts":posts}
    return render(request,"trainer.html",context)

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('handlelogin')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('attendance')
    return render(request,"attendance.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('handlelogin')
    # usernames are phone numbers in this project
    user_phone = request.user.username
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)


def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('handlelogin')
    
    return render(request,"signup.html")




def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('Home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('handlelogin')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('handlelogin')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('contact')
        
    return render(request,"contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('handlelogin')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('enroll')


    return render(request,"enroll.html",context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_trainers(request):
    trainers = Trainer.objects.all()
    context = {'trainers': trainers}
    return render(request, 'manage_trainers.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_add(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainer added successfully!')
            return redirect('manage_trainers')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_edit(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainer updated successfully!')
            return redirect('manage_trainers')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_delete(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        trainer.delete()
        messages.success(request, 'Trainer deleted successfully!')
        return redirect('manage_trainers')
    # This view will only handle POST requests, so we can redirect if it's a GET request
    return redirect('manage_trainers')

@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('manage_gallery')
    else:
        form = GalleryForm()
    
    gallery_items = Gallery.objects.all()
    context = {
        'form': form,
        'gallery_items': gallery_items
    }
    return render(request, 'manage_gallery.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def gallery_delete(request, pk):
    gallery_item = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        gallery_item.delete()
        messages.success(request, 'Image deleted successfully!')
        return redirect('manage_gallery')
    return redirect('manage_gallery')

@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'manage_products.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('manage_products')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('manage_products')
    return redirect('manage_products')