from django.shortcuts import redirect, render
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()

    # messages.info(request, 'Um texto que seja')
    # messages.warning(request, 'Um texto que seja')
    # messages.error(request, 'Um texto que seja')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')


    return render (
        request,
        'contact/register.html',
        {
            'form': form,
        }
    )