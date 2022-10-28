"""Introducing basic example where we might use classes and how we can use them to create our own custom types"""
import string
from typing import List
import pytest

class Contact():

    def __init__(self, name: str, number: str):
        self.name = name
        self.number =  number

class App():

    def __init__(self, name: str):
        self.name = name        

class Phone():

    def __init__(self, apps: List[App], number: str, contacts: List[Contact] = []):
        self.apps = apps 
        self.number = number
        self.keys = self.create_alphabet()
        self.contacts = contacts
        self.mode = 'idle'


    def request_answer(self, phone) -> bool:
        """im a docstring"""

        for contact in self.contacts:
            if contact.number == phone.number:
                return True
        
        return False

    def make_call(self, phone) -> bool:
        """Make a 'call' if receiving phone see's calling phone in contacts. returns bool for unit testing"""
        was_answered = phone.request_answer(self)

        if was_answered:
            print('call success')
            return True
        else:
            print('call failed')
            return False



    def make_text(self, str):
        for char in str:
            if char not in self.keys:
                return False
        return True

    def open_app(self):
        pass

    def download_app(self):
        #todo
        pass

    def create_alphabet(self):
        #create lower case alphabet list
        alphabet_string = string.ascii_lowercase
        alphabet_list_low = list(alphabet_string)

        #create capital alphabet list
        alphabet_string = string.ascii_uppercase
        alphabet_list_cap = list(alphabet_string)

        #merge lists and return
        alphabet = alphabet_list_low + alphabet_list_cap
        return alphabet

phone1 = Phone([], "1234", [Contact("Ben", "0000"), Contact("Jenny", "1111")])
phone2 = Phone([], "0000")

assert not phone1.make_call(phone2)
assert phone2.make_call(phone1)
