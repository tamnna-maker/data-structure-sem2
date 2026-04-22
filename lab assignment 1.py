# ------------------------------
# Part A: Stack ADT
# ------------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ------------------------------
# Part B: Factorial (Recursion)
# ------------------------------

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# ------------------------------
# Fibonacci (Naive)
# ------------------------------

naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# ------------------------------
# Fibonacci (Memoization)
# ------------------------------

memo_calls = 0
memo = {}

def fib_memo(n):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)

    return memo[n]


# ------------------------------
# Part C: Tower of Hanoi
# ------------------------------

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n-1, source, destination, auxiliary)

    print(f"Move disk {n} from {source} to {destination}")

    hanoi(n-1, auxiliary, source, destination)


# ------------------------------
# Part D: Recursive Binary Search
# ------------------------------

def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)

    else:
        return binary_search(arr, key, mid+1, high)


# ------------------------------
# MAIN FUNCTION (Test Cases)
# ------------------------------

def main():

    print("----- Stack ADT Demo -----")
    s = StackADT()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack size:", s.size())
    print("Top element:", s.peek())
    print("Pop:", s.pop())
    print("Stack size after pop:", s.size())


    print("\n----- Factorial -----")
    for n in [0,1,5,10]:
        print(f"factorial({n}) =", factorial(n))


    print("\n----- Fibonacci -----")
    for n in [5,10,20,30]:

        global naive_calls
        naive_calls = 0
        result1 = fib_naive(n)

        global memo_calls, memo
        memo_calls = 0
        memo = {}
        result2 = fib_memo(n)

        print(f"\nn = {n}")
        print("Naive Fibonacci:", result1, "| Calls:", naive_calls)
        print("Memo Fibonacci:", result2, "| Calls:", memo_calls)


    print("\n----- Tower of Hanoi (n=3) -----")
    hanoi(3, 'A', 'B', 'C')


    print("\n----- Binary Search -----")

    arr = [1,3,5,7,9,11,13]

    for key in [7,1,13,2]:
        index = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> Index:", index)

    arr = []
    print("Empty list search:", binary_search(arr, 5, 0, len(arr)-1))


# Run program
if __name__ == "__main__":
    main()