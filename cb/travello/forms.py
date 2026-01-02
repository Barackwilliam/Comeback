# myapp/forms.py
from django import forms
from .models import MountMeruSlide,CampingSafaris,HoneymoonSafaris,Serengeti_migration,Explore_zanzibar,Kilimanjaro_climbing_image,company,Service,Team,Step_for_booking,Travel,Trip_DB,User_Testimonial,Travels_Destination,Gallery,About_This_Organization,Tour,Welcome_text

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class companyAdminForm(forms.ModelForm):
    class Meta:
         model = company 
         fields = '__all__' 
         
    class Media: js = [ 'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js', ]


class Welcome_textAdminForm(forms.ModelForm):
    class Meta:
        model = Welcome_text
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]
        

class Kilimanjaro_climbing_imageAdminForm(forms.ModelForm):
    class Meta:
        model = Kilimanjaro_climbing_image
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

class MountMeruSlideAdminForm(forms.ModelForm):
    class Meta:
        model = MountMeruSlide
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class Step_for_bookingAdminForm(forms.ModelForm):
    class Meta:
        model = Step_for_booking
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class User_TestimonialForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]




class DestinationForm(forms.ModelForm):
    class Meta:
        model = Travels_Destination
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class About_This_OrganizationForm(forms.ModelForm):
    class Meta:
        model = Travels_Destination
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]


class Trip_DBForm(forms.ModelForm):
    class Meta:
        model = Trip_DB
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]
        
class Explore_zanzibarForm(forms.ModelForm):
    class Meta:
        model = Explore_zanzibar
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

        
class Serengeti_migrationForm(forms.ModelForm):
    class Meta:
        model = Serengeti_migration
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

       
class HoneymoonSafarisForm(forms.ModelForm):
    class Meta:
        model = HoneymoonSafaris
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]



class CampingSafarisForm(forms.ModelForm):
    class Meta:
        model = CampingSafaris
        fields = '__all__'

    class Media:
        js = [
            'https://ucarecdn.com/libs/widget/3.x/uploadcare.full.min.js',
        ]

from django import forms
from .models import Booking, TOUR_CHOICES

class BookingForm(forms.ModelForm):
    interested_in = forms.MultipleChoiceField(
        choices=TOUR_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=False,
        label="Interested In"
    )

    class Meta:
        model = Booking
        fields = [
            "first_name", "last_name", "email", "phone_number", "country",
            "arrival_date", "departure_date", "adults", "children",
            "interested_in", "message"
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Last Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Email Address"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Phone Number"
            }),
            "country": forms.Select(attrs={
                "class": "form-select form-select-lg"
            }),
            "arrival_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control form-control-lg"
            }),
            "departure_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control form-control-lg"
            }),
            "adults": forms.NumberInput(attrs={
                "class": "form-control form-control-lg",
                "min": "1",
                "placeholder": "Number of Adults"
            }),
            "children": forms.NumberInput(attrs={
                "class": "form-control form-control-lg",
                "min": "0",
                "placeholder": "Number of Children (Optional)"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control form-control-lg",
                "rows": 4,
                "placeholder": "Tell us about your dream trip, special requests, or any questions..."
            }),
        }

    def clean_interested_in(self):
        data = self.cleaned_data.get("interested_in", [])
        return ", ".join(data)
