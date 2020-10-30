from django.shortcuts import render, redirect

from django.contrib import messages

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import  SuccessMessageMixin

from .models import Proveedor, ComprasEnc, ComprasDet

from inv.models import Producto

from cmp.forms import ProveedorForm, ComprasEncForm

from bases.views import SinPrivilegios

from django.contrib.auth.decorators import login_required, permission_required


class ProveedorView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "cmp.view_proveedor"
    model =  Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class ProveedorNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.CreateView):
    permission_required = "cmp.add_proveedor"
    model = Proveedor
    template_name= "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    success_message= "Proveedor Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class ProveedorEdit(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "cmp.change_proveedor"
    model = Proveedor
    template_name= "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'
    success_message= "Proveedor Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('cmp.change_proveedor', login_url='bases:sin_privilegios')
def proveedor_inactivar(request, id):
    pro = Proveedor.objects.filter(pk=id).first()

    contexto = {}
    template_name = "cmp/inactivar_prv.html"

    if not pro:
        return redirect("cmp:proveedor_list")

    if request.method=='GET':
        contexto={"obj":pro}

    if request.method=='POST':
        pro.estado=False
        pro.save()
        messages.success(request, 'Proveedor Inactivado')
        return redirect('cmp:proveedor_list')

    return render(request,template_name,contexto)


    
class ComprasView(LoginRequiredMixin, SinPrivilegios, generic.ListView):
    permission_required = "cmp.view_comprasenc"
    model =  ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


@login_required(login_url='/login/')
@permission_required('cmp.view_comprasenc', login_url='bases:sin_privilegios')
def compras(request,compra_id=None):
    template_name="cmp/compras.html"
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm() 
