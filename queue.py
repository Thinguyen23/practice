import random

# Printer algo
class PrintQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ This method take in an item and insert into the list. Runtime is O(n) or linear time
        because inserting one item into the 0th of the list force all items to move one index to the right"""
        self.items.insert(0,item)

    def dequeue(self):
        """ Return and remove the front-most item of the Queue. Runtime is constant or O(1)"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
    
class Job:
    def __init__(self):
        self.pages = random.randint(1,11)

    def print_page(self):
        if self.pages > 0:
            self.pages -=1
    
    # Check wether all pages have been printed
    def check_complete(self):
        if self.pages == 0:
            return True
        return False

class Printer:
    def __init__(self):
        self.current_job = None
    
    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError: # Queue is empty
            return "No more job to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_page()
        
        if job.check_complete():
            return "Printing Complete"
        else:
            return "Error has occurred"