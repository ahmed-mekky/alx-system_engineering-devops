# comment

exec { 'fixing limit of nginx':
  command => 'sudo sed -i "s/15/4096/" /etc/default/nginx',
  provider    => 'bash'
}

exec { 'nginx-restart':
  command => 'sudo nginx restart',
  provider    => 'bash'
}
