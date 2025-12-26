$uri = "https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py"
$outputFile = "$env:temp\speedtest.py"
Invoke-WebRequest -Uri $uri -OutFile $outputFile

& python $outputFile