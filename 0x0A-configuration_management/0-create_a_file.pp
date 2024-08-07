# This Puppet manifest creates a file at /tmp/school with specific permissions, owner, group, and content.
file { '/tmp/school':
  ensure  => 'file',          # Ensure the resource is a file
  content => 'I love Puppet', # Content to be written to the file
  owner   => 'www-data',          # File owner
  group   => 'www-data',          # File group
  mode    => '0744',          # File permissions
}

