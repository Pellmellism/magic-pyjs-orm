
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
import datetime


def idc():
   return Column(Integer, primary_key=True) #_idc
def boolc():
   return Column(Boolean) #_boolc
def intc():
   return Column(Integer) #_intc
def floatc():
   return Column(Float) #_floatc
def textc():
   return Column(Text) #_textc
def stringc(length=None):
   return Column(String(length=length))
def datetimec():
   return Column(DateTime) #_datetimec
def foreignidc(key):
   return Column(Integer, ForeignKey(key))

class User(Base):
   __tablename__ = 'users'

   id = idc()
   counter = intc()
   debt_type = textc()

