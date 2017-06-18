import ctypes
def refcount(obj):
    return ctypes.c_size_t.from_address(id(obj))

a = ['python', 'is', 'cool']
print hex(id(a))
r = refcount(a)
print 'first count:{} list:{}'.format(r, a)
b = a # refcount
print 'second count:{} list:{}'.format(r, a)
r.value = 1 # now there's only one reference
print r, a
del b
c = ['please', 'do', 'not', 'do', 'this']
hex(id(c))== hex(id(a))
