# fixing nginx file limit

exec {'fixing_limits':
  command     => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider    => shell
}

exec {'nginx-restart':
  command     => 'service nginx restart',
  provider    => shell
}
