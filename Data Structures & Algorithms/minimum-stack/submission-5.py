class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            # Store the difference from the current min
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        # If the popped value is negative, it means we are popping the minimum
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        # If top is non-negative, the original value is top + self.min
        if top >0:
            return top + self.min
        # If top is negative, the original value was the current min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
