class Wallet():

    def __init__(self, val, name):
        if val not in ("USD", "EUR"):
            raise ValueError
        self.__money = 0
        self.val = val
        self.name = name

    def popolnenie(self, balance):
        self.__money = self.__money + balance
        return balance

    def trata(self, balance):
        if self.__money - balance < 0:
            raise ValueError("net")
        self.money = self.__money - balance
        return balance

    def info(self):
        return self.__money


wal1 = Wallet("USD", "Lineage2")
wal2 = Wallet("USD", "Interlude")
wal2.popolnenie(20)
wal1.popolnenie(20)
wal1.popolnenie(wal2.trata(10))
print(wal1.info())
print(wal2.info())
