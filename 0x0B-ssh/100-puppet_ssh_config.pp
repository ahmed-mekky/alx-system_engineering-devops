#this file is saving the world :)

file_line { 'name':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'name':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
}
