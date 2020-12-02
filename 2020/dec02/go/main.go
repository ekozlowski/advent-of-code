package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type passwordEntry struct {
	/* 6-7 z: dqzzzjbzz */
	pos1      int
	pos2      int
	character string
	password  string
}

func parseEntry(entry string) passwordEntry {
	var pe passwordEntry
	fmt.Sscanf(entry, "%d-%d %1s: %s", &pe.pos1, &pe.pos2, &pe.character, &pe.password)
	return pe
}

func readEntries(filePath string) []passwordEntry {
	f, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Could not open ../input.txt for reading.")
	}
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var entries []passwordEntry
	for scanner.Scan() {
		entries = append(entries, parseEntry(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return entries
}

func characterOccurenceValidator(pe passwordEntry) bool {
	/*
	 * If the first position, _or_ the second position match, the password is
	 * valid.  If _both_ match, the password is invalid.  If _neither_ match the
	 * password is invalid.
	 *
	 * By definition, this is a XOR logical operator.
	 */
	var positionOneMatches = string(pe.password[pe.pos1-1]) == pe.character
	var positionTwoMatches = string(pe.password[pe.pos2-1]) == pe.character
	// XOR implementation, since Go doesn't have one.

	return positionOneMatches != positionTwoMatches
}

func characterPositionalValidator(pe passwordEntry) bool {
	/*
	 * If the character appears _between_ p1 and p2 times in the password
	 * (inclusive), then the password is valid.
	 */
	var c = strings.Count(pe.password, pe.character)
	return pe.pos1 <= c && c <= pe.pos2

}

func getValidEntries(pes []passwordEntry, validator func(passwordEntry) bool) []passwordEntry {
	var validEntries []passwordEntry
	for _, pe := range pes {
		if validator(pe) {
			validEntries = append(validEntries, pe)
		}
	}
	return validEntries
}

func main() {
	var entries = readEntries("../input.txt")
	var validP1Entries []passwordEntry = getValidEntries(entries, characterPositionalValidator)
	fmt.Printf("There are %d valid Part 1 entries.\n", len(validP1Entries))
	var validP2Entries []passwordEntry = getValidEntries(entries, characterOccurenceValidator)
	fmt.Printf("There are %d valid Part 2 entries.\n", len(validP2Entries))
}
