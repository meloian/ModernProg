class SubscriptionManager:
    def __init__(self):
        self.subscribers = set()  # manage subscribers

    def register(self, subscriber, publisher):
        self.subscribers.add(subscriber)  # add a subscriber
        print(f"Subscriber {subscriber} registered to {publisher.__class__.__name__}.")

    def unregister(self, subscriber, publisher):
        if subscriber in self.subscribers:
            self.subscribers.discard(subscriber)  # remove a subscriber
            print(f"Subscriber {subscriber} unregistered from {publisher.__class__.__name__}.")
        else:
            print("Subscriber was not found.")

    def notify_subscribers(self, publisher, message):
        # send a message to all subscribers
        for subscriber in self.subscribers:
            subscriber.update(publisher, message)

class Publisher:
    def __init__(self):
        self.manager = SubscriptionManager()

    def register(self, subscriber):
        self.manager.register(subscriber, self)  # register a subscriber

    def unregister(self, subscriber):
        self.manager.unregister(subscriber, self)  # unregister a subscriber

    def notify_subscribers(self, message):
        self.manager.notify_subscribers(self, message)  # notify all subscribers

class StockPricePublisher(Publisher):
    def __init__(self):
        super().__init__()
        self._stock_prices = {}

    def update_stock_price(self, stock, price):
        self._stock_prices[stock] = price  # update a stock price
        self.notify_subscribers(f"Stock {stock} price updated to ${price}")

class CurrencyExchangeRatePublisher(Publisher):
    def __init__(self):
        super().__init__()
        self._exchange_rates = {}

    def update_exchange_rate(self, currency_pair, rate):
        self._exchange_rates[currency_pair] = rate  # update an exchange rate
        self.notify_subscribers(f"Exchange rate for {currency_pair} updated to {rate:.2f}")

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, publisher, message):
        # print the message from the publisher
        print(f"{self.name} received message from {publisher.__class__.__name__}: {message}")

    def __str__(self):
        return f"{self.name}"  # string representation of the subscriber

# example usage
if __name__ == "__main__":
    stock_publisher = StockPricePublisher()
    currency_publisher = CurrencyExchangeRatePublisher()
    subscribers = [Subscriber(f"Subscriber {i+1}") for i in range(5)]  # create subscribers

    for sub in subscribers:
        stock_publisher.register(sub)
        currency_publisher.register(sub)

    stock_publisher.update_stock_price("AAPL", 150)
    currency_publisher.update_exchange_rate("USD/EUR", 1.10)

    stock_publisher.unregister(subscribers[0])
    currency_publisher.unregister(subscribers[0])

    stock_publisher.update_stock_price("GOOGL", 2800)
    currency_publisher.update_exchange_rate("USD/GBP", 1.25)
