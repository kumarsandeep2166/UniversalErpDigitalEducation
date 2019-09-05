from django.urls import path
from . import views

urlpatterns = [
    path('booktypeformlist/',views.BookTypeFormList.as_view(), name='book_type_list'),
    path('booktypecreate/',views.BookTypeFormCreate.as_view(), name='book_type_create'),
    path('book_type_update/<int:pk>/',views.BookTypeUpdate.as_view(), name='book_type_update'),
    path('book_type_delete/<int:pk>/',views.BookTypeDelete.as_view(), name='book_type_delete'),
    path('book_list/',views.BookList.as_view(), name='book_list'),    
    path('add_product_category/',views.ProductCategoryCreate.as_view(), name='add_product_category'),
    path('product_category_list/',views.ProductCategoryList.as_view(), name='product_category_list'),
    path('product_category_update/<int:pk>/',views.ProductCategoryUpdate.as_view(), name='product_category_update'),       
    path('product_category_delete/<int:pk>/',views.ProductCategoryDelete.as_view(), name='product_category_delete'),
    path('add_vendor/',views.VendorCreate.as_view(), name='add_vendor'),
    path('vendor_list/',views.VendorList.as_view(), name='vendor_list'),
    path('vendor_update/<int:pk>/',views.vendor_update, name='vendor_update'),
    path('vendor_delete/<int:pk>/',views.VendorDelete.as_view(), name='vendor_delete'),
    path('purchase_order_create/',views.PurchaseOrderCreate.as_view(), name='purchase_order_create'),
    path('purchase_order_list/',views.PurchaseOrderList.as_view(), name='purchase_order_list'),
    path('purchaseorder_update/<int:pk>/',views.purchaseorder_update, name='purchaseorder_update'),
    path('purchaseorder_delete/<int:pk>/',views.PurchaseOrderDelete.as_view(), name='purchaseorder_delete'),
    path('location_create/',views.LocationCreate.as_view(), name='location_create'),
    path('location_list/',views.LocationList.as_view(), name='location_list'),
    path('location_update/<int:pk>/',views.LocationUpdate, name='location_update'),
    path('location_delete/<int:pk>/',views.LocationDelete.as_view(), name='location_delete'),
    path('library_create/',views.LibraryCreate.as_view(), name='library_create'),
    path('room_create/',views.RoomCreate.as_view(), name='room_create'),
    path('selve_create/',views.ShelveCreate.as_view(), name='selve_create'),
    path('load_room_ajax/',views.load_room_ajax, name='load_room_ajax'),
    path('library_list/',views.LibraryList.as_view(), name='library_list'), 
    path('room_list/',views.RoomList.as_view(), name='room_list'), 
    path('selve_list/',views.ShelveList.as_view(), name='selve_list'),
    path('load_selve_ajax/',views.load_shelve_no_ajax, name='load_selve_ajax'),
    path('add_book/',views.BookCreate.as_view(), name='add_book'),
    path('delete_book/<int:pk>/',views.BookDelete.as_view(), name='delete_book'),
    path('book_edit/<int:pk>/',views.bookeditview, name='book_edit'),
    path('add_journal/',views.JournalCreate.as_view(), name='add_journal'),
    path('journal_list/',views.JournalList.as_view(), name='journal_list'),
    path('journal_delete/<int:pk>/',views.JournalDelete.as_view(), name='journal_delete'),
    path('journal_edit/<int:pk>/',views.journalupdateview, name='journal_edit'),
    path('ebook_list/',views.EbookList.as_view(), name='ebook_list'),
    path('ebook_create/',views.EbookCreate.as_view(), name='ebook_create'),
    path('ebook_edit/<int:pk>/',views.ebookupdateview, name='ebook_edit'),
    path('ebook_delete/<int:pk>/',views.EbookDelete.as_view(), name='ebook_delete'),
]
