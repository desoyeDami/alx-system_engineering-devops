# Web Stack Debugging #0

## Project Overview
This project is part of the web stack debugging series designed to train you in the art of debugging. In this project, you are required to debug a Docker container running an Apache web server. The goal is to ensure that the web server returns a page containing "Hello Holberton" when queried at the root.

## Concepts
The following concepts are covered in this project:
- Network basics
- Docker
- Web stack debugging

## Project Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Bash scripts must pass `Shellcheck` without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

## Task
### 0. Give me a page!
**Objective**: Get Apache to run on the container and return a page containing "Hello Holberton" when querying the root of it.

**Steps**:
1. Run the Docker container:
   ```bash
   docker run -p 8080:80 -d -it holbertonschool/265-0

