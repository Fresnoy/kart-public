# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

from django.contrib.auth.models import User
from people.models import FresnoyProfile, Staff, Artist


def arg_to_unicode(bytestring):
    unicode_string = bytestring
    return unicode_string


class Command(BaseCommand):
    help = 'Create staff user like "Andy" "Wharhol" '

    def add_arguments(self, parser):
        parser.add_argument("firstname", type=arg_to_unicode, help="Set fist name user")
        parser.add_argument("lastname", type=arg_to_unicode, help="Set last name user")

    def handle(self, *args, **options):
        first_name = options["firstname"].strip().title()
        last_name = options["lastname"].strip().title()

        print("firstname: {0}".format(first_name))
        print("lastname: {0}".format(last_name))
        name = first_name + " " + last_name
        username = slugify(first_name.lower() + " " + last_name.lower())
        # init values
        user = False
        created = False
        # maybe is an artist name
        try:
            artist = Artist.objects.get(nickname__icontains=name)
            response = input(
                "It seems to be an artist name: {}\n"
                "from user: {}\n"
                "Do you want to continue with this user ? (yes or not)".format(
                    artist, artist.user
                )
            )
            if "y" in response:
                user = artist.user
        except Artist.DoesNotExist:
            pass
        # try to get USER with first name and lastname
        # cause username: mmouse can be Mickey Mouse OR Minnie Mouse
        if not user:
            try:
                user = User.objects.get(first_name=first_name, last_name=last_name)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=get_random_string(length=8),
                )
                FresnoyProfile.objects.create(user=user)
                created = True
                print("User {0} created".format(user))
            if not created:
                print("User {0} already created".format(user))
            # try to create STAFF
            staff = False
            created = False
        try:
            staff = Staff.objects.get(user=user)
        except Staff.DoesNotExist:
            staff = Staff(user=user)
            staff.save()
            created = True

        if created:
            print("Staff {0} created".format(staff))
        else:
            print("Staff {0} already created".format(staff))
