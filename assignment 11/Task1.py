# Stack implementation with push(), pop(), peek(), is_empty() methods

class Stack:
    """
    A simple Last-In-First-Out (LIFO) stack data structure.
    
    Methods
    -------
    push(item)
        Add an item to the top of the stack.
    pop()
        Remove and return the top item from the stack.
        Raises IndexError if stack is empty.
    peek()
        Return the top item without removing it.
        Raises IndexError if stack is empty.
    is_empty()
        Return True if the stack is empty, False otherwise.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return the top item without removing. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        """Return True if stack is empty, False otherwise."""
        return len(self._items) == 0
    
    def __len__(self):
        """Return the number of items in the stack."""
        return len(self._items)
    
    def __repr__(self):
        """Return string representation of the stack."""
        return f"Stack({self._items})"


if __name__ == "__main__":
    stack = Stack()
    
    print("Stack Operations Demo")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Display stack")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            item = input("Enter item to push: ").strip()
            stack.push(item)
            print(f"Pushed: {item}")
        
        elif choice == "2":
            try:
                popped = stack.pop()
                print(f"Popped: {popped}")
            except IndexError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                top = stack.peek()
                print(f"Top item: {top}")
            except IndexError as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            if stack.is_empty():
                print("Stack is empty")
            else:
                print(f"Stack is not empty (contains {len(stack)} items)")
        
        elif choice == "5":
            print(f"Stack contents: {stack}")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1-6.")