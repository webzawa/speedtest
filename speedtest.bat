@echo off

cd /d "C:\speedtest"
start speedtest.exe
timeout /nobreak 60

REM batファイルで特定の拡張子のみのデータをコピーするただ一つの方法
REM http://yamasekazuki.blog.jp/archives/8734322.html
for /R %%i in (*.csv) do copy /y "%%i" \\192.168.0.151\scan

exit B
