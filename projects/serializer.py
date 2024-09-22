from rest_framework import serializers
from .models import Project, MyProjects, Company, Ponds, Stocking, PondstoDoList, Sales, activityNames, stockSource
from .models import Staff


class ProjectsTemplates(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ( 'id','name', 'summary', 'fullsAddress', 'zipCode', 'creatorId')

class StocSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stocking
        fields = ('toPondId')
         #{"farmId":6,"toPondId":9,"fromPondId":8,"fishStage":"Fingerlings","fishId":2,"addedQuantity":66,"addedWeight":666,"comments":"ghgtfh"}:    


class MyProjectsTemplates(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ( 'id', 'projectId', 'levels', 'addedby_Id', 'position')
        
        

class CompanySerializersGet(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ( 
            'id', 'name', 'creatorId', 
            'contactName', 'contactEmail', 'Address', 'status', 
            )
        


class CompanySerializersPost(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ( 
            'name',
            'contactName', 
            'contactPhone', 
            'contactEmail', 
            'instagram', 
            'facebook',
            'Address',
            'City',
            'State',
            'Country',
            'zipCode',
            'comments',
            )
        

class PondSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ponds
        fields = ( 
            'id','name', 'projectId', 'position_row', 'width',
            'position_col', 'materialType', 'depth', 'lenght', 
            )
        


# class StockingSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Stocking
#         fields = ( 
#             'id','pondId','toPondId','waterLevel', 'type', 'totalWeight', 'quantity',
#             'recordDate', 'fishId', 'leadByName', 'followupTask', 'status', 'removed', 'addedQuantity', 'addedWeight','comments'
#             )

class StockingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stocking
        fields = ( 
            'toPondId','toPondId','fromPondId','pondId',
            'fishId', 'addedQuantity', 'addedWeight', 'comments'
            )
             
 #{"farmId":6,"toPondId":9,"fromPondId":8,"fishStage":"Fingerlings","fishId":2,"addedQuantity":66,"addedWeight":666,"comments":"ghgtfh"}:    

class GetStockingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stocking
        fields = ( 
            'pondId',
            'fishStage',
            'addedQuantity',
            'addedWeight',
            'fishId',
        )         


class PondstoDoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = PondstoDoList
        fields = ( 
            'id','pondId', 'taskId',
            'dueDate', 'urgency', 'status', 'requestorId', 'taskDetails', 'farmId'
            )
        
class SaleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ( 
            'id','pondId','dateSold', 'amount', 'unitPrice', 'fishId', 'weight',
            'buyerId', 'paid', 'status', 'paymentBal', 'comments', 'projectId'
            )
        
class activityNamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = activityNames
        fields = ( 
            'name',
            'description'
            )
class createActivityNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = activityNames
        fields = ( 
            'name',
            'description',
            'creatorId'
            )    

class activityNameIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = activityNames
        fields = ( 
            'name',
            'description',
            'creatorId',
            'id'
            ) 


class stockSourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = stockSource
        fields = ( 
            'name',
            'description',
            'PurchaseId',
            'farmId',
            'vendorId',
            'id'
        )         
   


class staffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ( 
            'id',
            'firstName',
            'lastName',
            'position',
            'managerId',
            'dateOfBirth',
            'userId',
            'farmId',
            'phoneMain',
            'phoneSecondary',
            'email',
            'homeAddress',
            'dataCreated',
            'employmentDate',
            'comments',
            'status'
        )   