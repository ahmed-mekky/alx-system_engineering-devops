# puppet touching the server
exec { 'update':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => 'sed -i "23i\	 rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}
exec {'HTTP header':
  command  => 'sed -i "24i\	 add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}
service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
