from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from travello.models import Travel, TravelPackageItem


class Command(BaseCommand):
    help = "Populate include and exclude items for all Travel records"

    def handle(self, *args, **options):
        # --- Includes ---
        travel_includes = [
            "Professional safari guide",
            "Transport (4×4 land cruiser with open roof)",
            "Park fees for vehicle and driver",
            "Accommodation on arrival day and departure in Arusha or Moshi",
            "Three meals during the safari",
            "Pickup and drop off from the Kilimanjaro airport",
            "Government taxes",
            "Bottled water and soft drinks",
        ]

        # --- Excludes ---
        travel_excludes = [
            "Flights",
            "Travel insurance",
            "Tips to your safari guide",
            "Visa fees",
            "Laundry services",
        ]

        # Get all Travel records
        travels = Travel.objects.all()
        if not travels.exists():
            self.stdout.write(self.style.WARNING("⚠️  No Travel records found in database."))
            return

        travel_ct = ContentType.objects.get_for_model(Travel)

        self.stdout.write(self.style.HTTP_INFO("\n🌍 Populating Travel package items..."))

        for travel in travels:
            self.stdout.write(self.style.NOTICE(f"➡️  Processing safari: {travel.title}"))

            # Includes
            for index, title in enumerate(travel_includes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=travel_ct,
                    object_id=travel.id,
                    item_type=TravelPackageItem.INCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"   ✅ Added include: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"   ⚠️ Already exists: {title}"))

            # Excludes
            for index, title in enumerate(travel_excludes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=travel_ct,
                    object_id=travel.id,
                    item_type=TravelPackageItem.EXCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"   ✅ Added exclude: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"   ⚠️ Already exists: {title}"))

        self.stdout.write(self.style.SUCCESS("\n🎉 Successfully populated Travel includes & excludes!"))



###python manage.py populate_travel_items
