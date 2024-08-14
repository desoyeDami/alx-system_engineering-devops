# Ensure correct permissions for the WordPress directory
file { '/path/to/your/wordpress':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Ensure Apache service is running and enabled
service { 'apache2':
  ensure => 'running',
  enable => true,
}
