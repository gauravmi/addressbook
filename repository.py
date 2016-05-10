import pickle
import yaml
import os

class Repository:
	with open('./config/database.yml', 'r') as stream:
		try:
			config = yaml.load(stream)
			storage_path = config['storage_path']
			os.makedirs(os.path.dirname(storage_path), exist_ok=True)
		except yaml.YAMLError as exc:
			print(exc)

	@staticmethod
	def is_storage_empty():
		return os.stat(Repository.storage_path).st_size==0

	@classmethod
	def all(self):
		f = open(self.storage_path,'rb')
		if self.is_storage_empty():
			f.close()
			return []
		else:
			contacts = pickle.load(f)
		f.close()
		return contacts

	@classmethod
	def find_by_number(self, number):
		contacts = self.all()
		contact = list(filter(lambda x: x.phone_number == number, contacts))
		if contact:
			return contact[0]

	@classmethod
	def find_by_name(self, name):
		contacts = self.all()
		contact = list(filter(lambda x: x.name == name, contacts))
		if contact:
			return contact[0]

	@classmethod
	def destroy_all(self):
		open(self.storage_path, 'w').close()

	def update(self, **attributes):
		contacts  = self.all()
		if not attributes:
			return None
		else:
			contacts = self.all()
			contact  = list(filter(lambda c: c.phone_number == self.phone_number, contacts))[0]
			for key, value in attributes.items():
				setattr(contact, key, value)

		[ contact if c.phone_number == self.phone_number else c for c in contacts ]

		with open(self.storage_path, 'w+b') as file:
			pickle.dump(contacts, file)

		return contact

	def save(self):
		if self.is_storage_empty():
			with open(self.storage_path, 'wb') as file:
				pickle.dump([self], file)
		else:
			with open(self.storage_path, 'rb') as file:
				contacts = pickle.load(file)

			with open(self.storage_path, 'w+b') as file:
				contacts.append(self)
				pickle.dump(contacts, file)
		return self

	def str():
		pass