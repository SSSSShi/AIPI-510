import csv

# write
with open('data.csv', 'w', newline='') as csvfile:
    testwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    testwriter.writerow(['First'] * 5 + ['Second'])
    testwriter.writerow(['First', 'Second', 'Third'])

# read
with open("data.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]


# unittest
import unittest

class TestStringMethods(unittest.TestCase):

    def test_length(self):
        self.assertEqual(len(rows), 2)

if __name__ == '__main__':
    unittest.main()