from django.shortcuts import render, redirect
from .models import plato
from django.contrib import messages

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
    # Obtiene los datos del formulario de registro de platos.
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    precio=request.POST['numprecio']
    # Crea un nuevo objeto de plato con los datos proporcionados y lo guarda en la base de datos.
    nuevo_plato=plato.objects.create(codigo=codigo, nombre=nombre, precio=precio)
    # Agrega un mensaje de éxito para indicar que el plato se ha registrado correctamente.
    messages.success(request, '¡Plato registrado!')
    # Redirecciona a la página principal.
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

