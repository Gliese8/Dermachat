from django.shortcuts import render, redirect
from dermachat.models import ImageMetadata
from .models import DoctorClassification

def doctor_classification_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        skin_tone = request.POST.get('skin_tone')
        malignant = request.POST.get('malignant') == 'true'

        # Retrieve the image_id from ImageMetadata
        image_metadata = ImageMetadata.objects.filter(user_id=user_id).first()
        if image_metadata:
            filename = f"{image_metadata.image.name.split('/')[-1]}"

            # Create DoctorClassification instance with retrieved image_id
            DoctorClassification.objects.create(
                user_id=user_id,
                skin_tone=skin_tone,
                malignant=malignant,
                image=filename  
            )

        # Redirect back to the doctor page
        return redirect('doctor_interface')  

    return render(request, 'doctor_interface.html')