# # 20:30
import pickle
from contact import Contact
from contact import Repository
from address_book import AddressBook

Contact.destroy_all()

address_book = AddressBook()

contact1 = Contact("p1", 1234567890, "gmi@ex.com")
contact2 = Contact("p2", 1234567890, "gmi@ex.com")
contact3 = Contact("p3", 1234567890, "gmi@ex.com")
contact = Contact.find_by_number()