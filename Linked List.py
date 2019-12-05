class Node: #Membuat wadah alokasi memori/malloc
	def __init__(self, harga, nama):
		self.harga = harga
		self.nama = nama
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__(self): #masih blm ada Element
		self.head = None
		self.tail = None

	#Push Depan
	def pushFront(self, harga, nama):
		curr = Node(harga, nama)

		if self.head is None:
			self.head = self.tail = curr
		else:
			curr.next = self.head
			self.head.prev = curr
			self.head = curr

		self.head.prev = None
		self.tail.next = None

	#Push Belakang
	def pushBack(self, harga, nama):
		curr = Node(harga, nama)
		
		if self.head is None:
			self.head = self.tail = curr
		else:
			self.tail.next = curr
			curr.prev = self.tail
			self.tail = curr

		self.head.prev = None
		self.tail.next = None

	#View All List
	def printList(self):
		if self.head is not None:
			curr = self.head

			while curr is not None:
				print("{} {}".format(curr.harga, curr.nama))
				curr = curr.next
		else:
			print("List Not Found!")

	def popFront()
		if self.head is not None:
			curr = self.head
			self.head = self.head.next
			

list = DoubleLinkedList()
list.prepend(10000, "a")
list.prepend(20000, "b")
list.prepend(30000, "c")
list.prepend(40000, "d")
list.prepend(40000, "e")

list.printList()