
from django.urls import path, reverse
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .models import Record1
from .admin import Record1Admin, CsvImportForm
from django.core.files.uploadedfile import SimpleUploadedFile

class TestModel(TestCase):

    def test_get_urls(self):
        url = reverse('admin:index')

    def test_upload_csv(self):
        self.records = Record1.objects.create(
            pruid=123,
            prname='Texas',
            prnameFR='Texas',
            date='2021-08-07',
            # update='',
            # numconf='',
            # numprob='',
            # numdeaths='',
            # numtotal='',
            # numtested='',
            # numrecover='',
            # percentrecover='',
            # ratetested='',
            # numtoday='',
            # percentoday='',
            # ratetotal='',
            # ratedeaths='',
            # numdeathstoday='',
            # percentdeath='',
            # numtestedtoday='',
            # numrecoveredtoday='',
            # percentactive='',
            # numactive='',
            # rateactive='',
            # numtotal_last14='',
            # ratetotal_last14='',
            # numdeaths_last14='',
            # ratedeaths_last14='',
            # numtotal_last7='',
            # ratetotal_last7='',
            # numdeaths_last7='',
            # ratedeaths_last7='',
            # avgtotal_last7='',
            # avgincidence_last7='',
            # avgdeaths_last7='',
            # avgratedeaths_last7='',
        )
        self.assertEquals(str(self.records[0]), 123)


# this tests the instance of the Record1Admin class and the admin request object
class ModelAdminTest(TestCase):

    # creates a module admin that will be used throughout the tests
    def setUp(self):
        self.recordModelAdmin=Record1Admin(model=Record1, admin_site=AdminSite())

    # returns true if added a record to the db in the admin webframe is permissiable.
    def test_has_add_permission(self):
        self.assertEquals(self.recordModelAdmin.has_add_permission(OurRequest), True)

    # returns true if deleting a db record in the admin webframe is permissiable.
    def test_has_delete_permission(self):
        self.assertEquals(self.recordModelAdmin.has_delete_permission(OurRequest), True)

    # def test_upload_file(self):
    #     csv_file = SimpleUploadedFile("blank_file.csv", "file_content", content_type='csv')
    #     self.assertEqual(response.status_code, HTTP_201_CREATED)
