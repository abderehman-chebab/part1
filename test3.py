def is_grandma_list(lst):
  """
  Advanced algorithm to check if a list is a grandma list
  (contains adjacent products in innermost integer lists).
  """

  def check_sublist(sublist, main_list):
    """Helper function to check if a sublist contains an adjacent product in the main list (or nested sublists)."""
    if isinstance(sublist, list) and len(sublist) >= 2:
      for i in range(len(sublist) - 1):
        if isinstance(sublist[i], int) and isinstance(sublist[i + 1], int):
          product = sublist[i] * sublist[i + 1]
          if product in main_list or any(is_grandma_list([product, sub_item]) for sub_item in main_list if isinstance(sub_item, list)):
            return True
    return False

  if isinstance(lst, list):
    for item in lst:
      if is_grandma_list(item):  # Recursive check for nested lists
        return True
      elif check_sublist(item, lst):  # Check the current sublist
        return True
  return False

# Sample Lists
test_cases = [
  [1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]],  # Grandma (1 * 2)
  [5, 9, 4, [[8, 7]], 4, 7, [[5]]],             # Not Grandma
  [1, 3, [2, 6]],                             # Grandma (2 * 6)
  [[[3, 4], [1, 5]], 15],                      # Grandma (3 * 4)
  [10, [5, 2], 50],                            # Grandma (5 * 2)
  [1, 2, [3, [4, 5]]],                          # Grandma (4 * 5)
  [[1, "a"], 2],                              # Not Grandma (non-integer)
  [[2, 4, 8, 16]],                             # Grandma (all adjacent products)
  [[[1, 2], 3], 2],                           # Grandma (1 * 2)
  [2, 5],                                       # Not Grandma (not enough elements)
  [[[[2, 3]]], 6],                            # Grandma (2 * 3) - Deeply nested
  [2, [[3, 4]], 12],                          # Grandma (3 * 4)
]

# Test and Print Results
for lst in test_cases:
  result = is_grandma_list(lst)
  print(f"Is {lst} a grandma list? {result}")






