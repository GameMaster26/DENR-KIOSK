from django import forms
from .models import PTPRApplication,COVApplication,CLOApplication,ChainsawRegistration,TreeCuttingApplication,TreeCuttingPublicApplication,PrivateLandTimberPermit,SLUPApplication,FLAGApplication,LumberDealerApplication,SeedlingRequest,WPPPermit

class PTPRApplicationForm(forms.ModelForm):
    class Meta:
        model = PTPRApplication
        fields = [
            'fullname',
            'letter_request',
            'brgy_certificate',
            'land_title_or_tax_declaration',
            'spa_document',
            'valid_id_with_signature',
        ]


class COVApplicationForm(forms.ModelForm):
    class Meta:
        model = COVApplication
        fields = ['fullname', 'plantation', 'species', 'volume_cubic']


class CLOApplicationForm(forms.ModelForm):
    class Meta:
        model = CLOApplication
        fields = ['fullname', 'plantation', 'species', 'volume_cubic', 'destination']


class ChainsawRegistrationForm(forms.ModelForm):
    class Meta:
        model = ChainsawRegistration
        fields = [
            'fullname',
            'dti',
            'affidavit',
            'permit_sell',
            'purchase_receipt',
            'application_form',
            'chainsaw_specification',   
            'mayors_permit',
            'serial_no',
            'spa_document',
            'valid_id_with_signature',
        ]


class TreeCuttingApplicationForm(forms.ModelForm):
    class Meta:
        model = TreeCuttingApplication
        fields = ['fullname', 'plantation', 'species']


class TreeCuttingPublicForm(forms.ModelForm):
    class Meta:
        model = TreeCuttingPublicApplication
        fields = ['fullname', 'plantation', 'species', 'volume']


class PrivateLandTimberPermitForm(forms.ModelForm):
    class Meta:
        model = PrivateLandTimberPermit
        fields = ['fullname', 'lot_location', 'tree_type', 'volume']


class SLUPApplicationForm(forms.ModelForm):
    class Meta:
        model = SLUPApplication
        fields = ['fullname', 'location', 'project']


class FLAGApplicationForm(forms.ModelForm):
    class Meta:
        model = FLAGApplication
        fields = ['fullname', 'project_type', 'location']


class LumberDealerForm(forms.ModelForm):
    class Meta:
        model = LumberDealerApplication
        fields = ['fullname', 'plantation', 'species', 'volume']


class SeedlingRequestForm(forms.ModelForm):
    class Meta:
        model = SeedlingRequest
        fields = ['fullname', 'species', 'quantity']


class WPPPermitForm(forms.ModelForm):
    class Meta:
        model = WPPPermit
        fields = ['applicant', 'location', 'capacity']





