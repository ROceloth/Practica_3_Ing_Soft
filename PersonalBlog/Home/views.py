from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

"""Lo que manda el cliente"""
def index(request):
	#return HttpResponse('Hola mundo')
	template = 'Home/index.html'
	context = {}
	return render(request, template, context)

class About(View):
    #Ahora el about se despliegua con una clase
    template = 'Home/about.html'
    context = {'title': 'About me'}

    def get(self, request):
        """
            Get in About me.
        """
        return render(request, self.template, self.context)