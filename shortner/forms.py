from django import forms
from .models import ShortURL
from django.core.exceptions import ValidationError
from django.utils import timezone


class ShortURLForm(forms.ModelForm):
    
    custom_code = forms.CharField(max_length=15, required=False)
    expires_at = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={"type": "datetime-local"} ),
                                     input_formats=["%Y-%m-%dT%H:%M"])
    

    class Meta:
        model = ShortURL
        fields= ["original_url", "custom_code", "expires_at"]
        
    def clean_custom_code(self):
        code = self.cleaned_data.get("custom_code")
        if code:
            code = code.lower()
            if ShortURL.objects.filter(short_code = code).exists():
                raise forms.ValidationError("This short code is already in use.")
        return code

    def clean_expires_at(self):
        expires_at = self.cleaned_data.get("expires_at")
        if expires_at and expires_at < timezone.now():
            raise ValidationError("Expiration date cannot be in the past.")
        return expires_at
    
