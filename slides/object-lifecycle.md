
## Object Lifecycle

```python
class Node(object):
    def __init__(self, value):
        self.value = value

n1 = Node('ABC')
n2 = Node('DEF')
n3 = Node('GHI')
```

---

## Object Lifecycle
<img src="/resources/three_nodes.png" height=400px>

<font size=5>http://patshaughnessy.net/2013/10/24/visualizing-garbage-collection-in-ruby-and-python</font>

---

## Refcount 0

<img src="/resources/del_node_0.png" height=400px>

<font size=5>http://patshaughnessy.net/2013/10/24/visualizing-garbage-collection-in-ruby-and-python</font>

---

## Reassigning Labels

<img src="/resources/reassign_labels.png" height=400px>

<font size=5>http://patshaughnessy.net/2013/10/24/visualizing-garbage-collection-in-ruby-and-python</font>

---

## Reference Cycles

<img src="/resources/creating_cycles.png" height=250px width=650px >
<img src="/resources/del_cycles.png" height=150px width=650px>
<font size=5>http://patshaughnessy.net/2013/10/30/generational-gc-in-python-and-ruby</font>
