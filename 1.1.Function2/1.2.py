class Contact:
    def __init__(self, name, surname, phone_number, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.kwargs = kwargs
        if favorite_contact:
            self.favorite_contact = 'Да'
        else:
            self.favorite_contact = 'Нет'

    def __str__(self):
        contact_info = 'Имя: {}\nФамилия: {}\nТелефон: {}\n' \
                       'В избранных: {}\nДополнительная информация:\n'.format(self.name, self.surname,
                                                                              self.phone_number,
                                                                              self.favorite_contact)
        for key, value in self.kwargs.items():
            contact_info += '\t{}: {}\n'.format(key, value)

        return contact_info


class PhoneBook:
    def __init__(self, name_book):
        self.name_book = name_book
        self.contact_list = []

    def add_contact(self, contact):
        return self.contact_list.append(contact)

    def show_list(self):
        for contact in self.contact_list:
            print(contact)

    def erase_contact_by_number(self, phone_number):
        for contact in self.contact_list[:]:
            if contact.phone_number == phone_number:
                self.contact_list.remove(contact)

    def search_all_favorite(self):
        for contact in self.contact_list:
            if contact.favorite_contact == 'Да':
                print(contact)

    def search_by_sur_name(self, name, surname):
        for contact in self.contact_list:
            if name.lower() == contact.name.lower():
                print(contact)
            elif surname.lower() == contact.surname.lower():
                print(contact)


new_phbk = PhoneBook('Телефонный справочник')

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
julia = Contact('Julia', 'Stenth', '+79117659812', telegram='@jubro', favorite_contact=True)
kostya = Contact('Kostya', 'Bro', '+79215557834', telegram='@kostyabr', email='kostyabr@bro.com')

new_phbk.add_contact(jhon)
new_phbk.add_contact(julia)
new_phbk.add_contact(kostya)

new_phbk.show_list()

# new_phbk.erase_contact_by_number('+71234567809')
#
# new_phbk.search_all_favorite()
#
# new_phbk.search_by_sur_name('Julia', 'Bro')
