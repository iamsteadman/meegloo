#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class Upload(models.Model):
	guid = models.CharField(max_length = 36, unique = True)
	filename = models.CharField(max_length = 255)
	
	def __unicode__(self):
		return self.filename