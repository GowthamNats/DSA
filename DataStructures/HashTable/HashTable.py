# Hashtable Implementation
class HashTable:
    def __init__(self, size):
        self.hashTable = [[],] * size

    def checkPrime(self, n):
        if n == 1 or n == 0:
            return 0

        for i in range(2, n//2):
            if n % i == 0:
                return 0

        return 1


    def getPrime(self, n):
        if n % 2 == 0:
            n = n + 1

        while not self.checkPrime(n):
            n += 2

        return n


    def hashFunction(self, key):
        capacity = self.getPrime(10)
        return key % capacity


    def insertData(self, key, data):
        index = self.hashFunction(key)
        self.hashTable[index] = [key, data]

    def removeData(self, key):
        index = self.hashFunction(key)
        self.hashTable[index] = 0

# Hashtable usage
if __name__ == '__main__':
    hash = HashTable(10)
    hash.insertData(123, "apple")
    hash.insertData(432, "mango")
    hash.insertData(213, "banana")
    hash.insertData(654, "guava")

    print(hash.hashTable)

    hash.removeData(123)

    print(hash.hashTable)