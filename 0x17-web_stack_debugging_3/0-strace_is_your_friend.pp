# Define the path to the file to edit
$file_to_edit = '/var/www/html/wp-settings.php'

# Define a variable for the desired repalcement
$old_string = 'phpp'
$new_string = 'php'

# Check if the file exists before proceeding
if !file_exists($file_to_edit) {
  fail("File ${file_to_edit} doest not exist")
}

# Define the exec resource to replace
# the line using the 'sed' command
exec {'fix bug':
  command     => "sed -i 's/${old_string}/${new_string}/g' ${file_to_edit}",
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  onlyif      => "grep -q 'phpp' ${file_to_edit}",
  subscribe   => File[$file_to_edit]
}
