class KPCBHashMap():

    def __init__(self, intended_size):
        """ Constructor for a KPCBHashMap with an intended maximum load value of
        0.667. Returns instance of KPCBHashMap with appropriate size.


        >>> x = KPCBHashMap(100)
        >>> x.size
        150
        >>> len(x.array)
        150
        >>> x.filled
        0

        """
        self.intended_size = intended_size
        self.size = intended_size + intended_size//2
        self.array = [None for count in range(self.size)]
        self.filled = 0;


    def set(self, key, value):
        """ Adds an element with key and value. Collisions are resolved with linear
        probing. Key-value pair of same key are replaced by latest value. Returns 
        True if element is added to KPCBHashMap, and False if beyond intended size.

        >>> x = KPCBHashMap(100)
        >>> x.set('abc', 'value')
        True
        >>> x.get('abc')
        'value'
        >>> x.set('abc', 'alternative') # override old value
        True
        >>> x.get('abc')
        'alternative'
        >>> x.set(1, 'one') # hash(1) = 1, for testing
        True
        >>> x.get(1)
        'one'
        >>> x.set(101, 'onehundredandone') # hash(101) = 101, bucket is 101%100 = 1
        True
        >>> x.get(101) # should probe down from 1st to 0th bucket
        'onehundredandone'

        >>> y = KPCBHashMap(1)
        >>> y.set('test', 'first') # maximum of 1 element
        True
        >>> y.set('test2', 'too_many')
        False

        """

        if(self.filled >= self.size):
            return False

        hash_value = hash(key)    
        bucket = hash_value % self.size
        
        target_bucket = self.array[bucket]

        while(target_bucket and target_bucket[1] != key):
            bucket = bucket - 1
            if( bucket < 0 ):
                bucket += self.size
            target_bucket = self.array[bucket]

        #arrived at open bucket/bucket with same key
        self.array[bucket] = (hash_value, key, value)

        self.filled += 1
        return True

    def get(self, key):
        """ Returns value associated with key. If key not found, return None.

        >>> x = KPCBHashMap(100)
        >>> x.set('abc', 'value')
        True
        >>> x.get('abc')
        'value'
        >>> x.delete('abc')
        'value'
        >>> x.set(1, 'one')
        True
        >>> x.get(1)
        'one'
        >>> x.set(101, 'onehundredandone') # hash(101) = 101, bucket is 101%100 = 1
        True
        >>> x.get(101) # should probe down from 1st to 0th bucket
        'onehundredandone'
        >>> x.delete(1)
        'one'
        >>> x.get(101) # not affected by loss of element at original bucket
        'onehundredandone'

        """
        
        hash_value = hash(key)    
        bucket = hash_value % self.size

        for count in range(self.size):
            elem = self.array[bucket]
            if( elem is None and count != 0):
                return None
                #no value was ever set if bucket
                #not including the 0th element reaches None in array
    
            # if None, element may have been deleted
            if( elem != None and  elem[0] == hash_value and elem[1] == key):
                return elem[2]
            else:
                bucket = bucket - 1
                if( bucket < 0 ):
                    bucket += self.size


    def delete(self, key):
        """ Deletes key value pair if found. Returns value if deletion successful,
        otherwise returns None if key not found.

        >>> x = KPCBHashMap(100)
        >>> x.set('abc', 'value')
        True
        >>> x.get('abc')
        'value'
        >>> x.delete('abc')
        'value'
        >>> x.delete('abc') #returns None since no value with key 'abc'

        """
        hash_value = hash(key)    
        bucket = hash_value % self.size

        for count in range(self.size):
            elem = self.array[bucket]
            if( elem is None ):
                return None

            if( elem != None and elem[0] == hash_value and elem[1] == key):
                target = elem[2]
                self.array[bucket] = None
                return target
            else:
                bucket = bucket - 1
                if( bucket < 0 ):
                    bucket += self.size

        self.filled -= 1


    def __str__(self):
        rv = ''
        for element in self.array:
            print(element)
            if(element):
                rv += (element[0]) + "\n"
        return rv

    @property
    def load(self):
        return self.filled/self.size

            
