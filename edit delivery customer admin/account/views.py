from django.shortcuts import render
from .forms import CustomUserEditForm
from .models import CustomUser
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    my_dict={'insert_me':""}
    return render(request,'upd.html',context=my_dict)


def my_view(request, pk):
    instance = CustomUser.objects.get(pk=pk)
    form = CustomUserEditForm(request.POST or None, instance=instance)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'my_template.html', {'form': form})