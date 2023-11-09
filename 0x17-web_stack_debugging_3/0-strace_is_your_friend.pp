# puppet manuscript that replaces a line in a file in the server

$file_to_edit = '/var/www/html/wp-settings.php'

# replace 'phpp' with 'php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
