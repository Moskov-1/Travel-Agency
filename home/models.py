from django.db import models

# Create your models here.

class Bkash(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    cus = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bkash'


class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    model = models.ForeignKey('Model', models.DO_NOTHING, blank=True, null=True)
    purchase = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class CarModel(models.Model):
    model_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30, blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=10, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_model'


class Customer(models.Model):
    cus_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    birthday = models.CharField(max_length=200, blank=True, null=True)
    addreas = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Guide(models.Model):
    guide_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    booking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guide'


class Loc(models.Model):
    loc_id = models.AutoField(primary_key=True)
    loc_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loc'


class Model(models.Model):
    model_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=10, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Nogot(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nogot'


class Spot(models.Model):
    spot_id = models.AutoField(primary_key=True)
    spot_name = models.CharField(max_length=30, blank=True, null=True)
    loc = models.ForeignKey(Loc, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spot'


class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    loc = models.ForeignKey(Loc, models.DO_NOTHING, blank=True, null=True)
    date = models.CharField(max_length=10, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class UserLogin(models.Model):
    mail = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login'
