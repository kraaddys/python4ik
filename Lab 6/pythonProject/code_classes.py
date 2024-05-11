import datetime
import re

name_pattern = '^[A-zА-я]{2,20}(-[A-zА-я]{2,10})?$'
phone_pattern = r'^\+373\d{8}$'
birthday_pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(196[0-9]|19[789][0-9]|200[0-7])$'
email_pattern = r'^[A-Za-z0-9._-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$'
position_pattern = '^[A-zА-я]{4,20}$'


class Employee:
    def __init__(self, name, phone, birthday, email, position):
        self._name = name
        self._phone = phone
        self._birthday = birthday
        self._email = email
        self._position = position

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if not re.match(name_pattern, value):
            print("Invalid name. The name must be 2 to 20 letters and may contain a hyphen.")
        else:
            self._name = value

    name = property(_get_name, _set_name)

    def _get_phone(self):
        return self._phone

    def _set_phone(self, value):
        if not re.match(phone_pattern, value):
            print("Invalid phone number. Phone number format: +373xxxxxxxx.")
        else:
            self._phone = value

    phone = property(_get_phone, _set_phone)

    def _get_birthday(self):
        return self._birthday

    def _set_birthday(self, value):
        if not re.match(birthday_pattern, value):
            print("Invalid birth date. Date format: dd.mm.yyyy, years 1960-2007.")
        else:
            self._birthday = value

    birthday = property(_get_birthday, _set_birthday)

    def _get_email(self):
        return self._email

    def _set_email(self, value):
        if not re.match(email_pattern, value):
            print("Invalid email address. Example of correct format: example@mail.com.")
        else:
            self._email = value

    email = property(_get_email, _set_email)

    def _get_position(self):
        return self._position

    def _set_position(self, value):
        if not re.match(position_pattern, value):
            print("Invalid job title. Job title must be 4 to 20 letters.")
        else:
            self._position = value

    position = property(_get_position, _set_position)

    def calculate_age(self):
        birthdate = datetime.datetime.strptime(self._birthday, "%d.%m.%Y")
        today = datetime.datetime.now()
        age = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1
        return age


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, hourly_wage, hours_worked):
        super().__init__(name, phone, birthday, email, position)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def _get_hourly_wage(self):
        return self._hourly_wage

    def _set_hourly_wage(self, value):
        if value <= 0:
            print("Hourly wage must be a positive number.")
        else:
            self._hourly_wage = value

    hourly_wage = property(_get_hourly_wage, _set_hourly_wage)

    def _get_hours_worked(self):
        return self._hours_worked

    def _set_hours_worked(self, value):
        if value < 0:
            print("Hours worked cannot be negative.")
        else:
            self._hours_worked = value

    hours_worked = property(_get_hours_worked, _set_hours_worked)

    def _calculate_salary(self):
        return self.hourly_wage * self.hours_worked


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, position, monthly_salary):
        super().__init__(name, phone, birthday, email, position)
        self.monthly_salary = monthly_salary

    def _get_monthly_salary(self):
        return self._monthly_salary

    def _set_monthly_salary(self, value):
        if value <= 0:
            print("Monthly salary must be a positive amount.")
        else:
            self._monthly_salary = value

    monthly_salary = property(_get_monthly_salary, _set_monthly_salary)

    def _calculate_salary(self):
        return self.monthly_salary