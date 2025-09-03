# biodiversity/forms.py
from django import forms
from .models import WildlifeRegistration,WildlifeFarmPermit,LocalTransportPermit,GratuitousPermitMOA,SpecialLocalTransportPermit,MarineResearchClearance




class WildlifeFarmPermitForm(forms.ModelForm):
    class Meta:
        model = WildlifeFarmPermit
        fields = ['full_name', 'address', 'contact_number', 'habitat_type',]



class WildlifeRegistrationForm(forms.ModelForm):
    class Meta:
        model = WildlifeRegistration
        fields = [
            'full_name', 'address', 'contact_number', 
            'cultural_type',
        ]


class LocalTransportPermitForm(forms.ModelForm):
    class Meta:
        model = LocalTransportPermit
        fields = ['full_name', 'address', 'contact_number', 'provision_type']




class GratuitousPermitMOAForm(forms.ModelForm):
    class Meta:
        model = GratuitousPermitMOA
        fields = [
            'full_name', 'address', 'contact_number',
            'regulation_type', 
        ]


class SpecialLocalTransportPermitForm(forms.ModelForm):
    class Meta:
        model = SpecialLocalTransportPermit
        fields = ['full_name', 'address', 'contact_number', 'adaptation_type']


class MarineResearchClearanceForm(forms.ModelForm):
    class Meta:
        model = MarineResearchClearance
        fields = ['full_name', 'address', 'contact_number', 'support_type']