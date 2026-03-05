from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (User.USERNAME_FIELD,)