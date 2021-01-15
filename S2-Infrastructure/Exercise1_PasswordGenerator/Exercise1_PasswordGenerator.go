package main

import (
	"fmt"
	"io"
	"log"
	"math/rand"
)

func main()  {
	lowerLetters := "abcdefghijklmnopqrstuvwyz"
	upperLetters := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numbers := "0123456789"
	specialCharacters := "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
	combined := lowerLetters
	passwordVal := false
	complexityVal := false
	password := ""

	// PASSWORD LENGTH INPUT
	passwordLength := 0
	for passwordVal == false{
		fmt.Println("\nEnter the length of the password:")
		_, err := fmt.Scanln(&passwordLength)
		if err != nil{
			if err==io.EOF { break }
			log.Fatal("Please select a valid number!")
		}
		if passwordLength < 1{
			fmt.Println("Please select a valid number!")
			passwordVal = false
		} else {
			passwordVal = true
		}
	}

	// PASSWORD COMPLEXITY INPUT
	complexity := 0
	for complexityVal == false {
		fmt.Println("\nEnter the complexity of the password:")
		_, err := fmt.Scanln(&complexity)
		if err != nil{
			if err==io.EOF { break }
			log.Fatal("Please select a valid number!")
		}
		if complexity < 1 || complexity > 3 {
			fmt.Println("Please select a valid number! (1, 2 or 3)")
			complexityVal = false
		} else {
			complexityVal = true
		}
	}

	if complexityVal == true && passwordVal == true {
		// ADD LETTERS, NUMBERS AND SPECIAL CHARACTERS BASED ON COMPLEXITY INPUT
		if complexity == 1{
			combined += upperLetters
		}
		if complexity == 2{
			combined += upperLetters + numbers
		}
		if complexity == 3{
			combined += upperLetters + numbers + specialCharacters
		}

		for i := 0; i < passwordLength; i++ {
			p := combined[rand.Intn(len(combined))]
			password += string(p)
		}
		fmt.Println("\nYour password is: " + password)
	}
}
