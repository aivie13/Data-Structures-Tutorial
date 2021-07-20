class PriorityQueueNode:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None

class PriorityQueue:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return True if self.head == None else False
	
	def push(self, value, priority):
            if isinstance(priority, str):
                if priority.upper() == "gold".upper():
                    priority = 2
                elif priority.upper() == "silver".upper():
                    priority = 1
                else:
                    priority = 0
            if self.isEmpty() == True:
                self.head = PriorityQueueNode(value, priority)
            else:
                if self.head.priority > priority:
                    newNode = PriorityQueueNode(value, priority)
                    newNode.next = self.head
                    self.head = newNode
                else:
                    temp = self.head
                    while temp.next:
                        if priority <= temp.next.priority:
                            break
                        temp = temp.next
                    newNode = PriorityQueueNode(value, priority)
                    newNode.next = temp.next
                    temp.next = newNode

	def pop(self):
		if self.isEmpty() == True:
			return
		else:
			self.head = self.head.next
			return 1
			
	def peek(self):
		if self.isEmpty() == True:
			return
		else:
			return self.head.data

	def traverse(self):
		if self.isEmpty() == True:
			return "Queue is empty"
		else:
			temp = self.head
			while temp is not None:
				print(temp.data, end = " ")
				temp = temp.next

pq = PriorityQueue()
pq.push("John", "gold")
pq.push("Tim", "silver")
pq.push("Kevin", "silver")
pq.push("Lysandra", 0)
pq.traverse()

