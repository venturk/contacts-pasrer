from datetime import datetime
from base64 import b64decode
from os.path import isfile
from re import sub
import webbrowser


class Contact(object):
    def __init__(self, first_name, last_name, phone_numbers, time, image):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + ' ' + self.last_name

        self.phone_numbers = phone_numbers
        self.time = time
        self.image = image

    def __repr__(self):
        str = ''

        str += 'Full name:\n'
        str += 16 * ' ' + self.full_name + '\n'

        str += 'Phone number(s):\n'

        for phone in self.phone_numbers:
            str += 16 * ' ' + phone + '\n'

        str += 'Creation time:\n'
        str += 16 * ' ' + self.time + '\n'

        return str

    def show_image(self):
        self.save_image()
        img_name = self.full_name + '.jpg'

        if isfile(img_name):
            webbrowser.open(img_name)

    def save_image(self):
        if self.image:
            img_name = self.full_name + '.jpg'

            if not isfile(img_name):
                img_data = b64decode(self.image)

                with open(img_name, 'wb') as f:
                    f.write(img_data)
                f.close()

    @property
    def time(self):
        return self._call_logs

    @time.setter
    def time(self, value):
        self._call_logs = datetime.fromtimestamp(int(value)).strftime('%Y-%m-%d %H:%M:%S')

    @property
    def phone_numbers(self):
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, value):
        self._phone_numbers = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = sub(r'[^\x00-\x7F]+', ' ', value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = sub(r'[^\x00-\x7F]+', ' ', value)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value.rstrip()
