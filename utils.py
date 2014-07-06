# -*- coding: utf-8 -*-
import inspect
        
class ChoiceBase(object):
    '''Klasa bazowa do dziedziczenia dla kas reprezentujacych opje wyboru e modelach (np. CharField)
    Pomysl zaczerpniety z http://tomforb.es/using-python-metaclasses-to-make-awesome-django-model-field-choices'''
    class __metaclass__(type):
        def __init__(self, name, type, other):
            self._data = []
            for name, value in inspect.getmembers(self):
                if not name.startswith("_") and not inspect.isfunction(value):
                    if isinstance(value,tuple) and len(value) > 1:
                        data = value
                    else:
                        data = (value, " ".join([x.capitalize() for x in name.split("_")]),)
                    self._data.append(data)
                    setattr(self, name, data[0])
            self._choice_dict = dict(self._data)

        def __iter__(self):
            for value, data in self._data:
                yield value, data

    @classmethod
    def _get_value(cls, key):
        return cls._choice_dict[key]
