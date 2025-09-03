from django.db import models



class LandClassificationApplication(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    number_of_trees = models.PositiveIntegerField()
    reason_for_cutting = models.TextField()
    documents = models.FileField(upload_to='land_documents/', blank=True, null=True)

    STATUS_CHOICES = [
        ('under_verification', 'Under Verification'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='under_verification')
    remarks = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = "Land Classification Status"
        verbose_name_plural = "Land Classification Status"




class SurveyAuthorityApplication(models.Model):
    STATUS_CHOICES = [
        ('under_verification', 'Under Verification'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
        ('for_payment', 'For Payment'),
        ('on_process', 'On Process'),
        ('released', 'Released'),
    ]

    full_name = models.CharField(max_length=255, verbose_name='Full Name', blank=True, null=True)
    confirmation_of_affidavit_of_adjoining_owners = models.FileField(upload_to='survey_authority/affidavit_confirmation/', verbose_name='Confirmation of Affidavit of Adjoining Owners', blank=True, null=True)
    dar_certification = models.FileField(upload_to='survey_authority/dar_certification/', verbose_name='DAR Certification (as to no title issued)', blank=True, null=True)
    denr_and_certification = models.FileField(upload_to='survey_authority/denr_and_certification/', verbose_name='DENR A&D Certification (as to no title issued)', blank=True, null=True)
    technical_description = models.FileField(upload_to='survey_authority/technical_description/', verbose_name='Technical Description (DENR)', blank=True, null=True)
    brgy_clearance = models.FileField(upload_to='survey_authority/brgy_clearance/', verbose_name='Brgy. Clearance', blank=True, null=True)
    deed_of_conveyance = models.FileField(upload_to='survey_authority/deed_of_conveyance/', verbose_name='Deed of Conveyance (Deed of Sale/Tax Dec., Etc.)', blank=True, null=True)
    letter_request = models.FileField(upload_to='survey_authority/letter_request/', verbose_name='Letter Request', blank=True, null=True)
    sketch_plan = models.FileField(upload_to='survey_authority/sketch_plan/', verbose_name='Sketch Plan', blank=True, null=True)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='under_verification')
    remarks = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name}"
    

    class Meta:
        verbose_name = "Survey Authority"
        verbose_name_plural = "Survey Authority"


    


class AgriculturalApplication(models.Model):
    CONSTRUCTION_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('infrastructure', 'Public Infrastructure'),
        ('industrial', 'Industrial'),
    ]

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]

    reference_no = models.CharField(max_length=20, unique=True, editable=False)
    owner_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    construction_type = models.CharField(max_length=50, choices=CONSTRUCTION_TYPES)
    environmental_doc = models.FileField(upload_to='construction_docs/')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            last_id = AgriculturalApplication.objects.count() + 1
            self.reference_no = f"CA-{last_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.project_name}"
    
    class Meta:
        verbose_name= "Agricultural Free Patent"
        verbose_name_plural= "Agricultural Free Patent"
    



class ResidentialFreePatentApplication(models.Model):
    project_name = models.CharField(max_length=255)
    proponent_name = models.CharField(max_length=255)
    project_location = models.CharField(max_length=500)
    eia_document = models.FileField(upload_to='residential_free_patent/', blank=True, null=True)

    STATUS_CHOICES = [
        ('under_verification', 'Under Verification'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('for_inspection', 'For Inspection'),
        ('under_evaluation', 'Under Evaluation'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='under_verification')
    remarks = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.proponent_name} - {self.get_status_display()}"

    class Meta:
        ordering = ['-last_updated']
        verbose_name = "Residential Free Patent"
        verbose_name_plural = "Residential Free Patent"

        



class SurveyPlanApplication(models.Model):
    fullname = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    
    ROLE_CHOICES = [
        ('tree_volunteer', 'Tree Planting Volunteer'),
        ('donor', 'Donor'),
        ('event_organizer', 'Event Organizer'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('for_compliance', 'For Compliance'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.get_status_display()}"

    class Meta:
        ordering = ['-date_submitted']
        verbose_name = "Survey Plan"
        verbose_name_plural = "Survey Plan"


