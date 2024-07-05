# 0x0B. SSH

## Tasks

### 0. Use a private key
Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

#### File: 
- `0-use_a_private_key`

### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair named `school` with 4096 bits, protected by the passphrase `betty`.

#### File: 
- `1-create_ssh_key_pair`

### 2. Client configuration file
Configure your SSH client to use the private key `~/.ssh/school` and refuse password authentication.

#### File: 
- `2-ssh_config`

### 3. Let me in!
Add the provided SSH public key to your server to allow access using the `ubuntu` user.
