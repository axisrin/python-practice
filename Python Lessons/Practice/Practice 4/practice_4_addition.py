class Practice_4_Dictionary:

    keys = tuple()
    values = tuple()

    __total_keys = 0
    #
    # def __init__(self, key, value):
    #     keys = (key,)
    #     values = (value,)

    @classmethod
    def add_item(self, key, value):
        self.keys = self.keys + (hash(key),)
        self.values = self.values + (value,)
        self.__total_keys = self.__total_keys + 1

    @classmethod
    def length(self):
        return self.__total_keys

    @classmethod
    def clear(self):
        temp_values = list(self.values)
        temp_keys = list(self.keys)
        temp_keys.clear()
        temp_values.clear()
        self.keys = tuple(temp_keys)
        self.values = tuple(temp_values)
        self.__total_keys = 0

    @classmethod
    def copy(self):
        return self

    @classmethod
    def get_by_key(self,key):
        for c_key in self.keys:
            if c_key is hash(key):
                index = self.keys.index(c_key)
                return self.values[index]
        return None

    @classmethod
    def get_key_by_value(self,value):
        for c_value in self.values:
            if c_value is value:
                index = self.values.index(c_value)
                return self.keys[index]
        return None


dictionary = Practice_4_Dictionary()
# dictionary.add_item('2','bad')
# dictionary.add_item('mac','worst')
# dictionary2 = dictionary.copy()
# print(dictionary2.keys)
# print(dictionary.values)
# print(dictionary.length())
# print(dictionary.get_by_key(2))
# print(dictionary.get_by_key(3))
# print(dictionary.get_key_by_value('bad'))
dictionary.add_item('0','hello')
dictionary.add_item('10','world')
print(dictionary.length())
print(dictionary.get_by_key('5'))