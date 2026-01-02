from django.contrib import admin
from .models import TravelPackageItem, Travels_Destination,Service,Team,User_Testimonial,Travel,Step_for_booking,Gallery,About_This_Organization,Trip_DB,Trip_Itinerary_DB
from .models import Headline,CampingSafaris,Camping_Itiner,Honeymoon_Itiner,HoneymoonSafaris,Serengeti_Itiner,zanzibar_Itiner,Explore_zanzibar,Kilimanjaro_climbing_image,Tour,Contact_Message,Tour_Itinerary,Travel_Itiner,Welcome_text,company,Serengeti_migration
from django.utils.safestring import mark_safe
from .forms import MountMeruSlideAdminForm,CampingSafarisForm,HoneymoonSafarisForm,Serengeti_migrationForm, Explore_zanzibarForm,Kilimanjaro_climbing_imageAdminForm,companyAdminForm, ServiceAdminForm,Step_for_bookingAdminForm,DestinationForm,User_TestimonialForm,TourForm,About_This_OrganizationForm,GalleryForm,TravelForm,Trip_DBForm,Welcome_textAdminForm

# Register your models here.

#admin.site.register(Destination)

class DestinationAdmin(admin.ModelAdmin):
    form = DestinationForm


    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',  # Badilisha na key yako halisi kama ni tofauti
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('location', 'Offer_in_percent', 'image_preview')

admin.site.register(Travels_Destination, DestinationAdmin)



# Inline kwa kuhariri includes/excludes ndani ya parent
class TravelPackageItemInline(admin.TabularInline):
    model = TravelPackageItem
    extra = 0
    fields = ('item_type', 'title', 'description', 'order')
    ordering = ('order',)


# Usimamizi wa PackageItem mwenyewe
@admin.register(TravelPackageItem)
class TravelPackageItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'content_object', 'order')
    list_filter = ('item_type', 'content_type')
    search_fields = ('title', 'description')
    ordering = ('content_type', 'object_id', 'order')



class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('title', 'image_preview')

admin.site.register(Service, ServiceAdmin)



from .models import Team
from .forms import TeamForm

class TeamAdmin(admin.ModelAdmin):
    form = TeamForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;">')
        return "No Image"

    image_preview.short_description = 'Image Preview'

    list_display = ('Full_name', 'designation', 'image_preview')

admin.site.register(Team, TeamAdmin)


class UserTestimonialAdmin(admin.ModelAdmin):
    form = User_TestimonialForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Full_name', 'country', 'image_preview')

admin.site.register(User_Testimonial, UserTestimonialAdmin)


class StepForBookingAdmin(admin.ModelAdmin):
    form = Step_for_bookingAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Title', 'image_preview')


admin.site.register(Step_for_booking, StepForBookingAdmin)
    

class TravelAdmin(admin.ModelAdmin):

    form = TravelForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'featured_image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
 
    image_preview.short_description = 'Preview'
    list_display = ('title', 'location', 'safari_type', 'days', 'price')



admin.site.register(Travel, TravelAdmin)


class GalleryAdmin(admin.ModelAdmin):

    form = GalleryForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Title', 'image_preview')

admin.site.register(Gallery, GalleryAdmin)




class About_This_OrganizationAdmin(admin.ModelAdmin):

    form = About_This_OrganizationForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
 
    image_preview.short_description = 'Preview'
    list_display = ('title','content','mission','vision', 'image')


admin.site.register(About_This_Organization, About_This_OrganizationAdmin)



@admin.register(Contact_Message)
class Contact_MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created_at')
    search_fields =  ('name','email', 'subject')





class TourAdmin(admin.ModelAdmin):

    form = TourForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'featured_image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
 
    image_preview.short_description = 'Preview'
    list_display = ('title', 'location', 'tour_type', 'days', 'price')


admin.site.register(Tour, TourAdmin)



@admin.register(Tour_Itinerary)
class Tour_ItineraryAdmin(admin.ModelAdmin):
    list_display = ('tour', 'day_number', 'title', 'elevation_start', 'elevation_end', 'distance_km', 'hiking_time', 'habitat')
    search_fields = ('title', 'description', 'habitat')
    list_filter = ('tour', 'habitat')




@admin.register(Travel_Itiner)
class Travel_ItinerAdmin(admin.ModelAdmin):
    list_display = ('travel', 'day_number', 'title', 'elevation_start', 'elevation_end', 'distance_km', 'hiking_time', 'habitat')
    search_fields = ('title', 'description', 'habitat')
    list_filter = ('travel', 'habitat')


class Trip_DBAdmin(admin.ModelAdmin):

    form = Trip_DBForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'featured_image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"
 
    image_preview.short_description = 'Preview'
    list_display = ('title', 'location', 'trip_type', 'days', 'price')



admin.site.register(Trip_DB, Trip_DBAdmin)



@admin.register(Trip_Itinerary_DB)
class Trip_Itinerary_DBAdmin(admin.ModelAdmin):
    list_display = ('trip', 'day_number', 'title')
    search_fields = ('title', 'description')
    list_filter = ('trip',)




# class Welcome_textAdmin(admin.ModelAdmin):
#     form = Welcome_textAdminForm

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         formfield = super().formfield_for_dbfield(db_field, **kwargs)
#         if db_field.name == 'image':
#             formfield.widget.attrs.update({
#                 'role': 'uploadcare-uploader',
#                 'data-public-key': '76122001cca4add87f02', 
#             })
#         return formfield

#     def image_preview(self, obj):
#         if obj.image:
#             return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
#         return "No Image"

#     image_preview.short_description = 'Preview'

#     list_display = ('title','subtitle', 'image_preview')

# admin.site.register(Welcome_text, Welcome_textAdmin)


class Welcome_textAdmin(admin.ModelAdmin):
    form = Welcome_textAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('title', 'subtitle', 'image_preview')


admin.site.register(Welcome_text, Welcome_textAdmin)



class companyAdmin(admin.ModelAdmin):
    form = companyAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99', 
            })
        return formfield

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.get_image_url()}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('company_name', 'image_preview')

admin.site.register(company, companyAdmin)



class Kilimanjaro_climbing_imageAdmin(admin.ModelAdmin):
    form = Kilimanjaro_climbing_imageAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="{obj.get_image_url()}" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('title_1','title_2','title_3','title_4','title_5','title_6','title_7','title_8', 'image_preview')


admin.site.register(Kilimanjaro_climbing_image, Kilimanjaro_climbing_imageAdmin)


class Explore_zanzibarAdmin(admin.ModelAdmin):
    form = Explore_zanzibarForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Tour_title','Tour_Descriptions','Tour_price')


admin.site.register(Explore_zanzibar, Explore_zanzibarAdmin)





@admin.register(zanzibar_Itiner)
class zanzibar_ItinerAdmin(admin.ModelAdmin):
    list_display = ('zanzibar_tour', 'day_number', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')






class Serengeti_migrationAdmin(admin.ModelAdmin):
    form = Serengeti_migrationForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Tour_title','Tour_Descriptions','Tour_price')


admin.site.register(Serengeti_migration, Serengeti_migrationAdmin)





@admin.register(Serengeti_Itiner)
class Serengeti_ItinerAdmin(admin.ModelAdmin):
    list_display = ('serengeti_tour', 'day_number', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')





class HoneymoonSafarisAdmin(admin.ModelAdmin):
    form = HoneymoonSafarisForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Tour_title','Tour_Descriptions','Tour_price')


admin.site.register(HoneymoonSafaris, HoneymoonSafarisAdmin)





@admin.register(Honeymoon_Itiner)
class Honeymoon_ItinerAdmin(admin.ModelAdmin):
    list_display = ('Honeymoon_tour', 'day_number', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')








class CampingSafarisAdmin(admin.ModelAdmin):
    form = CampingSafarisForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image']:
            img_val = getattr(obj, img_field)
            if img_val:
                previews.append(
                    f'<img src="https://ucarecdn.com/{img_val}/-/format/jpg/-/quality/smart/" '
                    f'style="max-height: 100px; margin-right: 5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"

    image_preview.short_description = 'Preview'

    list_display = ('Tour_title','Tour_Descriptions','Tour_price')


admin.site.register(CampingSafaris, CampingSafarisAdmin)





@admin.register(Camping_Itiner)
class Camping_ItinerAdmin(admin.ModelAdmin):
    list_display = ('Camping_tour', 'day_number', 'title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')



from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    search_fields = ("question", "answer")


from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "country",
        "arrival_date",
        "departure_date",
        "adults",
        "children",
        "created_at",
    )
    list_filter = ("country", "arrival_date", "departure_date", "created_at")
    search_fields = ("first_name", "last_name", "email", "country", "interested_in")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


from .models import UserVisit, UserActivity


@admin.register(UserVisit)
class UserVisitAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "country", "region", "city", "visit_count", "timestamp", "page_visited")
    list_filter = ("country", "region", "city", "timestamp")
    search_fields = ("ip_address", "page_visited", "user_agent")
    ordering = ("-timestamp",)


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("visit", "activity_type", "activity_details", "timestamp")
    list_filter = ("activity_type", "timestamp")
    search_fields = ("visit__ip_address", "activity_details")
    ordering = ("-timestamp",)




@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('name_of_headline',)
    search_fields =  ('name_of_headline',)


from django.contrib import admin
from .models import TermsAndConditions

@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'last_updated')
    search_fields = ('title', 'content')
    ordering = ('-last_updated',)
    readonly_fields = ('last_updated',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'version')
        }),
        ('Metadata', {
            'fields': ('last_updated',),
            'classes': ('collapse',),
        }),
    )

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import MountMeruSlide
from django.utils.html import format_html

@admin.register(MountMeruSlide)
class MountMeruSlideAdmin(admin.ModelAdmin):
    form = MountMeruSlideAdminForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['image1', 'image2', 'image3', 'image4', 'image5']:
            formfield.widget.attrs.update({
                'role': 'uploadcare-uploader',
                'data-public-key': 'c250e902196b9ac60e99',
            })
        return formfield

    def image_preview(self, obj):
        previews = []
        for img_field in ['image1', 'image2', 'image3', 'image4', 'image5']:
            img_val = getattr(obj, img_field)
            if img_val:  # img_val is already a URL string in Cloudinary
                previews.append(
                    f'<img src="{img_val}" '
                    f'style="max-height: 100px; margin-right: 5px; border-radius:5px;" />'
                )
        return mark_safe("".join(previews)) if previews else "No Image"


    list_display = ("title", "created_at", "image_preview")
    readonly_fields = ("image_preview",)
