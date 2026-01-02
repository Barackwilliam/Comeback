from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from travello.models import Trip_DB, TravelPackageItem


class Command(BaseCommand):
    help = "Populate include and exclude items for all Trip_DB records"

    def handle(self, *args, **options):
        includes = [
            "A knowledgeable tour guide",
            "Entrance fees to attractions",
            "Lunch and refreshments",
            "Transportations",
            "Activities",
        ]

        excludes = [
            "Travel insurance",
            "Alcoholic beverage",
            "Souvenirs and shopping",
            "Flights",
            "Accommodations",
            "Additional activities",
            "Gratuities for guide and drivers",
        ]

        trip_ct = ContentType.objects.get_for_model(Trip_DB)
        trips = Trip_DB.objects.all()

        if not trips.exists():
            self.stdout.write(self.style.WARNING("⚠️  No trips found in database."))
            return

        for trip in trips:
            self.stdout.write(self.style.HTTP_INFO(f"\nProcessing trip: {trip.title}"))

            for index, title in enumerate(includes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=trip_ct,
                    object_id=trip.id,
                    item_type=TravelPackageItem.INCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"  ✅ Added include: {title}"))
                else:
                    self.stdout.write(self.style.NOTICE(f"  ⚠️  Already exists: {title}"))

            for index, title in enumerate(excludes):
                obj, created = TravelPackageItem.objects.get_or_create(
                    content_type=trip_ct,
                    object_id=trip.id,
                    item_type=TravelPackageItem.EXCLUDE,
                    title=title,
                    defaults={"order": index + 1},
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"  ✅ Added exclude: {title}"))
                else:
                    self.stdout.write(self.style.NOTICE(f"  ⚠️  Already exists: {title}"))

        self.stdout.write(self.style.SUCCESS("\n🎉 Done populating includes & excludes for all trips!"))


###python manage.py populate_package_items
