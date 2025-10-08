package main

import (
    "fmt"
    "time"
)

func job(id int) {
    fmt.Printf("Job %d started\n", id)
    time.Sleep(2 * time.Second)
    fmt.Printf("Job %d finished\n", id)
}

func main() {
    // Launch multiple jobs concurrently
    for i := 1; i <= 3; i++ {
        go job(i)
    }

    // Wait for jobs to finish
    time.Sleep(3 * time.Second)
}

// Result
/*
Job 1 started
Job 2 started
Job 3 started
Job 2 finished
Job 1 finished
Job 3 finished
*