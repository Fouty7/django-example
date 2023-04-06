from django.http import HttpResponse

def home(request):
   text = """<h1>Django Example Elastic Beanstalk</h1>"""
   return HttpResponse(text)