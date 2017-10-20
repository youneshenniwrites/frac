'''
We want to ensure that the slug field will be
generated automaticall and in a unique way
for every single post.
'''

import random
import string

from django.utils.text import slugify

# avoids conflict with the create url in urls.py
DO_NOT_USE = ['create']


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    '''
    Returns a random string of characters
    '''

    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    '''
    Uses the above function to generate a unique url
    slug for our post instance.
    Assumes that the model has a slug attribute.
    '''

    if new_slug is not None:
        slug = new_slug
    elif instance.title is not None:
        # build a title slug
        slug = slugify(instance.title)

    if not instance.title:
        # build a random slug
        titless_slug = random_string_generator(size=8)
        slug = slugify(titless_slug)

    if slug in DO_NOT_USE:
        new_slug = '{slug}-{randstr}'.format(
                                        slug=slug,
                                        randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{randstr}'.format(
                                        slug=slug,
                                        randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
