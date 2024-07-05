# 0x04. Loops, conditions and parsing

## Description
This project is part of the ALX Software Engineering curriculum. It covers various aspects of shell scripting, including loops, conditionals, and parsing techniques. The goal is to develop a deeper understanding of how to automate tasks using Bash scripts.

## Learning Objectives
By the end of this project, you should be able to:
- Create SSH keys
- Understand the advantages of using `#!/usr/bin/env bash` over `#!/bin/bash`
- Use `while`, `until`, and `for` loops
- Use `if`, `else`, `elif`, and `case` condition statements
- Use the `cut` command
- Utilize file and other comparison operators effectively

## Requirements
- All files will be interpreted on Ubuntu 20.04 LTS.
- Each file should end with a new line.
- A `README.md` file is mandatory at the root of the project folder.
- All Bash scripts must be executable.
- No use of `awk` is allowed.
- All scripts must pass `Shellcheck` (version 0.7.0) without any error.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line should be a comment explaining what the script does.

## Tasks
### 0. Create a SSH RSA key pair
- Generate an RSA key pair.
- Share the public key in the file `0-RSA_public_key.pub`.
- Fill the SSH public key field of your intranet profile with the public key.
- Keep the private key secure.

### 1. For Best School loop
- Write a Bash script that displays "Best School" 10 times using a `for` loop.

### 2. While Best School loop
- Write a Bash script that displays "Best School" 10 times using a `while` loop.

### 3. Until Best School loop
- Write a Bash script that displays "Best School" 10 times using an `until` loop.

### 4. If 9, say Hi!
- Write a Bash script that displays "Best School" 10 times, but for the 9th iteration, it displays "Best School" and then "Hi" on a new line using a `while` loop and an `if` statement.

### 5. 4 bad luck, 8 is your chance
- Write a Bash script that loops from 1 to 10:
  - Displays "bad luck" for the 4th iteration.
  - Displays "good luck" for the 8th iteration.
  - Displays "Best School" for all other iterations.
  - Use a `while` loop and `if`, `elif`, and `else` statements.

### 6. Superstitious numbers
- Write a Bash script that displays numbers from 1 to 20:
  - Displays "4" and then "bad luck from China" for the 4th iteration.
  - Displays "9" and then "bad luck from Japan" for the 9th iteration.
  - Displays "17" and then "bad luck from Italy" for the 17th iteration.
  - Use a `while` loop and `case` statements.

### 7. Clock
- Write a Bash script that displays the time for 12 hours and 59 minutes:
  - Display hours from 0 to 12.
  - Display minutes from 1 to 59.
  - Use a `while` loop.

### 8. For ls
- Write a Bash script that displays the content of the current directory in a list format:
  - Only display the part of the name after the first dash.
  - Use a `for` loop and do not display hidden files.

### 9. To file, or not to file
- Write a Bash script that gives information about the `school` file:
  - Check if the file exists and print a message accordingly.
  - If the file exists, check if it is empty and if it is a regular file.
  - Use `if` and `else` statements.

### 10. FizzBuzz
- Write a Bash script that displays numbers from 1 to 100:
  - Displays "FizzBuzz" for numbers that are multiples of 3 and 5.
  - Displays "Fizz" for numbers that are multiples of 3.
  - Displays "Buzz" for numbers that are multiples of 5.
  - Otherwise, displays the number.
  - Use a list format.

## Installation
To install and use `Shellcheck` on your local machine, follow these steps:
```sh
# On Ubuntu
sudo apt-get update
sudo apt-get install -y shellcheck

# On macOS using Homebrew
brew install shellcheck

