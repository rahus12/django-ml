from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import keras
from keras.preprocessing import image
from django.core.files.storage import FileSystemStorage


# Create your views here.
def predictor(file):
	model = keras.models.load_model('image_app/my_model.h5')
	img = image.load_img('media/images/'+ file)
	img2  = image.img_to_array(img)
	img3  = img2.reshape((1,) + img2.shape)
	predict = model.predict_classes(img3)[0]
	return str(predict)

def Alphabet_img_view(request):

	if request.method == "POST":
		form = AlphabetForm(request.POST,request.FILES)
		#post = request.POST # if using normal forms
		print("\n\n THE print Statement  ")
		print(request.FILES['Alphabet_img'].name) # to get info  from normal forms
		file = request.FILES['Alphabet_img'].name
		print("\n\n")

		if form.is_valid():
			form.save()
			predict = predictor(file)
			print(predict)
			AlphabetForm.number = predict
			AlphabetForm.img = "media/images/"+request.FILES['Alphabet_img'].name
			#return redirect('success',predict)
			#return HttpResponse("The number is: "+predict)
	else:
		form = AlphabetForm()

	return render(request,'image_app/page.html',{'form':form})

def success(request):	
	return HttpResponse('success')



		


