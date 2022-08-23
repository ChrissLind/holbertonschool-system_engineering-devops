#Change to config file

file_line { 'BatchMode':
ensure => 'present',
line   => 'PasswordAuthentication no',
path   => '/etc/ssh/ssh_config'
}

file_line { 'IdentifyFile':
ensure => 'present',
line   => 'IdentityFile ~/.ssh/school',
path   => '/etc/ssh/ssh_config'
}
