from django import forms
from .models import LandClassificationApplication,SurveyAuthorityApplication,AgriculturalApplication,ResidentialFreePatentApplication,SurveyPlanApplication

class LandClassificationApplicationForm(forms.ModelForm):
    class Meta:
        model = LandClassificationApplication
        fields = ['full_name', 'address', 'number_of_trees', 'reason_for_cutting', 'documents']


class SurveyAuthorityApplicationForm(forms.ModelForm):
    class Meta:
        model = SurveyAuthorityApplication
        fields = ['full_name', 
                  'confirmation_of_affidavit_of_adjoining_owners', 
                  'dar_certification', 
                  'denr_and_certification', 
                  'technical_description', 
                  'brgy_clearance', 
                  'deed_of_conveyance', 
                  'letter_request', 
                  'sketch_plan', 

                ]


class AgriculturalApplicationForm(forms.ModelForm):
    class Meta:
        model = AgriculturalApplication
        fields = ['owner_name', 'project_name', 'location', 'construction_type', 'environmental_doc']



class ResidentialFreePatentApplicationForm(forms.ModelForm):
    class Meta:
        model = ResidentialFreePatentApplication
        fields = ['project_name', 'proponent_name', 'project_location', 'eia_document']



class SurveyPlanApplicationForm(forms.ModelForm):
    class Meta:
        model = SurveyPlanApplication
        fields = ['fullname', 'community', 'contact', 'role']

