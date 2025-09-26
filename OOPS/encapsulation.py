# 5. Encapsulation (Access Modifiers)
# Explanation:
# Public → accessible anywhere
# Protected (_var) → internal use (just a convention)
# Private (__var) → restricted access


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # public
        self._balance = balance    # protected
        self.__pin = "1234"        # private

    def get_balance(self):
        return self._balance

acc = BankAccount("Souvik", 1000)
print(acc.owner)       # Public
print(acc._balance)    # Protected (not recommended)
print(acc._BankAccount__pin)  # Access private using name mangling