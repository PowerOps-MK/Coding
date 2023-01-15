package main

import (
    "fmt"
    "time"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
      //  fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
        fmt.Println("hello.")
    })

    server := &http.Server{
        Addr:              ":8080",
        ReadHeaderTimeout: 3 * time.Second,
    }

    err := server.ListenAndServe()
    if err != nil {
        panic(err)
    }
}
