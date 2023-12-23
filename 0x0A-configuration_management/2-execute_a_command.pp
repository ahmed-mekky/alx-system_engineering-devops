#!/usr/bin/pup
#doing some stuff

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
