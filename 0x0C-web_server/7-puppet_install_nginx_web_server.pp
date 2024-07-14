# 7-puppet_install_nginx_web_server.pp
# This Puppet manifest installs and configures Nginx with specified requirements

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Configure the Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('alx-system_engineering-devops/0x0C-web_server/templates/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Create the content for the root page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

