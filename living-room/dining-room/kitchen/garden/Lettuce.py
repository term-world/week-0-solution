import sys

from inventory import Acquire
from inventory.Item import ItemSpec

class Lettuce(ItemSpec):

  def __init__(self):
    super().__init__(__file__)

def main():
  Acquire(sys.argv[0])
  print("You acquired a crisp head of lettuce! 🥬")

if __name__ == "__main__":
  main()