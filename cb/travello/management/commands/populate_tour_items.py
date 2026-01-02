from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from travello.models import Tour, TravelPackageItem

class Command(BaseCommand):
    help = "Populate include and exclude items for all Tour records"

    def handle(self, *args, **options):
        includes = [
            "Guided Kilimanjaro Trek: Full climb from start to summit and back, tailored to your selected route.",
            "Certified Guide: English-speaking guide with Wilderness First Responder (WFR) & CPR training.",
            "Skilled Support Crew: Proper ratio of experienced porters and a professional mountain cook.",
            "Hotel Accommodation: Two nights in a comfortable hotel (Bed & Breakfast) before and after the trek.",
            "All Park Fees: Entry, camping/hut fees, rescue, crew permits, and VAT.",
            "Full-Board Meals: Nutritious breakfast, lunch, dinner, and drinking water during the entire trek.",
            "Airport Transfers: Transport to/from Kilimanjaro International Airport (JRO).",
            "Camping Gear: High-quality tents, sleeping mats, dining equipment & more (excluding personal gear).",
        ]

        excludes = [
            "Flights: International and domestic airfares are not included.",
            "Visa Fees: Clients are responsible for Tanzania entry visas.",
            "Insurance: Travel and medical insurance is highly recommended but not provided.",
            "Tips: Gratuities for guides, porters, and cooks are not included.",
            "Personal Gear: Bring your own trekking boots, sleeping bag, clothes, etc.",
            "Extra Beverages: Soft drinks, alcohol, and snacks outside meals are excluded.",
            "Extra Hotel Nights: If descending early or needing extra rest days, extra hotel costs apply.",
            "Optional Excursions: Tours or experiences not listed in the main itinerary are at your own cost.",
        ]

        tours = Tour.objects.all()
        if not tours.exists():
            self.stdout.write(self.style.WARNING("⚠️  No Tour records found in database."))
            return

        tour_ct = ContentType.objects.get_for_model(Tour)
        self.stdout.write(self.style.HTTP_INFO("\n🗻 Populating Tour package items..."))

        for tour in tours:
            self.stdout.write(self.style.NOTICE(f"➡️  Processing tour: {tour.title}"))

            # Includes
            for index, title in enumerate(includes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=tour_ct,
                    object_id=tour.id,
                    item_type=TravelPackageItem.INCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"   ✅ Added include: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"   ⚠️ Already exists: {title}"))

            # Excludes
            for index, title in enumerate(excludes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=tour_ct,
                    object_id=tour.id,
                    item_type=TravelPackageItem.EXCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"   ✅ Added exclude: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"   ⚠️ Already exists: {title}"))

        self.stdout.write(self.style.SUCCESS("\n🎉 Successfully populated Tour includes & excludes!"))

###python manage.py populate_tour_items
