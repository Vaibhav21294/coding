"""
Absolutely! Let's start from scratch and build a solid understanding of the Observer Design Pattern, 
including the concept, real-life analogy, Python implementation, and interview points.

Observer Design Pattern

The Observer Pattern is a Behavioral Design Pattern.

Its purpose is:

When one object changes its state, all interested objects are automatically notified.

Think of it as a one-to-many relationship.

One object (the Subject) has many Observers.

When something happens, the Subject notifies all its Observers.

Real-Life Example: YouTube

Suppose you subscribe to a YouTube channel.

            YouTube Channel
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Alice      Bob      Charlie

When the channel uploads a new video:

Alice gets notified
Bob gets notified
Charlie gets notified

The channel doesn't manually call Alice, Bob, and Charlie.

It simply says:

"A new video is available."

Everyone who subscribed receives the notification.

This is exactly the Observer Pattern.

Another Example: Weather App

Imagine a weather station.

         Weather Station
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 Mobile App    TV      Website

Temperature changes.

The Weather Station notifies:

Mobile App
TV
Website

The Weather Station doesn't know how each one displays the information.

Software Example

Suppose an order is placed.

Immediately:

Send Email
Send SMS
Update Inventory
Update Analytics
Generate Invoice

One event triggers many actions.

Without Observer Pattern
class OrderService:

    def place_order(self):

        print("Order placed")

        send_email()

        send_sms()

        update_inventory()

        generate_invoice()

        update_analytics()

Problem:

Every time a new requirement comes:

"Also notify Slack."

You modify this class.

Soon it becomes huge.

This violates the Open/Closed Principle.

With Observer Pattern

Instead:

              OrderService
                   │
              Notify()
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Email       SMS     Inventory

OrderService only knows:

"I have observers."

It doesn't know what they actually do.

Components

Every Observer Pattern has four parts.

1. Subject (Publisher)

Responsible for:

keeping a list of observers
notifying them

Example:

OrderService

2. Observer

Defines what every observer must implement.

Example:

update(order_id)

3. Concrete Observers

These perform the real work.

Example:

EmailService
SMSService
InventoryService

4. Client

Registers observers.

Python Implementation
Step 1: Observer Interface
from abc import ABC, abstractmethod

class OrderObserver(ABC):

    @abstractmethod
    def update(self, order_id):
        pass

Think of this as:

"Every observer must have an update() method."

Step 2: Concrete Observers
Email
class EmailService(OrderObserver):

    def update(self, order_id):
        print(f"Email sent for {order_id}")

SMS
class SMSService(OrderObserver):

    def update(self, order_id):
        print(f"SMS sent for {order_id}")
Inventory
class InventoryService(OrderObserver):

    def update(self, order_id):
        print(f"Inventory updated for {order_id}")

Each observer performs a different task.

Step 3: Subject
class OrderService:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, order_id):

        for observer in self.observers:
            observer.update(order_id)

    def place_order(self, order_id):

        print(f"Order {order_id} placed")

        self.notify(order_id)

This is the most important class.

This is the most important class.

Notice:

self.observers = []

stores everyone interested in order events.

Step 4: Client
order_service = OrderService()

order_service.subscribe(EmailService())
order_service.subscribe(SMSService())
order_service.subscribe(InventoryService())

order_service.place_order("ORD1001")

Step 4: Client
order_service = OrderService()

order_service.subscribe(EmailService())
order_service.subscribe(SMSService())
order_service.subscribe(InventoryService())

order_service.place_order("ORD1001")

Complete Python Code
"""

from abc import ABC, abstractmethod


# Observer Interface
class OrderObserver(ABC):

    @abstractmethod
    def update(self, order_id):
        pass


# Concrete Observer
class EmailService(OrderObserver):

    def update(self, order_id):
        print(f"Email sent for {order_id}")


# Concrete Observer
class SMSService(OrderObserver):

    def update(self, order_id):
        print(f"SMS sent for {order_id}")


# Concrete Observer
class InventoryService(OrderObserver):

    def update(self, order_id):
        print(f"Inventory updated for {order_id}")


# Subject
class OrderService:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, order_id):

        for observer in self.observers:
            observer.update(order_id)

    def place_order(self, order_id):

        print(f"\nOrder {order_id} placed")

        self.notify(order_id)


# Client

order_service = OrderService()

order_service.subscribe(EmailService())
order_service.subscribe(SMSService())
order_service.subscribe(InventoryService())

order_service.place_order("ORD1001")

"""
Step-by-Step Flow
Step 1
order_service = OrderService()

Creates:

OrderService

observers = []
Step 2
order_service.subscribe(EmailService())

Now:

observers

↓

EmailService
Step 3
order_service.subscribe(SMSService())

Now:

observers

↓

EmailService

SMSService
Step 4
order_service.subscribe(InventoryService())

Now:

observers

↓

EmailService

SMSService

InventoryService
Step 5

Call:

order_service.place_order("ORD1001")

Inside:

self.notify(order_id)
Step 6

notify() executes:

for observer in self.observers:
    observer.update(order_id)

Iteration 1

EmailService.update()

Iteration 2

SMSService.update()

Iteration 3

InventoryService.update()

Each observer decides what to do.

What happens when a new requirement comes?

Manager says:

"Whenever an order is placed, also update Analytics."

Simply create:

class AnalyticsService(OrderObserver):

    def update(self, order_id):
        print(f"Analytics updated for {order_id}")

Then:

order_service.subscribe(AnalyticsService())

Done.

No changes to OrderService.

This is the biggest advantage of the Observer Pattern.

Real-world Uses

You'll find the Observer Pattern in many frameworks and applications:

GUI frameworks: A button notifies registered click listeners when it's clicked.
Chat applications: New messages notify all connected users.
Stock market apps: Investors are notified when stock prices change.
Notification systems: Email, SMS, push notifications, and analytics all react to the same event.
Event-driven systems: Services publish events that multiple consumers listen to.

Strategy vs Observer

These two patterns are commonly confused.
| Strategy Pattern             | Observer Pattern                         |
| ---------------------------- | ---------------------------------------- |
| One behavior is selected     | Many observers are notified              |
| Solves "Which algorithm?"    | Solves "Who should be notified?"         |
| One object performs the work | Multiple objects react to the same event |

Strategy
processor = PaymentProcessor(CreditCardPayment())
processor.checkout(500)

Only one payment strategy runs.

Observer
order_service.place_order("ORD1001")

This single call can trigger:

Email
SMS
Inventory update
Analytics
Invoice generation

All registered observers react automatically.

Interview Answer (30 seconds)

If an interviewer asks:

"What is the Observer Pattern?"

A strong answer is:

"The Observer Pattern is a behavioral design pattern that establishes a one-to-many relationship between objects. 
A subject maintains a list of observers and automatically notifies them whenever its state changes. 
This reduces coupling between the publisher and the subscribers, 
making it easy to add or remove listeners without changing the publisher's code."

Easy Memory Trick

Remember this sentence:

Factory Pattern → Who creates the object?
Strategy Pattern → Which algorithm should I use?
Observer Pattern → Who should be notified when something happens?

If you keep these three questions in mind, you'll be able to distinguish these patterns easily during interviews.
"""