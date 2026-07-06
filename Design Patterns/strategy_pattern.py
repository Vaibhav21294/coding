"""
Excellent! The Strategy Pattern is one of the most commonly used design patterns 
in real-world software and interviews. Once you understand it, you'll start noticing it everywhere.

A simple way to remember it is:

Factory decides which object to create.

Strategy decides which algorithm or behavior to use.

What is the Strategy Pattern?

The Strategy Pattern is a Behavioral Design Pattern.

Its purpose is:

Define a family of algorithms, encapsulate each one, and make them interchangeable.

Instead of writing lots of if-else statements, you create separate classes for each behavior.

Problem Without Strategy

Suppose you're building a navigation app.

Users can travel by:

Car 🚗
Bike 🚲
Walking 🚶

Without Strategy:

"""
class Navigator:

    def navigate(self, mode):

        if mode == "car":
            print("Finding fastest road")

        elif mode == "bike":
            print("Finding bike lanes")

        elif mode == "walk":
            print("Finding walking paths")

"""
Now imagine adding:

Bus
Train
Ferry
Taxi

The if-elif chain keeps growing.

Solution: Strategy Pattern

Separate each algorithm into its own class.

               Navigator

                   |

          Route Strategy

         /      |       \

      Car     Bike     Walk

The Navigator doesn't know how each route is calculated.

It simply calls the selected strategy.

Step 1: Strategy Interface
from abc import ABC, abstractmethod

class RouteStrategy(ABC):

    @abstractmethod
    def build_route(self):
        pass

Every strategy must implement:

build_route()

Step 2: Concrete Strategies
class CarStrategy(RouteStrategy):

    def build_route(self):
        print("Driving route")


class BikeStrategy(RouteStrategy):

    def build_route(self):
        print("Bike route")


class WalkStrategy(RouteStrategy):

    def build_route(self):
        print("Walking route")

Step 3: Context

The Context is the class that uses the strategy.

class Navigator:

    def __init__(self, strategy):
        self.strategy = strategy

    def navigate(self):
        self.strategy.build_route()

Notice:

The Navigator doesn't care which strategy it has.

Step 4: Client
navigator = Navigator(CarStrategy())

navigator.navigate()

Output:

Driving route

Switch to bike:

navigator = Navigator(BikeStrategy())

navigator.navigate()

Output:

Bike route

The Navigator code never changes.

Why is this useful?

Suppose tomorrow we add:

Train Strategy

Without Strategy Pattern:

Modify the huge if-else.

With Strategy Pattern:

Simply create:

class TrainStrategy(RouteStrategy):

    def build_route(self):
        print("Train route")

Nothing else changes.

Real-Life Example: Payment System

Suppose your app supports:

Credit Card
PayPal
UPI

Without Strategy:

if payment == "card":
    ...

elif payment == "paypal":
    ...

elif payment == "upi":
    ...

With Strategy:

Payment Processor

       |

Payment Strategy

 /      |       \

Card  PayPal   UPI

Python:

processor = PaymentProcessor(UPIStrategy())

processor.pay()

Tomorrow you add:

Apple Pay

Just create:

class ApplePayStrategy(PaymentStrategy):

Done.

Another Example: Sorting

Suppose your application allows users to choose:

Quick Sort
Merge Sort
Bubble Sort

Without Strategy:

if algorithm == "quick":
    ...

elif algorithm == "merge":
    ...

elif algorithm == "bubble":
    ...

With Strategy:

Sorter

↓

Sorting Strategy

↓

QuickSort

MergeSort

BubbleSort

Real-World Example: Compression

Suppose Windows lets you compress files as:

ZIP
RAR
7Z

Each compression algorithm is a strategy.

The UI doesn't change.

Only the algorithm changes.

Visual

Without Strategy

Client

↓

Huge if-else

With Strategy

Client

↓

Context

↓

Strategy Interface

↓

Concrete Strategy

Much cleaner.

Benefits
1. No giant if-else

Instead of:

if...
elif...
elif...
elif...

each algorithm becomes its own class.

2. Easy to add new behavior

Add a new class.

Don't modify existing code.

3. Follows the Open/Closed Principle

Open for extension.

Closed for modification.

One of the SOLID principles.

4. Easier Testing

Each strategy can be tested independently.

Factory vs Strategy

This is one of the most common interview questions.

Factory

Purpose:

Create objects

vehicle = VehicleFactory.create("car")

Question answered:

Which object should I create?

Strategy

Purpose:

Choose behavior

navigator = Navigator(CarStrategy())

Question answered:

Which algorithm should I use?

Together

Factories and Strategies are often used together.

Example:

strategy = PaymentStrategyFactory.create("paypal")

processor = PaymentProcessor(strategy)

processor.pay()

Factory creates the strategy.

Strategy performs the work.

UML
             Client

                |

                ▼

            Context

                |

         Strategy Interface

         /       |        \

      Car     Bike     Walk

Interview Tip

When should you think of the Strategy Pattern?

Use it when:

Multiple algorithms solve the same problem.
You want to switch behavior at runtime.
You keep writing large if-elif or switch statements based on a type or mode.
Different implementations share the same interface.

Examples:

Payment methods
Shipping cost calculation
Discount calculation
Authentication methods (OAuth, SAML, JWT)
Sorting/compression algorithms
Route planning (car, bike, walking)

Factory vs Strategy in One Sentence

This is the easiest way to remember the difference:

Factory Pattern	Strategy Pattern
Creates the correct object	Uses the correct algorithm
Solves object creation	Solves behavior selection
"Which object?"	"Which behavior?"

Example

Suppose you're building an e-commerce checkout:

A Factory creates the appropriate payment strategy:
strategy = PaymentStrategyFactory.create("credit_card")
The Strategy executes the payment logic:
processor = PaymentProcessor(strategy)
processor.pay()

The factory answers "What object should I instantiate?", 
while the strategy answers "How should this operation be performed?"

Can you please give me a full code example of strategy design pattern
Absolutely! Let's build a complete, realistic Python example of the Strategy Pattern.

We'll use a Payment System, which is one of the classic interview examples.

Problem

Suppose an e-commerce website supports:

Credit Card
PayPal
UPI

The checkout process should work the same way, 
but the payment algorithm changes depending on the payment method.

Without Strategy Pattern
class PaymentProcessor:

    def pay(self, amount, payment_type):

        if payment_type == "card":
            print(f"Paid ${amount} using Credit Card")

        elif payment_type == "paypal":
            print(f"Paid ${amount} using PayPal")

        elif payment_type == "upi":
            print(f"Paid ${amount} using UPI")

Imagine adding:

Apple Pay
Google Pay
Crypto

This method becomes larger and larger.

With Strategy Pattern
Step 1: Strategy Interface
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

Every payment method must implement pay().

Step 2: Concrete Strategies
Credit Card
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")
PayPal
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")
UPI
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using UPI")

Each class contains its own payment algorithm.

Step 3: Context

The context is the class that uses a strategy.

class PaymentProcessor:

    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        print("Starting checkout...")
        self.payment_strategy.pay(amount)
        print("Checkout complete.")

Notice something important:

PaymentProcessor has no idea whether it's using:

Credit Card
PayPal
UPI

It simply calls:

self.payment_strategy.pay(amount)

That's the entire Strategy Pattern.

Step 4: Client Code
processor = PaymentProcessor(CreditCardPayment())

processor.checkout(500)

Output:

Starting checkout...
Paid $500 using Credit Card
Checkout complete.

Switch to PayPal:

processor = PaymentProcessor(PayPalPayment())

processor.checkout(750)

Output:

Starting checkout...
Paid $750 using PayPal
Checkout complete.

No changes to PaymentProcessor.

Switch to UPI:

processor = PaymentProcessor(UPIPayment())

processor.checkout(100)

Output:

Starting checkout...
Paid $100 using UPI
Checkout complete.

Again, no changes.

Complete Code
"""

from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")


# Concrete Strategy 3
class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using UPI")


# Context
class PaymentProcessor:

    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        print("Starting checkout...")
        self.payment_strategy.pay(amount)
        print("Checkout complete.\n")


# Client Code

processor = PaymentProcessor(CreditCardPayment())
processor.checkout(500)

processor = PaymentProcessor(PayPalPayment())
processor.checkout(750)

processor = PaymentProcessor(UPIPayment())
processor.checkout(100)

"""
Output
Starting checkout...
Paid $500 using Credit Card
Checkout complete.

Starting checkout...
Paid $750 using PayPal
Checkout complete.

Starting checkout...
Paid $100 using UPI
Checkout complete.

Visual Flow
                Client
                   │
                   ▼
     PaymentProcessor (Context)
                   │
                   ▼
          PaymentStrategy
          (Interface)
          /      |      \
         ▼       ▼       ▼
 CreditCard  PayPal     UPI

The Client chooses the strategy, and the PaymentProcessor uses it 
without knowing the implementation details. 

What if we add Apple Pay?

Simply create a new strategy:

class ApplePayPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ${amount} using Apple Pay")

Then use it:

processor = PaymentProcessor(ApplePayPayment())
processor.checkout(300)

No changes are needed in:

PaymentProcessor
CreditCardPayment
PayPalPayment
UPIPayment

This is why the Strategy Pattern follows the Open/Closed Principle: 
you can extend the system by adding new strategies without modifying the existing, tested code. 
That's one of the main reasons interviewers like this pattern.
"""