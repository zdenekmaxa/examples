<?php

    $logFile =  "log";

    function getVariable($varName, $default)
    {
        if($var = getenv($varName))
        {
            return $var;
        }
        else
        {
            return $default;
        }
    }


    function getLogInfo()
    {
        $date = gmdate("d/M/Y:H:i:s");
        $remoteAddr = getVariable("REMOTE_ADDR", "-ra-");
        $remoteHost = getVariable("REMOTE_HOST", "-rh-");
        $remoteUser = getVariable("REMOTE_USER", "-ru-");
        $remoteIdent = getVariable("REMOTE_IDENT", "-ri-");
        $serverName = getVariable("SERVER_NAME", "-sn-");
        $requestUri = getVariable("REQUEST_URI", "-ru-");
        $userAgent = getVariable("HTTP_USER_AGENT", "-ua-");

        $log = "$date $remoteAddr $remoteHost $remoteIdent $remoteUser\n";
        $log .= "    $requestUri $userAgent\n";

        return $log;
    }


    function writeLog()
    {
        if($fd = @fopen($GLOBALS["logFile"], "a"))
        {
            $log = getLogInfo();
            fputs($fd, $log);
            fclose($fd);
        }
        else
        {
            //    echo "open log file failed";
        }
    }



    if(isset($_GET['cv']))
    {
        // accessed with ?cv in URL - ok, display CV links
        $link = "<a href=\"zdenek_maxa-cv.pdf\">PDF</a>";
        $page = "Zdenek Maxa CV:&nbsp;&nbsp;" . $link;
        writeLog();
    }
    else
    {
        // accessed without ?cv in URL
        $host = getenv("HTTP_HOST");
        $uri = getenv("REQUEST_URI");
        $link = "Requested URL: " . $host . $uri . "<br>";
        $msg = "My professional CV is available under the link "
            ."stated in the job application e-mail.";
        $page = $link . $msg;
        writeLog();

    }
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Zdenek Maxa</title>

<style type="text/css">

body {
  font: 90% 'Lucida Grande', Verdana, Geneva, Lucida, Arial, Helvetica, sans-serif;
  color: black;
  margin: 2em;
  padding: 2em;
}

a[href] {
  color: #436976;
  background-color: transparent;
}

a.toc-backref {
  text-decoration: none;
}

h1 a[href] {
  text-decoration: none;
  color: #fcb100;
  background-color: transparent;
}

a.strong {
  font-weight: bold;
}

img {
  margin: 0;
  border: 0;
}

p {
  margin: 0.5em 0 1em 0;
  line-height: 1.5em;
}
p a {
  text-decoration: underline;
}
p a:visited {
  color: purple;
  background-color: transparent;
}
p a:active {
  color: red;
  background-color: transparent;
}
a:hover {
  text-decoration: none;
}
p img {
  border: 0;
  margin: 0;
}

h1, h2, h3, h4, h5, h6 {
  color: #003a6b;
  background-color: transparent;
  font: 100% 'Lucida Grande', Verdana, Geneva, Lucida, Arial, Helvetica, sans-serif;
  margin: 0;
  padding-top: 0.5em;
}

h1 {
  font-size: 160%;
  margin-bottom: 0.5em;
  border-bottom: 1px solid #fcb100;
}
h2 {
  font-size: 140%;
  margin-bottom: 0.5em;
  border-bottom: 1px solid #aaa;
}
h3 {
  font-size: 130%;
  margin-bottom: 0.5em;
}
h4 {
  font-size: 110%;
  font-weight: bold;
}
h5 {
  font-size: 100%;
  font-weight: bold;
}
h6 {
  font-size: 80%;
  font-weight: bold;
}

ul a, ol a {
  text-decoration: underline;
}

dt {
  font-weight: bold;
}
dt a {
  text-decoration: none;
}

dd {
  line-height: 1.5em;
  margin-bottom: 1em;
}

legend {
  background: #ffffff;
  padding: 0.5em;
}

form {
  margin: 0;
}


dl.form {
  margin: 0;
  padding: 1em;
}

dl.form dt {
  width: 30%;
  float: left;
  margin: 0;
  padding: 0 0.5em 0.5em 0;
  text-align: right;
}

input {
  font: 100% 'Lucida Grande', Verdana, Geneva, Lucida, Arial, Helvetica, sans-serif;
  color: black;
  background-color: white;
  vertical-align: middle;
}

abbr, acronym, .explain {
  color: black;
  background-color: transparent;
}

q, blockquote {
}

code, pre {
  font-family: monospace;
  font-size: 1.2em;
  display: block;
  padding: 10px;
  border: 1px solid #838183;
  background-color: #eee;
  color: #000;
  overflow: auto;
  margin: 0.5em 1em;
}

tt.docutils {
  background-color: #eeeeee;
}

</style>

</head>

<body background="background.jpg">

    <div>
        <?php
            print $page;
        ?>
    </div>
</body>
</html>


