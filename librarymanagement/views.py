from django.shortcuts import render, redirect,get_object_or_404
from .models import (BookDetails, BookType, Vendor,
                        ProductCategory, PurchaseOrder, Location, 
                        LibraryNumber, RoomNo, SelveNo, Journal,
                        E_Book, Magazine)
from django.views.generic import ListView, CreateView, DeleteView, DetailView, DeleteView, UpdateView
from .forms import (BookAddForm,BookTypeForm,VendorForm,ProductCategoryForm,
                    ProductCategoryFormUpdate,BookTypeFormUpdate,PurchaseOrderForm,
                    LocationForm,LibraryNumberCreateForm,RoomNoCreateForm,ShelveForm,
                    LocationUpdateForm, JournalForm, EBookForm, MagazineForm)
from django.urls import reverse_lazy
from django.http import HttpResponse


class BookTypeFormList(ListView):
    template_name='library/booktypelist.html'
    queryset=BookType.objects.all()
    context_object_name='book_type_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)        
        return context

class BookTypeFormCreate(CreateView):
    model = BookType
    template_name = 'library/booktype.html'
    form_class = BookTypeForm

    def get_context_data(self, *args ,**kwargs):
        context=super(BookTypeFormCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':BookTypeForm()}
        return render(request,'library/booktype.html',context)
    
    def post(self,request,*args,**kwargs):
        form=BookTypeForm(request.POST or None,request.FILES or None)        
        if form.is_valid():
            form.save()
            return redirect('book_type_list')
        return render(request,'library/booktype.html',{'form':form})

class BookTypeUpdate(UpdateView):
    model = BookType
    template_name = 'library/booktype.html'
    success_url=reverse_lazy('book_type_list')
    form_class = BookTypeFormUpdate

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(BookType, pk=pk)
        form = BookTypeFormUpdate(request.POST or None, request.FILES or None, instance=instance)
        print(pk)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('book_type_list'))

class BookTypeDelete(DeleteView):
    model = BookType
    template_name = 'library/booktype_confirm_delete.html'
    success_url=reverse_lazy('book_type_list')


class BookList(ListView):
    template_name='library/booklist.html'
    queryset=BookDetails.objects.all()
    context_object_name='book_list'    
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class BookEdit(UpdateView):
    pass

def bookeditview(request,pk):
    obj = get_object_or_404(BookDetails, pk=pk)
    if request.method=="POST":
        form = BookAddForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('book_list'))
    else:
        form = BookAddForm()
        form.fields["name"].initial = obj.name
        form.fields["ISBN"].initial = obj.ISBN
        form.fields["book_author"].initial = obj.book_author
        form.fields["publication_date"].initial = obj.publication_date
        form.fields["book_type"].initial = obj.book_type
        form.fields["product_category"].initial = obj.product_category
        form.fields["book_price"].initial = obj.book_price
        form.fields["book_description"].initial = obj.book_description
        form.fields["barcode"].initial = obj.barcode
        form.fields["cover"].initial = obj.cover
        form.fields["book_number"].initial = obj.book_number
        form.fields["book_subtitle"].initial = obj.book_subtitle
        form.fields["book_sub_author"].initial = obj.book_sub_author
        form.fields["book_sub_author1"].initial = obj.book_sub_author1
        form.fields["book_sub_author2"].initial = obj.book_sub_author2
        form.fields["book_sub_author3"].initial = obj.book_sub_author3
        form.fields["publisher"].initial = obj.publisher
        form.fields["genre"].initial = obj.genre
        form.fields["no_of_pages"].initial = obj.no_of_pages
        form.fields["language"].initial = obj.language
        form.fields["edition"].initial = obj.edition
        form.fields["link"].initial = obj.link
        form.fields["location"].initial = obj.location
        form.fields["supplier"].initial = obj.supplier
        form.fields["subject"].initial = obj.subject
        return render(request,'library/editbook.html',{'form':form})

class BookDelete(DeleteView):
    model = BookDetails
    success_url = reverse_lazy('book_list')

class BookCreate(CreateView):
    model = BookDetails
    template_name = 'library/addbook.html'
    form_class = BookAddForm

    def get_context_data(self, *args ,**kwargs):
        context=super(BookCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':BookAddForm()}
        return render(request,'library/addbook.html',context)
    
    def post(self,request,*args,**kwargs):
        form=BookAddForm(request.POST or None,request.FILES or None)
        
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
            return redirect('book_list')
        else:
            print("error")
            print(form.errors)
        return render(request,'library/addbook.html',{'form':form})



class VendorCreate(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'library/vendor_create.html'

    def get_context_data(self, *args ,**kwargs):
        context=super(VendorCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':VendorForm()}
        return render(request,'library/vendor_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=VendorForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('vendor_list')        
        return render(request,'library/vendor_create.html',{'form':form})



class VendorList(ListView):
    template_name='library/vendor_list.html'
    queryset=Vendor.objects.all()
    context_object_name='vendor_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)        
        return context

def vendor_update(request, pk):
    obj = get_object_or_404(Vendor, pk=pk)
    if request.method=="POST":
        form = VendorForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('vendor_list'))

    else:
        form = VendorForm()
        form.fields["name"].initial = obj.name
        form.fields["contact"].initial = obj.contact
        form.fields["email"].initial = obj.email
        form.fields["address"].initial = obj.address
        return render(request,'library/vendor_edit.html',{'form':form})


class VendorDelete(DeleteView):
    model = Vendor
    success_url=reverse_lazy('vendor_list')

class ProductCategoryCreate(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'library/add_product_category.html'

    def get_context_data(self, *args ,**kwargs):
        context=super(ProductCategoryCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':ProductCategoryForm()}
        return render(request,'library/add_product_category.html',context)
    
    def post(self,request,*args,**kwargs):
        form=ProductCategoryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('product_category_list')        
        return render(request,'library/add_product_category.html',{'form':form})

class ProductCategoryList(ListView):
    model = ProductCategory
    queryset = ProductCategory.objects.all()
    template_name='library/product_category_list.html'
    context_object_name='product_category_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)        
        return context

class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    template_name='library/add_product_category.html'
    success_url=reverse_lazy('product_category_list')
    form_class = ProductCategoryFormUpdate

    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(ProductCategory, pk=pk)
        form = ProductCategoryFormUpdate(request.POST or None, request.FILES or None, instance=instance)
        print(pk)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('product_category_list'))

class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    template_name = 'library/productcategory_confirm_delete.html'
    success_url=reverse_lazy('product_category_list')

class PurchaseOrderCreate(CreateView):
    model = PurchaseOrder
    template_name = 'library/purchasorder_create.html'
    form_class = PurchaseOrderForm

    def get_context_data(self, *args ,**kwargs):
        context=super(PurchaseOrderCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':PurchaseOrderForm()}
        return render(request,'library/purchasorder_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=PurchaseOrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('purchase_order_list')        
        return render(request,'library/purchasorder_create.html',{'form':form})

class PurchaseOrderList(ListView):
    model = PurchaseOrder
    queryset = PurchaseOrder.objects.all()
    template_name='library/purchase_order_list.html'
    context_object_name='purchase_order_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)        
        return context

def purchaseorder_update(request,pk):
    obj = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method=="POST":
        form = PurchaseOrderForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('purchase_order_list'))

    else:
        form = PurchaseOrderForm()
        form.fields["vendor"].initial = obj.vendor
        form.fields["call_no"].initial = obj.call_no
        form.fields["bill_no"].initial = obj.bill_no
        form.fields["bill_date"].initial = obj.bill_date
        form.fields["price"].initial = obj.price
        return render(request,'library/purchase_order_update.html',{'form':form})

class PurchaseOrderDelete(DeleteView):
    model = PurchaseOrder
    success_url=reverse_lazy('purchase_order_list')


class LocationCreate(CreateView):
    model = Location
    template_name = 'library/location_create.html'
    form_class = LocationForm

    def get_context_data(self, *args ,**kwargs):
        context=super(LocationCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':LocationForm()}
        return render(request,'library/location_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=LocationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('location_list')        
        return render(request,'library/location_create.html',{'form':form})

class LocationList(ListView):
    model = Location
    queryset = Location.objects.all()
    template_name='library/location_list.html'
    context_object_name='location_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class LocationDelete(DeleteView):
    model = Location
    success_url=reverse_lazy('location_list')

def LocationUpdate(request,pk):
    obj = get_object_or_404(Location, pk=pk)
    if request.method=="POST":
        form = LocationUpdateForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        else:
            print(form.errors)
        return redirect(reverse_lazy('location_list'))

    else:
        form = LocationUpdateForm()        
        form.fields["selve_no"].initial = obj.selve_no
        form.fields["rack_no"].initial = obj.rack_no
        form.fields["capacity"].initial = obj.capacity
        return render(request,'library/location_update.html',{'form':form})

class LibraryCreate(CreateView):
    model = LibraryNumber
    template_name = 'library/library_create.html'
    form_class = LibraryNumberCreateForm

    def get_context_data(self, *args ,**kwargs):
        context=super(LibraryCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':LibraryNumberCreateForm()}
        return render(request,'library/library_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=LibraryNumberCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('library_list')
        return render(request,'library/library_create.html',{'form':form})

class LibraryList(ListView):
    model = LibraryNumber
    queryset = LibraryNumber.objects.all()
    template_name='library/library_list.html'
    context_object_name='library_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class RoomCreate(CreateView):
    model = RoomNo
    template_name = 'library/room_create.html'
    form_class = RoomNoCreateForm

    def get_context_data(self, *args ,**kwargs):
        context=super(RoomCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':RoomNoCreateForm()}
        return render(request,'library/room_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=RoomNoCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('room_list')
        return render(request,'library/room_create.html',{'form':form})

class RoomList(ListView):
    model = RoomNo
    queryset = RoomNo.objects.all()
    template_name='library/room_list.html'
    context_object_name='room_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class ShelveCreate(CreateView):
    model = SelveNo
    template_name = 'library/shelve_no_create.html'
    form_class = ShelveForm

    def get_context_data(self, *args ,**kwargs):
        context=super(ShelveCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':ShelveForm()}
        return render(request,'library/shelve_no_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=ShelveForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('selve_list')
        return render(request,'library/shelve_no_create.html',{'form':form})
    
class ShelveList(ListView):
    model = SelveNo
    queryset = SelveNo.objects.all()
    template_name='library/selve_list.html'
    context_object_name='selve_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

def load_room_ajax(request):
    library_num_id = request.GET.get('library_num_id')
    queryset = RoomNo.objects.filter(library_num=library_num_id)
    print(queryset)
    context = {
        'queryset':queryset,
    }
    return render(request,'library/includes/room_no_ajax.html',context)

def load_shelve_no_ajax(request):
    library_num_id = request.GET.get('library_num_id')
    room_num_id = request.GET.get('room_num_id')
    queryset = SelveNo.objects.filter(library_num=library_num_id,room_no=room_num_id)
    context = {'queryset':queryset}
    return render(request,'library/includes/shelve_no_ajax.html',context)

class JournalCreate(CreateView):
    model = Journal
    form_class =JournalForm
    template_name = 'library/addjournal.html'

    def get_context_data(self, *args ,**kwargs):
        context=super(JournalCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':JournalForm()}
        return render(request,'library/addjournal.html',context)
    
    def post(self,request,*args,**kwargs):
        form=JournalForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
        return render(request,'library/addjournal.html',{'form':form})
    

class JournalList(ListView):
    model = Journal
    queryset = Journal.objects.all()
    template_name='library/journal_list.html'
    context_object_name='journal_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
    
class JournalDelete(DeleteView):
    model = Journal
    success_url=reverse_lazy('journal_list')

def journalupdateview(request,pk):
    obj = get_object_or_404(Journal, pk=pk)
    if request.method=="POST":
        form = JournalForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('journal_list'))    
    else:
        form = JournalForm()
        form.fields["journal_no"].initial = obj.journal_no
        form.fields["publisher"].initial = obj.publisher
        form.fields["ISSN"].initial = obj.ISSN
        form.fields["E_ISSn"].initial = obj.E_ISSn
        form.fields["location"].initial = obj.location
        form.fields["category"].initial = obj.category
        form.fields["journal_type"].initial = obj.journal_type
        form.fields["source"].initial = obj.source
        form.fields["subject"].initial = obj.subject
        form.fields["journal_format"].initial = obj.journal_format
        form.fields["supplier"].initial = obj.supplier
        form.fields["subject"].initial = obj.subject     
        return render(request,'library/journal_edit.html',{'form':form})

class EbookCreate(CreateView):
    model = E_Book
    form_class =EBookForm
    template_name = 'library/ebook_create.html'

    def get_context_data(self, *args ,**kwargs):
        context=super(EbookCreate,self).get_context_data(**kwargs)        
        return context
    
    def get(self,request,*args,**kwargs):        
        context={'form':EBookForm()}
        return render(request,'library/ebook_create.html',context)
    
    def post(self,request,*args,**kwargs):
        form=EBookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
        return render(request,'library/ebook_create.html',{'form':form})
    

class EbookList(ListView):
    model = E_Book
    queryset = E_Book.objects.all()
    template_name='library/ebook_list.html'
    context_object_name='ebook_list'
    
    def get_context_data(self, *args ,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
    
class EbookDelete(DeleteView):
    model = E_Book
    success_url=reverse_lazy('ebook_list')

def ebookupdateview(request,pk):
    obj = get_object_or_404(E_Book, pk=pk)
    if request.method=="POST":
        form = EBookForm(request.POST or None)
        if form.is_valid():
            form.update(obj)
        return redirect(reverse_lazy('ebook_list'))    
    else:
        form = EBookForm()
        form.fields["name"].initial = obj.name
        form.fields["publisher"].initial = obj.publisher
        form.fields["publication_year"].initial = obj.publication_year
        form.fields["location"].initial = obj.location
        form.fields["category"].initial = obj.category
        form.fields["ISBN"].initial = obj.ISBN
        form.fields["book_author"].initial = obj.book_author
        form.fields["book_sub_author"].initial = obj.book_sub_author
        form.fields["book_sub_author1"].initial = obj.book_sub_author1
        form.fields["ebook_format"].initial = obj.ebook_format
        form.fields["supplier"].initial = obj.supplier
        form.fields["subject"].initial = obj.subject
        form.fields["remark"].initial = obj.remark
        form.fields["remarkq"].initial = obj.remarkq
        form.fields["remark2"].initial = obj.remark2
        form.fields["price"].initial = obj.price
        form.fields["ebook_type"].initial = obj.ebook_type
        return render(request,'library/ebook_edit.html',{'form':form})

