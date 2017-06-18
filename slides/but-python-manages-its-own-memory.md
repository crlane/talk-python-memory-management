##  But...Python Manages its Own Memory

<img src="/resources/archer_meme.png" height=500px>

Note:
Python actually has two different ways to manage memory
- reference counting
- garbage collection

Most of the time, this is sufficient. However, there are some edge cases to consider
- globally scoped variables
- open connections, files
- Collections of objects
- objects with a `__del__` method
