from django.http import HttpResponse
from django.views.generic import TemplateView

def hellofunc(request):#requestはwebサーバー⇒アプリケーションサーバ(wsgi)⇒から送られてきたリクエストのこと
    return HttpResponse("hello")

class Helloclass(TemplateView):
    template_name="hello.html"