package main

import (
	"fmt"
	"io/ioutil"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := ioutil.ReadFile("../input.txt")
	counter := 0
	first_neg_pos := 0
	check(err)
	for i, c := range dat {
		if string(c) == "(" {
			counter = counter + 1
		}
		if string(c) == ")" {
			counter = counter - 1
		}
		if counter < 0 && first_neg_pos == 0 {
			first_neg_pos = i + 1
		}
	}
	fmt.Println("Ending Floor:", counter)
	fmt.Println("First Negative Floor at position:", first_neg_pos)
}
