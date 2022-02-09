from django.db import models
from datetime import date

from django.forms import CharField, DateTimeField, FloatField, IntegerField
import peewee as pw

db = pw.SqliteDatabase("db.sqlite3")

class DBBase(pw.Model):
    class Meta:
        database = db

class Bid(DBBase):
    BidValue = pw.IntegerField()
    auctionItem = pw.CharField()
        

class Employee(DBBase):
    employeeID = pw.IntegerField()
    name = pw.CharField()


class StorageUnitSite(DBBase):
    contactdetails = pw.CharField()
    location = pw.CharField()
    auctionItem = pw.CharField()


class User(DBBase):
    Name = pw.CharField()
    Contactdetails = pw.CharField()
    Password = pw.CharField()


class AuctionItem(DBBase):
    Typeofitem = pw.CharField()
    description = pw.CharField()
    start_endtime = pw.DateTimeField()
    Location = pw.ForeignKeyField(StorageUnitSite, backref="Location")   
    bid = []

class BidValues(DBBase):
    BidOnObject = pw.IntegerField()
