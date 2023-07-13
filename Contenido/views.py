from django.shortcuts import render, redirect
from .models import Plantita, Categoria
from .forms import PlantitaForm, LoginForm
from .models import User
from Contenido.compra import Carrito
from django.contrib.auth.decorators import login_required
# Create your views here.


def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Inicio.html')  # Cambia 'home' por la URL a la que quieres redirigir después del inicio de sesión exitoso
            else:
                form.add_error(None, "Credenciales inválidas")  # Agrega un error al formulario si las credenciales son inválidas
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def Incio(request):
    return render(request,'Incio.html')
    
def formulario(request):
    return render(request,'formulario.html')

@login_required
def APIrets(request):
    return render(request,'APIrets.html')

@login_required
def desplegable(request):
    return render(request,'desplegable.html')

@login_required
def mision(request):
    return render(request,'mision.html')

@login_required
def base(request):
    return render(request,'base.html')

@login_required
def index(request):
    plantitas= Plantita.objects.all()
    datos={'plantitas' : plantitas}
    return render(request, 'index.html', datos)


@login_required
def crear(request):
    if request.method == 'POST':
        plantitaform = PlantitaForm(request.POST, request.FILES)
        if plantitaform.is_valid():
            plantitaform.save() #similar en funcion al metodo insert
            return redirect ('index')
    else:
        plantitaform=PlantitaForm()
    return render(request, 'crear.html', {'plantitaform' : plantitaform})

@login_required
def modificar(request,id):
    plantitaModificada = Plantita.objects.get(idProducto = id)
    datos ={
        'form': PlantitaForm(instance=plantitaModificada)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = PlantitaForm(data=request.POST, instance=plantitaModificada)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('index')
    return render(request,'modificar.html', datos)

@login_required
def eliminar(request, id):
    plantitaEliminada=Plantita.objects.get(idProducto=id)
    plantitaEliminada.delete()
    return redirect('index')


def tienda(request):
    plantitas = Plantita.objects.all()
    datos={
        'plantitas':plantitas
    }
    return render(request, 'tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    plantitas = Plantita.objects.get(idProducto=id)
    carrito_compra.agregar(plantita=plantitas)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    plantitas = Plantita.objects.get(idProducto=id)
    carrito_compra.eliminar(plantita=plantitas)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    plantitas = Plantita.objects.get(idProducto=id)
    carrito_compra.restar(plantita=plantitas)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar(plantita=plantitas)
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Plantita.objects.get(idProducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)