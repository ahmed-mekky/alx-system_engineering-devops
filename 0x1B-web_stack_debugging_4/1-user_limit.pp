# comment

exec { 'giving limits to holberton':
  command  => 'sed -i "s/nofile 5/nofile 4096/" /etc/security/limits.conf',
  provider  => shell
}
exec { 'more limits':
  command  => 'sed -i "s/nofile 4/nofile 2048/" /etc/security/limits.conf',
  provider  => shell
}
