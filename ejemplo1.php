server.modules += ( "mod_fastcgi" )

fastcgi.server = ( ".php" =>
  ((
    "socket" => "/tmp/php.socket",
    "bin-path" => "/usr/local/bin/php-cgi",
    "bin-environment" => (
      "PHP_FCGI_CHILDREN" => "16",
      "PHP_FCGI_MAX_REQUESTS" => "10000"
    ),
    "min-procs" => 1,
    "max-procs" => 1,
    "idle-timeout" => 20
  ))
)
