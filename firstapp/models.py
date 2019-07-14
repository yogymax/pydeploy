from django.db import models
# Create your models here.



class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    pincode = models.IntegerField()

    class Meta:
        db_table = "Address_Info"



class Company(models.Model):
    companyWebsite = models.CharField(max_length=50)
    companyEmail = models.CharField(max_length=50)
    landline = models.IntegerField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE,related_name='comp')

    class Meta:
        db_table = "Company_Info"



class Employee(models.Model):
   employeeEmail = models.CharField(max_length = 50)
   employeename = models.CharField(max_length = 50)
   employeecontact = models.IntegerField()
   employeeage = models.IntegerField()
   empaddress = models.ManyToManyField(Address)
   company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='emp')

   class Meta:
      db_table = "Employee_Info"


