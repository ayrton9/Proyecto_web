from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from django.contrib import messages

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Categoria, SubCategoria , Marca, UnidadMeidida, Producto

from .forms import CategoriaForm, SubCategoriaForm , MarcaForm , UMForm, ProductoForm

from bases.views import SinPrivilegios

from django.contrib.messages.views import  SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required



class CategoriaView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_categoria"
    model = Categoria
    template_name= "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'
    success_message= "Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_categoria"
    model = Categoria
    template_name= "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'
    success_message= "Categoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_categoria', login_url='bases:sin_privilegios')
def categoria_inactivar(request, id):
    cat = Categoria.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not cat:
        return redirect("inv:categoria_list")

    if request.method=='GET':
        contexto={"obj":cat}

    if request.method=='POST':
        cat.estado=False
        cat.save()
        messages.success(request,'Categoria Inactivada')
        return redirect('inv:categoria_list')

    return render(request,template_name,contexto)


class SubCategoriaView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class SubCategoriaNew(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_subcategoria"
    model = SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'
    success_message= "SubCategoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_subcategoria"
    model = SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = 'bases:login'
    success_message= "SubCategoria Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_subcategoria', login_url='bases:sin_privilegios')
def subcategoria_inactivar(request, id):
    sub = SubCategoria.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not sub:
        return redirect("inv:subcategoria_list")

    if request.method=='GET':
        contexto={"obj":sub}

    if request.method=='POST':
        sub.estado=False
        sub.save()
        messages.success(request,'SubCategoria Inactivada')
        return redirect('inv:subcategoria_list')

    return render(request,template_name,contexto)


class MarcaView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MarcaNew(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_marca"
    model = Marca
    template_name= "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = 'bases:login'
    success_message= "Marca Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_marca"
    model = Marca
    template_name= "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = 'bases:login'
    success_message= "Marca Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method=='GET':
        contexto={"obj":marca}

    if request.method=='POST':
        marca.estado=False
        marca.save()
        messages.success(request,'Marca Inactivada')
        return redirect('inv:marca_list')

    return render(request,template_name,contexto)


class UMView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "inv.view_unidadmeidida"
    model = UnidadMeidida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class UMNew(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_unidadmeidida"
    model = UnidadMeidida
    template_name= "inv/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = 'bases:login'
    success_message= "UM Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class UMEdit(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_unidadmeidida"
    model = UnidadMeidida
    template_name= "inv/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")
    login_url = 'bases:login'
    success_message= "UM Actualizada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_unidadmeidida', login_url='bases:sin_privilegios')
def um_inactivar(request, id):
    um = UnidadMeidida.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not um:
        return redirect("inv:um_list")

    if request.method=='GET':
        contexto={"obj":um}

    if request.method=='POST':
        um.estado=False
        um.save()
        messages.success(request,'UM Inactivada')
        return redirect('inv:um_list')

    return render(request,template_name,contexto)


class ProductoView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class ProductoNew(SuccessMessageMixin, LoginRequiredMixin,SinPrivilegios, generic.CreateView):
    permission_required = "inv.add_producto"
    model = Producto
    template_name= "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = 'bases:login'
    success_message= "Producto Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProductoEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "inv.change_producto"
    model = Producto
    template_name= "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = 'bases:login'
    success_message= "Producto Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()

    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method=='GET':
        contexto={"obj":prod}

    if request.method=='POST':
        prod.estado=False
        prod.save()
        messages.success(request,'Producto Inactivado')
        return redirect('inv:producto_list')

    return render(request,template_name,contexto)