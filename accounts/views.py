from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import AccountUser
from .utils import generate_salt, hash_password

# ==========================================
# Registration Module
# Handles user creation by generating a salt
# and hashing the password before database storage.
# ==========================================
def register_view(request):
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            # Check if user already exists
            if AccountUser.objects.filter(username=username).exists():
                message = "Username already exists"
            else:
                # 1. Generate a random unique salt for the user
                salt = generate_salt()

                # 2. Hash the password with the salt and pepper
                password_hash = hash_password(password, salt)
                
                # 3. Store only the username, hashed password, and salt in the database
                AccountUser.objects.create(
                    username=username,
                    password_hash=password_hash,
                    salt=salt,
                )
                message = "Registration Successful"
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form, "message": message})


# ==========================================
# Login Module
# Handles user authentication by retrieving 
# the stored salt and verifying the password hash.
# ==========================================
def login_view(request):
    if request.session.get("username"):
        return redirect("home")

    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                # 1. Retrieve the corresponding user from the database
                user = AccountUser.objects.get(username=username)
                
                # 2. Re-apply the hash using the input password, stored salt, and secret pepper
                computed_hash = hash_password(password, user.salt)
                
                # 3. Compare the result with the stored hash
                if computed_hash == user.password_hash:
                    request.session["username"] = user.username
                    request.session["login_success"] = True
                    return redirect("home")
                else:
                    message = "Invalid Username or Password"
            except AccountUser.DoesNotExist:
                message = "Invalid Username or Password"
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form, "message": message})


def home_view(request):
    username = request.session.get("username")
    login_message = None
    if request.session.pop("login_success", False):
        login_message = "Login Successful"
    return render(
        request,
        "accounts/home.html",
        {"username": username, "message": login_message},
    )


def logout_view(request):
    request.session.flush()
    return redirect("login")
