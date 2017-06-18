##  gc

- standard library module
- provides visibility into garbage collection

---

## gc

```python
>>> import gc
>>> gc.get_referrers(obj)
...
>>> gc.get_referents(obj)
>>> gc.collect([generation])
...
>>> gc.get_threshold()
(700, 10, 10)
>>> gc.set_threshold(100, 5, 5)
>>> gc.set_debug(gc.DEBUG_LEAK) # DEBUG_STATS, et al.
```
