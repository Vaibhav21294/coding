"""
factory pattern
Absolutely! The Factory Pattern is one of the easiest 
and most commonly asked Design Patterns in Software Engineering interviews.

What is the Factory Pattern?

The Factory Pattern is a Creational Design Pattern.

Its purpose is:

Create objects without exposing the object creation logic to the client.

Instead of doing:

car = Car()

you do:

car = VehicleFactory.create_vehicle("car")

The factory decides which object to create.

Why do we need it?

Imagine you're building a ride-sharing app.

You have:

Car
Bike
Truck

Without a factory:

vehicle_type = "car"

if vehicle_type == "car":
    vehicle = Car()
elif vehicle_type == "bike":
    vehicle = Bike()
elif vehicle_type == "truck":
    vehicle = Truck()

Now imagine you have 20 vehicle types.

Everywhere in your code, you'll have long if-elif statements.

That's difficult to maintain.

Solution: Factory

Create one class responsible for object creation.

        Client

           |

           ▼

    VehicleFactory

      /    |    \

    Car  Bike Truck

The client doesn't know how the objects are created.

Example in Python
Step 1: Base Class
class Vehicle:
    def drive(self):
        pass
        
Step 2: Concrete Classes
class Car(Vehicle):
    def drive(self):
        print("Driving a car")


class Bike(Vehicle):
    def drive(self):
        print("Riding a bike")


class Truck(Vehicle):
    def drive(self):
        print("Driving a truck")

Step 3: Factory
class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()

        elif vehicle_type == "truck":
            return Truck()

        else:
            raise ValueError("Unknown vehicle")

Step 4: Client Code
vehicle = VehicleFactory.create_vehicle("bike")

vehicle.drive()

Output:

Riding a bike

Notice:

The client never writes:

Bike()

The factory does it.

Real-Life Example

Imagine ordering coffee.

You say:

"I'd like a cappuccino."

You don't make it yourself.

The barista (factory) decides:

Which beans to use
How much milk
Which cup

You simply receive the finished coffee.

The barista is the factory.

Another Example: Notifications

Suppose your application can send:

Email
SMS
Push notifications

Without a factory:

if notification == "email":
    sender = EmailSender()

elif notification == "sms":
    sender = SmsSender()

elif notification == "push":
    sender = PushSender()

With a factory:

sender = NotificationFactory.create_sender(notification)
sender.send()

Much cleaner.

Benefits
1. Loose Coupling

Without factory:

client

↓

Car()

The client knows about Car.

With factory:

Client

↓

Factory

↓

Car

The client only knows about the factory.    

2. Easier to Add New Types

Suppose tomorrow you add:

Bus

Without a factory:

You may need to update object creation logic in many places.

With a factory:

You only update the factory.

elif vehicle_type == "bus":
    return Bus()

Client code doesn't change.

3. Better Organization

Object creation is centralized.

Instead of dozens of files creating objects differently, one factory controls it.

Where is Factory Used?

Very common in:

Database connections
Logging frameworks
Payment gateways
Cloud SDKs
UI frameworks

Real Example: Database

Imagine your application supports:

MySQL
PostgreSQL
MongoDB

Without factory:

if db == "mysql":
    connection = MySQLConnection()

elif db == "postgres":
    connection = PostgreSQLConnection()

With factory:

connection = DatabaseFactory.create_connection(db)

Now switching databases requires minimal changes.

Factory vs Simple Object Creation

Without Factory

car = Car()

Direct creation.

With Factory

car = VehicleFactory.create_vehicle("car")

Creation logic is hidden.

Factory vs Builder

These patterns are often confused.

Factory

Creates one object.

car = Factory.create_car()
Builder

Builds a complex object step by step.

builder.add_engine()

builder.add_wheels()

builder.add_sunroof()

car = builder.build()

Use Builder when object construction has many optional parts.

Factory vs Singleton

Another common interview comparison.

Factory

Creates objects.

Factory.create_car()

You may get a new object each time.

Singleton

Ensures only one instance exists.

Logger.get_instance()

Everyone shares the same logger.

UML View
                Vehicle
                   ▲
          ┌────────┴────────┐
          │                 │
        Car              Bike
          ▲                 ▲
          └────────┬────────┘
                   │
           VehicleFactory
                   ▲
                   │
                Client

The client only interacts with the factory.

Interview Answer (30 seconds)

If an interviewer asks:

"What is the Factory Pattern?"

A strong answer is:

"The Factory Pattern is a creational design pattern that centralizes object creation. 
Instead of instantiating classes directly with new (or calling constructors directly in Python), 
the client asks a factory to create the appropriate object. 
This reduces coupling, hides creation logic, 
and makes it easier to add new implementations without changing client code."

When should you use the Factory Pattern?

Think of Factory when:

You have multiple implementations of the same interface.
The exact object to create depends on configuration or input.
You want to avoid repeated if-elif or switch statements throughout the code.
You want to hide complex object creation from the rest of the application.

For example, in a payment system:

payment = PaymentFactory.create_payment("credit_card")
payment.process()

The client doesn't care whether it receives a CreditCardPayment, PayPalPayment, 
or UPIPayment object—it simply uses the common interface. 
That's the key idea behind the Factory Pattern.
"""