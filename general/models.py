from django.db import models
from datetime import datetime
from users.models import User

# Create your models here.

class Item(models.Model):
    dbName = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000, null=True)

class Purchase(models.Model):
    companyId = models.IntegerField() #Eg: Farm Id
    companyBranchId = models.IntegerField() #Eg: Farm Id
    itemTbId = models.IntegerField()
    itemId = models.IntegerField() #Eg fish batch Id
    unitCost = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.DecimalField(max_digits=20, decimal_places=2)
    totalcost = models.IntegerField()
    expensesDate = models.DateTimeField()
    paymentDetailsId = models.IntegerField(null=True)
    #vendorId =
    media = models.CharField(max_length=4000, null=True) #Eg [Recipt /// ghhg.jpg] [delivey /// deliveringstuff.jpg]
    comments = models.CharField(max_length=1000, null=True) # enter things like recipt or invoice number  / Items breakdown

class Vendor(models.Model):
    ownerTypes = {
        "Company": "Company",
        "User": "User",
        "Contacts": "Contacts",
        "Branch": "Branch"
    }
    ownerType = models.CharField(max_length=10, choices=ownerTypes)
    ownerId = models.IntegerField()
    creatorId = models.IntegerField()
    approverId = models.IntegerField()

class AML(models.Model):
    itemId = models.IntegerField()
    VendorId = models.IntegerField()
    companyId = models.IntegerField()
    branchId = models.IntegerField()
    addedById = models.IntegerField()
    approverId = models.IntegerField()
    status = models.IntegerField(null=True)
    comments = models.CharField(max_length=1000, null=True)

#******** ITEMS START ********
class FishFeed(models.Model):
    companyId = models.IntegerField() #Eg: Farm Id
    companyBranchId = models.IntegerField() #Eg: Farm Id
    sizes = {
        0.5: "0.5mm",
        0.8: "0.8mm",
        1.5: "1.5mm",
        2: "2mm",
        3: "3mm",
        4: "4mm",
        6: "6mm",
        9: "9mm",
    }
    size = models.DecimalField(max_digits=4, decimal_places=2, choices=sizes)
    brands = {
        "blc": "Blue Crown",
        "eco": "Eco Float",
        "cupen": "Cupen",
    }
    brand = models.CharField(max_length=10, choices=brands)
    quantity = models.DecimalField(max_digits=20, decimal_places=2)
    units = {
        "Kg": "Kg",
        "Ibs": "Pounds",
        "Bag": "Bag",
    }
    unit = models.CharField(max_length=5, choices=units)
    desc = models.CharField(max_length=500)
    comments = models.CharField(max_length=1000, null=True)


class DogFeedMaterial(models.Model):
    companyId = models.IntegerField() #Eg: Farm Id
    companyBranchId = models.IntegerField() #Eg: Farm Id
    type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    types = {
        "FI": "Fish_Intstines",
        "CI": "Chicken_Intestine",
    }
    type = models.CharField(max_length=5, choices=types)

#******** ITEMS END ********

class ItemBeneficiary(models.Model):
    itemNumber = models.IntegerField()
    beneficiaryNumber = models.IntegerField()
    comments = models.CharField(max_length=1000, null=True)

class ItemGroup(models.Model):
    itemNumber = models.IntegerField()
    itemParent = models.IntegerField()

class PaymentDetails(models.Model):
    PaymentMethodId =  models.IntegerField()
    purchaseId =  models.IntegerField()
    reciptNumber = models.CharField(max_length=100, null=True)
    dataCreated = models.DateTimeField()
    comments = models.CharField(max_length=1000, null=True)

class PaymentMethod(models.Model):
    ownerId = models.IntegerField()
    paymentTypes = {
        "BankTransfer": "BT",
        "Zelle": "Zelle",
        "Crypto": "Crypto",
        "Cash": "Cash"
    }
    paymentType = models.CharField(max_length=20, choices=paymentTypes)
    ownerTypes = {
        "Company": "Company",
        "User": "User",
        "Contacts": "Contacts",
        "Branch": "Branch"
    }
    ownerType = models.CharField(max_length=10, choices=ownerTypes)

class BankPaymentMethod(models.Model):
    PaymentMethodId = models.IntegerField()
    Fullname = models.CharField(max_length=1000)
    models.DecimalField(max_digits=25, decimal_places=10)
    accountNumber = models.IntegerField()
    bankName = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)

class ZellePaymentMethod(models.Model):
    PaymentMethodId = models.IntegerField()
    email_phone = models.CharField(max_length=1000)
    Fullname = models.CharField(max_length=1000)
    bankName = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)

class CyptoPaymentMethod(models.Model):
    PaymentMethodId = models.IntegerField()
    address = models.CharField(max_length=1000)
    network = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)

class Images(models.Model):
    tableName  = models.CharField(max_length=100)
    tableId = models.IntegerField()
    image = models.ImageField()
    dataCreated = models.DateTimeField(default=datetime.now)
    addedById = models.IntegerField()


class contacts(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    creatorId = models.IntegerField()
    approverId = models.IntegerField()

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    creatorId = models.IntegerField()
    approverId = models.IntegerField()
    Phone =  models.BigIntegerField()
    Email = models.EmailField(max_length=254)
    website = models.CharField(max_length=100)
    comments = models.CharField(max_length=1000)

class Staff(models.Model):
    userId = models.IntegerField(default=0)
    companyId = models.IntegerField()
    #workPhone = models.CharField(max_length=100, unique=True) #option too select same as that in profile // avoid duplicates
    #workEmail = models.EmailField(max_length=1000, null=True, unique=True) #option too select same as that in profile // avoid duplicates
    dataCreated = models.DateTimeField(default=datetime.now)
    joinedCompanyDate = models.DateTimeField(null=True) #only manager and higher with authority can add too this / only level 4 and above can edit wih permision from level 5
    comments = models.CharField(max_length=2000, null=True)
    addedById = models.IntegerField()
    approvedById = models.IntegerField()

class RelationshipLink(models.Model):
    ownerTypes = {
        "Company": "Company",
        "User": "User",
        "Contacts": "Contacts",
        "Branch": "Branch"
    }
    ownerType = models.CharField(max_length=10, choices=ownerTypes)
    ownerId = models.IntegerField()
    relationTypes = {
        "User": "User",
        "Contacts": "Contacts",
    }
    relationType = models.CharField(max_length=10, choices=relationTypes)
    relationId = models.IntegerField()
    relationDetails = models.CharField(max_length=1000)
    addedById = models.IntegerField()
    dateAddded = models.DateTimeField(default=datetime.now)
    approverId = models.IntegerField()
    comments = models.CharField(max_length=1000)


class Address(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipCode =  models.IntegerField()
    country = models.CharField(max_length=100)
    creatorId = models.IntegerField()
    approverId = models.IntegerField()
    Phone =  models.BigIntegerField()
    Email = models.EmailField(max_length=254)
    contactName = models.CharField(max_length=100)


class Authority(models.Model):
    tableName = models.CharField(max_length=100)
    companyId = models.IntegerField(null=True)
    requestedId = models.IntegerField()
    approverId = models.IntegerField()
    levels = [
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ]
    view = models.CharField( max_length=1, choices=levels, default=5,)
    add = models.CharField( max_length=1, choices=levels, default=5,)
    edit = models.CharField( max_length=1, choices=levels, default=5,)
    delete = models.CharField( max_length=1, choices=levels, default=5,)
    accept = models.CharField( max_length=1, choices=levels, default=5,)
    approve = models.CharField( max_length=1, choices=levels, default=5,)
    authorityGranted = models.DateTimeField(default=datetime.now)