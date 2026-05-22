import re
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"id": "id_password", "autocomplete": "new-password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"id": "id_confirm_password", "autocomplete": "new-password"}),
        label="Confirm Password",
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password") or ""
        confirm_password = cleaned_data.get("confirm_password") or ""

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        if password:
            if len(password) < 12:
                self.add_error("password", "Password must be at least 12 characters.")
            if not re.search(r"[a-z]", password):
                self.add_error("password", "Password must include at least one lowercase letter.")
            if not re.search(r"[A-Z]", password):
                self.add_error("password", "Password must include at least one uppercase letter.")
            if not re.search(r"\d", password):
                self.add_error("password", "Password must include at least one digit.")
            if not re.search(r"[^A-Za-z0-9]", password):
                self.add_error("password", "Password must include at least one symbol.")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
