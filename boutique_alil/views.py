from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail





def contact_page(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            title = f"Message from {name} ({email})"
            send_mail(
                title,
                message,
                "studentinstitute2024@gmail.com",
                ["studentinstitute2024@gmail.com"],
                fail_silently=False,
            )
            messages.success(
                request, "Your message has been sent successfully!")
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})