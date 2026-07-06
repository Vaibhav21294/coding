"""
Excellent! The Builder Pattern is another very common interview topic. 
It's especially useful when an object has many optional fields.

A simple way to remember it is:

Factory Pattern → Creates which object.

Builder Pattern → Creates one complex object step by step.

What is the Builder Pattern?

The Builder Pattern is a Creational Design Pattern.

Its purpose is:

Construct a complex object step by step, allowing different representations of the same object.

Why do we need it?

Suppose you have a House class.

It has:

Number of bedrooms
Number of bathrooms
Garage
Swimming pool
Garden
Balcony
Solar panels

Without Builder, the constructor becomes messy.
house = House(
    bedrooms=3,
    bathrooms=2,
    garage=True,
    swimming_pool=False,
    garden=True,
    balcony=True,
    solar_panels=False
)

Imagine the class has 20 optional fields. It becomes difficult to read and easy to make mistakes.

Solution: Builder Pattern

Instead, build the object step by step.

house = (
    HouseBuilder()
        .add_bedrooms(3)
        .add_bathrooms(2)
        .add_garage()
        .add_garden()
        .build()
)

This reads almost like English.

Real-Life Analogy

Think about ordering a burger.

You tell the restaurant:

Add cheese

Add lettuce

Add tomato

No onions

Extra sauce

The chef builds one burger step by step.

The chef is the Builder.

Example: Computer

Suppose we want to build a computer.

A computer may have:

CPU
RAM
SSD
GPU
WiFi
Bluetooth

Not every computer has all of these.

Step 1: Product
class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.ssd = None
        self.gpu = None

    def __str__(self):
        return (
            f"CPU: {self.cpu}, "
            f"RAM: {self.ram}, "
            f"SSD: {self.ssd}, "
            f"GPU: {self.gpu}"
        )

This is the object we want to build.

Step 2: Builder
class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_ssd(self, ssd):
        self.computer.ssd = ssd
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

Notice something interesting:

Every setter returns:

return self

This allows method chaining.

Step 3: Client
computer = (
    ComputerBuilder()
        .set_cpu("Intel i9")
        .set_ram("32 GB")
        .set_ssd("1 TB")
        .set_gpu("RTX 4090")
        .build()
)

print(computer)

Output:

CPU: Intel i9, RAM: 32 GB, SSD: 1 TB, GPU: RTX 4090

Complete Code
"""

class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.ssd = None
        self.gpu = None

    def __str__(self):
        return (
            f"CPU: {self.cpu}, "
            f"RAM: {self.ram}, "
            f"SSD: {self.ssd}, "
            f"GPU: {self.gpu}"
        )


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_ssd(self, ssd):
        self.computer.ssd = ssd
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


computer = (
    ComputerBuilder()
        .set_cpu("Intel i9")
        .set_ram("32 GB")
        .set_ssd("1 TB")
        .set_gpu("RTX 4090")
        .build()
)

print(computer)

"""
What's happening internally?

When you write:

builder = ComputerBuilder()

Memory:

ComputerBuilder
      │
      ▼
 Computer

The builder owns a Computer object.

Next:

builder.set_cpu("Intel i9")

The builder updates:

Computer

CPU = Intel i9
RAM = None
SSD = None
GPU = None

Then:

builder.set_ram("32 GB")

Now:

Computer

CPU = Intel i9
RAM = 32 GB
SSD = None
GPU = None

Each method modifies the same Computer object.

Finally:

computer = builder.build()

build() simply returns the completed object.

Why return self?

Look at this method:

def set_cpu(self, cpu):
    self.computer.cpu = cpu
    return self

Suppose you write:

builder.set_cpu("Intel")

It returns the builder itself.

So Python can immediately call:

.set_ram("32 GB")

on the same builder.

Without return self, you'd have to write:

builder = ComputerBuilder()

builder.set_cpu("Intel i9")
builder.set_ram("32 GB")
builder.set_ssd("1 TB")
builder.set_gpu("RTX 4090")

computer = builder.build()

Both work, but method chaining is cleaner.

Real-World Uses

Builder is commonly used for:

Constructing HTTP requests
SQL query builders
HTML/XML document builders
Complex configuration objects
Test data builders
UI component builders

For example:

request = (
    HttpRequestBuilder()
        .set_url("https://api.example.com")
        .set_method("POST")
        .add_header("Authorization", "Bearer token")
        .set_body(data)
        .build()
)

Builder vs Factory

This is a very common interview question.
Builder vs Factory

This is a very common interview question.

| Factory                        | Builder                       |
| ------------------------------ | ----------------------------- |
| Creates an object in one step  | Builds an object step by step |
| Chooses which object to create | Configures one complex object |
| Good for different subclasses  | Good for many optional fields |

Factory Example
vehicle = VehicleFactory.create("car")

The factory decides whether to create a Car, Bike, or Truck.

Builder Example
house = (
    HouseBuilder()
        .add_garage()
        .add_garden()
        .add_pool()
        .build()
)

The builder constructs one House with the desired features.

Builder vs Singleton
| Builder                        | Singleton                          |
| ------------------------------ | ---------------------------------- |
| Builds complex objects         | Ensures only one instance exists   |
| Creates a new object each time | Returns the same object every time |

Pros
Handles many optional parameters cleanly.
Improves readability with method chaining.
Separates construction logic from the product.
Makes it easier to create different configurations of the same object.
Cons
Requires additional classes.
Can feel like overkill for simple objects with only a few fields.
Adds some extra boilerplate code.

Interview Answer (30 seconds)

If an interviewer asks:

"What is the Builder Pattern?"

A strong answer is:

"The Builder Pattern is a creational design pattern used to construct complex objects step by step. 
Instead of passing many constructor parameters, a builder gradually configures the object 
and finally returns the completed instance. 
It improves readability, supports optional fields, and separates object construction from the object's representation."

Easy Memory Trick

Remember these four creational patterns:

Factory → Which object should I create?
Builder → How do I build this complex object?
Singleton → There should only be one object.
Observer (behavioral, not creational) → Who should be notified?

Keeping those questions in mind makes it much easier to recognize which pattern fits a given problem during an interview.
"""