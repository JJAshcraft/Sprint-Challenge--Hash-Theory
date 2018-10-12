def reconstruct_trip(tickets):
  ticket_table = {}
  for ticket in tickets:
    ticket_table[ticket[0]] = ticket[1]
  print(ticket_table)

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  short_set = [
      (None, 'PDX'),
      ('PDX', 'DCA'),
      ('DCA', None)
    ]
  reconstruct_trip(short_set)

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
      