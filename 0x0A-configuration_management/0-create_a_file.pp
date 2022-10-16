# creates a file in /tmp

file { '/tmp/school':
path    => '/tmp/school',
content => 'I love Puppet',
mode    => '0744',
group   => 'www-data',
owner   => 'www-data',
}
