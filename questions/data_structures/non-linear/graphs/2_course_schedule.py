"""
Excellent choice. Course Schedule is one of the most important Graph interview questions because it introduces the idea of cycle detection in a directed graph.

Problem Statement

There are numCourses courses numbered from 0 to numCourses - 1.

You are given:

prerequisites = [[a, b]]

which means:

To take course a, you must first complete course b.

Return:

True if it is possible to finish all courses.
False otherwise.

Example 1
numCourses = 2

prerequisites = [[1,0]]

Meaning:

Take 0 first

↓

Then take 1

Graph:

0 -----> 1

Possible?

Yes.

Answer:

True

Example 2
numCourses = 2

prerequisites = [[1,0],[0,1]]

Graph:

0 -----> 1
↑         |
|         |
+---------+

This says:

To take 1, finish 0.
To take 0, finish 1.

Impossible!

Answer:

False

Why is this a Graph?

Every course is a node.

Every prerequisite is a directed edge.

Example:

[[3,1],[3,2]]

means

1 ----\
       \
        → 3

2 ----/

The Big Idea

The question is really asking:

Does this directed graph contain a cycle?

If YES

Impossible to finish all courses.

If NO

Possible.

Why does a cycle matter?

Imagine

A → B → C → A

To take A,

you need C.

To take C,

you need B.

To take B,

you need A.

You're stuck forever.

Solution: DFS + Cycle Detection

We perform DFS.

While doing DFS we keep track of:

1. visited

Courses we've already completely processed.

2. visiting

Courses currently in the recursion stack.

This is the important one.

Suppose we're exploring:

0 → 1 → 2

Current recursion stack:

visiting

{0,1,2}

If during DFS we again reach

1

then

0 → 1 → 2 → 1

We've found a cycle.

Return False.
"""