"""
Learn these concepts:
Load Balancers
Caching (Redis)
Database Sharding
Message Queues (Kafka)
CAP Theorem
Consistent Hashing
Microservices vs Monoliths

These are the core System Design concepts that interviewers expect you to know. 
I'll explain each one in the same style as the DSA topics 
we've covered—simple, visual, and interview-focused.

1. Load Balancer
Problem

Imagine your website has only one server.

         Users
           │
           ▼
      Web Server

Initially:

10 users ✅
100 users ✅

But then:

100,000 users

One server cannot handle all the requests.

Solution

Put a Load Balancer in front.

             Users
                │
                ▼
         Load Balancer
        /      |      \
       ▼       ▼       ▼
   Server1  Server2  Server3

The Load Balancer distributes requests.

Example:

User 1 → Server1

User 2 → Server2

User 3 → Server3

Why?

Benefits:

Prevents one server from becoming overloaded.
Allows horizontal scaling.
Improves availability.

If one server dies:

Server2 ❌

The Load Balancer simply stops sending traffic there.

Common Algorithms
Round Robin
S1

↓

S2

↓

S3

↓

S1

Everyone gets equal traffic.

Least Connections

Send the request to the server with the fewest active users.

Very common.

IP Hash

Same user always goes to the same server.

Useful for session-based applications.

Interview Tip

Whenever you hear:

"Millions of users"

mention:

"I'd put a Load Balancer in front of multiple application servers."

2. Caching (Redis)
Problem

Suppose every request needs to query the database.

User

↓

Server

↓

Database

Database queries are relatively slow.

Imagine 1 million users requesting the same URL.

Without cache:

1,000,000

↓

Database

Database becomes overloaded.

Solution

Add a cache.

User

↓

Server

↓

Redis Cache

↓

Database

First Request
Cache

↓

Miss

↓

Database

↓

Store in Cache

Second Request
Cache

↓

Hit

↓

Return immediately

Database isn't involved.

Cache Hit

Data found.

Very fast.

Cache Miss

Data not found.

Go to database.

Redis

Redis is an in-memory key-value store.

Example:

Key

abc123

↓

Value

https://google.com

Reading from memory is much faster than reading from disk.

Interview Tip

Use Redis when data is:

Frequently read
Changes infrequently
Can be regenerated if lost

Reading from memory is much faster than reading from disk.

is memory referring to cache and disk referring to database

Yes, exactly! That's the right way to think about it.

When we say:

"Reading from memory is much faster than reading from disk."

we usually mean:

Memory → RAM, where a cache like Redis stores data.
Disk → The persistent storage used by your database (SSD or HDD).

Why is RAM so much faster?

Approximate access times:
| Storage                | Typical Access Time |
| ---------------------- | ------------------: |
| CPU Cache              |       ~1 nanosecond |
| RAM (Redis cache)      |    ~100 nanoseconds |
| SSD (Database storage) |   ~100 microseconds |
| HDD                    |  ~5–10 milliseconds |

3. Database Sharding
Problem

One database:

1 Billion Users

Eventually becomes:

Too large
Too slow

Solution

Split data.

        Application
             │
     ┌───────┼────────┐
     ▼       ▼        ▼
Shard1   Shard2   Shard3

Each shard stores part of the data.

Example:

A–H

↓

Shard1

I–P

↓

Shard2

Q–Z

↓

Shard3

Now each database is much smaller.

Why?

Instead of one huge database:

1 TB

Use:

250 GB

250 GB

250 GB

250 GB

Queries become faster.

Challenge

How do you know which shard contains the data?

This leads to...

4. Consistent Hashing

Imagine adding servers.

Initially:

Server1

Server2

Server3

Later:

Add Server4

Without consistent hashing:

Almost every user moves to a different server.

Terrible!

Consistent Hashing maps:

Users

↓

Hash Ring

↓

Servers

When a new server is added:

Only a small fraction of users move.

Used in:

Distributed caches
Database sharding
Distributed storage systems
Interview Tip

If you discuss adding or removing servers dynamically, 
mentioning Consistent Hashing is a strong signal that you understand distributed systems.

Normal Hashing

Suppose you have 3 servers.

To decide where to store a user, you do:

server = hash(user_id) % 3

5. Message Queues (Kafka)
Problem

User uploads a photo.

Tasks:

Resize image
Send notification
Store metadata
Scan for viruses

Without a queue:

Upload

↓

Resize

↓

Scan

↓

Notify

↓

Done

User waits.

Slow.

Solution

Use a Message Queue.

User

↓

Upload Service

↓

Kafka Queue

↓

Worker1

Worker2

Worker3

The upload finishes immediately.

Workers process tasks in the background.

Why?
Faster user experience
Services become independent
Easy to scale workers

Common Queues

Kafka
RabbitMQ
Amazon SQS

Interview Tip

Whenever a task can happen later, think:

"I'll process it asynchronously using a message queue."

Examples:

Email
SMS
Image processing
Video encoding

6. CAP Theorem

Distributed databases cannot guarantee all three simultaneously.

C

Consistency

Everyone sees the latest data.

A

Availability

System always responds.

P

Partition Tolerance

Works even if servers can't communicate.

Example

Two databases.

Network cable breaks.

DB1

❌

DB2

Now choose.

Option 1

Wait until communication is restored.

Users may get errors.

Consistency is preserved.

Option 2

Continue serving users independently.

System stays available.

But users may see different data.

CAP says:

During a network partition, you must choose between:

Consistency
Availability

You can't have both.

Interview Tip

Most modern distributed systems must tolerate partitions, so the real trade-off is usually:

Consistency
Availability

What is a Network Partition?

A network partition happens when two or more servers cannot communicate with each other 
because of a network failure, even though the servers themselves are still running.

7. Monolith vs Microservices
Monolith

Everything in one application.

Application

├── Login

├── Payments

├── Orders

└── Notifications

Advantages:

Easy to develop
Easy to deploy

Disadvantages:

Hard to scale parts independently
One bug can affect the whole application

Microservices

Split into independent services.

           API Gateway

               │

      ┌────────┼────────┐

      ▼        ▼        ▼

 Login   Orders   Payments

Each service:

Own code
Own deployment
Own database (often)

Advantages

Scale independently.

Example:

Payments

100 servers

Orders

20 servers

No need to scale everything.

Disadvantages

More complexity:

Network calls
Monitoring
Service discovery
Distributed debugging
Interview Tip

For small startups:

Monolith is often the right choice.

For large companies:

Microservices make scaling and independent deployments much easier.

Quick Cheat Sheet
| Concept                   | One-Line Definition                                                                                           | Typical Use                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **Load Balancer**         | Distributes requests across servers                                                                           | Scale application servers                    |
| **Redis Cache**           | Stores frequently accessed data in memory                                                                     | Reduce database load                         |
| **Database Sharding**     | Splits one large database into smaller databases                                                              | Handle massive datasets                      |
| **Kafka / Message Queue** | Processes work asynchronously                                                                                 | Background jobs (emails, image processing)   |
| **CAP Theorem**           | In distributed systems, you can't guarantee Consistency, Availability, and Partition Tolerance simultaneously | Reason about distributed database trade-offs |
| **Consistent Hashing**    | Minimizes data movement when servers are added or removed                                                     | Sharding, caching, distributed storage       |
| **Monolith**              | Single application containing all functionality                                                               | Simpler systems, early-stage products        |
| **Microservices**         | Independent services communicating over the network                                                           | Large-scale systems with independent teams   |

📚 System Design Learning Roadmap

Now that you've learned the fundamentals, I'd recommend practicing these interview problems in order:

✅ Design URL Shortener (TinyURL) – APIs, database, cache, load balancer
Design Rate Limiter – counters, Redis, distributed systems
Design Chat Application (WhatsApp) – WebSockets, message queues
Design Notification System – Kafka, retries, worker services
Design YouTube – object storage, CDN, video processing
Design Instagram Feed – fan-out strategies, caching, timelines

These six designs introduce almost every major concept asked in entry-level 
and mid-level system design interviews. Once you're comfortable explaining them, 
you'll have a strong foundation for interviews at most technology companies.
"""

