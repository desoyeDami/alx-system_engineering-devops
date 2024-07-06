# Puppet manifest to configure SSH client settings
# Ensures SSH client uses specified private key and disables password authentication
file { '/root/.ssh':
  ensure  => 'directory',
  owner   => 'root',
  group   => 'root',
  mode    => '0700',
}

file { '/root/.ssh/config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => @("EOF"),
Host my-server
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF
}

file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^    PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^    IdentityFile',
}

