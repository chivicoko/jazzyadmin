from django.contrib import admin
from django import forms
from .models import Profiler


class ProfilerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfilerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].help_text = 'New help text'

        class Meta:
            model = Profiler
            exclude = ('is_approved',)

class ProfilerFormAdmin(admin.ModelAdmin):
    form = ProfilerForm

admin.site.register(Profiler, ProfilerFormAdmin)



# class ProfilerAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'is_approved')
#     search_fields = ('first_name', 'last_name', 'email')
#     list_filter = ('is_approved',)

# class ProfilerAdminArea(admin.AdminSite):
#     site_header = 'Profiler Admin Area'
#     site_title = 'Profiler Admin Page'
#     index_title = "Profiler Panel"

# profiler_site = ProfilerAdminArea(name='ProfilerAdmin')

# profiler_site.register(Profiler, ProfilerAdmin)
# admin.site.register(Profiler, ProfilerAdmin)