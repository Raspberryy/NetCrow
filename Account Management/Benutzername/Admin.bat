@echo off 
title Passwortabfrage
set eins=1
set zwei=2
set drei=3
set vier=4
set zahl=3
set funf=5
set nu=0

color 03
:a1
cls
echo.
echo.
echo      Gebe dein Passwort ein.
echo.
set /p pw=
if exist Benutzername\%eingabe%\%pw%.txt goto True 
:falsch
set /a zahl= %zahl%-1
echo.
echo    Das Passwort ist falsch!
echo.
echo       Noch %zahl% Versuche
pause > nul
if %zahl%==%nu% goto exit
goto a1




:True
cls
color 03
echo.
echo.
echo      Willkommen Zurueck!
echo.
echo           1 Account Informationen
echo           2 Logout
echo           3 Geheime Dateien
echo           4 Account Loeschen
echo           5 Beschwerden
echo.
set /p abfrage=
if %abfrage%==%eins% goto aci
if %abfrage%==%zwei% goto cl
if %abfrage%==%drei% goto lg
if %abfrage%==%vier% goto losch
if %abfrage%==%funf% goto besch
goto True
:cl
call Launcher

:aci 
call Benutzername\Aci%eingabe%

:lg
call Benutzername\Launcherg.bat

:exit
taskkill /f /im cmd.exe

:losch
call Benutzername\Admin\Loescher.bat

:besch
start Benutzername\Admin\Beschwerden.txt
goto True
