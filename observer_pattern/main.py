from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    The Subject interface declares a set of method for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        :param observer:
        :return:
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject
        :param observer:
        :return:
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        :return:
        """
        pass

class ConcreteSubject(Subject):
    """
    The Subject owns some import state and notified observers when the state changes.
    """
    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all 
    subscribers, is stored in this variable.
    """
    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored 
    more comprehensively (categorized by event type, etc.). 
    """
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods. 
    """
    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        :return:
        """
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_bussiness_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subjct can
        really do. Subjects commonly hold some import business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("\nSubject: I'm doing something import.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update form subject.
        :param subject:
        :return:
        """
        pass

"""
Concrete Observer react to the updates issued by the Subject they had been 
attached to.
"""
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client Code.
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_bussiness_logic()
    subject.some_bussiness_logic()

    subject.detach(observer_a)

    subject.some_bussiness_logic()




































