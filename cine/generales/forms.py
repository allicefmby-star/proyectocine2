
# En tu_app/forms.py

from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    """
    Este formulario hereda de UserCreationForm de Django.
    
    Automáticamente incluye los campos:
    - username (nombre de usuario)
    - password (contraseña)
    - password2 (confirmación de contraseña)
    
    También se encarga de validar que las dos contraseñas coincidan.
    """
    class Meta(UserCreationForm.Meta):
        # Puedes añadir más campos aquí si lo necesitas, como 'email' o 'first_name'
        # fields = UserCreationForm.Meta.fields + ('email',)
        pass