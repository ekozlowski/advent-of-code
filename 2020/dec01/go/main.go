package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func getIntegerListFromFile(filePath string) []int {
	var numbers []int
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Failed opening file %s", err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		val, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatalf("Could not convert %s to an integer.", scanner.Text())
		}
		numbers = append(numbers, val)
	}

	file.Close()
	return numbers
}

func main() {
	var numbers = getIntegerListFromFile("../data.txt")

	for _, x := range numbers {
		for _, y := range numbers {
			for _, z := range numbers {
				if x+y+z == 2020 {
					/* Why does this print three times? */
					fmt.Printf("x=%d, y=%d, z=%d\n", x, y, z)
				}
			}
		}
	}

}
