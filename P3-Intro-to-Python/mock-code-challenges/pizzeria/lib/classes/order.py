class Order:
    catalog = []

    def __init__(self, customer, pizza, price):
        self.customer = customer
        self.pizza = pizza
        self.price = price

        Order.catalog.append(self)

        pizza.access_current_orders(self)
        pizza.access_current_customers(customer)

        customer.access_current_orders(self)
        customer.access_current_pizzas(pizza)

    def __repr__(self):
        return f"{self.customer.name} ordered a {self.pizza.name} for ${self.price}."

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if not isinstance(customer, Customer):
            raise Exception("Must be a valid Customer")
        self._customer = customer

    @property
    def pizza(self):
        return self._pizza
    
    @pizza.setter
    def pizza(self, pizza):
        from classes.pizza import Pizza
        if not isinstance(pizza, Pizza):
            raise Exception("Must be a valid Pizza")
        self._pizza = pizza
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if not 1 < price < 10:
            raise Exception("Price must be at least")
        self._price = price