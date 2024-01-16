# puppet touching the server
exec {'add_header':
  command  => 'sed -i "49i add_header X-Served-By "\$hostname";" /etc/nginx/sites-available/default',
  provider => 'shell'
}
service {'nginx':
  ensure  => running,
}
