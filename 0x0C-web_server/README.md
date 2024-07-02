
# 0x0C. Web server

## Description
This project focuses on configuring a web server using Nginx and automating tasks through Bash scripts. The tasks include transferring files, installing Nginx, setting up a domain name, configuring redirections, and creating custom 404 pages. The aim is to understand the workings of a web server and automate repetitive tasks.

## Learning Objectives
By the end of this project, you should be able to explain:
- The main role of a web server.
- The concept of a child process and why web servers use parent and child processes.
- The main HTTP requests.
- The role of DNS and its record types (A, CNAME, TXT, MX).

## Resources
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://nginx.org/en/docs/)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)
- [Child process concept](https://www.geeksforgeeks.org/fork-system-call/)
- [Root and subdomain](https://www.cloudflare.com/learning/dns/glossary/subdomain/)
- [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP redirection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [Log files on Linux](https://www.loggly.com/ultimate-guide/linux-logging-basics/)

## Requirements
- All scripts should be written in Bash.
- Scripts must pass Shellcheck (version 0.3.7) without any errors.
- All scripts should be executable.
- Scripts should not use `systemctl` for restarting processes.

## Tasks

### 0. Transfer a file to your server
Write a Bash script that transfers a file from the client to a server using `scp`.

### 1. Install nginx web server
Write a Bash script to install Nginx on an Ubuntu server and configure it to respond with "Hello World!" on a GET request to its root.

### 2. Setup a domain name
Set up a domain name using `.TECH Domains` and configure DNS records to point to your server's IP.

### 3. Redirection
Configure Nginx to redirect requests from `/redirect_me` to another page with a 301 Moved Permanently status.

### 4. Not found page 404
Configure Nginx to serve a custom 404 page with the content "Ceci n'est pas une page" for non-existent pages.

## Usage
To run the scripts, use the following commands:

### Transfer a file
```sh
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

### Install Nginx
```sh
./1-install_nginx_web_server
```

### Setup a domain name
```sh
./2-setup_a_domain_name
```

### Configure redirection
```sh
./3-redirection
```

### Configure custom 404 page
```sh
./4-not_found_page_404
```
