from django.contrib import admin

# Register your models here.
from .models import Item, Purchase, Vendor, AML, FishFeed, DogFeedMaterial, ItemBeneficiary, ItemGroup, PaymentDetails, PaymentMethod, contacts, Company, RelationshipLink, Address, Authority

class ItemAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['dbName', 'desc', 'comments']
admin.site.register(Item, ItemAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['companyBranchId', 'itemTbId', 'itemId']
admin.site.register(Purchase, PurchaseAdmin)

class VendorAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['ownerType', 'ownerId', 'creatorId', 'approverId']
admin.site.register(Vendor, VendorAdmin)

class AMLAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['itemId', 'VendorId', 'companyId', 'branchId']
admin.site.register(AML, AMLAdmin)

class FishFeedAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'brand', 'weight', 'desc']
admin.site.register(FishFeed, FishFeedAdmin)

class DogFeedMaterialAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['id', 'type', 'quantity', 'type',]
admin.site.register(DogFeedMaterial, DogFeedMaterialAdmin)

class ItemBeneficiaryAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['id', 'itemNumber', 'beneficiaryNumber', 'comments']
admin.site.register(ItemBeneficiary, ItemBeneficiaryAdmin)

class ItemGroupAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['id', 'itemNumber', 'itemParent']
admin.site.register(ItemGroup, ItemGroupAdmin)


class PaymentDetailsAdmin(admin.ModelAdmin):
    #list_editable = ['dbName']
    list_display = ['id', 'PaymentMethodId', 'purchaseId', 'reciptNumber', 'dataCreated']
admin.site.register(PaymentDetails, PaymentDetailsAdmin)


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['id', 'ownerId', 'paymentType', 'ownerType']
admin.site.register(PaymentMethod, PaymentMethodAdmin)

class contactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstName']
admin.site.register(contacts, contactsAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'website', 'comments']
admin.site.register(Company, CompanyAdmin)

class RelationshipLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'ownerType', 'ownerId', 'relationType', 'relationId']
admin.site.register(RelationshipLink, RelationshipLinkAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'street', 'city', 'contactName']
admin.site.register(Address, AddressAdmin)

class AuthorityAdmin(admin.ModelAdmin):
    list_display = ['id', 'tableName', 'view', 'add', 'edit',
                    'delete','accept', 'approve'
                ]
admin.site.register(Authority, AuthorityAdmin)