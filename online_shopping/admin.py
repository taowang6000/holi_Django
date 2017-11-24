from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Item, UserRole, UserAccount, CheckoutOrder, Role, PasswordResetToken, SpringSession, SpringSessionAttributes 

# Register your models here.
admin.site.register(Item)

#class SpringSessionAttributesInline(admin.StackedInline):
#    model = SpringSessionAttributes
#    extra = 0

class UserRoleInline(NestedStackedInline):
    model = UserRole
    extra = 0 

class ItemInline(NestedStackedInline):
    model = Item
    extra = 0 

class CheckoutOrderInline(NestedStackedInline):
    model = CheckoutOrder
    extra = 0
    inlines = [ItemInline]
class PasswordResetTokenInline(NestedStackedInline):
    model = PasswordResetToken
    extra = 0 
class UserAccountAdmin(NestedModelAdmin):
    inlines = [CheckoutOrderInline, UserRoleInline, PasswordResetTokenInline]
    search_fields = ['user_name']
class CheckoutOrderAdmin(NestedModelAdmin):
    inlines = [ItemInline]
class RoleAdmin(NestedModelAdmin):
    inlines = [UserRoleInline]
#class SpringSessionAdmin(admin.ModelAdmin):
#    inlines = [SpringSessionAttributesInline]

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(CheckoutOrder, CheckoutOrderAdmin)
admin.site.register(Role, RoleAdmin)
#admin.site.register(SpringSession, SpringSessionAdmin)
