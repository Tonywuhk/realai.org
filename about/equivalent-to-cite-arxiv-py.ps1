param([String]$id)

# Test if the input parameter has an allowed format
If (-Not ($id -match "^(\d{1,4}\.)?(\d{1,5})$")) {
    Write-Output "Paper ID must have (regex) format ^(\d{1,4}\.)?\d{1,5}$"
}

# Obtain the full paper $id
$yyMM = (Get-Date).ToString("yyMM")
If ($Matches.ContainsKey(1)) {
    $prefix = $yyMM.Substring(0, (5 - $Matches[1].Length)) + $Matches[1]
} Else {
    $prefix = $yyMM + "."
}
$id = $prefix + $Matches[2].PadLeft(5, "0")

# Retrieve online data
$xml = [xml](Invoke-WebRequest -Uri ("http://export.arxiv.org/api/query?id_list=" + $id))
$entry = $xml.feed.entry

# Transform a string of datetime
$dt = [datetime]$entry.updated
$dtStr = $dt.ToUniversalTime().ToString("yyyy MMMM d")

# Arrange author names
$names = $entry.author.name

if($names -is [System.String]) {
    $auStr = $names
} else {
    if($names.Length -eq 2) {
        $auStr = $names[0] + " and " + $names[1]
    } else {
        $auStr = ""
        for($i=0; $i -lt $names.Length-1; $i++) {
            $auStr = $auStr + $names[$i] + ", "
        }
        $auStr = $auStr + "and " + $names[$names.Length-1]
    }
}

$title = $entry.title -replace '\n',''

# Final output
$cite = "* " + $dtStr + ", " + $auStr + ". [" + $title + "](https://arxiv.org/abs/" + $id + "). *arXiv:" + $id + "*."
Write-Output $cite