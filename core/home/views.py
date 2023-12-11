from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("""<h1>Hey I am a Django Server.</h1>
                        <p>Hey this is coming from Django server</p>
                        <hr>
                        <h3 style="color:red">Hope you are loving me</h3>
                        """)
def htmlpage(request):
    return render(request,"home/index.html")

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")
