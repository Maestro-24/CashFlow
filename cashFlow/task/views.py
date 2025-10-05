from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class RecordListView(ListView):
    model = FinancialRecord
    template_name = 'finance/record_list.html'
    context_object_name = 'records'
    paginate_by = 20

    def get_queryset(self):
        queryset = FinancialRecord.objects.select_related(
            'status', 'operation_type', 'category', 'subcategory'
        ).order_by('-record_date', '-created_at')
        
        # Фильтрация
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        status = self.request.GET.get('status')
        operation_type = self.request.GET.get('operation_type')
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        
        if date_from:
            queryset = queryset.filter(record_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(record_date__lte=date_to)
        if status:
            queryset = queryset.filter(status_id=status)
        if operation_type:
            queryset = queryset.filter(operation_type_id=operation_type)
        if category:
            queryset = queryset.filter(category_id=category)
        if subcategory:
            queryset = queryset.filter(subcategory_id=subcategory)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['operation_types'] = OperationType.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context

class RecordCreateView(CreateView):
    model = FinancialRecord
    form_class = FinancialRecordForm
    template_name = 'finance/record_form.html'
    success_url = reverse_lazy('finance:record_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class RecordUpdateView(UpdateView):
    model = FinancialRecord
    form_class = FinancialRecordForm
    template_name = 'finance/record_form.html'
    success_url = reverse_lazy('finance:record_list')

class RecordDeleteView(DeleteView):
    model = FinancialRecord
    template_name = 'finance/record_confirm_delete.html'
    success_url = reverse_lazy('finance:record_list')

def reference_management(request):
    # Status management
    if request.method == 'POST' and 'add_status' in request.POST:
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    
    # Operation Type management
    if request.method == 'POST' and 'add_operation_type' in request.POST:
        form = OperationTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    
    # Category management
    if request.method == 'POST' and 'add_category' in request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    
    # Subcategory management
    if request.method == 'POST' and 'add_subcategory' in request.POST:
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    
    context = {
        'statuses': Status.objects.all(),
        'operation_types': OperationType.objects.all(),
        'categories': Category.objects.all(),
        'subcategories': SubCategory.objects.all(),
        'status_form': StatusForm(),
        'operation_type_form': OperationTypeForm(),
        'category_form': CategoryForm(),
        'subcategory_form': SubcategoryForm(),
    }
    return render(request, 'finance/reference_management.html', context)

def delete_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    status.delete()
    return redirect('finance:reference_management')

def delete_operation_type(request, pk):
    operation_type = get_object_or_404(OperationType, pk=pk)
    operation_type.delete()
    return redirect('finance:reference_management')

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('finance:reference_management')

def delete_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect('finance:reference_management')

def get_categories_by_type(request):
    operation_type_id = request.GET.get('operation_type_id')
    categories = Category.objects.filter(operation_type_id=operation_type_id)
    data = [{'id': cat.id, 'name': cat.name} for cat in categories]
    return JsonResponse(data, safe=False)

def get_subcategories_by_category(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id)
    data = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
    return JsonResponse(data, safe=False)


def edit_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    else:
        form = StatusForm(instance=status)
    
    return render(request, 'finance/edit_reference.html', {
        'form': form,
        'title': 'Редактирование статуса',
        'cancel_url': 'finance:reference_management'
    })

def edit_operation_type(request, pk):
    operation_type = get_object_or_404(OperationType, pk=pk)
    if request.method == 'POST':
        form = OperationTypeForm(request.POST, instance=operation_type)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    else:
        form = OperationTypeForm(instance=operation_type)
    
    return render(request, 'finance/edit_reference.html', {
        'form': form,
        'title': 'Редактирование типа операции',
        'cancel_url': 'finance:reference_management'
    })

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'finance/edit_reference.html', {
        'form': form,
        'title': 'Редактирование категории',
        'cancel_url': 'finance:reference_management'
    })

def edit_subcategory(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('finance:reference_management')
    else:
        form = SubcategoryForm(instance=subcategory)
    
    return render(request, 'finance/edit_reference.html', {
        'form': form,
        'title': 'Редактирование подкатегории',
        'cancel_url': 'finance:reference_management'
    })