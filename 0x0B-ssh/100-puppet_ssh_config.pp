# Puppet manifest to configure global SSH client settings

file { '/etc/ssh':
  ensure  => 'directory',
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
}

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @("EOF"),
# Global SSH client configuration
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF
}
