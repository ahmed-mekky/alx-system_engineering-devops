# puppet touching the server
exec { 'update':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
}

file {'/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => 'sed -i "23i rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
}
