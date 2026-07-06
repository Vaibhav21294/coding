"""
Excellent! The Singleton Pattern is one of the simplest and most frequently asked design patterns in interviews.

What is the Singleton Pattern?

The Singleton Pattern is a Creational Design Pattern.

Its purpose is:

Ensure that only one instance of a class exists and provide a global way to access it.

In simple words:

No matter how many times you ask for the object, you always get the same one.

Why do we need it?

Imagine your application has a Logger.

Without Singleton:

logger1 = Logger()

logger2 = Logger()

logger3 = Logger()

Now you have three different loggers.

Problems:

Different log files
Different configurations
More memory usage

Instead, you want:

Entire Application
        │
        ▼
     One Logger

Everyone shares the same logger.

Real-Life Analogy

Think of the President of a company.

There is only one CEO.

Everyone talks to the same CEO.

You don't create a new CEO every time someone asks.

That's exactly what Singleton does.

Another Example

Suppose your application has:

1000 users
500 requests

Every request needs:

Configuration Settings

You don't want:

Request 1 → Config Object

Request 2 → Config Object

Request 3 → Config Object

Instead:

               Config Object
            /       |       \
           /        |        \
      Request1  Request2  Request3

Everyone shares one object.

Python Implementation
Without Singleton
class Logger:

    pass


logger1 = Logger()

logger2 = Logger()

print(logger1 == logger2)

Output

False

Two different objects.

Singleton Implementation

Python lets us control object creation using __new__.

class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

Client
logger1 = Logger()

logger2 = Logger()

logger3 = Logger()

print(logger1 is logger2)

print(logger2 is logger3)

Output

True

True

Every variable refers to the same object.

Complete Code
"""

class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            print("Creating Logger...")

            cls._instance = super().__new__(cls)

        return cls._instance


logger1 = Logger()

logger2 = Logger()

logger3 = Logger()

print(logger1 is logger2)

print(logger2 is logger3)

"""
Output

Creating Logger...

True

True

First call
logger1 = Logger()

Creates:

Logger Object
Second call
logger2 = Logger()

Returns:

Logger Object

No new object.

Third call
logger3 = Logger()

Returns:

Logger Object

Still the same object.

Memory:
logger1 ─────┐
             │
logger2 ─────┼────► Logger Object
             │
logger3 ─────┘

Real-World Uses

Singleton is commonly used for:

Logger

One logger for the whole application.

Configuration Manager

Read configuration once.

Everyone shares it.

Cache Manager

One cache object.

Database Connection Pool

One pool manages many database connections.

Note: It's usually the connection pool that's a singleton—not a single database connection.

Application Settings

Global configuration.

Advantages
1. Only One Instance

Guaranteed.

Useful for shared resources.

2. Saves Memory

Instead of:

100 Logger Objects

You have:

1 Logger Object

3. Global Access

Anyone can access the same object.

Example:

logger = Logger()

Anywhere in the application.

4. Shared State

Everyone sees the same data.

Example:

config.language = "English"

Every module sees:

English

Disadvantages

Singleton is often considered an anti-pattern if overused.

1. Global State

Everything shares the same object.

If one part changes it:

config.theme = "Dark"

Everyone now sees:

Dark

This can create unexpected behavior.

2. Difficult to Test

Suppose a test changes the singleton's state.

The next test sees the modified state unless you reset it.

This can make unit tests interfere with each other.

3. Hidden Dependencies

Suppose a class does:

logger = Logger()

inside its methods.

Looking at the constructor, you don't know it depends on a logger.

A better design is to pass dependencies explicitly (Dependency Injection).

4. Thread Safety

Suppose two threads execute:

Logger()

at exactly the same time.

Without synchronization, both threads could see _instance as None and each create a new object.

In multithreaded applications, you need locking or another thread-safe approach.

Interview Question

Is this Singleton thread-safe?

class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

Answer:

No.

Two threads can enter the if block simultaneously and create two different instances.

Factory vs Singleton
| Factory                            | Singleton                                    |
| ---------------------------------- | -------------------------------------------- |
| Creates objects                    | Restricts object creation                    |
| May create many objects            | Creates only one object                      |
| Focuses on how objects are created | Focuses on ensuring a single shared instance |

Strategy vs Singleton
| Strategy             | Singleton                 |
| -------------------- | ------------------------- |
| Changes behavior     | Controls object creation  |
| Multiple strategies  | One shared instance       |
| Chooses an algorithm | Ensures one object exists |

Observer vs Singleton
| Observer                           | Singleton                         |
| ---------------------------------- | --------------------------------- |
| One object notifies many observers | One shared object used everywhere |
| Event-driven communication         | Shared global resource            |

Interview Answer (30 seconds)

If an interviewer asks:

"What is the Singleton Pattern?"

A strong answer is:

"The Singleton Pattern is a creational design pattern that ensures only one instance of a class exists 
throughout the application's lifetime while providing a global access point to that instance. 
It's commonly used for shared resources like loggers, configuration managers, and cache managers. 
However, it should be used carefully because it introduces global state, can make testing harder, 
and requires thread-safe implementation in multithreaded applications."

One Interview Tip

Many modern applications, especially those built with frameworks that support Dependency Injection (DI) (such as ASP.NET Core or Spring Boot), don't implement the Singleton pattern manually.

Instead, they let the DI container manage the lifetime:

Singleton: One instance for the entire application.
Scoped: One instance per request.
Transient: A new instance every time it's requested.

For example, in ASP.NET Core:

builder.Services.AddSingleton<ILogger, Logger>();

The framework ensures only one Logger instance exists, so you get the benefits of a singleton
without writing the singleton logic yourself. 
This is the preferred approach in many production systems today.
"""