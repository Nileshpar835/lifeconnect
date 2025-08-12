from django.shortcuts import render,redirect,get_object_or_404
from .models import HelpRequest
from .forms import HelpRequestForm

# Create your views here.
def help_list(request):
    helps = HelpRequest.objects.all()  # Changed from help to helps to match template
    return render(request, 'askhelp/help_list.html', {'helps': helps})

def help_create(request):
    if request.method == 'POST':
        form = HelpRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('help_list')
    else:
        form = HelpRequestForm()
    return render(request, 'askhelp/help_form.html', {'form': form})

def help_update(request,pk):
    help_item=get_object_or_404(HelpRequest,pk=pk)
    if request.method=='POST':
        form=HelpRequestForm(request.POST,instance=help_item)
        if form.is_valid():
            form.save()
            return redirect('help_list')
    else:
        form =HelpRequestForm(instance=help_item)
    return render(request,'askhelp/help_form.html',{'form':form})
    
def help_delete(request,pk):
    help_item=get_object_or_404(HelpRequest,pk=pk)
    if request.method=='POST':
        help_item.delete()
        return redirect('help_list')
    return render(request,'askhelp/help_confirm_delete.html',{'help_item':help_item})