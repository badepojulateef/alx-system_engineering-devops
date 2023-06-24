class school_module::school_file {
	# Define variables for file attributes
	$filepath = '/tmp/school'
	$filemode = '0744'
	$fileowner = 'www-data'
	$filegroup = 'www-data'
	$filecontent = 'I love puppet\n'
}

# Create the file resources
file { $filepath:
	ensure => file,
	mode => $filemode,
	owner => $fileowner
	group => $filegroup
	content => $filecontent
}

include school_module::school_file
