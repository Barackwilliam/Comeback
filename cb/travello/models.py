from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# from cloudinary.models import CloudinaryField


# Create your models here.


class TravelPackageItem(models.Model):
    INCLUDE = 'include'
    EXCLUDE = 'exclude'
    ITEM_TYPE_CHOICES = [
        (INCLUDE, 'Included'),
        (EXCLUDE, 'Excluded'),
    ]

    # Generic relation to any parent (Tour, Travel, Trip_DB, Destination...)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = "Include and Execlude"
        verbose_name_plural = "Include and Execludetions"

        ordering = ['order']
        indexes = [
            models.Index(fields=['content_type', 'object_id', 'item_type']),
        ]

    def __str__(self):
        return f"{self.get_item_type_display()}: {self.title}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)  # Hifadhi Uploadcare UUID au URL

    def __str__(self):
        return self.title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"
        return ''

    # Kwa matumizi ya kawaida kwenye site (speed optimized)
    def get_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
        return ''


class Team(models.Model):
    Full_name = models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)  # Uploadcare image URL
    designation = models.TextField()
    facebook_link = models.URLField(max_length=300, blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True, null=True)
    instagram_link = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.Full_name

    # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
   


class Step_for_booking(models.Model):
    Title =  models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)
    # image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()

    
    class Meta:
        verbose_name = "Step to Book"
        verbose_name_plural = "Steps to book"
        ordering = ['Title']

    def __str__(self):
        return self. Title

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        # Optionally, we can add Uploadcare transformations here if needed
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
   



class Travel(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    days = models.IntegerField(validators=[MinValueValidator(1)])
    route = models.CharField(max_length=100, blank=True, null=True)
    overview = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    safari_type = models.CharField(max_length=100, default='Safari')
    package_items = GenericRelation(TravelPackageItem, related_query_name='travel')


    class Meta:
        verbose_name = "Safari"
        verbose_name_plural = "Safaris"
        ordering = ['title']


    def __str__(self):
        return self.title

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/format/jpg/-/quality/smart/"

    @property
    def includes(self):
        return self.package_items.filter(item_type=TravelPackageItem.INCLUDE)

    @property
    def excludes(self):
        return self.package_items.filter(item_type=TravelPackageItem.EXCLUDE)
   





class Travel_Itiner(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, related_name='itiner')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    elevation_start = models.CharField(max_length=50, blank=True, null=True)
    elevation_end = models.CharField(max_length=50, blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)
    hiking_time = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()



    class Meta:
        verbose_name = "Safari Itinenary"
        verbose_name_plural = "Safari Itinenary"
        ordering = ['title']
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"

   

class User_Testimonial(models.Model):
    Full_name =  models.CharField(max_length=100)
    # image = CloudinaryField('image', blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    country =  models.CharField(max_length=100)

    def __str__(self):
        return self. Full_name

    # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"



class Gallery(models.Model):
    Title =  models.CharField(max_length=100)
    image = models.CharField(max_length=255, blank=True, null=True)
    # image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self. Title

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
   



class About_This_Organization(models.Model):
    title = models.CharField(max_length=200, default="Welcome to  Kilihappy Tanzania Advantures")
    content = models.TextField(default="Kilihappy Tanzania Adventures was founded in 2025 by a group of passionate Tanzanians who were eager to share the richness of our country with the world. From a small team of nature lovers and adventurers, we have grown into a trusted partner for tourists looking for authentic and unforgettable experiences in Tanzania.")
    mission = models.TextField(blank=True, default="To provide unique and high-quality tourism experiences, both locally and internationally, in a safe, sustainable, and environmentally friendly manner while prioritizing customer service and community development.")
    vision = models.TextField(blank=True, default="To become the leading tourism company in East Africa, recognized globally for excellence, innovation, and social responsibility.")
    image = models.CharField(max_length=255, blank=True, null=True)
    # image = CloudinaryField('image', blank=True, null=True)



    class Meta:
        verbose_name = "About Organisation"
        verbose_name_plural = "About Organisation"
        ordering = ['title']

    def __str__(self):
        return self.title

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
   


from django.db import models

from django.db import models

class Contact_Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.subject}"

from django.db import models

class Tour(models.Model):
    TOUR_TYPES = [
        ('Beach', 'Beach'),
        ('Hiking', 'Hiking'),
        ('Safari', 'Safari'),
        ('Cultural', 'Cultural'),
        ('Kilimanjaro', 'Kilimanjaro'),
    ]

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    days = models.IntegerField(validators=[MinValueValidator(1)])
    route = models.CharField(max_length=100, blank=True, null=True)
    overview = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    # featured_image = CloudinaryField('image', blank=True, null=True)
    tour_type = models.CharField(max_length=100, choices=TOUR_TYPES, default='Safari')
    package_items = GenericRelation(TravelPackageItem, related_query_name='tour')

    class Meta:
        verbose_name = "Trekking"
        verbose_name_plural = "Trekkings"
        ordering = ['title']



    def __str__(self):
        return self.title

    @property
    def includes(self):
        return self.package_items.filter(item_type=TravelPackageItem.INCLUDE)

    @property
    def excludes(self):
        return self.package_items.filter(item_type=TravelPackageItem.EXCLUDE)

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/format/jpg/-/quality/smart/"
   


class Tour_Itinerary(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='itinerary')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    elevation_start = models.CharField(max_length=50, blank=True, null=True)
    elevation_end = models.CharField(max_length=50, blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)
    hiking_time = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"


    class Meta:
        verbose_name = "Trekking Itinerary"
        verbose_name_plural = "Trekking Itinenary"
        ordering = ['title']




class Trip_DB(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    days = models.IntegerField(validators=[MinValueValidator(1)])
    route = models.CharField(max_length=100, blank=True, null=True)
    overview = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    # featured_image = CloudinaryField('image', blank=True, null=True)
    trip_type = models.CharField(max_length=100, default='Safari')
    package_items = GenericRelation(TravelPackageItem, related_query_name='trip')


    class Meta:
        verbose_name = "Day Trip"
        verbose_name_plural = "Day Trips"
        ordering = ['title']


    def __str__(self):
        return self.title

     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.featured_image}/-/format/jpg/-/quality/smart/"

    
    @property
    def includes(self):
        return self.package_items.filter(item_type=TravelPackageItem.INCLUDE)

    @property
    def excludes(self):
        return self.package_items.filter(item_type=TravelPackageItem.EXCLUDE)
   


class Trip_Itinerary_DB(models.Model):
    trip = models.ForeignKey(Trip_DB, on_delete=models.CASCADE, related_name='itinerary')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    elevation_start = models.CharField(max_length=50, blank=True, null=True)
    elevation_end = models.CharField(max_length=50, blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)
    hiking_time = models.CharField(max_length=50, blank=True, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"


    class Meta:
        verbose_name = "Day Trip Itinerary"
        verbose_name_plural = "Day Trip Itenerary"
        ordering = ['title']






class Travels_Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    Offer_in_percent =  models.IntegerField(blank=True,null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    # image = CloudinaryField('image', blank=True, null=True)
    location = models.CharField(max_length=255)  # e.g. "Northern Tanzania"
    description = models.TextField()  # Full description or overview
    slug = models.SlugField(max_length=255, blank=True, null=True)
    is_unesco_site = models.BooleanField(default=False)
    package_items = GenericRelation(TravelPackageItem, related_query_name='destination')

    
    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        ordering = ['name']

    def __str__(self):
        return self.name  # badili kuwa jina; ni maana zaidi kuliko location


     # Kwa Open Graph preview
    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    # Kwa frontend display optimized
    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"

    @property
    def includes(self):
        return self.package_items.filter(item_type=TravelPackageItem.INCLUDE)

    @property
    def excludes(self):
        return self.package_items.filter(item_type=TravelPackageItem.EXCLUDE)
   





class company(models.Model):
    company_name = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)  

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "company"
        ordering = ['company_name']

    def __str__(self):
        return self.company_name

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"
        return ''
    # Kwa matumizi ya kawaida kwenye site (speed optimized)
    def get_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"
        return ''






class Welcome_text(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image_1 = models.CharField(max_length=255, blank=True, null=True)  
    image_2 = models.CharField(max_length=255, blank=True, null=True)  
    image_3 = models.CharField(max_length=255, blank=True, null=True)  
    image_4 = models.CharField(max_length=255, blank=True, null=True)  
    image_5 = models.CharField(max_length=255, blank=True, null=True)  
    image_6 = models.CharField(max_length=255, blank=True, null=True)  


    def __str__(self):
        return self.title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image_1:
            return f"https://ucarecdn.com/{self.image_1}/-/resize/1200x630/-/format/auto/"
        return ''

    # Kwa matumizi ya kawaida kwenye site (speed optimized)
    def get_image_url(self):
        if self.image_1:
            return f"https://ucarecdn.com/{self.image_1}/-/format/jpg/-/quality/smart/"
        return ''




class MountMeruSlide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Five images for the slider
    image1 = models.CharField(max_length=255, blank=True, null=True) 
    image2 = models.CharField(max_length=255, blank=True, null=True) 
    image3 = models.CharField(max_length=255, blank=True, null=True) 
    image4 = models.CharField(max_length=255, blank=True, null=True) 
    image5 = models.CharField(max_length=255, blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Mount Meru Slide"
        verbose_name_plural = "Mount Meru Slides"
        ordering = ['title']






class Kilimanjaro_climbing_image(models.Model):
    title_1 = models.CharField(max_length=100)
    image_1 = models.CharField(max_length=255, blank=True, null=True) 

    title_2 = models.CharField(max_length=100)
    image_2 = models.CharField(max_length=255, blank=True, null=True) 

    title_3 = models.CharField(max_length=100)
    image_3 = models.CharField(max_length=255, blank=True, null=True)

    title_4 = models.CharField(max_length=100)
    image_4 = models.CharField(max_length=255, blank=True, null=True) 

    title_5 = models.CharField(max_length=100)
    image_5 = models.CharField(max_length=255, blank=True, null=True) 

    title_6 = models.CharField(max_length=100)
    image_6 = models.CharField(max_length=255, blank=True, null=True)

    title_7 = models.CharField(max_length=100)
    image_7 = models.CharField(max_length=255, blank=True, null=True)  

    title_8 = models.CharField(max_length=100)
    image_8 = models.CharField(max_length=255, blank=True, null=True)  


    def __str__(self):
        return self.title_1

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image_1:
            return f"https://ucarecdn.com/{self.image_1}/-/resize/1200x630/-/format/auto/"
        return ''

    # Kwa matumizi ya kawaida kwenye site (speed optimized)
    def get_image_url(self):
        if self.image_1:
            return f"https://ucarecdn.com/{self.image_1}/-/format/jpg/-/quality/smart/"
        return ''



class Explore_zanzibar(models.Model):
    Tour_title = models.CharField(max_length=500)    
    Tour_Descriptions = models.TextField()
    Tour_price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        verbose_name = "Explore zanzibar"
        verbose_name_plural = "Explore zanzibar"
        ordering = ['Tour_title']

    
    def __str__(self):
        return self.Tour_title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/" 




class zanzibar_Itiner(models.Model):
    zanzibar_tour = models.ForeignKey(Explore_zanzibar, on_delete=models.CASCADE, related_name='itiner')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()



    class Meta:
        verbose_name = "Zanzibar Itinenary"
        verbose_name_plural = "Zanzibar Itinenary"
        ordering = ['title']
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"







class Serengeti_migration(models.Model):
    Tour_title = models.CharField(max_length=500)    
    Tour_Descriptions = models.TextField()
    Tour_price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        verbose_name = "Serengeti Migration"
        verbose_name_plural = "Serengeti Migrations"
        ordering = ['Tour_title']

    
    def __str__(self):
        return self.Tour_title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/" 




class Serengeti_Itiner(models.Model):
    serengeti_tour = models.ForeignKey(Serengeti_migration, on_delete=models.CASCADE, related_name='itiner')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()



    class Meta:
        verbose_name = "Serengeti Itinenary"
        verbose_name_plural = "Serengeti Itinenary"
        ordering = ['title']
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"









class HoneymoonSafaris(models.Model):
    Tour_title = models.CharField(max_length=500)    
    Tour_Descriptions = models.TextField()
    Tour_price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        verbose_name = "SHoneymoon Safaris"
        verbose_name_plural = "Honeymoon Safaris"
        ordering = ['Tour_title']

    
    def __str__(self):
        return self.Tour_title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/" 




class Honeymoon_Itiner(models.Model):
    Honeymoon_tour = models.ForeignKey(HoneymoonSafaris, on_delete=models.CASCADE, related_name='itiner')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()



    class Meta:
        verbose_name = "Honeymoon Itinenary"
        verbose_name_plural = "Honeymoon Itinenary"
        ordering = ['title']
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"




class CampingSafaris(models.Model):
    Tour_title = models.CharField(max_length=500)    
    Tour_Descriptions = models.TextField()
    Tour_price = models.IntegerField(null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    
    class Meta:
        verbose_name = "Tanzania Camping Safaris"
        verbose_name_plural = "Tanzania Camping Safaris"
        ordering = ['Tour_title']

    
    def __str__(self):
        return self.Tour_title

    # Kwa Open Graph preview (Facebook, WhatsApp etc.)
    def get_og_image_url(self):
        if self.image:
            return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/" 




class Camping_Itiner(models.Model):
    Camping_tour = models.ForeignKey(CampingSafaris, on_delete=models.CASCADE, related_name='itiner')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()



    class Meta:
        verbose_name = "Camping Itinenary"
        verbose_name_plural = "Camping Itinenary"
        ordering = ['title']
    
    def __str__(self):
        return f"Day {self.day_number} - {self.title}"

from django.db import models

class FAQ(models.Model):
    question = models.CharField("Swali", max_length=255)
    answer = models.TextField("Jibu")

    class Meta:
        verbose_name = "Swali na Jibu"
        verbose_name_plural = "Maswali na Majibu"

    def __str__(self):
        return self.question



from django.db import models
from django_countries.fields import CountryField

TOUR_CHOICES = [
    ("wildlife", "Wildlife"),
    ("trekking", "Trekking"),
    ("beach", "Beach"),
    ("cultural", "Cultural"),
]

class Booking(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    email = models.EmailField("Email Address")
    phone_number = models.CharField("Phone Number", max_length=15)
    country = CountryField(blank_label="Select Country")
    arrival_date = models.DateField("Arrival Date")
    departure_date = models.DateField("Departure Date")
    adults = models.PositiveIntegerField("Number of Adults")
    children = models.PositiveIntegerField("Number of Children", blank=True)
    interested_in = models.CharField("Interested In", max_length=255, blank=True)  # comma-separated values
    message = models.TextField("Message", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



from django.db import models


class UserVisit(models.Model):
    ip_address = models.GenericIPAddressField()
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    visit_count = models.PositiveIntegerField(default=1)
    user_agent = models.TextField(blank=True, null=True)
    referrer = models.URLField(blank=True, null=True)
    page_visited = models.URLField()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "User Visit"
        verbose_name_plural = "User Visits"

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"


class UserActivity(models.Model):
    visit = models.ForeignKey(UserVisit, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    activity_details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.visit.ip_address} - {self.activity_type}"




class Headline(models.Model):
    name_of_headline = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.name_of_headline


from django.utils import timezone
from ckeditor.fields import RichTextField  # Import this

class TermsAndConditions(models.Model):
    """
    Updated model with RichTextField for formatted content.
    """
    title = models.CharField(max_length=200, default="Terms and Conditions")
    content = RichTextField()  # Use RichTextField instead of TextField for rich editing
    last_updated = models.DateTimeField(default=timezone.now)
    version = models.CharField(max_length=10, default="1.0")

    def __str__(self):
        return f"{self.title} - Version {self.version}"