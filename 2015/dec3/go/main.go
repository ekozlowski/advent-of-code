package main

import (
	"fmt"
	"io"
	"os"
)

type house struct {
	xpos     int
	ypos     int
	presents int
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getHashKey(x int, y int) string {
	return fmt.Sprintf("%d %d", x, y)
}

func main() {
	f, err := os.Open("../input.txt")
	check(err)
	houseMap := make(map[string]house)
	ypos := 0
	xpos := 0
	bypos := 0
	bxpos := 0
	count = 0
	b1 := make([]byte, 1)

	for {
		n1, err := f.Read(b1)
		if err != nil {
			if err == io.EOF {
				break
			} else {
				panic(err)
			}
		}

		h := houseMap[getHashKey(xpos, ypos)]
		h.presents += 1

		s := string(b1)
		if s == "^" {
			ypos += 1
		} else if s == ">" {
			xpos += 1
		} else if s == "v" {
			ypos -= 1
		} else if s == "<" {
			xpos -= 1
		} else {
			panic("Unknown direction in file")
		}

		h = houseMap[getHashKey(xpos, ypos)]
		h.presents += 1
		houseMap[getHashKey(xpos, ypos)] = h

		fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	}
	fmt.Println(houseMap)
	fmt.Println(len(houseMap))
}
