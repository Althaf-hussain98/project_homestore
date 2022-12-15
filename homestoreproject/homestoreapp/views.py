from django.shortcuts import render
from homestoreapp.models import*
from django.contrib.auth.models import User

import hashlib
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
	data=products.objects.all()
	return render(request,'index.html',{'datakey':data})


def customer_login(request):
	if request.method=='POST':
		username=request.POST['username']
		Password=request.POST['Password']
		hashpass=hashlib.md5(Password.encode('utf8')).hexdigest()
		check=customer.objects.all().filter(username=username,password=hashpass)
		if check:
			for x in check:
				request.session["uid"]=x.id
				request.session["username"]=x.username
				return render(request,"index.html",{"succes":"Loged in "})
		else:
			return render(request,"index.html",{"error":"Login Error"})
	else:
		return render(request,"index.html")




def customer_register(request):
	if request.method == 'POST':
		cname=request.POST['username']
		cemail=request.POST['email']
		password = request.POST['Password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=customer.objects.filter(email=cemail)
		if check:
			return render(request,"index.html",{"error":"Email or username alredy in use"})
		else:
			add = customer(username=cname,email=cemail,password=hashpass)
			add.save()
			# imgsave= imgModel(upload=img)
			# imgsave.save
			return render(request,"index.html",{"succes":"Rigistered"})
	else:
		return render(request,"index.html",{"error":"Login Error"})



def cu_logout(request):
	if request.session.has_key('uid'):
		del request.session["uid"]
	return render(request,'index.html')


def adminlogin(request):
	if request.method=="POST":
	    Password=request.POST['password']
	    Email=request.POST['email']
	    check=User.objects.filter(email=Email,password=Password)
	    if check:
	    	for x in check:
	    		request.session["adminuid"]=x.id
	    		request.session["adminemail"]=x.email
	    	return render(request,"admin/index.html",{"succes":"Rigistered"})
	    else:
	    	return render(request,"admin/login.html",{"error":"Login Error"})
	else:
		return render(request,"admin/login.html")






def owner_register(request):
	if request.method == 'POST':
		cname=request.POST['username']
		cemail=request.POST['email']
		password = request.POST['Password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=owner.objects.filter(email=cemail)
		if check:
			return render(request,"index.html",{"error":"Email or username alredy in use"})
		else:
			add = owner(username=cname,email=cemail,password=hashpass)
			add.save()
			# imgsave= imgModel(upload=img)
			# imgsave.save
			return render(request,"index.html",{"succes":"Rigistered"})
	else:
		return render(request,"index.html",{"error":"Login Error"})




def owner_login(request):
	if request.method=='POST':
		username=request.POST['username']
		Password=request.POST['Password']
		hashpass=hashlib.md5(Password.encode('utf8')).hexdigest()
		check=owner.objects.all().filter(username=username,password=hashpass,status=1)
		if check:
			for x in check:
				request.session["oid"]=x.id
				request.session["oname"]=x.username
				return render(request,"index.html",{"succes":"loged in"})
			else:
				return render(request,"index.html",{"error"})
	else:
		return render(request,"index.html")




def ow_logout(request):
	if request.session.has_key('oid'):
		del request.session["oid"]
	return render(request,'index.html')



def admintable(request):
	data=owner.objects.all()
	return render (request,"admin/tables.html",{'datakey':data})

def deleteowner(request):
	empid=request.GET['eid']
	query=owner.objects.all().filter(id=empid).delete()
	return HttpResponseRedirect('/admintables/')

def approveowner(request):
	empid=request.GET['eid']
	query=owner.objects.all().filter(id=empid).update(status=1)
	return HttpResponseRedirect('/admint/')

def contactus(request):
	return render(request,'contact.html')



def addproduct(request):
	if request.session.has_key('oid'):
		if request.method=='POST':
		# return render(request,"turfupload.html")
			productname=request.POST['productname']
			description=request.POST['description']
			category=request.POST['category']			
			img=request.FILES['pro']
			price=request.POST['price']

			ouid=request.session["oid"]
			tid=owner.objects.get(id=ouid)

			add = products(productname=productname,description=description,category=category,price=price,upload=img,owner_id=tid)
			add.save()
			# imgsave= turf()
			# imgsave.save
			return render(request,"addproduct.html",{"succes":"uploaded"})
		else:
			return render(request,"addproduct.html",{"error":" Error"})
	else:
		return render(request,"addproduct.html")






def userlist(request):
	data=customer.objects.all()
	return render (request,"admin/userlist.html",{'datakey':data})


def approveuser(request):
	empid=request.GET['eid']
	query=customer.objects.all().filter(id=empid).update(status=1)
	return HttpResponseRedirect('/userlist/')



def deleteuser(request):
	empid=request.GET['eid']
	query=customer.objects.all().filter(id=empid).delete()
	return HttpResponseRedirect('/userlist/')


def allproducts(request):
	data=products.objects.all()
	return render (request,"admin/allproducts.html",{'datakey':data})


def yourproducts(request):
    ouid=request.session["oid"]
    data=products.objects.filter(owner_id=ouid)
    return render(request,"yourproducts.html",{'datakey':data})


def singlepage(request):
	pid=request.GET['pid']
	data=products.objects.all().filter(id=pid)
	return render (request,"single.html",{'datakey':data})




# def tocheckout(request):
  
# 	productid=request.GET['productid']
# 	pid=products.objects.get(id=productid)
# 	data=products.objects.all().filter(id=productid)
# 	for x in data:
# 		ower=x.owner_id.id
# 		own=owner.objects.get(id=ower)
# 	userid=request.session["uid"]

# 	uidx=customer.objects.get(id=userid)

# 	book=buying(userid=uidx,ownerid=own,purchasingitem=pid)
# 	book.save()

# 	cartdet= buying.objects.all().filter(userid=userid)

# 	return render (request,"checkout.html",{'datakey':cartdet})
		



def addaddress(request):
	did=request.GET['details']
	data=buying.objects.filter(id=did)
	return render (request,"addaddress.html",{"data":data})




def makepayment(request):
	if request.method=='POST':
		name=request.POST['name']
		deliver_address=request.POST['address']
		did=request.GET['details']
		data=buying.objects.all().filter(id=did).update(name=name,deliver_address=deliver_address,status='confirmed')
		dataset=buying.objects.all().filter(id=did)
		return render (request,"payment/index.html",{'dataset':dataset})
	else:
		return render (request,"payment/index.html")





def paymetupdate(request):
	bid=request.GET['details']
	data=buying.objects.filter(id=bid).update(paymwnt='paid')
	return render(request,'index.html')





def trackorder(request):
	data=buying.objects.all()
	return render (request,"trackorder.html",{'datakey':data})

def cancelorder(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).delete()
	return HttpResponseRedirect('/trackorder/')

def returnorder(request):
	bid=request.GET['eid']
	data=buying.objects.filter(id=bid).update(status='return requsted')
	return HttpResponseRedirect('/trackorder/')


def ordersfromcustomers(request):
	if request.session.has_key('oid'):
	 goid=request.session['oid']
	 data=buying.objects.all().filter(ownerid=goid)
	 return render (request,"ordersfromcustomers.html",{'datakey':data})



def approveorder(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).update(status='Dispatched')
	return HttpResponseRedirect('/ordersfromcustomers/')


def oredershiped(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).update(status='Shipped')
	return HttpResponseRedirect('/ordersfromcustomers/')



def orederdelivered(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).update(status='Delivered')
	return HttpResponseRedirect('/ordersfromcustomers/')

def approvereturn(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).update(status='Return Approved')
	return HttpResponseRedirect('/ordersfromcustomers/')



def deletemyproduct(request):
	empid=request.GET['eid']
	query=products.objects.all().filter(id=empid).delete()
	return HttpResponseRedirect('/yourproducts/')



def tocheckout(request):
	if request.session.has_key('uid'):
		productid=request.GET['productid']
		pid=products.objects.get(id=productid)
		data=products.objects.all().filter(id=productid)
		for x in data:
			ower=x.owner_id.id
			own=owner.objects.get(id=ower)
		userid=request.session["uid"]
		uidx=customer.objects.get(id=userid)
		book=buying(userid=uidx,ownerid=own,purchasingitem=pid)
		book.save()
		cartdet= buying.objects.all().filter(userid=userid,status="awaiting")
		return  HttpResponseRedirect('/')
	else:
		return render(request,"index.html")



def tocart(request):
	if request.session.has_key('uid'):
		userid=request.session["uid"]
		uidx=customer.objects.get(id=userid)
		cartdet= buying.objects.all().filter(userid=userid,status="awaiting")
		return render (request,"checkout.html",{'datakey':cartdet})
	else:
		return render(request,"index.html")


def removefromcart(request):
	empid=request.GET['eid']
	query=buying.objects.all().filter(id=empid).delete()
	return HttpResponseRedirect('/tocart/')


def profile(request):
	if request.session.has_key('uid'):
		pid=request.session['uid']
		data=customer.objects.all().filter(id=pid)
		return render(request,"profile.html",{'datakey':data})
	else:
		return render(request,"index.html")


def editprofile(request):
	if request.session.has_key('uid'):
		edit=request.session['uid']
		data=customer.objects.all().filter(id=edit)
		return render(request,"editprofile.html",{'datakey':data})
	else:
		return render(request,"profile.html")




def updateprofile(request):
	if request.method=='POST':
		username=request.POST['name']
		email=request.POST['Email']
		phone=request.POST['phone']
		edit=request.session['uid']
		data=customer.objects.all().filter(id=edit).update(username=username,email=email,phone=phone)
		return HttpResponseRedirect('/profile/')
	else:
		return render(request,"editprofile.html")






def search(request):
    if request.GET.get('myform'): # write your form name here      
        search_name =  request.GET.get('myform')      
        try:
            status = products.objects.filter(productname__icontains=search_name)
            return render(request,"searchresult.html",{"books":status})
        except:
            return render(request,"searchresult.html",{'books':status})
    else:
        return render(request, 'searchresult.html')

	




def buyall(request):
	if request.session.has_key('uid'):
		userid=request.session["uid"]
		uidx=customer.objects.get(id=userid)
		cartdet= buying.objects.all().filter(userid=userid,status="awaiting")
		return render (request,"addaddress.html",{'datakey':cartdet})
	else:
		return render(request,"index.html")




def makepaymentforall(request):
	if request.session.has_key('uid'):
		userid=request.session['uid']
		uidx=customer.objects.get(id=userid)
		name=request.POST['name']
		deliver_address=request.POST['address']
		cartdet= buying.objects.all().filter(userid=userid,status=0).update(name=name,deliver_address=deliver_address,status='confirmed')
		dataset=customer.objects.filter(id=userid)

		return render (request,"payment/index.html",{'datakey':dataset})
	else:
		return render(request,"index.html")


def paymetupdateall(request):
	data=buying.objects.all().filter(paymwnt="Pending").update(paymwnt='paid',status='confirmed')
	return render(request,'index.html')















	# 	userid=request.POST["uid"]
	# 	uidx=buying.objects.get(id=userid)
	# 	address=request.POST['address']
	# 	name=request.POST['name']
	# 	# ownerid=request.POST['owner_id']
	# 	# owneridx=products.objects.get(id=ownerid)
	

	# 	book=buying(userid=uidx,ownerid=owner,purchasingitem=owneridx,deliver_address=address,name=name)
	# 	book.save()
	# 	dataset=buying.objects.all()
	# 	for x in dataset:
	# 		tid=x.id
	# 	return render (request,"payment/index.html",{'tid':tid})
	# else:
	# 	data=products.objects.all()
	# 	return HttpResponseRedirect('/')



# if request.method=='POST':
# 		userid=request.session["uid"]
# 		uidx=customer.objects.get(id=userid)
# 		ownerid=request.POST['owid']
# 		owneridx=owner.objects.get(id='ownerid')



