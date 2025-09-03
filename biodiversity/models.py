# biodiversity/models.py
from django.db import models
from django.core.validators import MinValueValidator



class WildlifeRegistration(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)
    
    CULTURAL_TYPE_CHOICES = [
        ('ecotourism', 'Ecotourism Visit / Site Access'),
        ('environmental-education', 'Environmental Education Request'),
        ('cultural-heritage', 'Cultural Heritage or Indigenous Knowledge Access'),
        ('research', 'Academic or Cultural Research'),
        ('spiritual', 'Spiritual or Traditional Ritual'),
    ]
    cultural_type = models.CharField(max_length=50, choices=CULTURAL_TYPE_CHOICES)

    
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.full_name} ({self.cultural_type})"
    
    class Meta:
        verbose_name = "Wildlife Registration"
        verbose_name_plural = "Wildlife Registration"



class WildlifeFarmPermit(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)

    HABITAT_TYPE_CHOICES = [
        ('restoration', 'Habitat Restoration Assistance'),
        ('native-trees', 'Native Tree Planting Support'),
        ('wildlife-corridor', 'Wildlife Corridor Maintenance'),
        ('species-monitoring', 'Habitat Monitoring for Key Species'),
        ('protected-zone', 'Support for Protected Habitat Zone'),
    ]
    habitat_type = models.CharField(max_length=50, choices=HABITAT_TYPE_CHOICES)

    date_submitted = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.habitat_type})"
    
    class Meta:
        verbose_name = "Wildlife Farm Permit"
        verbose_name_plural = "Wildlife Farm Permit"



class LocalTransportPermit(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)

    PROVISION_TYPE_CHOICES = [
        ('seedlings', 'Seedling Distribution'),
        ('water', 'Water Extraction Access'),
        ('forest-products', 'Forest Product Collection'),
        ('wildlife-collection', 'Wildlife/Plant Collection (for research)'),
        ('bioprospecting', 'Bioprospecting Permit'),
    ]
    provision_type = models.CharField(max_length=50, choices=PROVISION_TYPE_CHOICES)

    date_submitted = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.provision_type})"


    class Meta:
        verbose_name = "Local Transport Permit"
        verbose_name_plural = "Local Transport Permit"




class GratuitousPermitMOA(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    regulation_type = models.CharField(max_length=100, choices=[
        ('tree-cutting', 'Tree Cutting or Earth-balling Permit'),
        ('pollution-control', 'Wastewater or Emission Control'),
        ('watershed-protection', 'Watershed Protection'),
        ('pest-management', 'Pest Management Support'),
        ('climate-buffer', 'Climate Buffer Zoning'),
    ])


    status = models.CharField(max_length=50, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ])
    remarks = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.regulation_type}"
    
    class Meta:
        verbose_name = "Gratuitous Permit"
        verbose_name_plural = "Gratuitous Permit"




class SpecialLocalTransportPermit(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)

    ADAPTATION_TYPE_CHOICES = [
        ('climate-adaptation', 'Climate Adaptation Support'),
        ('disaster-recovery', 'Ecosystem-based Disaster Recovery'),
        ('mangrove-restoration', 'Mangrove or Coastal Buffer Zone Restoration'),
        ('community-resilience', 'Community-Based Resilience Program'),
    ]
    adaptation_type = models.CharField(max_length=50, choices=ADAPTATION_TYPE_CHOICES)

    date_submitted = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.adaptation_type})"
    
    class Meta:
        verbose_name = "Special Local Transport Permit"
        verbose_name_plural = "Special Local Transport Permit"
    


class MarineResearchClearance(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    contact_number = models.CharField(max_length=20)

    SUPPORT_TYPE_CHOICES = [
        ('soil-study', 'Soil Formation Study / Request'),
        ('biodiversity-monitoring', 'Biodiversity or Ecosystem Monitoring'),
        ('research', 'Academic Research on Ecological Processes'),
        ('habitat-mapping', 'Habitat Mapping or Nutrient Survey'),
    ]
    support_type = models.CharField(max_length=50, choices=SUPPORT_TYPE_CHOICES)

    date_submitted = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.support_type})"
    
    class Meta:
        verbose_name = "Marine Research Clearance"
        verbose_name_plural = "Marine Research Clearance"