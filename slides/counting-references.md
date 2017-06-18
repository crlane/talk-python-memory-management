##  Counting References

<img src="/resources/pyobj_code.png"> <!-- .element: class="fragment" data-fragment-index="1" -->

Note:
- each objects C struct maintains a count of how many times an object has been referenced
    - incremented when new reference is created
    - decremented when set to `None`, going out of scope, or `del`
    - when ref_count == 0, memory is freed
- some refcounts *never* go to 0 while program is active
- observing objects changes their refcount, so be ware
- `sys.refcount`

---

## Inspecting Refcounts

```python
>>> a = ['python', 'is', 'cool']
>>> hex(id(a))
'0x1088835a8'
>>> import ctypes
>>> def refcount(obj):
        return ctypes.c_size_t.from_address(id(obj))
```

---

## Inspect a Memory Address

```python
>>> a_ref_count = refcount(a)
>>> a_ref_count
c_ulong(1L)
```

---

## Break Reference Counting

```python
>>> b = a
>>> a_ref_count
c_ulong(2L)
>>> a_ref_count.value = 1
>>> a_ref_count
c_ulong(1L)
```

---

## Dirty, Dirty Hacks
```python
>>> a
['python', 'is', 'cool']
>>> del b
c = ['please', 'do', 'not', 'do', 'this']
>>> a
['please', 'do', 'not', 'do', 'this']
>>> hex(id(c))== hex(id(a))
True
```
