from django.core.cache import cache
from webassets.cache import BaseCache, make_hashable
import cPickle as pickle


class DjangoCache(BaseCache):

    def __eq__(self, other):
        """Return equality with the config values that instantiate
        this instance.
        """
        return False == other or \
               None == other or \
               id(self) == id(other)

    def get(self, key, python=None):
        key = make_hashable(key)
        value = cache.get(key, None)
        if value:
            try:
                value = pickle.loads(value)
            except:
                value = None

        return value

    def set(self, key, value):
        key = make_hashable(key)
        cache.set(key, pickle.dumps(value))
