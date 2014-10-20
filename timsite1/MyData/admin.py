from django.contrib import admin
from MyData.models import DataList
from MyData.models import StringParameter, IntegerParameter
from MyData.models import BooleanParameter, DecimalParameter, UnitParameter

# Register your models here.

class StringParameterInline(admin.TabularInline):
	model = StringParameter
	extra = 1

class IntegerParameterInline(admin.TabularInline):
	model = IntegerParameter
	extra = 1
	
class BooleanParameterInline(admin.TabularInline):
	model = BooleanParameter
	extra = 1
	
class DecimalParameterInline(admin.TabularInline):
	model = DecimalParameter
	extra = 1
		
class UnitParameterInline(admin.TabularInline):
	model = UnitParameter
	extra = 1
	
class DataListInline(admin.TabularInline):
	model = DataList
	extra = 1	
	
class StringParameterAdmin(admin.ModelAdmin):
	list_display = ('name','value', 'myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
class IntegerParameterAdmin(admin.ModelAdmin):
	list_display = ('name','value', 'myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
class BooleanParameterAdmin(admin.ModelAdmin):
	list_display = ('name','value', 'myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
class DecimalParameterAdmin(admin.ModelAdmin):
	list_display = ('name','value', 'myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
class UnitParameterAdmin(admin.ModelAdmin):
	list_display = ('name', 'myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
class DatalistAdmin(admin.ModelAdmin):
	fieldsets = [
		('Node information', {'fields': ['name','myParent']}),
	]
	list_display = ('name','myParent')
	list_filter = ['myParent']
	search_fields = ['name']
	
	inlines = [StringParameterInline]
	inlines.append(IntegerParameterInline)
	inlines.append(BooleanParameterInline)
	inlines.append(DecimalParameterInline)
	inlines.append(UnitParameterInline)
	inlines.append(DataListInline)

admin.site.register(DataList,DatalistAdmin)
admin.site.register(StringParameter, StringParameterAdmin)
admin.site.register(IntegerParameter, IntegerParameterAdmin)
admin.site.register(BooleanParameter, BooleanParameterAdmin)
admin.site.register(DecimalParameter, DecimalParameterAdmin)
admin.site.register(UnitParameter, UnitParameterAdmin)