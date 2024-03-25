import unittest
from queue_implementation import Queue 

class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue('test')
        self.assertFalse(queue.is_empty())

    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        self.assertEqual(queue.dequeue(), 'test1')
        self.assertEqual(queue.dequeue(), 'test2')

    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        queue.enqueue('test')
        self.assertEqual(queue.size(), 1)
        queue.dequeue()
        self.assertEqual(queue.size(), 0)

if __name__ == '__main__':
    unittest.main()
