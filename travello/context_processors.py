from .forms import BookingForm

def booking_form_processor(request):
    return {"booking_form": BookingForm()}
