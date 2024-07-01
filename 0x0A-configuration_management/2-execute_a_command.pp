# This Puppet manifest kills a process named killmenow using the pkill command.
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep -f killmenow',
}

