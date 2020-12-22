import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    prices = [
      {'a':100, 'b':10},
      {'a':1, 'b':100},
      {'a':10, 'b':10},
    ]
    """ ------------ Add the assertion below ------------ """
    for price in prices:
      self.assertEqual(getRatio(price['a'], price['b']), price['a']/price['b'])


  def test_getRatio_calculateRatioPriceBEqualZero(self):
    price_a = 100
    price_b = 0
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(price_a, price_b), None)

  def test_getRatio_calculateRatioPriceAEqualZero(self):
    price_a = 0
    price_b = 100
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getRatio(price_a, price_b), 0)

if __name__ == '__main__':
    unittest.main()
