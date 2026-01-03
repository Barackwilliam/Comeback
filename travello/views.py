from django.shortcuts import render,redirect
from django.db.models import Prefetch
from .models import UserVisit, UserActivity
from django.views import View
import json


from .models import  MountMeruSlide,Headline,FAQ,CampingSafaris,HoneymoonSafaris,Serengeti_migration,zanzibar_Itiner,Explore_zanzibar, Kilimanjaro_climbing_image,company, TravelPackageItem,Welcome_text,Service,Travels_Destination,Travel,Step_for_booking,Team,User_Testimonial,Gallery,About_This_Organization,Trip_DB
#from .models import Destination

# Create your views here.

package_items_prefetch = Prefetch(
    'package_items',
    queryset=TravelPackageItem.objects.order_by('order'),
    to_attr='prefetched_package_items'
)


def index(request):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect("index")
    else:
        form = BookingForm()
    qn = FAQ.objects.all()
    compan = company.objects.all()[:1]
    home_text = Welcome_text.objects.all()[:1]
    climbing = Kilimanjaro_climbing_image.objects.all()
    tour_list = Explore_zanzibar.objects.all()[:3]
    headline = Headline.objects.all()[:1]
    slider = MountMeruSlide.objects.first()  



    services = Service.objects.all()[:3]
    destinations = Travels_Destination.objects.all()[:3]
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    abouts = About_This_Organization.objects.all()[:1]
    step =  Step_for_booking.objects.all()[:3]
    teams = Team.objects.all()[:3]
    testimonial = User_Testimonial.objects.all()[:3]
    # all_safaries = Safari.objects.all()
    # tours = Tour.objects.all()[:4]
    tours = Tour.objects.all()[::-1]



    gallery = Gallery.objects.all()

    context = {
        'slider':slider,
          'qn':qn,
        "form": form,
      'tour_list':tour_list,
        'tours':tours,
        'services':services,
        'destinations':destinations,
        'headline':headline,
       "trips_list": trips_list,
        "safari_list": safari_list,
        # 'packages': all_packages,
        'step':step,
        'compan':compan,
        'teams':teams,
       'climbing':climbing,
        'testimonial':testimonial,
        'gallery':gallery,
        'abouts':abouts,
        'home_text':home_text
    }

    return render(request, 'index.html',context)
    #return render(request,'close-page.html')


from django.shortcuts import render, get_object_or_404
from .models import Travels_Destination
from django.core.paginator import Paginator

def destinations_list(request):
    qn = FAQ.objects.all()

    compan = company.objects.all()[:1]
    qs = Travels_Destination.objects.all()

    # Optional: filtering kwa location au best_time_to_visit kupitia query params
    location = request.GET.get("location")
    if location:
        qs = qs.filter(location__icontains=location)

    best = request.GET.get("best_time")
    if best:
        qs = qs.filter(best_time_to_visit__icontains=best)

    paginator = Paginator(qs, 9)  # 9 kwa ukurasa
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    gallery = Gallery.objects.all()
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

        'tours':tours,
        "destinations": page_obj, 
        "paginator": paginator,
        "page_obj": page_obj,
        "filters": {"location": location or "", "best_time": best or ""},
        'gallery':gallery,
        'compan':compan,
        "trips_list": trips_list,
        "safari_list": safari_list,

    }

    return render(request, "destination_list.html", context)

def destination_detail(request, pk):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking inquiry has been submitted successfully! We will contact you soon.")
            return redirect(request.path)  # rudisha user pale pale alipo
    else:
        form = BookingForm()
    compan = company.objects.all()[:1]

    dest = get_object_or_404(
        Travels_Destination.objects.prefetch_related(package_items_prefetch),
        pk=pk
    )
    includes = dest.includes.all() if hasattr(dest, 'includes') else []
    excludes = dest.excludes.all() if hasattr(dest, 'excludes') else []

    context = {
        "form":form,
        "destination": dest,
        'compan':compan,
        "includes": includes,
        "excludes": excludes,
        "other_destinations": Travels_Destination.objects.exclude(pk=pk)[:6],
    }
    return render(request, "destination_detail.html", context)

def service(request):
    qn = FAQ.objects.all()

    services = Service.objects.all()
    gallery = Gallery.objects.all()
    trips_list = Trip_DB.objects.all()
    compan = company.objects.all()[:1]
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()



    testimonial = User_Testimonial.objects.all()

    context = { 
          'qn':qn,

   'services':services,
    'tours':tours,
        'compan':compan,

    "trips_list": trips_list,
    "safari_list": safari_list,
    'testimonial':testimonial,
    'gallery':gallery,
    # 'packages': all_packages,


  
    }
    return render(request, 'service.html',context)

def team(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()



    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'team.html',context)



from django.shortcuts import render, get_object_or_404
from .models import Travel




def testimonial(request):
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()



    testimonial = User_Testimonial.objects.all()
    gallery = Gallery.objects.all()

    context = { 
    'testimonial':testimonial,
    'gallery':gallery,
        'compan':compan,

    "trips_list": trips_list,
    "safari_list": safari_list,
    'tours':tours,
    # 'packages': all_packages,


    }

    return render(request, 'testimonial.html',context)


from django.contrib import messages
from .models import Contact_Message

def contact(request):
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()

    # all_packages = Package.objects.all()
    gallery = Gallery.objects.all()
    tours = Tour.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            Contact_Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all the fields.")

    context = {
        'gallery': gallery,
        "trips_list": trips_list,
        'tours':tours,
            'compan':compan,

        "safari_list": safari_list,


        # 'packages': all_packages,

    }
    return render(request, 'contact.html', context)

def about(request):
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    teams = Team.objects.all()


    # all_packages = Package.objects.all()
    tours = Tour.objects.all()


    abouts = About_This_Organization.objects.all()[:1]


    context = { 
    'abouts':abouts,
     'teams': teams,
    'tours':tours,
        'compan':compan,

        "trips_list": trips_list,
        "safari_list": safari_list,
        # 'packages': all_packages,

    }
    return render(request, 'about.html',context)


# def about_us(request):
#     abouts = About_This_Organization.objects.all()
#     return render(request, 'test.html',{'abouts':abouts})




from django.shortcuts import render, get_object_or_404
from .models import Tour


def tour_list(request):
    qn = FAQ.objects.all()

    tours = Tour.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()    # all_packages = Package.objects.all()
    location = request.GET.get('location')
    tour_type = request.GET.get('type')

    if location:
        tours = tours.filter(location__icontains=location)
    if tour_type:
        tours = tours.filter(tour_type__iexact=tour_type)

    # Collect unique tour types for dropdown
    tour_types = Tour.objects.order_by('tour_type').values_list('tour_type', flat=True).distinct()

    return render(request, 'tour_list.html', {'qn':qn,'compan':compan,"safari_list": safari_list,'tours': tours, 'tour_types': tour_types})

def safari_list(request):
    qn = FAQ.objects.all()

    tours = Tour.objects.all()
    compan = company.objects.all()[:1]
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    location = request.GET.get('location')
    safari_type = request.GET.get('type')

    if location:
        safari = safari.filter(location__icontains=location)
    if safari_type:
        safari = safari.filter(safari_type__iexact=safari_type)

    # Collect unique tour types for dropdown
    safari_types = Travel.objects.order_by('safari_type').values_list('safari_type', flat=True).distinct()

    return render(request, 'safari_list.html', {'trip': trip,'qn':qn,
'compan':compan,'tours': tours, 'safari_types': safari_types,'safari':safari,"trips_list": trips_list,
        "safari_list": safari_list,})

# def tour_detail(request, pk):
#     safari = Travel.objects.all()
#     tours = Tour.objects.all()
#     trip = Trip_DB.objects.all()

#     # all_packages = Package.objects.all()


#     tour = get_object_or_404(
#         Tour.objects.prefetch_related(package_items_prefetch),
#         pk=pk
#     )

#     includes = tour.excludes.all() if hasattr(dest, 'includes') else []
#     excludes = tour.excludes.all() if hasattr(dest, 'excludes') else []



#     context = {
#         "tours": tours,
#         "tour": tour,
#         "trip":trip,
#         'safari':safari,
#         "includes":includes,
#         "excludes":excludes,
#         "related_safaris": Travel.objects.filter(location__icontains=tour.location)[:3],
#         "related_trips": Trip_DB.objects.filter(location__icontains=tour.location)[:3],
#     }
#     return render(request, 'tour_detail.html', context)





def tour_detail(request, pk):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect("index")
    else:
        form = BookingForm()
    qn = FAQ.objects.all()

    safari_list = Travel.objects.all()
    compan = company.objects.all()[:1]
    tours = Tour.objects.all()
    trips_list = Trip_DB.objects.all()
    tour = get_object_or_404(
        Tour.objects.prefetch_related(package_items_prefetch),
        pk=pk
    )

    includes = tour.includes.all()
    excludes = tour.excludes.all()

    context = {
          'qn':qn,

        "tours": tours,
        "tour": tour,
            'compan':compan,
    "form": form,

        "trips": trips_list,         # use trips_list here
        "trips_list": trips_list,    # optional, only if template uses both
        "safari_list": safari_list,
        "safaris": safari_list,
        "includes": includes,
        "excludes": excludes,
        "related_safaris": Travel.objects.filter(location__icontains=tour.location)[:3],
        "related_trips": Trip_DB.objects.filter(location__icontains=tour.location)[:3],
    }
    return render(request, 'tour_detail.html', context)


def safari_detail(request, pk):

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect("index")
    else:
        form = BookingForm()
    qn = FAQ.objects.all()

    tours = Tour.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()

    safari_obj = get_object_or_404(
        Travel.objects.prefetch_related(package_items_prefetch),
        pk=pk
    )

    includes = safari_obj.includes.all()
    excludes = safari_obj.excludes.all()

    context = {
          'qn':qn,
          "form": form,
      "safaris": safari_obj,        # specific safari
       "safari_list": safari_list,
        "safari": safari_obj,          # if template expects both, else unify naming
        "tours": tours,
        "trip": trips_list,
            'compan':compan,

        "includes": includes,
        "excludes": excludes,
        "other_tours": Tour.objects.filter(location__icontains=safari_obj.location)[:3],
        "related_trips": Trip_DB.objects.filter(location__icontains=safari_obj.location)[:3],
    }
    return render(request, 'safari_detail.html', context)






def Trip_list(request):
    qn = FAQ.objects.all()

    compan = company.objects.all()[:1]

    tours = Tour.objects.all()
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    location = request.GET.get('location')
    trip_type = request.GET.get('type')

    if location:
        trip = trip.filter(location__icontains=location)
    if trip_type:
        trip = trip.filter(trip_type__iexact=trip_type)

    # Collect unique tour types for dropdown
    trip_types = Trip_DB.objects.order_by('trip_type').values_list('trip_type', flat=True).distinct()

    return render(request, 'trip_list.html', {'compan':compan,'qn':qn,'tours': tours, 'trip': trip, 'trip_types': trip_types,
        "trips_list": trips_list,
        "safari_list": safari_list,})




def Trip_detail(request, pk):
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect("index")
    else:
        form = BookingForm()
    qn = FAQ.objects.all()

    compan = company.objects.all()[:1]

    safari_list = Travel.objects.all()
    trips_list = Trip_DB.objects.all()
    tours = Tour.objects.all()

    trip = get_object_or_404(
        Trip_DB.objects.prefetch_related(package_items_prefetch),
        pk=pk
    )

    includes = trip.includes.all()
    excludes = trip.excludes.all()

    context = {
          'qn':qn,
                "form": form,

       "trips_list": trips_list,
        "safari_list": safari_list,
        "tours": tours,
        "trip": trip,
            'compan':compan,

        "includes": includes,
        "excludes": excludes,
        "related_tours": Tour.objects.filter(location__icontains=trip.location)[:3],
        "related_safaris": Travel.objects.filter(location__icontains=trip.location)[:3],
    }
    return render(request, 'trip_detail.html', context)




def Arusha_highlight(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'Arusha_highlight.html',context)

def Bird_Watching(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'Bird_Watching.html',context)

def Cultural_Immersion(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'Cultural_Immersion.html',context)

def Culinary_Adventure(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'Culinary_Adventure.html',context)


def explore_zanzibar(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    tour_list = Explore_zanzibar.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = {
          'qn':qn,
 
      'tours':tours,
      'compan':compan,
    'tour_list': tour_list,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'explore-zanzibar.html',context)


def Zanzibar_Tour(request,pk):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    tour = get_object_or_404(Explore_zanzibar, pk=pk)

    itineraries = tour.itiner.all().order_by("day_number")
    gallery = Gallery.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

    'itineraries': itineraries,
      'tours':tours,
      'compan':compan,
      'teams':teams,
      'tour': tour,
      'itineraries':itineraries,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'z-tour.html',context)



def serengeti_migration(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    tour_list = Serengeti_migration.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
    'tour_list': tour_list,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'serengeti_migration.html',context)


def serengeti_Tour(request,pk):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    tour = get_object_or_404(Serengeti_migration, pk=pk)

    itineraries = tour.itiner.all().order_by("day_number")
    gallery = Gallery.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

    'itineraries': itineraries,
      'tours':tours,
      'compan':compan,
      'teams':teams,
      'tour': tour,
      'itineraries':itineraries,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'serengeti_tour.html',context)







def honeymoon_safaris(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    tour_list = HoneymoonSafaris.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
          'qn':qn,

      'tours':tours,
      'compan':compan,
    'tour_list': tour_list,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'honeymoon_safaris.html',context)


def honeymoon_Tour(request,pk):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    tour = get_object_or_404(HoneymoonSafaris, pk=pk)

    itineraries = tour.itiner.all().order_by("day_number")
    gallery = Gallery.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
    'itineraries': itineraries,
      'tours':tours,
      'qn':qn,

      'compan':compan,
      'teams':teams,
      'tour': tour,
      'itineraries':itineraries,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'honeymoon_Tour.html',context)



def camping_safaris(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()
    tour_list = CampingSafaris.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
              'qn':qn,

      'tours':tours,
      'compan':compan,
    'tour_list': tour_list,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'camping_safari.html',context)


def camping_Tour(request,pk):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    tour = get_object_or_404(CampingSafaris, pk=pk)

    itineraries = tour.itiner.all().order_by("day_number")
    gallery = Gallery.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
    'qn':qn,

    'itineraries': itineraries,
      'tours':tours,
      'compan':compan,
      'teams':teams,
      'tour': tour,
      'itineraries':itineraries,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'camping_tour.html',context)



def questions(request):
    qn = FAQ.objects.all()

    trip = Trip_DB.objects.all()   
    teams = Team.objects.all()
    gallery = Gallery.objects.all()

    compan = company.objects.all()[:1]

    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    tours = Tour.objects.all()
    context = { 
      'qn':qn,
      'tours':tours,
      'compan':compan,
      'teams':teams,
      'gallery':gallery,
      "trips_list": trips_list,
      "safari_list": safari_list,   
    }

    return render(request, 'questions.html',context)




from django.contrib import messages
from .forms import BookingForm

def booking_form_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking inquiry has been submitted successfully! We will contact you soon.")
            return redirect(request.path)  # rudisha user pale pale alipo
    else:
        form = BookingForm()
    return {"booking_form": form}




def fly_Tz(request):
    qn = FAQ.objects.all()

    services = Service.objects.all()
    gallery = Gallery.objects.all()
    trips_list = Trip_DB.objects.all()
    compan = company.objects.all()[:1]
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()



    testimonial = User_Testimonial.objects.all()

    context = { 
          'qn':qn,

   'services':services,
    'tours':tours,
        'compan':compan,

    "trips_list": trips_list,
    "safari_list": safari_list,
    'testimonial':testimonial,
    'gallery':gallery,
    # 'packages': all_packages,


  
    }
    return render(request, 'fly_Tz.html',context)


def Tanzania_Visa(request):
    qn = FAQ.objects.all()

    services = Service.objects.all()
    gallery = Gallery.objects.all()
    trips_list = Trip_DB.objects.all()
    compan = company.objects.all()[:1]
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()



    testimonial = User_Testimonial.objects.all()

    context = { 
          'qn':qn,

   'services':services,
    'tours':tours,
        'compan':compan,

    "trips_list": trips_list,
    "safari_list": safari_list,
    'testimonial':testimonial,
    'gallery':gallery,
    # 'packages': all_packages,


  
    }
    return render(request, 'Tanzania_Visa.html',context)


def form(request):
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect("index")
    else:
        form = BookingForm()
    qn = FAQ.objects.all()

    services = Service.objects.all()
    gallery = Gallery.objects.all()
    trips_list = Trip_DB.objects.all()
    compan = company.objects.all()[:1]
    safari_list = Travel.objects.all()
    # all_packages = Package.objects.all()
    tours = Tour.objects.all()



    testimonial = User_Testimonial.objects.all()

    context = { 
          'qn':qn,

   'services':services,
    'tours':tours,
        'compan':compan,

    "trips_list": trips_list,
    "safari_list": safari_list,
    'testimonial':testimonial,
    'gallery':gallery,
     "form": form,
    # 'packages': all_packages,
    }


  
    return render(request ,'sample_form.html',context)













import json
import requests
from django.db.models import Count, Avg
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import UserVisit, UserActivity

IPINFO_TOKEN = "0fe180f7e54cf6"

# def get_location_from_ip(ip_address):
#     """Get location information using ipinfo.io"""
#     if ip_address in ["127.0.0.1", "localhost"]:
#         return {"country": "Localhost", "region": None, "city": None}

#     try:
#         url = f"https://ipinfo.io/{ip_address}?token={IPINFO_TOKEN}"
#         response = requests.get(url, timeout=5)
#         if response.status_code == 200:
#             data = response.json()
#             return {
#                 "country": data.get("country"),
#                 "region": data.get("region"),
#                 "city": data.get("city")
#             }
#     except Exception as e:
#         print(f"IP lookup error: {e}")
#     return {"country": None, "region": None, "city": None}
def get_location_from_ip(ip):
    # LOCALHOST SPECIAL CASE
    if ip in ["127.0.0.1", "localhost"]:
        return {"country": "Localhost", "region": None, "city": None}

    # ------------ PRIMARY PROVIDER: ip-api (Unlimited, No Token) ---------------
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url, timeout=4).json()

        if r.get("status") == "success":
            return {
                "country": r.get("countryCode"),
                "region": r.get("regionName"),
                "city": r.get("city")
            }
    except:
        pass

    # ------------ FALLBACK PROVIDER: ipinfo.io (Optional) ---------------
    try:
        url = f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}"
        r = requests.get(url, timeout=4).json()

        return {
            "country": r.get("country"),
            "region": r.get("region"),
            "city": r.get("city")
        }
    except:
        return {"country": None, "region": None, "city": None}




def get_client_ip(request):
    """Get client IP address safely"""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


@method_decorator(csrf_exempt, name="dispatch")
class TrackVisitView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))

        ip_address = get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        page_visited = data.get("page_visited", "")
        referrer = data.get("referrer", "")

        visit, created = UserVisit.objects.get_or_create(
            ip_address=ip_address,
            page_visited=page_visited,
            defaults={
                "user_agent": user_agent,
                "referrer": referrer,
                "visit_count": 1,
            },
        )

        if not created:
            visit.visit_count += 1
            visit.save()

        location = get_location_from_ip(ip_address)
        if location["country"]:
            visit.country = location["country"]
            visit.region = location["region"]
            visit.city = location["city"]
            visit.save()

        return JsonResponse({"status": "success", "visit_id": visit.id})




@method_decorator(csrf_exempt, name="dispatch")
class TrackVisitView(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))

        ip_address = get_client_ip(request)
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        page_visited = data.get("page_visited", "")
        referrer = data.get("referrer", "")

        visit, created = UserVisit.objects.get_or_create(
            ip_address=ip_address,
            page_visited=page_visited,
            defaults={
                "user_agent": user_agent,
                "referrer": referrer,
                "visit_count": 1,
            },
        )

        if not created:
            visit.visit_count += 1
            visit.save()

        # GET LOCATION USING NEW SYSTEM
        location = get_location_from_ip(ip_address)
        visit.country = location["country"]
        visit.region = location["region"]
        visit.city = location["city"]
        visit.save()

        return JsonResponse({"status": "success", "visit_id": visit.id})


class TrackActivityView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))
            visit_id = data.get("visit_id")
            activity_type = data.get("activity_type")
            activity_details = data.get("activity_details", "")

            if not visit_id or not activity_type:
                return JsonResponse({"error": "Missing fields"}, status=400)

            try:
                visit = UserVisit.objects.get(id=visit_id)
            except UserVisit.DoesNotExist:
                return JsonResponse({"error": "Visit not found"}, status=404)

            UserActivity.objects.create(
                visit=visit,
                activity_type=activity_type,
                activity_details=activity_details
            )

            return JsonResponse({"status": "success"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


# @method_decorator(csrf_exempt, name="dispatch")
# class TrackActivityView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body.decode("utf-8"))
#             visit_id = data.get("visit_id")
#             activity_type = data.get("activity_type")
#             activity_details = data.get("activity_details", "")

#             visit = UserVisit.objects.get(id=visit_id)

#             UserActivity.objects.create(
#                 visit=visit,
#                 activity_type=activity_type,
#                 activity_details=activity_details,
#             )
#             return JsonResponse({"status": "success"})
#         except Exception as e:
#             return JsonResponse({"status": "error", "message": str(e)}, status=400)



from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Avg

# Helper: hakikisha user ni staff/admin
def staff_check(user):
    return user.is_staff or user.is_superuser



@login_required(login_url="/admin/login/")   # peleka kwa login ya admin
@user_passes_test(staff_check)              # zuia non-admin wasione
def dashboard_view(request):
    visits = UserVisit.objects.all().order_by("-timestamp")[:100]
    total_visits = UserVisit.objects.count()

    visits_by_country = (
        UserVisit.objects.values("country")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    avg_visits_per_ip = (
        UserVisit.objects.values("ip_address")
        .annotate(total=Count("id"))
        .aggregate(avg=Avg("total"))["avg"]
        or 0
    )
    avg_visits_per_ip = round(avg_visits_per_ip, 2)

    new_visits = (
        UserVisit.objects.values("ip_address")
        .annotate(c=Count("id"))
        .filter(c=1)
        .count()
    )
    returning_visits = (
        UserVisit.objects.values("ip_address")
        .annotate(c=Count("id"))
        .filter(c__gt=1)
        .count()
    )
    local_visits = UserVisit.objects.filter(country="TZ").count()

    context = {
        "visits": visits,
        "total_visits": total_visits,
        "visits_by_country": visits_by_country,
        "avg_visits_per_ip": avg_visits_per_ip,
        "new_visits": new_visits,
        "returning_visits": returning_visits,
        "local_visits": local_visits,
    }
    return render(request, "dashboard.html", context)



def meru_climbing(request):
    qn = FAQ.objects.all()
    compan = company.objects.all()[:1]
    home_text = Welcome_text.objects.all()[:1]
    climbing = Kilimanjaro_climbing_image.objects.all()
    tour_list = Explore_zanzibar.objects.all()
    headline = Headline.objects.all()[:1]


    services = Service.objects.all()[:3]
    destinations = Travels_Destination.objects.all()[:3]
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    abouts = About_This_Organization.objects.all()[:1]
    step =  Step_for_booking.objects.all()[:3]
    teams = Team.objects.all()[:3]
    testimonial = User_Testimonial.objects.all()[:3]
    # all_safaries = Safari.objects.all()
    tours = Tour.objects.all()


    gallery = Gallery.objects.all()
    
    context = {
          'qn':qn,
        "form": form,
      'tour_list':tour_list,
        'tours':tours,
        'services':services,
        'destinations':destinations,
        'headline':headline,
       "trips_list": trips_list,
        "safari_list": safari_list,
        # 'packages': all_packages,
        'step':step,
        'compan':compan,
        'teams':teams,
       'climbing':climbing,
        'testimonial':testimonial,
        'gallery':gallery,
        'abouts':abouts,
        'home_text':home_text
    }


    return render(request, "meru_climbing.html", context) 

def Momela_route_3(request):
    qn = FAQ.objects.all()
    compan = company.objects.all()[:1]
    home_text = Welcome_text.objects.all()[:1]
    climbing = Kilimanjaro_climbing_image.objects.all()
    tour_list = Explore_zanzibar.objects.all()
    headline = Headline.objects.all()[:1]


    services = Service.objects.all()[:3]
    destinations = Travels_Destination.objects.all()[:3]
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    abouts = About_This_Organization.objects.all()[:1]
    step =  Step_for_booking.objects.all()[:3]
    teams = Team.objects.all()[:3]
    testimonial = User_Testimonial.objects.all()[:3]
    # all_safaries = Safari.objects.all()
    tours = Tour.objects.all()


    gallery = Gallery.objects.all()
    
    context = {
          'qn':qn,
        "form": form,
      'tour_list':tour_list,
        'tours':tours,
        'services':services,
        'destinations':destinations,
        'headline':headline,
       "trips_list": trips_list,
        "safari_list": safari_list,
        # 'packages': all_packages,
        'step':step,
        'compan':compan,
        'teams':teams,
       'climbing':climbing,
        'testimonial':testimonial,
        'gallery':gallery,
        'abouts':abouts,
        'home_text':home_text
    }


    return render(request, "Momela_route_3.html", context) 

def Momela_route_4(request):
    qn = FAQ.objects.all()
    compan = company.objects.all()[:1]
    home_text = Welcome_text.objects.all()[:1]
    climbing = Kilimanjaro_climbing_image.objects.all()
    tour_list = Explore_zanzibar.objects.all()
    headline = Headline.objects.all()[:1]


    services = Service.objects.all()[:3]
    destinations = Travels_Destination.objects.all()[:3]
    trips_list = Trip_DB.objects.all()
    safari_list = Travel.objects.all()
    abouts = About_This_Organization.objects.all()[:1]
    step =  Step_for_booking.objects.all()[:3]
    teams = Team.objects.all()[:3]
    testimonial = User_Testimonial.objects.all()[:3]
    # all_safaries = Safari.objects.all()
    tours = Tour.objects.all()


    gallery = Gallery.objects.all()
    
    context = {
          'qn':qn,
      'tour_list':tour_list,
        'tours':tours,
        'services':services,
        'destinations':destinations,
        'headline':headline,
       "trips_list": trips_list,
        "safari_list": safari_list,
        # 'packages': all_packages,
        'step':step,
        'compan':compan,
        'teams':teams,
       'climbing':climbing,
        'testimonial':testimonial,
        'gallery':gallery,
        'abouts':abouts,
        'home_text':home_text
    }


    return render(request, "Momela_route_4.html",context) 



# views.py (in your Django app, e.g., myapp/views.py)
from django.views.generic import DetailView
from .models import TermsAndConditions

class TermsAndConditionsView(DetailView):
    """
    A view to display the Terms and Conditions page.
    Assumes there's only one active instance; you can filter if needed.
    """
    model = TermsAndConditions
    template_name = 'terms_and_conditions.html'
    context_object_name = 'terms'

    def get_object(self):
        # Fetch the latest version; adjust as per your needs
        return TermsAndConditions.objects.latest('last_updated')