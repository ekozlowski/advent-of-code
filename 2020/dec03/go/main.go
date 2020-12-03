package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func readLines(filePath string) []string {
	f, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Could not open ../input.txt for reading.")
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return lines
}

func getTrees(step int, skip int) int {
	var lines = readLines("../input.txt")
	var treeCount int = 0
	for i, line := range lines {
		if i%skip != 0 {
			continue // skip lines if we have a modulus on skip.
		}
		if line[((step*i)/skip)%len(line)] == '#' {
			treeCount++
		}
	}
	return treeCount
}

func solvePartOne() {
	fmt.Printf("Part One Tree count: %d", getTrees(3, 1))
}

func solvePartTwo() {
	var total int
	total = getTrees(1, 1) * getTrees(3, 1) * getTrees(5, 1) * getTrees(7, 1) * getTrees(1, 2)
	fmt.Printf("Part two number: %d", total)
}

func main() {
	solvePartOne()
	solvePartTwo()
}
