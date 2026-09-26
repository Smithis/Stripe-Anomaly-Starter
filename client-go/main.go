package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	body := []byte(`{"amount": 500.0, "hour": 2}`)
	resp, err := http.Post("http://127.0.0.1:8000/score", "application/json", bytes.NewBuffer(body))
	if err != nil {
		fmt.Println("start API first: uvicorn app:app --reload")
		return
	}
	defer resp.Body.Close()
	fmt.Println("score status:", resp.Status)
}
