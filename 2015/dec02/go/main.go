package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type present struct {
	length int
	width  int
	height int
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func (p present) getRibbonNeeded() int {
	ribbon := 0
	bow := 0
	dimensions := []int{p.length, p.width, p.height}
	sort.Ints(dimensions)
	fmt.Println("dimensions", dimensions)
	ribbon = ribbon + (dimensions[0] * 2) + (dimensions[1] * 2)
	bow = (dimensions[0] * dimensions[1] * dimensions[2])
	return ribbon + bow
}

func (p present) getPaperNeeded() int {
	least_area := 0
	total_area := 0

	areas := []int{p.length * p.height, p.width * p.height, p.width * p.length}
	fmt.Println(areas)
	for _, a := range areas {
		fmt.Println(a)
		if least_area > a || least_area == 0 {
			least_area = a
		}
		total_area = total_area + (2 * a)
		fmt.Println(total_area)

	}
	return total_area + least_area

}

func getPresent(s string) present {
	t := strings.Split(s, "x")
	a, err := strconv.Atoi(t[0])
	check(err)
	b, err := strconv.Atoi(t[1])
	check(err)
	c, err := strconv.Atoi(t[2])
	check(err)
	return present{a, b, c}
}

func main() {
	file, err := os.Open("../input.txt")
	defer file.Close()
	check(err)
	scanner := bufio.NewScanner(file)
	paper := 0
	ribbon := 0
	for scanner.Scan() {
		p := getPresent(scanner.Text())
		paper = paper + p.getPaperNeeded()
		ribbon = ribbon + p.getRibbonNeeded()
	}

	fmt.Println("Paper needed:", paper)
	fmt.Println("Ribbon needed:", ribbon)
}
