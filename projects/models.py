
from django.db import models
from datetime import datetime    
from django.db.models.signals import post_save

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    creatorId =  models.IntegerField()
    contactName = models.CharField(max_length=100)
    contactPhone =  models.IntegerField()
    contactEmail = models.EmailField(max_length=254)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    status = models.IntegerField()
    Address = models.CharField(max_length=1000)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    zipCode =  models.IntegerField()
    comments = models.CharField(max_length=1000)

class contacts(models.Model):
    userId = models.IntegerField(null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    dateOfBirth = models.DateTimeField(null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    creatorId =  models.IntegerField(null=True)
    phoneOne =  models.IntegerField(null=True)
    phoneTwo =  models.IntegerField(null=True)
    emailOne = models.EmailField(max_length=254, null=True)
    emailTwo = models.EmailField(max_length=254, null=True)
    instagram = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    status = models.IntegerField(null=True)
    Address = models.CharField(max_length=1000, null=True)
    comments = models.CharField(max_length=1000, null=True)

#bankInfo
    #link by contacts id
#kinInfo
    #link by parent to child id


    
#branch of a company. such as a farm
class Project(models.Model):
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000, null=True)
    createdDate = models.DateField(default=datetime.now)
    creatorId = models.IntegerField()
    contactName = models.CharField(max_length=100, null=True)
    contactPhone =  models.BigIntegerField(null=True)
    contactEmail = models.EmailField(max_length=254)
    country = models.CharField(max_length=100, default='' , null=True)
    state = models.CharField(max_length=100, default='', null=True)
    zipCode = models.IntegerField(default='')
    fullsAddress = models.CharField(max_length=1000, default='', null=True)
    area = models.IntegerField(default=0, null=True)
    length = models.IntegerField(default=0, null=True)
    width = models.IntegerField(default=0, null=True)
    Status = models.IntegerField(default=1)
    comments = models.CharField(max_length=1000, null=True)
    website = models.CharField(max_length=200, null=True)
    instagram = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    tiktok = models.CharField(max_length=100, null=True)
    otherOnline = models.CharField(max_length=100, null=True)

    #def addToMyProjects(self):
        #project = MyProjects.objects.get(user=self)

class MyProjects(models.Model):
    userId = models.IntegerField()
    projectId = models.IntegerField()
    addedby_Id = models.IntegerField()
    #addedDate = models.DateField(datetime.now + datetime(days=1))
    addedDate = models.DateField(default=datetime.now)
    levels = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Ponds(models.Model):
    name = models.CharField(max_length=100)
    projectId = models.IntegerField()
    position_row = models.IntegerField()
    position_col = models.IntegerField()
    materialType = models.CharField(max_length=100)
    depth = models.IntegerField()
    lenght = models.IntegerField()
    width = models.IntegerField()

class stockSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    unitCost = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    totalcost = models.IntegerField()
    totalWeight = models.IntegerField()
    aveLength = models.IntegerField(null=True)
    dob = models.DateTimeField()
    purchaseDate = models.DateTimeField()
    PurchaseId = models.IntegerField()
    farmId = models.IntegerField()
    vendorId = models.IntegerField()
    #add image

class feeding(models.Model):
    pondId = models.IntegerField()
    feedDateTime = models.DateTimeField()
    quantity = models.IntegerField()
    reactions = {
        "H": "Hyper",
        "N": "Normal",
        "BE": "Barely Eating",
        "NE": "Not Eating"
    }
    reaction = models.CharField(max_length=2, choices=reactions)

    brands = [
        ('IH', 'INHOUSE'),
        ('ECO', 'ECO'),
        ('BC', 'BLUE CROWN'),
        ('FLOAT', 'FLOAT'),
        ('CUPPEN', 'CUPPEN'),
        ('ALAQUA', 'ALAQUA'),
        ('BSF_LARVE', 'BSF_LARVE'),
        ('OTHERS', 'OTHERS'),
    ]
    brand = models.CharField(
        max_length=10,
        choices=brands,
        default='active',
    )
    feedSize = models.TextChoices('0.5', '0.8', '1', '1.5', '2', '3', '4', '6', '9', 'others')
    comments = models.CharField(max_length=1000, null=True) 

class WaterChange(models.Model):
    pondId = models.IntegerField()
    eventDate = models.DateField()  
    depth = models.IntegerField()
    preWaterColor = models.CharField(max_length=100)
    preWaterCond = models.CharField(max_length=600)

class PondstoDoList(models.Model):
    pondId = models.IntegerField()
    farmId = models.IntegerField()
    pomdName = models.CharField(max_length=100, null=True)
    taskName = models.CharField(max_length=100, null=True)
    #Sorting = 1, 
    taskId = models.IntegerField()
    createDate = models.DateTimeField(default=datetime.now)
    dueDate = models.DateTimeField()  
    #1 to 5, 5 been most urgent 
    urgency = models.IntegerField()
    # 1 = completed, 2 = In progress, 3 = Not Started
    status = models.IntegerField()
    completeDate = models.DateTimeField(null=True)  
    requestorId = models.IntegerField()
    assignedToId = models.IntegerField(null=True)
    taskDetails = models.CharField(max_length=1000)

class Stocking(models.Model):
    pondId = models.IntegerField()
    toPondId = models.IntegerField()
    toVendorId = models.IntegerField(null=True)
    fromPondId = models.IntegerField(null=True)
    fromVendordId = models.IntegerField(null=True)
    waterLevel = models.IntegerField(null=True)
    #treated = models.BooleanField()
    addedimage = models.ImageField(upload_to="images", null=True)
    fishStage = models.TextChoices('Eggs', 'Fries', 'Fingerlings', 'Post_Fingerlings', 'Juvenie', 'Jumbo', 'drying_size', 'table_size', 'smoking_size', '1kg')
    type = models.CharField(max_length=100, null=True)
    averageWeight = models.IntegerField(null=True)
    totalWeight = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    recordDate = models.DateTimeField(default=datetime.now)
    fishId = models.IntegerField(null=True)
    leadByName = models.CharField(max_length=100, null=True)
    leadById = models.IntegerField(null=True)
    assittedByName = models.CharField(max_length=100, null=True)
    assittedById = models.IntegerField(null=True)
    followupTask = models.CharField(max_length=100, null=True)
    followupTaskDueDate = models.DateTimeField(null=True)
    standing = models.TextChoices('Completed', 'Not Started', 'In Progress', 'Suspended', 'Paused', 'Cancled')
    status = models.CharField(max_length=100, null=True)
    addedQuantity = models.IntegerField(null=True)
    addedSize = models.IntegerField(null=True)
    addedWeight = models.IntegerField(null=True)
    removed = models.IntegerField(null=True)
    removedSize = models.IntegerField(null=True)
    removedWeight = models.IntegerField(null=True)
    comments = models.CharField(max_length=1000, null=True)

class ActivitiesImages(models.Model):
    activityId = models.IntegerField()
    pondId = models.IntegerField()
    projectId = models.IntegerField()
    title = models.CharField(max_length=100, null=True)
    src = models.ImageField(upload_to="images", null=True)
    comments = models.CharField(max_length=1000, null=True)
    uploadDate = models.DateTimeField(default=datetime.now)

class followupTask(models.Model):
    activityId = models.IntegerField()
    notificationId = models.IntegerField()

class activityNames(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    creatorId = models.IntegerField()
    #dateCreated = models.DateTimeField(default=datetime.now)
    
class followupTaskSuggestion(models.Model):
    activityNamesId = models.IntegerField()
    followupNameId = models.IntegerField()   

class Sales(models.Model):
    pondId = models.IntegerField()
    projectId = models.IntegerField()
    dateSold = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField(null=True)
    weight = models.IntegerField()
    unitPrice = models.IntegerField()
    fishId = models.IntegerField()
    buyerId = models.IntegerField()
    paid = models.IntegerField()
    paymentBal = models.IntegerField()
    status = models.IntegerField()
    comments = models.CharField(max_length=1000, null=True)

class employee(models.Model):
    contactId =  models.IntegerField(default=0)
    farmId = models.IntegerField()
    position = models.CharField(max_length=100)
    employmentDate = models.DateTimeField(null=True)
    positionDate = models.DateTimeField(null=True)

    #changedPosition, #currentPosition, #fired, #resigned
    status = models.IntegerField(default=1)

    comments = models.CharField(max_length=1000, null=True)



class Staff(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    managerId = models.IntegerField(null=True)
    dateOfBirth = models.DateTimeField(null=True)
    userId = models.IntegerField(null=True)
    farmId = models.IntegerField()
    phoneMain = models.CharField(max_length=100)
    phoneSecondary = models.CharField(max_length=100)
    email = models.CharField(max_length=1000, null=True)
    homeAddress = models.CharField(max_length=1000, null=True)
    relationId = models.IntegerField(null=True)
    dataCreated = models.DateTimeField(default=datetime.now)
    employmentDate = models.DateTimeField(null=True)
    status = models.IntegerField(default=1)
    comments = models.CharField(max_length=1000, null=True)

class Expense(models.Model):
    farmId = models.IntegerField()
    itemDescription = models.CharField(max_length=2000) # per Item : (quantity-unitCost-transportation(going)-deliveryCost)
    unitCost = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    totalcost = models.IntegerField()
    expensesDate = models.DateTimeField()
    paymentToId = models.IntegerField(null=True)
    shopId = models.IntegerField(null=True)
    comments = models.CharField(max_length=1000, null=True)

class purchaseDelivery(models.Model):
    expenseId = models.IntegerField()
    deliveryCost = models.IntegerField()
    deliveryStatus = models.IntegerField() #1: Completly delivered, 2:partialy delivered, 3:Delvered
    shipperId = models.IntegerField(null=True)
    mainHandler = models.CharField(max_length=1000) #could be driver, deliver person etc... / fullname - contact - position
    secondaryHandler = models.CharField(max_length=1000, null=True) #could be driver, deliver person etc... / fullname - contact - position
    shippingLocation = models.CharField(max_length=1000, null=True)
    deliveryPickupLocation = models.CharField(max_length=1000)
    estimatedShipTime = models.DateTimeField(max_length=1000)
    estimatedDeliveryTime = models.DateTimeField()
    receivierStaffId = models.IntegerField()

class expenseItemTableLink (models.Model):
    expenseId = models.IntegerField()
    itemId = models.IntegerField()
    #itemTableName = models.CharField(max_length=1000)
    quantityPercentage = models.IntegerField()
    costPercentage = models.IntegerField()
    deliveryCostPercentage = models.IntegerField()

class Items(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000, null=True)

class ItemParent(models.Model):
    itemId = models.IntegerField(null=True)
    parentId = models.IntegerField(null=True)

class ExpensesDisbursement(models.Model):
    expenseId = models.IntegerField()
    sharePecentage = models.IntegerField()
    allocatedToId = models.IntegerField()
    ItemsGroupId = models.IntegerField()
    cost = models.IntegerField()
