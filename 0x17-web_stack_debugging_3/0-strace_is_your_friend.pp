# Define the path to the file to edit
$file_to_edit = '/var/www/html/wp-settings.php'

# Define a variable for the desired repalcement
$old_string = 'phpp'
$new_string = 'php'


# Define the exec resource to replace
# the line using the 'sed' command
exec {'fix bug':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin', '/usr/bin']
}
