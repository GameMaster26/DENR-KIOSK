from django.db import models
from django.utils import timezone



class PTPRApplication(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Full Name",blank=False)

    letter_request = models.FileField(upload_to='ptpr/letter_requests/',verbose_name="Letter Request",blank=True,null=True)
    brgy_certificate = models.FileField(upload_to='ptpr/brgy_certificates/',verbose_name="Brgy. Certificate",blank=True,null=True)
    land_title_or_tax_declaration = models.FileField(upload_to='ptpr/land_titles/',verbose_name="Land Title or Tax Declaration",blank=True,null=True)
    spa_document = models.FileField(upload_to='ptpr/spa_documents/',verbose_name="SPA Document",blank=True,null=True)
    valid_id_with_signature = models.FileField(upload_to='ptpr/valid_ids/',verbose_name="Valid ID with Signature",blank=True,null=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = "Private Tree Plantation"
        verbose_name_plural = "Private Tree Plantation"
    

class COVApplication(models.Model):
    fullname = models.CharField(max_length=255)
    plantation = models.CharField(max_length=500)
    species = models.CharField(max_length=255)
    volume_cubic = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = COVApplication.objects.filter(reference_no__startswith=f"COV-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"COV-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name ="COV – Tree Transport"
        verbose_name_plural ="COV – Tree Transport"
    

class CLOApplication(models.Model):
    fullname = models.CharField(max_length=255)
    plantation = models.CharField(max_length=500)
    species = models.CharField(max_length=255)
    volume_cubic = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    destination = models.CharField(max_length=255)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = CLOApplication.objects.filter(reference_no__startswith=f"CLO-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"CLO-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    

    class Meta:
        verbose_name = "Lumber Origin(CLO)"
        verbose_name_plural = "Lumber Origin(CLO)"
    

class ChainsawRegistration(models.Model):
    fullname = models.CharField(max_length=255)
    
    dti = models.FileField(upload_to='chainsaw_registration/dti/',verbose_name="Business Name Registration(DTI)",blank=True,null=True)
    affidavit = models.FileField(upload_to='chainsaw_registration/affidavit/',verbose_name="Affidavit of Ownership(Atty.)",blank=True,null=True)
    permit_sell = models.FileField(upload_to='chainsaw_registration/permit_sell/',verbose_name="Permit to Sell",blank=True,null=True)
    purchase_receipt = models.FileField(upload_to='chainsaw_registration/purchase_receipt/',verbose_name="Purchase of Chainsaw Official Receipt",blank=True,null=True)
    application_form = models.FileField(upload_to='chainsaw_registration/application_form/',verbose_name="Application Form from DENR",blank=True,null=True)
    chainsaw_specification = models.FileField(upload_to='chainsaw_registration/chainsaw_specification/',verbose_name="Chainsaw Specification from DENR",blank=True,null=True)
    mayors_permit = models.FileField(upload_to='chainsaw_registration/mayors_permit/',verbose_name="Mayor's Permit",blank=True,null=True)
    serial_no = models.FileField(upload_to='chainsaw_registration/serial_no/',verbose_name="Stencil of Serial No.",blank=True,null=True)
    spa_document = models.FileField(upload_to='chainsaw_registration/dti/',verbose_name="SPA Document",blank=True,null=True)
    valid_id_with_signature = models.FileField(upload_to='chainsaw_registration/dti//',verbose_name="Valid ID with Signature",blank=True,null=True)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = ChainsawRegistration.objects.filter(reference_no__startswith=f"CS-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"CS-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    

    class Meta:
        verbose_name = "Chainsaw Registration"
        verbose_name_plural = "Chainsaw Registration"
    

class TreeCuttingApplication(models.Model):
    fullname = models.CharField(max_length=255)
    plantation = models.CharField(max_length=500)  # Source of Lumber
    species = models.CharField(max_length=255)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = TreeCuttingApplication.objects.filter(reference_no__startswith=f"TCLO-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"TCLO-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    

    class Meta:
        verbose_name = "Tree Cutting (National)"
        verbose_name_plural = "Tree Cutting (National)"
    

class TreeCuttingPublicApplication(models.Model):
    fullname = models.CharField(max_length=255)
    plantation = models.CharField(max_length=500)  # Source of Lumber / Facility
    species = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=6, decimal_places=2, help_text="Volume in cubic meters")

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')

    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = TreeCuttingPublicApplication.objects.filter(reference_no__startswith=f"TCP-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"TCP-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Tree Cutting (Public)"
        verbose_name_plural = "Tree Cutting (Public)"
    

class PrivateLandTimberPermit(models.Model):
    fullname = models.CharField(max_length=255)
    lot_location = models.CharField(max_length=500)
    tree_type = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=6, decimal_places=2, help_text="Volume in cubic meters")

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = PrivateLandTimberPermit.objects.filter(reference_no__startswith=f"LOP-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"LOP-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Private Land Timber"
        verbose_name_plural = "Private Land Timber"
    

class SLUPApplication(models.Model):
    fullname = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    project = models.CharField(max_length=255)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = SLUPApplication.objects.filter(reference_no__startswith=f"SLUP-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"SLUP-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Special Land Use Permit"
        verbose_name_plural = "Special Land Use Permit"
    

class FLAGApplication(models.Model):
    fullname = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    location = models.CharField(max_length=500)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = FLAGApplication.objects.filter(reference_no__startswith=f"FLAG-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"FLAG-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Forest Land Use Agreement"
        verbose_name_plural = "Forest Land Use Agreement"
    

class LumberDealerApplication(models.Model):
    fullname = models.CharField(max_length=255)
    plantation = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    volume = models.DecimalField(max_digits=6, decimal_places=2)

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = LumberDealerApplication.objects.filter(reference_no__startswith=f"LDRC-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"LDRC-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Lumber Dealer"
        verbose_name_plural = "Lumber Dealer"
    

class SeedlingRequest(models.Model):
    fullname = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)

    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = SeedlingRequest.objects.filter(reference_no__startswith=f"SR-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"SR-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.fullname}"
    
    class Meta:
        verbose_name = "Seedling Request"
        verbose_name_plural = "Seedling Request"


class WPPPermit(models.Model):
    applicant = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(help_text="Capacity in m³/year")

    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('disapproved', 'Disapproved'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, unique=True, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference_no:
            year = timezone.now().year
            last = WPPPermit.objects.filter(reference_no__startswith=f"WPP-{year}").order_by('-id').first()
            num = 1 if not last else last.id + 1
            self.reference_no = f"WPP-{year}-{num:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.applicant}"

    class Meta:
        verbose_name = "Wood Processing Plant Permit"
        verbose_name_plural = "Wood Processing Plant Permit"
    























