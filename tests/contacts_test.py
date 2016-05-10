import unittest
import sys
sys.path.append('../addressbook')

from contact import Contact


class ContactTest(unittest.TestCase):
	def setUp(self):
		Contact.destroy_all()

	def test_get_empty_list_when_no_records_found(self):
		contacts = Contact.all()
		self.assertEqual(contacts, [])

	def test_get_all_list_of_contacts(self):
		contact1 = Contact("p1",123,"a@b.c")
		contact2 = Contact("p2",123,"a@b.c")
		contact1.save()
		contact2.save()
		contacts = Contact.all()
		self.assertEqual(len(contacts), 2)

	def test_find_a_contact_by_number(self):
		contact1 = Contact("p1",123,"a@b.c").save()
		contact2 = Contact("p2",124,"a@b.c").save()
		contact = Contact.find_by_number(123)
		self.assertEqual(contact.name, contact1.name)

	def test_find_a_contact_by_name(self):
		contact1 = Contact("p1",123,"a@b.c").save()
		contact2 = Contact("p2",124,"a@b.c").save()
		contact = Contact.find_by_name("p2")
		self.assertEqual(contact.name, contact2.name)

	def test_updating_a_contact(self):
		contact1 = Contact("p1",123,"a@b.c").save()
		contact = Contact.find_by_name("p1")
		contact.update(**{'name': "pp1"})
		self.assertEqual(Contact.find_by_name("pp1").phone_number, 123)

if __name__ == '__main__':
	unittest.main()