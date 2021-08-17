from django.shortcuts import render

# Create your views here.

  
from django.shortcuts import render
from .form import CustomerForm


def index(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'myresume/index.html', context)