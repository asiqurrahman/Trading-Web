from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import zipcodes


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username' , 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username' , 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image' , 'location', 'detail_location']

    def clean_location(self, *args, **kwargs):
        location = self.cleaned_data.get("location")
        if location is None:
            raise forms.ValidationError("Please Enter A Valid ZipCode")
        else:
            valid_zipcode = location.isdigit()
        if valid_zipcode is True:
            valid_zipcode2 = zipcodes.is_real('{}'.format(location))
            if valid_zipcode2 is True:
                return location
            else:
                raise forms.ValidationError("Please Enter A Valid ZipCode")
        else:
            raise forms.ValidationError("Please Enter A Valid ZipCode")
    
    def clean_detail_location(self, *args, **kwargs):
        detail_location = self.cleaned_data.get("location")

        if detail_location:
            zipcode = detail_location
            user_location = zipcodes.matching('{}'.format(zipcode))
            city = user_location[0]['city']
            state = user_location[0]['state']
            detail_location = city + ',' + ' ' + state
            return detail_location
           