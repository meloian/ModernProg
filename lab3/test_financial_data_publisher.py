import unittest
from financial_data_publisher import SubscriptionManager, StockPricePublisher, Publisher, CurrencyExchangeRatePublisher, Subscriber 

class TestSubscriptionManager(unittest.TestCase):
    def setUp(self):
        self.manager = SubscriptionManager()
        self.subscriber = Subscriber("Test Subscriber")
        self.publisher = Publisher()

    def test_register_and_unregister(self):
        self.manager.register(self.subscriber, self.publisher)
        self.assertIn(self.subscriber, self.manager.subscribers)
        self.manager.unregister(self.subscriber, self.publisher)
        self.assertNotIn(self.subscriber, self.manager.subscribers)

        self.manager.register(self.subscriber, self.publisher)
        self.manager.register(self.subscriber, self.publisher) 
        self.manager.unregister(self.subscriber, self.publisher)
        self.manager.unregister(self.subscriber, self.publisher) 
        self.assertNotIn(self.subscriber, self.manager.subscribers)

    def test_notify_subscribers(self):
        self.manager.register(self.subscriber, self.publisher)
        self.subscriber.messages = []
        self.subscriber.update = lambda publisher, message: self.subscriber.messages.append(message)
        self.manager.notify_subscribers(self.publisher, "Test Message")
        self.assertIn("Test Message", self.subscriber.messages)

class TestStockPricePublisher(unittest.TestCase):
    def setUp(self):
        self.publisher = StockPricePublisher()
        self.subscriber = Subscriber("Test Subscriber")

    def test_update_stock_price(self):
        self.publisher.register(self.subscriber)
        self.subscriber.messages = []
        self.subscriber.update = lambda publisher, message: self.subscriber.messages.append(message)
        self.publisher.update_stock_price("AAPL", 200)
        self.assertIn("Stock AAPL price updated to $200", self.subscriber.messages)

class TestCurrencyExchangeRatePublisher(unittest.TestCase):
    def setUp(self):
        self.publisher = CurrencyExchangeRatePublisher()
        self.subscriber = Subscriber("Test Subscriber")

    def test_update_exchange_rate(self):
        self.publisher.register(self.subscriber)
        self.subscriber.messages = []
        self.subscriber.update = lambda publisher, message: self.subscriber.messages.append(message)
        self.publisher.update_exchange_rate("USD/EUR", 1.20)
        self.assertIn("Exchange rate for USD/EUR updated to 1.20", self.subscriber.messages)

if __name__ == "__main__":
    unittest.main()


