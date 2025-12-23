from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount: float) -> None:
        print(f"Оплата картой на сумму {amount:.2f} руб.")
    
    def refund(self, amount: float) -> None:
        print(f"Возврат на карту на сумму {amount:.2f} руб.")
class PayPalPayment(PaymentSystem):
    def pay(self, amount: float) -> None:
        print(f"Оплата через PayPal на сумму {amount:.2f} USD.")
    def refund(self, amount: float) -> None:
        print(f"Возврат через PayPal на сумму {amount:.2f} USD.")