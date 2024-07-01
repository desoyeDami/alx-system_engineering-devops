# 0x0A. Configuration Management

This directory contains Puppet manifests for various configuration management tasks as part of the ALX Software Engineering program.

## Tasks

### 0. Create a file

Using Puppet, create a file in `/tmp`.

**Requirements:**
- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File contains: `I love Puppet`

**Manifest:**
- `0-create_a_file.pp`

### 1. Install a package

Using Puppet, install Flask from `pip3`.

**Requirements:**
- Install Flask
- Version: `2.1.0`

**Manifest:**
- `1-install_a_package.pp`

### 2. Execute a command

Using Puppet, create a manifest that kills a process named `killmenow`.

**Requirements:**
- Must use the `exec` Puppet resource
- Must use `pkill`

**Manifest:**
- `2-execute_a_command.pp`

## How to Apply Manifests

1. Ensure Puppet is installed on your system.
2. Navigate to the directory containing the manifests.
3. Apply the desired manifest using the `puppet apply` command.

```sh
# Apply the manifest to create a file
sudo puppet apply 0-create_a_file.pp

# Apply the manifest to install Flask
sudo puppet apply 1-install_a_package.pp

# Apply the manifest to kill the killmenow process
sudo puppet apply 2-execute_a_command.pp

