class Borg:

    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dictionary


class Singleton(Borg):

    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attrubute dictionary by inserting a new key-value pair
        self._shared_data.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_data)


# Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# Print the object
print(x)

# Let's create another singleton object and
# if it refers to the same atrribute dictionary
# by adding another acronym
y = Singleton(SNMP="Simple Network Management Protocol")

# Print the object
print(y)
