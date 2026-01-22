from django.db import models
class Hero(models.Model):
    image = models.ImageField(upload_to='hero/')

    def __str__(self):
        return "Hero Section"
    
class ServiceSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return "Services Section"


class Stat(models.Model):
    icon = models.ImageField(upload_to='stats/')
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Service(models.Model):
    GRADIENT_CHOICES = [
        ('gradient-pink', 'Pink'),
        ('gradient-blue', 'Blue'),
        ('gradient-orange', 'Orange'),
        ('gradient-green', 'Green'),
    ]

    card_title = models.CharField(max_length=100)
    card_description = models.TextField()
    icon = models.ImageField(upload_to='services/')
    gradient = models.CharField(max_length=50, choices=GRADIENT_CHOICES)

    def __str__(self):
        return self.card_title

class FeatureSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return "Why Choose Section"

class Feature(models.Model):
    BG_CHOICES = [
        ('bg-orange', 'Orange'),
        ('bg-green', 'Green'),
        ('bg-blue', 'Blue'),
        ('bg-pink', 'Pink'),
        ('bg-red', 'Red'),
        ('bg-purple', 'Purple'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='features/')
    bg_class = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title

class TestimonialSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()

    def __str__(self):
        return "Testimonials Section"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    message = models.TextField()
    rating = models.IntegerField(default=5)  # ⭐ rating
    def __str__(self):
        return self.name

class FAQSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(blank=True)

    def __str__(self):
        return "FAQ Section"

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


from django.db import models

class ContactSection(models.Model):
    # Section heading
    title = models.CharField(max_length=100, default="Contact Us")
    subtitle = models.TextField()

    # Phone
    phone = models.CharField(max_length=20)
    phone_note = models.CharField(max_length=100)

    # Email
    email = models.EmailField()
    email_note = models.CharField(max_length=100)

    # Address
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)

    def __str__(self):
        return "Contact Section"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Footer(models.Model):
    # Brand
    brand_name = models.CharField(max_length=100)
    brand_description = models.TextField()

    # Services links
    service_1 = models.CharField(max_length=100)
    service_2 = models.CharField(max_length=100)
    service_3 = models.CharField(max_length=100)
    service_4 = models.CharField(max_length=100)

    # Company links
    company_1 = models.CharField(max_length=100)
    company_2 = models.CharField(max_length=100)
    company_3 = models.CharField(max_length=100)
    company_4 = models.CharField(max_length=100)

    # Connect links
    connect_1 = models.CharField(max_length=100)
    connect_2 = models.CharField(max_length=100)
    connect_3 = models.CharField(max_length=100)
    connect_4 = models.CharField(max_length=100)

    # Bottom text
    copyright_text = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name
    
    