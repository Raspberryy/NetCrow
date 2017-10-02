@echo off 
title Willkommen 
color 02
cls
 
:a
cls
set newname=
set newend=
set ausw= 
set ei=1
set zw=2
set dr=3
set vi=4
set fu=5
echo.
echo      1 Neue Datei erstellen
echo      2 Datei ansehen 
echo      3 Datei Loeschen 
echo      4 Info Dateien
echo      5 Zurueck 
echo.
set /p ausw=
if %ausw%==%ei% goto New
if %ausw%==%zw% goto Lis
if %ausw%==%dr% goto Loe
if %ausw%==%vi% goto Inf
if %ausw%==%fu% goto back
goto a

:New
cls 
color 0a
echo.
echo      Wie soll die Datei heißen?
echo.
set /p newname=
cls   
echo.
echo    Wie soll die Endung lauten?  
echo.
set /p newend=
cls
echo.
echo.
echo               DIE DATEI WIRDERSTELLT
notepad.exe Benutzername\%eingabe%\%newname%.txt:%newend%
echo "Die Datei --> "%newname%.txt:%newend%" wurde ERSTELLT" >> Benutzername\%eingabe%\info.txt
ping 127.0.0.1 -n 2 > nul
goto a

:Lis
cls 
color 0a
echo.
echo      Wie heisst die Datei ?
echo.
set /p newname=
cls   
echo.
echo    Wie lautet die Endung ?  
echo.
set /p newend=
cls
echo.
echo.
echo               DIE DATEi WIRD GEOEFFNET
ping 127.0.0.1 -n 2 > nul
notepad.exe Benutzername\%eingabe%\%newname%.txt:%newend%
ping 127.0.0.1 -n 2 > nul
goto a

:Loe
cls 
color 0a
echo.
echo      Wie heisst die Datei ?
echo.
set /p newname=
cls   
echo.
echo    Wie lautet die Endung ?  
echo.
set /p newend=
cls
echo.
echo.
echo               DIE DATEi WIRD GELOESCHT
ping 127.0.0.1 -n 2 > nul
del Benutzername\%eingabe%\%newname%.txt
echo "Die Datei --> "%newname%.txt:%newend%" wurde GELOESCHT" >> Benutzername\%eingabe%\info.txt
ping 127.0.0.1 -n 2 > nul
goto a

:Inf
start Benutzername\%eingabe%\info.txt
goto a

:back
call Benutzername\%eingabe%.bat
