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
        fields = ['image' , 'location', 'detail_location', 'detail_lat', 'detail_lng']

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
    
    def clean_detail_lat(self, *args, **kwargs):
        detail_lat = self.cleaned_data.get("location")

        if detail_lat:
            zipcode = detail_lat
            user_location = zipcodes.matching('{}'.format(zipcode))
            latitude = user_location[0]['lat']
            detail_lat = latitude
            return detail_lat
    
    def clean_detail_lng(self, *args, **kwargs):
        detail_lng= self.cleaned_data.get("location")

        if detail_lng:
            zipcode = detail_lng
            user_location = zipcodes.matching('{}'.format(zipcode))
            longitude = user_location[0]['long']
            detail_lng = longitude
            return detail_lng
           
           
           