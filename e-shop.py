from faker import Faker
import random
import database as db


class Basket:
    """
    makes a user cart

    Attributes:
        content (list): list of products in their basket
        id (int): customer id
        name (str): customer name
        address (str): customer address
        has_paid (bool): True if the customer has paid
        previous_order (list): list of previous `content`
    """

    def __init__(self, _db, name, address):
        self.content = []
        self.id = len(_db.keys())
        self.name = name
        self.address = address
        self.has_paid = False
        self.previous_order = []
        _db[self.id] = self

    def __modify_item(self, item, instr):
        """
        adds an item to the basket's content
        :param str item: the item to remove
        :param str instr: instruction to add or remove `item`
        """
        if instr == 'remove':
            try:
                self.content.remove(item)
                print(f'{self.name} removed {item} from the basket')
            except ValueError:
                print(f'{item} is not in the basket')
        else:
            self.content.append(item)
            print(f'{self.name} added {item} to the basket')

    def add_items(self, *args):
        """
        add items to customer basket
        :param list args: items to be added to basket
        """
        for item in args:
            self.__modify_item(item, 'add')

    def remove_items(self, *args):
        """
        remove items from customer basket
        :param list args: items to be removed
        """
        for item in args:
            self.__modify_item(item, 'remove')

    def __prev_order(self):
        """Add users previous purchase"""
        if len(self.content) > 0 and self.has_paid:
            self.previous_order.extend(self.content)
            self.content = []
            self.has_paid = False

    def paying(self, is_paying):
        """
        customer paying for their item
        :param bool is_paying: True is customer is paying
        """
        if len(self.content) > 0 and is_paying:
            self.has_paid = True
            self.__prev_order()


def generate_data(_db, product_name, num=10):
    """
    responsible for generating random customer data
    :param int num: number of data to create
    :param dict _db: database for customer data
    :param list product_name: list of available product
    :return: the database for customer data
    :rtype: dict
    """
    fake = Faker()

    for n in range(0, num):
        index = random.randint(0, len(product_name))
        remove_index = random.randint(0, int(len(product_name) / 2))

        customer_basket = Basket(_db, fake.name(), fake.address())

        for _name in product_name[:index]:
            customer_basket.add_items(_name)

        for _name in product_name[:remove_index]:
            customer_basket.remove_items(_name)

        customer_basket.paying(random.choice([True, False]))

    return _db


data = db.load_db()
new_data = generate_data(data, db.PRODUCT_NAME)
db.save_db(new_data)
