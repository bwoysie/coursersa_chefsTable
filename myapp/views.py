from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
  content =" <html><body><h1> Yow Batty Bwoy!! ..Welcome to Jamaica </h1></body></html>"
  return HttpResponse(content)

def demoapp(request):
  content1 =" <html><body><h1> Yow Batty Bwoy!! ..I like america </h1></body></html>"
  return HttpResponse(content1)
