def reconstruct_trip(tickets):
  ticket_table = {}
  route = []
  for i, ticket in enumerate(tickets):
    ticket_table[ticket[0]] = ticket[1]
  if None in ticket_table:
    route.append(ticket_table[None])
  for i in range(len(tickets)-1):
    if (route[i] in ticket_table):
      if(ticket_table[route[i]] == None):
        break
      else:
        route.append(ticket_table[route[i]])
    else:
      return []

  print(ticket_table)
  print(route)
  return route

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  # short_set = [
  #     (None, 'PDX'),
  #     ('PDX', 'DCA'),
  #     ('DCA', None)
  #   ]
  long_set = [
      ('PIT', 'ORD'), #8
      ('XNA', 'CID'), #5
      ('SFO', 'BHM'), #2
      ('FLG', 'XNA'), #4
      (None, 'LAX'),  #0
      ('LAX', 'SFO'), #1
      ('CID', 'SLC'), #6
      ('ORD', None),
      ('SLC', 'PIT'), #7
      ('BHM', 'FLG'), #3
    ]
  reconstruct_trip(long_set)

# class Node(object):

#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node

#     def get_data(self):
#         return self.data

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next
        
# class LinkedList(object):
#     def __init__(self, head=None):
#         self.head = head
#     def insert(self, data):
#       new_node = Node(data)
#       new_node.set_next(self.head)
#       self.head = new_node
#     def all(self):
      