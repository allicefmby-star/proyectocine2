from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm

# Create your views here.

def registro(request):
    """
    Vista para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        # Si el método es POST, se enviaron datos.
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo usuario.
            user = form.save()
            # Inicia sesión automáticamente para el usuario recién registrado.
            login(request, user)
            # Redirige al usuario a la página de inicio (o donde prefieras).
            # ¡Asegúrate de tener una URL con name='home' o cambia 'home' por la que necesites!
            return redirect('home') 
    else:
        # Si el método es GET, se muestra un formulario vacío.
        form = RegistroUsuarioForm()
        
    # Renderiza la plantilla 'register.html' con el formulario como contexto.
    return render(request, 'register.html', {'form': form})
