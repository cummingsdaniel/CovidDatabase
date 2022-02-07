import csv, sqlite3
from sqlite3 import Error
from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin
'''
Daniel Cummings
CST8333 Programming Language Research Project
'''
# MALE, FEMALE = range(2)
# GENDER = (
#     (MALE, 'MALE'),
#     (FEMALE, 'FEMALE')
# )
#
# CHINESE, SPANISH, ENGLISH, FRENCH, HINDI, ARABIC, RUSSIAN = range(7)
# LANGUAGES = (
#     (CHINESE, 'CHINESE'),
#     (SPANISH, 'SPANISH'),
#     (ENGLISH, 'ENGLISH'),
#     (FRENCH, 'FRENCH'),
#     (HINDI, 'HINDI'),
#     (ARABIC, 'ARABIC'),
#     (RUSSIAN, 'RUSSIAN'),
# )
#
# class Student(models.Model):
#     full_name = models.CharField('Full Name', max_length=50)
#     gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
#     language = models.PositiveSmallIntegerField('Language', choices=LANGUAGES, default=ENGLISH)
#     grades = models.CharField('Grades', max_length=2)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = ('Student')
# ALBERTA, BRITISH_COLUMBIA, CANADA, MANITOBA, NEW_BRUNSWICK, NEWFOUNDLAND_AND_LABRADOR, NORTHWEST_TERRITORIES, NOVA_SCOTIA, NUNAVUT, ONTARIO, PRINCE_EDWARD_ISLAND, QUEBEC, REPATRIATED_TRAVELLERS, SASKATCHEWAN, YUKON = range(15)
# PRNAME = ((ALBERTA,'ALBERTA'),
#           (BRITISH_COLUMBIA),
#           (CANADA, 'CANADA'),
#           (MANITOBA, 'MANITOBA'),
#           (NEW_BRUNSWICK, 'NEW_BRUNSWICK'),
#           (NEWFOUNDLAND_AND_LABRADOR, 'NEWFOUNDLAND_AND_LABRADOR'),
#           (NORTHWEST_TERRITORIES, 'NORTHWEST_TERRITORIES'),
#           (NOVA_SCOTIA, 'NOVA_SCOTIA'),
#           (NUNAVUT, 'NUNAVUT'),
#           (ONTARIO, 'ONTARIO'),
#           (PRINCE_EDWARD_ISLAND, 'PRINCE_EDWARD_ISLAND'),
#           (QUEBEC, 'QUEBEC'),
#           (REPATRIATED_TRAVELLERS, 'REPATRIATED_TRAVELLERS'),
#           (SASKATCHEWAN, 'SASKATCHEWAN'),
#           (YUKON, 'YUKON'),
#           )
class Record1(models.Model):
    pruid = models.IntegerField("Province_Id", blank=False)
    prname = models.CharField("Province_Name", max_length=200, blank=False)
    prnameFR = models.CharField("Province_French_Name", max_length=200, blank=False)
    date = models.DateField('date')
    update = models.CharField(blank=True, max_length=20)
    numconf = models.CharField("Number_of_confirmed", blank=True, max_length=255)
    numprob = models.CharField(blank=True, max_length=255)
    numdeaths = models.CharField("Number_of_deaths", blank=True, max_length=255)
    numtotal = models.CharField("Total_number_of_cases", blank=True, max_length=255)
    numtested = models.CharField("Number_of_tested", blank=True, max_length=255)
    numrecover = models.CharField("Number_of_recovered", blank=True, max_length=255)
    percentrecover = models.CharField(blank=True, max_length=255)
    ratetested = models.CharField(blank=True, max_length=255)
    numtoday = models.CharField(blank=True, max_length=255)
    percentoday = models.CharField(blank=True, max_length=255)
    ratetotal = models.CharField(blank=True, max_length=255)
    ratedeaths = models.CharField(blank=True, max_length=255)
    numdeathstoday = models.CharField(blank=True, max_length=255)
    percentdeath = models.CharField(blank=True, max_length=255)
    numtestedtoday = models.CharField(blank=True, max_length=255)
    numrecoveredtoday = models.CharField(blank=True, max_length=255)
    percentactive = models.CharField(blank=True, max_length=255)
    numactive = models.CharField(blank=True, max_length=255)
    rateactive = models.CharField(blank=True, max_length=255)
    numtotal_last14 = models.CharField(blank=True, max_length=255)
    ratetotal_last14 = models.CharField(blank=True, max_length=255)
    numdeaths_last14 = models.CharField(blank=True, max_length=255)
    ratedeaths_last14 = models.CharField(blank=True, max_length=255)
    numtotal_last7 = models.CharField(blank=True, max_length=255)
    ratetotal_last7 = models.CharField(blank=True, max_length=255)
    numdeaths_last7 = models.CharField(blank=True, max_length=255)
    ratedeaths_last7 = models.CharField(blank=True, max_length=255)
    avgtotal_last7 = models.CharField(blank=True, max_length=255)
    avgincidence_last7 = models.CharField(blank=True, max_length=255)
    avgdeaths_last7 = models.CharField(blank=True, max_length=255)
    avgratedeaths_last7 = models.CharField(blank=True, max_length=255)

# class EmailSubscriber(models.Model):
#     email = models.EmailField()
#     created_at = models.DateTimeField()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:/Users/upegasmite/PycharmProjects/Assignment3.0/db.sqlite")

def __str__(self):
    return self.prname

