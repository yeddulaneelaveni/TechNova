from django.shortcuts import render, redirect 
from django.contrib import messages
from .models import *

def home(request):
    # Handle contact form submission
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        messages.success(request, "✅ Your message has been sent successfully!")
        return redirect('/')   # prevents duplicate submit

    # Page data
    context = {
        'hero': Hero.objects.first(),
        'stats': Stat.objects.all(),
        'service_section': ServiceSection.objects.first(),
        'services': Service.objects.all(),
        'features': Feature.objects.all(),
        'about': About.objects.first(),
        'testimonials': Testimonial.objects.all(),
        'testimonial_section': TestimonialSection.objects.first(),
        'faq_section': FAQSection.objects.first(),
        'faqs': FAQ.objects.all(),
        'feature_section': FeatureSection.objects.first(),
        'footer': Footer.objects.first(),
        'contact': ContactSection.objects.first(),
        
    }

    return render(request, 'core/home.html', context)
