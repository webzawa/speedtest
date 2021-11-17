Set ws = CreateObject("Wscript.Shell")
Dim dayName

' 曜日名を取得する
dayName = Weekday(Now)

' 曜日によって処理を変える
Select Case dayName
  ' 月曜
  Case 2
    ws.run "cmd /c C:\speedtest\speedtest.bat", vbhide
  ' 火曜
  Case 3
    ws.run "cmd /c C:\speedtest\speedtest.bat", vbhide
  ' 水曜
  Case 4  
    ws.run "cmd /c C:\speedtest\speedtest.bat", vbhide
  ' 木曜
  Case 5
    ws.run "cmd /c C:\speedtest\speedtest.bat", vbhide
  Case Else
End Select
