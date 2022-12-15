from django.urls import path,include
from homestoreapp import views


urlpatterns = [
   path("",views.index),
   path("customer_register/",views.customer_register),
   path("customer_login/",views.customer_login),
   path("cu_logout/",views.cu_logout),
   path("tocheckout/",views.tocheckout),
   path("single/",views.singlepage),
   path("addaddress/",views.addaddress),
   path("makepayment/",views.makepayment),
   path("paymetupdate/",views.paymetupdate),
   path("trackorder/",views.trackorder),
   path("cancelorder/",views.cancelorder),
   path('ordersfromcustomers/',views.ordersfromcustomers),
   path('approveorder/',views.approveorder),
   path('oredershiped/',views.oredershiped),
   path('orederdelivered/',views.orederdelivered),
   path('tocart/',views.tocart),
   path('removefromcart/',views.removefromcart),
   path('profile/',views.profile),
   path('returnorder/',views.returnorder),
   path('editprofile/',views.editprofile),
   path('updateprofile/',views.updateprofile),
   path('search/',views.search),
   path('buyall/',views.buyall),
   path('makepaymentforall/',views.makepaymentforall),
   path('paymetupdateall/',views.paymetupdateall),









   #admin
   path("admin/",views.adminlogin),
   path("adminlogin/",views.adminlogin),
   path("admintables/",views.admintable),
   path("delete_owner/",views.deleteowner),
   path("approve_owner/",views.approveowner),
   path("userlist/",views.userlist),
   path("delete_user/",views.deleteuser),
   path("approve_user/",views.approveuser),
   path("allproducts/",views.allproducts),
   path("approvereturn/",views.approvereturn),







   # owner
   path("owner_register/",views.owner_register),
   path("owner_login/",views.owner_login),
   path("contact/",views.contactus),
   path("addproduct/",views.addproduct),
   path("ow_logout/",views.ow_logout),
   path("yourproducts/",views.yourproducts),
   path("deletemyproduct/",views.deletemyproduct)





   ]