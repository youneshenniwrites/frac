from django.contrib import admin

from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    '''
    customizing the way infos about
    our model post are displayed in the
    Django admin
    '''

    list_display = (
                    'id',
                    'user',
                    'title',
                    'slug',
                    #'content',
                    'updated',
                    'created'
                    )

    list_display_links = ('user', 'updated')
    list_editable = ['title'] #, 'content']
    list_filter = ('updated', 'created')

    '''
    admin should be able to retreive a user post
    by using one the following indicators
    '''
    search_fields = [
                    'user__username',
                    'user__first_name',
                    'user__last_name',
                    'slug',
                    'title',
                    'content'
                    ]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
