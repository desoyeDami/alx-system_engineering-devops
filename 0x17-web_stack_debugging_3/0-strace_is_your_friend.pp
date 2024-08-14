# Ensure Apache service is running and enabled
service { 'apache2':
  ensure => 'running',
  enable => true,
}

# Ensure correct permissions for the web directory
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Ensure Apache configuration files have correct permissions
file { '/etc/apache2/apache2.conf':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Optionally: Adjust PHP configuration if necessary
file { '/etc/php/7.4/apache2/php.ini':
  ensure => file,
  source => 'puppet:///modules/your_module/php.ini',
  notify => Service['apache2'],
}
