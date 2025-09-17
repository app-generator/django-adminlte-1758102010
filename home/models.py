# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pos(models.Model):

    #__Pos_FIELDS__
    inv = models.CharField(max_length=255, null=True, blank=True)
    tg_inv = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cust = models.CharField(max_length=255, null=True, blank=True)
    konter = models.CharField(max_length=255, null=True, blank=True)
    ket = models.TextField(max_length=255, null=True, blank=True)
    inuser = models.CharField(max_length=255, null=True, blank=True)
    intime = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Pos_FIELDS__END

    class Meta:
        verbose_name        = _("Pos")
        verbose_name_plural = _("Pos")


class Dpos(models.Model):

    #__Dpos_FIELDS__
    no_kw = models.CharField(max_length=255, null=True, blank=True)
    warna = models.CharField(max_length=255, null=True, blank=True)
    hgj = models.IntegerField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    fkey = models.ForeignKey(Pos, on_delete=models.CASCADE)

    #__Dpos_FIELDS__END

    class Meta:
        verbose_name        = _("Dpos")
        verbose_name_plural = _("Dpos")



#__MODELS__END
