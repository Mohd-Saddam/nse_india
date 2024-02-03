from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import Index, DailyPrice

class DailyPriceResource(resources.ModelResource):
    index = fields.Field(column_name='index', attribute='index', widget=ForeignKeyWidget(Index, 'name'))

    class Meta:
        model = DailyPrice
        fields = ('id', 'index', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover', 'created_at')
        import_id_fields = ['id']

class DailyPriceAdmin(ImportExportModelAdmin):
    resource_class = DailyPriceResource
    list_display = ('index', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover', 'created_at')
    search_fields = ['index__name', 'date']

    # Enable export action in admin
    actions = ['export_as_csv']

    # Custom export action to handle date format
    def export_as_csv(self, request, queryset):
        resource = self.get_export_resource()
        response = self.get_export_response(request, resource.export(queryset))
        return response

    export_as_csv.short_description = "Export selected as CSV"

admin.site.register(Index, ImportExportModelAdmin)
admin.site.register(DailyPrice, DailyPriceAdmin)
