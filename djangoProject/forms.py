from django import forms
from app2.models import employee
from app2.models import merchants
from app2.models import partners
from app2.models import manufacturer

class EmpForms(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"

class MerchantForms(forms.ModelForm):
    class Meta:
        model = merchants
        fields = "__all__"

class PartnerForms(forms.ModelForm):
    class Meta:
        model = partners
        fields = "__all__"

class ManufacturerForms(forms.ModelForm):
     billingtype = forms.CharField(
        max_length=200,
        required=False,
     )
     materialtype = forms.CharField(
         max_length=200,
         required=False,

     )
     addonstype = forms.CharField(
         max_length=200,
         required=False,

     )
     addonsnumber = forms.CharField(
         max_length=200,
         required=False,

     )

     class Meta:
        model = manufacturer
        # fields = "__all__"
        fields = ['id1', 'name' , 'emailid' , 'address' , 'passcode' ,  'billingtype' ,'materialtype' , 'addonstype' , 'addonsnumber' , 'phoneno' ]