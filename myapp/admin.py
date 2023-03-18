from django.contrib import admin
from . models import Data, Predictions
from . forms import DataForm, PredictionsForm
from django.utils.html import format_html

# Register your models here.


class PredictionsAdmin(admin.ModelAdmin):
    list_filter = ['Predictions']
    list_display = ["software_name", "total_Op", "total_Opnd", "branchCount", "Predictions"]
    list_per_page = 10


admin.site.register(Predictions, PredictionsAdmin)

class DataAdmin(admin.ModelAdmin):
    list_filter = ['predictions']
    list_display = ["software_id", "license_key",
                    "hashvalue", "branchCount", "status", "_"]
    list_per_page = 10

    # Function to change the icon
    def _(self, obj):
        if obj.predictions == 'Genuine':
            return True
        elif obj.predictions == 'Bugs':
            return None
        else:
            return False
    _.boolean = True

    # # Function to color the text

    def status(self, obj):
        if obj.predictions == 'Genuine':
            color = '#28a745'
        elif obj.predictions == 'Bugs':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.predictions))

    status.allow_tags = True

admin.site.register(Data, DataAdmin)
