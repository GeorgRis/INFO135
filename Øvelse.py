from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class PayingCustomer(Customer):
    def __init__(self, name, id, address):
        self.__name = name
        self.__id = id
        self.__address = address

    def get_full_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def change_address(self, new_address):
        self.__address = new_address

class BankApp(ABC):
    @abstractmethod
    def bank_account_info(self):
        pass

class PayApp(BankApp):
    def __init__(self, name, address, id, password, max_lim):
        self.__paying_customer = PayingCustomer(name,id,address)
        self.__password = password
        self.__max_lim = max_lim
        self.__balance = 0

    def bank_account_info(self):
        print(self.__paying_customer.get_full_name())
        print(self.__paying_customer.get_address())

    def set_password(self, oldp, newp):
        if oldp == self.__password:
            self.__password = newp
            print("New password set")
        else: print("Password is not correct")

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        if money > self.__max_lim:
            print("Limit exceeded")
        else:
            self.__balance += money
            print("Successful deposit")


from abc import ABC, abstractmethod

class AbstractArtist(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class Artist(AbstractArtist):
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_full_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone



class ArtGallery(ABC):
    @abstractmethod
    def gallety_info(self):
        pass

class OnlineArtgallery(ArtGallery):
    def __init__(self, name, phone, password, address, followers):
        self.__artist = Artist(name, phone, address)
        self.__password = password
        self.__followers = followers
        self.list_of_art_items = []

    def gallery_info(self):
        print(self.__artist.get_full_name())
        print(self.__artist.get_phone())

    def set_password(self, currentp, newp):
        if currentp == self.__password:
            self.__password = newp
            print("Password set")
        else: print("Passwrod incorrect")

    def get_sold_items(self):
        return self.list_of_art_items

    def add_new_art_item(self, new):
        if len(self.list_of_art_items) == 9:
            self.list_of_art_items.append(new)
            print("Item added! The list is now full!")
        elif len(self.list_of_art_items) >= 10:
            print("list is full cant add more")
        else:
            self.list_of_art_items.append(new)
            print("The list is added and the list is not full!")



class Car:
    def __init__(self, model, company, reg_id, prod_year):
        self.model = model
        self.company = company
        self.reg_id = reg_id
        self.prod_year = prod_year
        self.is_available = True

    def get_brand(self):
        return self.company

    def get_prod_year(self):
        return self.prod_year

class CarSharing:
    total_num_cars = 0

    def __init__(self):
        self.shared_cars = []

    def add_car(self, model, company, reg_id, prod_year):
        new_car = Car(model, company, reg_id, prod_year)
        self.shared_cars.append(new_car)
        CarSharing.total_num_cars += 1

    @classmethod
    def print_total_num_cars(cls):
        print(cls.total_num_cars)


class Electricdevice:
    def __init__(self, type, brand, serial_num, prod_year):
        self.type = type
        self.brand = brand
        self.serial_num = serial_num
        self.prod_year = prod_year
        self.turned_on = False

    def get_brand(self):
        return self.brand

    def get_production_year(self):
        return self.prod_year

class House:
    total_num_of_devices = 0

    def __init__(self):
        self.list_of_devices = []

    def add_device(self, type, brand, serial_num, prod_year):
        new_dev = Electricdevice(type, brand, serial_num, prod_year)
        self.list_of_devices.append(new_dev)
        House.total_num_of_devices += 1

    @classmethod
    def print_num_of_devices(cls):
        print(cls.total_num_of_devices)

def fun2(n, memo = {}):
    if n not in memo:
        if n < 4:
            memo[n] = 1
        elif n == 4:
            memo[n] = 4
        else:
            memo[n] = fun2(n-1,memo) + fun2(n-2,memo) + fun2(n-3,memo) + fun2(n-4,memo)
    return memo[n]

for n in range(1,6):
    print(fun2(n))

from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_full_name(self):
        pass

class PayingCustomer(Customer):
    def __init__(self, name, id, address):
        self.__name = name
        self.__id = id
        self.__address = address

    def get_full_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def change_address(self, newadd):
        self.__address = newadd

class BankApp(ABC):
    @abstractmethod
    def bank_account_info(self):
        pass

class PayApp(BankApp):
    def __init__(self, name, address, id, password, max_lim):
        self.__payingcustomer = PayingCustomer(name,address,id)
        self.__password = password
        self.__max_lim = max_lim
        self.__balance = 0

    def bank_account_info(self):
        print(self.__payingcustomer.get_address())
        print(self.__payingcustomer.get_full_name())

    def set_password(self, currpass, newpass):
        if currpass == self.__password:
            self.__password = newpass
            print("New password is set!")
        else: print("Password is not correct")

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > self.__max_lim:
            print("Limit exceeded")
        else:
            self.__balance += amount
            print("Successful deposit")
