from django.contrib import admin
from baloons.models import Airline, Pilot, Flight, Baloon, User


class PilotAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name', 'surname', 'year_of_birth', 'get_level_of_experience']
    search_fields = ['name', 'surname']
    list_editable = ['year_of_birth']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['total_hours_of_flight', 'year_of_birth']
    fields = ['name','surname', 'year_of_birth',  'created_at', 'updated_at']


    @admin.display(
        description="Level of experience"
    )
    def get_level_of_experience(request, self):
        return 'dummy value'


class FlightAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['code', 'user', 'photo', 'pilot', 'airline']
    readonly_fields = ['user']
    fieldsets = [
        (
            'General',
            {
                "fields": ['code', 'user', 'photo', 'pilot'],
            },
        ),
        (
            "Airport related",
            {
                "fields": ["airport_from", "airport_to"],
            },
        ),
    ]
    #
    # def has_view_permission(self, request, obj=None):
    #     return False

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    # #
    # def has_delete_permission(self, request, obj=None):
    #     request.user.is_superuser

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user

        super(FlightAdmin, self).save_model(request, obj, form, change)


class BaloonAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_filter = ['type',]


admin.site.register(Pilot, PilotAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Baloon, BaloonAdmin)


