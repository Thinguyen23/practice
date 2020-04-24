class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        """Add item to end of list and return nothing. Run time for this method is O(1) or constant time"""
        return self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

# check symbol string balance
def match_symbols(symbols):
    symbol_pairs = {
        "{":"}",
        "[":"]",
        "(":")"
    }
    openers = symbol_pairs.keys()
    closers = symbol_pairs.values()
    symbol_stack = Stack()

    i = 0
    while i < len(symbols):
        symbol = symbols[i]
        
        if symbol in openers:
            symbol_stack.push(symbol)
        elif symbol in closers: 
            if symbol_stack.is_empty():
                return False
            else:
                top_item = symbol_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        i += 1
    if symbol_stack.is_empty():
        return True

print(match_symbols("{[(dgagdjah)hgg]}(hfahf)"))
print(match_symbols("{[()hgg)]}(hfahf))"))