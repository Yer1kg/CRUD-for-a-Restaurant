from django.shortcuts import render, redirect
from .models import plato
from django.contrib import messages
from django.db import IntegrityError

MAX_PLATOS = 6  # Establece tu límite aquí

# La función home renderiza la página principal y lista todos los platos.
def home(request):
    # Obtiene todos los platos de la base de datos.
    platoslistados =plato.objects.all()
    # Agrega un mensaje de éxito para indicar que los platos se han listado correctamente.
    messages.success(request, '¡Plato listado!')
    # Renderiza la página gestiondeplatos.html con la lista de platos.
    return render(request, "gestiondeplatos.html", {"platos": platoslistados})

# La función registrarPlato registra un nuevo plato en la base de datos.
def registrarPlato(request):
    if request.method == "POST":
        # Verifica si se ha alcanzado el límite
        if plato.objects.count() >= MAX_PLATOS:
            messages.error(request, "No puedes crear más de {} platos.".format(MAX_PLATOS))
            return redirect('/')
        
        try:
            # Obtiene el código del POST
            codigo = request.POST.get("txtcodigo")
            
            # Verifica si ya existe un plato con este código
            if plato.objects.filter(codigo=codigo).exists():
                # Si existe, muestra un mensaje de error
                messages.error(request, "El código ya está en uso. Por favor, elige otro.")
                return redirect('/registrarPlato/')

            # Si el código es único, crea un nuevo plato
            nuevo_plato = plato(
                codigo=codigo,
                nombre=request.POST.get("txtnombre"),
                precio=int(request.POST.get("numprecio", 0))  # Convertir a número
            )
            
            # Guarda el nuevo plato
            nuevo_plato.save()
            messages.success(request, '¡Plato registrado con éxito!')
            return redirect('/')
        
        except Exception as e:
            # Maneja otros posibles errores
            messages.error(request, f"Error al registrar el plato: {str(e)}")
            return redirect('/registrarPlato/')
    
    # Si no es POST, redirige a la página de inicio
    return redirect('/')


# La función edicionPlato renderiza la página de edición de un plato específico.
def edicionPlato(request, codigo):
    # Obtiene el plato específico de la base de datos utilizando el código proporcionado.
    plato_nuevo = plato.objects.get(codigo=codigo)
    # Renderiza la página edicionPlato.html con el plato a editar.
    return render(request, "edicionPlato.html", {"plato": plato_nuevo})

# La función editarPlato actualiza la información de un plato en la base de datos.
def editarPlato(request):
    # Obtiene los datos del formulario de edición de platos. 
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    precio=request.POST['numprecio']
    # Obtiene el plato específico de la base de datos utilizando el código proporcionado.
    plato_nuevo = plato.objects.get(codigo=codigo)
    # Actualiza el nombre y el precio del plato.
    plato_nuevo.nombre = nombre
    plato_nuevo.precio = precio
    plato_nuevo.save()
    # Agrega un mensaje de éxito para indicar que el plato se ha actualizado correctamente.
    messages.success(request, '¡Plato Actualizado!')
    # Redirecciona a la página principal.
    return redirect('/')

# La función eliminarPlato elimina un plato de la base de datos.    
def eliminarPlato(request, codigo):
    # Obtiene el plato específico de la base de datos utilizando el código proporcionado.
    nuevo_plato = plato.objects.get(codigo=codigo)
    # Elimina el plato de la base de datos.
    nuevo_plato.delete()
    # Agrega un mensaje de éxito para indicar que el plato se ha eliminado correctamente.
    messages.success(request, '¡Plato Eliminado!')
    # Redirecciona a la página principal.
    return redirect('/')

# La función contacto renderiza la página de contacto.
def contacto(request):
    return render(request, 'contacto.html')



    
  
