from django.shortcuts import render
from .models import TreeMain, Category

# Create your views here.
def treeHome(request):
    cat = Category.objects.all()
    return render(request, 'tree/home.html',{'object':cat})

def treeDetail(request, pk):
    tree = TreeMain.objects.get(id=pk)
    return render(request, 'tree/tree-detail.html',{'object':tree})