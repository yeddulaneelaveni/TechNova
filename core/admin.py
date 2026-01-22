from django.contrib import admin
from .models import *
from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse

# ==================== HERO SECTION ====================
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview')
    
    def image_preview(self, obj):
        if obj.image:
            return f'✅ Image uploaded'
        return '❌ No image'
    image_preview.short_description = 'Image Status'
    
    def has_add_permission(self, request):
        # Only allow one Hero instance
        return not Hero.objects.exists()


# ==================== STATS SECTION ====================
@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('label', 'number', 'icon_preview')
    list_editable = ('number',)
    search_fields = ('label',)
    
    def icon_preview(self, obj):
        if obj.icon:
            return f'✅ Icon uploaded'
        return '❌ No icon'
    icon_preview.short_description = 'Icon Status'


# ==================== SERVICES SECTION ====================
@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle_preview')
    
    def subtitle_preview(self, obj):
        return obj.subtitle[:50] + '...' if len(obj.subtitle) > 50 else obj.subtitle
    subtitle_preview.short_description = 'Subtitle'
    
    def has_add_permission(self, request):
        return not ServiceSection.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('card_title', 'gradient', 'icon_preview', 'description_preview')
    list_filter = ('gradient',)
    search_fields = ('card_title', 'card_description')
    list_editable = ('gradient',)
    
    fieldsets = (
        ('Service Details', {
            'fields': ('card_title', 'card_description')
        }),
        ('Visual Design', {
            'fields': ('icon', 'gradient')
        }),
    )
    
    def icon_preview(self, obj):
        if obj.icon:
            return '✅'
        return '❌'
    icon_preview.short_description = 'Icon'
    
    def description_preview(self, obj):
        return obj.card_description[:40] + '...' if len(obj.card_description) > 40 else obj.card_description
    description_preview.short_description = 'Description'


# ==================== FEATURES SECTION ====================
@admin.register(FeatureSection)
class FeatureSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle_preview')
    
    def subtitle_preview(self, obj):
        return obj.subtitle[:50] + '...' if len(obj.subtitle) > 50 else obj.subtitle
    subtitle_preview.short_description = 'Subtitle'
    
    def has_add_permission(self, request):
        return not FeatureSection.objects.exists()


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'bg_class', 'icon_preview', 'description_preview')
    list_filter = ('bg_class',)
    search_fields = ('title', 'description')
    list_editable = ('bg_class',)
    
    fieldsets = (
        ('Feature Details', {
            'fields': ('title', 'description')
        }),
        ('Visual Design', {
            'fields': ('icon', 'bg_class')
        }),
    )
    
    def icon_preview(self, obj):
        if obj.icon:
            return '✅'
        return '❌'
    icon_preview.short_description = 'Icon'
    
    def description_preview(self, obj):
        return obj.description[:40] + '...' if len(obj.description) > 40 else obj.description
    description_preview.short_description = 'Description'


# ==================== ABOUT SECTION ====================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    
    fieldsets = (
        ('About Content', {
            'fields': ('title', 'paragraph_1', 'paragraph_2')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return '✅ Image uploaded'
        return '❌ No image'
    image_preview.short_description = 'Image Status'
    
    def has_add_permission(self, request):
        return not About.objects.exists()


# ==================== TESTIMONIALS SECTION ====================
@admin.register(TestimonialSection)
class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle_preview')
    
    def subtitle_preview(self, obj):
        return obj.subtitle[:50] + '...' if len(obj.subtitle) > 50 else obj.subtitle
    subtitle_preview.short_description = 'Subtitle'
    
    def has_add_permission(self, request):
        return not TestimonialSection.objects.exists()


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'message_preview')
    list_filter = ('rating',)
    search_fields = ('name', 'role', 'message')
    list_editable = ('rating',)
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'


# ==================== FAQ SECTION ====================
@admin.register(FAQSection)
class FAQSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle_preview')
    
    def subtitle_preview(self, obj):
        return obj.subtitle[:50] + '...' if len(obj.subtitle) > 50 else obj.subtitle
    subtitle_preview.short_description = 'Subtitle'
    
    def has_add_permission(self, request):
        return not FAQSection.objects.exists()


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_preview')
    search_fields = ('question', 'answer')
    
    def answer_preview(self, obj):
        return obj.answer[:60] + '...' if len(obj.answer) > 60 else obj.answer
    answer_preview.short_description = 'Answer'


# ==================== CONTACT SECTION ====================
@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')
    
    fieldsets = (
        ('Section Heading', {
            'fields': ('title', 'subtitle')
        }),
        ('Phone Information', {
            'fields': ('phone', 'phone_note')
        }),
        ('Email Information', {
            'fields': ('email', 'email_note')
        }),
        ('Address', {
            'fields': ('address_line1', 'address_line2')
        }),
    )
    
    def has_add_permission(self, request):
        return not ContactSection.objects.exists()


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'message_preview')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'created_at')
        }),
        ('Message', {
            'fields': ('message',)
        }),
    )
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'
    
    def has_add_permission(self, request):
        return False  # Users submit these, not admin


# ==================== FOOTER SECTION ====================
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'copyright_text')
    
    fieldsets = (
        ('Brand Information', {
            'fields': ('brand_name', 'brand_description'),
            'description': 'Your company brand and description'
        }),
        ('Services Links', {
            'fields': ('service_1', 'service_2', 'service_3', 'service_4'),
            'description': 'Links related to services'
        }),
        ('Company Links', {
            'fields': ('company_1', 'company_2', 'company_3', 'company_4'),
            'description': 'Links related to company information'
        }),
        ('Connect Links', {
            'fields': ('connect_1', 'connect_2', 'connect_3', 'connect_4'),
            'description': 'Social media and contact links'
        }),
        ('Copyright', {
            'fields': ('copyright_text',),
            'description': 'Footer copyright text'
        }),
    )
    
    def has_add_permission(self, request):
        return not Footer.objects.exists()

