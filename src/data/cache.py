class Cache: 
    def __init__(self): self._store = {} 
    def get(self, key): return self._store.get(key) 
    def set(self, key, val): self._store[key] = val 
 
_cache = Cache() 
def get_cache(): return _cache 
