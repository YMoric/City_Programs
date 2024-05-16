$num = (Get-ChildItem -Recurse).count;
$length = 0;
Get-ChildItem -Recurse | ForEach-Object { $length += $_.Length };
Write-Host "ファイルの数は、 $num ファイルサイズは $length です。"