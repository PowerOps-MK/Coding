package main

import (
    "fmt"
    "net/http"
)

funcmain() {
    http.HandleFunc("/", HelloServer)
    http.ListenAndServe(":8080", nil)
}
