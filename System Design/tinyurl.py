"""
Excellent choice! Design a URL Shortener (like TinyURL or Bitly) is one of the most common System Design interview questions. It teaches many fundamental concepts that apply to larger systems.

Since you're preparing for Software Engineering interviews, I'll explain it from beginner → interview level.

What is a URL Shortener?

Suppose you have a long URL:

https://www.amazon.com/electronics/mobile-phones/apple-iphone-17-pro-max-black-256gb?tracking=abc123xyz

A URL shortener converts it into something like:

https://tinyurl.com/aB7xY2

When someone visits:

https://tinyurl.com/aB7xY2

they are automatically redirected to the original URL.

Step 1: Functional Requirements

Interviewers first want to know what the system should do.

Must Have
Accept a long URL.
Generate a short URL.
Redirect users to the original URL.
Short URLs should be unique.
Nice to Have
Expiration dates
Custom aliases

Example:

tinyurl.com/chatgpt

instead of

tinyurl.com/X8kQ1m
Click analytics
QR code generation

Step 2: High-Level Design

The system has two main APIs.

API 1 – Shorten URL

User sends:

POST /shorten

{
    "url": "https://google.com/maps/..."
}

Server returns:

{
    "shortUrl": "tinyurl.com/aB7xY2"
}
API 2 – Redirect

User opens:

tinyurl.com/aB7xY2

Server looks it up and responds with:

HTTP 302 Redirect

Location:
https://google.com/maps/...

The browser then automatically loads the original page.

Step 3: Overall Architecture
              User
                │
                ▼
          Load Balancer
                │
     ┌──────────┴──────────┐
     ▼                     ▼
 API Server           API Server
     │                     │
     └──────────┬──────────┘
                ▼
           Database

Components

Load Balancer

Distributes traffic across multiple servers.

Application Servers

Handle:

Creating short URLs
Looking up URLs
Redirecting users

Database

Stores mappings like:
| Short Code | Original URL                                    |
| ---------- | ----------------------------------------------- |
| aB7xY2     | [https://google.com/](https://google.com/)...   |
| xY98Za     | [https://youtube.com/](https://youtube.com/)... |

Step 4: Database Design

Simple table:
| id | short_code | original_url                             | created_at |
| -- | ---------- | ---------------------------------------- | ---------- |
| 1  | aB7xY2     | [https://google.com](https://google.com) | ...        |

Step 5: How Do We Generate Short URLs?
This is where interview discussions get interesting.
This is where interview discussions get interesting.

Option 1 – Auto Increment ID

Database:

1

2

3

4

5

Convert each number into Base62.

Base62 contains:

a-z

A-Z

0-9

Total:

62 characters

Example:

125

↓

cb

Very short.

Advantages:

No collisions
Simple
Option 2 – Random String

Generate:

Ax7PdQ

Check database.

Already exists?

Generate another.

Advantages:

Harder to predict
Doesn't expose the number of URLs created
Why Base62?

Suppose ID:

1000000

Decimal:

1000000

Base62:

4c92

Much shorter.

Step 6: Redirect Flow

User enters:

tinyurl.com/aB7xY2

Server:

SELECT original_url
FROM urls
WHERE short_code='aB7xY2'

Returns:

https://amazon.com/...

Server responds:

302 Redirect

Browser opens Amazon.

Step 7: Scaling the System

Suppose TinyURL becomes very popular.

100 Million URLs

No problem.

1 Billion URLs

Database becomes huge.

We need improvements.

Cache

Most URLs are accessed repeatedly.

Instead of querying the database every time:

User

↓

Cache

↓

Database (only if needed)

Popular links stay in memory.

A cache lookup is much faster than a database query.

Multiple Servers

Instead of:

Users

↓

1 Server

Use:

Users

↓

Load Balancer

↓

Server 1

Server 2

Server 3

This allows many requests to be handled simultaneously.

Database Replication

One database may become overloaded.

Use:

          Primary
          Database
          /      \
         /        \
 Replica       Replica

Writes go to the primary.

Reads can be served by replicas.

Since redirects are mostly reads, this scales well.

Step 8: Possible Bottlenecks
Database

Too many lookups.

Solution:

Cache
Read replicas

Collision

Randomly generated short code already exists.

Solution:

Generate another code.

Hot URLs

Suppose one shortened URL goes viral.

Millions of people click it.

Without caching:

Millions

↓

Database

Database gets overwhelmed.

With caching:

Millions

↓

Cache

↓

Database (rarely)

Much more efficient.

Step 9: Security

Possible issues:

Spam URLs

Someone shortens phishing links.

Solutions:

URL validation
Safe browsing checks
Abuse reporting

Brute Force

Someone tries:

tinyurl.com/aaaaaa

tinyurl.com/aaaaab

tinyurl.com/aaaaac

to discover URLs.

Solutions:

Longer random codes
Rate limiting
Monitoring unusual access patterns

Time Complexity

Creating a URL:

Insert into DB

≈ O(1)

Lookup:

Hash lookup / indexed lookup

≈ O(1)

Very fast.

What Interviewers Usually Ask Next

After you've explained the basic design, they often ask follow-up questions like:
1. How do you avoid duplicate short codes?

Answer:

Use Base62 encoding of unique IDs, or
Generate random codes and retry on collision.

2. What if one URL gets 100 million clicks?

Answer:

Cache popular mappings.
Scale horizontally with multiple application servers.
Use read replicas for the database.

3. How would you support custom aliases?

Example:

tinyurl.com/vaibhav

Store the custom alias as the short_code after checking it's not already taken.

4. What if users want links to expire?

Add columns like:

short_code	original_url	expires_at
aB7xY2	https://...	2026-12-31

On redirect, check whether the current time is past expires_at.

Final Architecture
                User
                  │
                  ▼
          Load Balancer
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   App Server 1        App Server 2
        │                   │
        └─────────┬─────────┘
                  ▼
               Cache
                  │
                  ▼
          Primary Database
             │         │
             ▼         ▼
        Read Replica  Read Replica

Interview Tips

For system design interviews, don't jump straight into architecture. A structured approach impresses interviewers:

Clarify requirements (functional and non-functional).
Estimate scale (users, requests, storage).
Design APIs.
Design the database/schema.
Draw the high-level architecture.
Discuss scaling, caching, and reliability.
Address bottlenecks and trade-offs.

For a URL Shortener, the key concepts interviewers want to hear are:

REST APIs (POST /shorten, GET /{shortCode})
Unique short-code generation (often Base62)
Database indexing on short_code
Caching for popular links
Load balancing and horizontal scaling
Read replicas for heavy redirect traffic
Security measures like rate limiting and abuse detection

Mastering this problem gives you a strong foundation because many other system design questions 
(chat systems, file storage, notification services, etc.) build on these same principles.

Additional
For a URL shortener, there are two different users:

The person creating the short URL
The person clicking the short URL

These users interact with different APIs.

API 1: Create a Short URL

The creator wants to shorten a URL.

Request
POST /api/v1/urls

Body:

{
    "longUrl": "https://www.amazon.com/electronics/mobile-phones/iphone17"
}
Server

The server:

Validates the URL.
Generates a short code (e.g., aB7xY2).
Stores it in the database.
Returns the shortened URL.

Database:

Short Code	Long URL
aB7xY2	https://www.amazon.com/...
Response
{
    "shortUrl": "https://tinyurl.com/aB7xY2"
}

API 2: Redirect to the Original URL

Later, someone clicks:

https://tinyurl.com/aB7xY2

The browser makes a request like:

GET /aB7xY2

Notice:

There is no request body.

The short code is already part of the URL.

Server

The server:

Reads aB7xY2.
Looks it up in the database.
Finds the original URL.
Sends an HTTP redirect.

Response:

HTTP/1.1 302 Found
Location: https://www.amazon.com/electronics/mobile-phones/iphone17

The browser automatically loads Amazon.

Overall Flow
          Creator

              |
              |
 POST /api/v1/urls
(long URL)
              |
              ▼
        URL Shortener
              |
              |
       Store in Database
              |
              ▼
Return short URL
              |
              |
https://tinyurl.com/aB7xY2

Later...
          Another User

                |
                |
      GET /aB7xY2
                |
                ▼
         URL Shortener
                |
        Lookup Database
                |
                ▼
HTTP 302 Redirect
                |
                ▼
 Original Website

 Typical Interview API Design

If asked to design a URL shortener, this is usually sufficient:
| Method   | Endpoint                         | Purpose                               |
| -------- | -------------------------------- | ------------------------------------- |
| `POST`   | `/api/v1/urls`                   | Create a short URL                    |
| `GET`    | `/{shortCode}`                   | Redirect to the original URL          |
| `GET`    | `/api/v1/urls/{shortCode}/stats` | View analytics (optional)             |
| `DELETE` | `/api/v1/urls/{shortCode}`       | Delete a short URL (optional)         |
| `PUT`    | `/api/v1/urls/{shortCode}`       | Update the destination URL (optional) |

"""