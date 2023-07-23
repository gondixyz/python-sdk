import multiprocessing as mp
import os

lock = mp.RLock()


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        key = (os.getpid(), self)
        with lock:
            if key not in self._instances:
                self._instances[key] = super().__call__(*args, **kwargs)
        return self._instances[key]

    def new(self, *args, **kwargs):
        """creates a new instance without reusing current"""
        return super().__call__(*args, **kwargs)

    def override(self, instance):
        """overrides current instance with the argument"""
        key = (os.getpid(), self)
        with lock:
            self._instances[key] = instance

    @classmethod
    def destroy_all(cls):
        cls._instances = {}

    @property
    def instance(self) -> "Singleton":
        """returns current instance without having to call the constructor"""
        key = (os.getpid(), self)
        return self._instances[key]
