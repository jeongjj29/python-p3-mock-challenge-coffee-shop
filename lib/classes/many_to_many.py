class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            # raise Exception
            return

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.num_orders() == 0:
            return 0
        else:
            return sum([order.price for order in self.orders()]) / self.num_orders()


class Customer:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            # raise Exception
            return

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        total_spent = {}
        for customer in coffee.customers():
            total_spent[customer] = sum(
                [order.price for order in coffee.orders() if order.customer == customer]
            )

        return max(total_spent, key=total_spent.get)


class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            # raise Exception
            return

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            # raise Exception
            return

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price
        else:
            # raise Exception
            return
