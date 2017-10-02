@echo off
:back
set %agpw%=
set %newpw%=
set %aktpw%=
set %abfrage%=
set %pw%=
set %eingabe%=
set %bname%=
set %rname%=
set %mail%=
set %prf%=
set lpw=

:h1
title Einloggen
color 02
set accn=1
set eingabe=
cls
set eingabe=
echo    Launcher 4.3
echo.
echo          *************
echo          Benutzername:
echo          *************
echo.
echo.
echo      Registrieren   1
echo      Fehler melden  2
echo.
set /p eingabe=
if "%eingabe%" == "1" goto r1
if "%eingabe%" == "2" goto q2
if exist Benutzername\%eingabe%.bat goto call
goto nano



:r1 
cls
title Registrieren
color 0a
echo.
echo.
echo     Gib deinen Benutzer-/Ingame-Name ein.
echo.
set /p bname=
cls 
echo   Name %bname%
echo.
echo     Gib deinen vollstaendigen Namen ein
echo.
set /p rname=
title Account fuer %rname%   /   %bname%
cls 
echo   Name %bname%
echo.
echo     Gib deine E-Mail Adresse 
echo.
set /p mail=


:r2
cls
echo.
echo.
echo    Deine Daten lauten:
echo.
echo     InGame:    %bname%
echo     Name:      %rname%
echo     Email:     %mail%
echo.      

:Abfrage 
msg "%username%" Ist alles richtig, dann gebe "Ja" ein. Falls nicht gebe ein was falsch ist ( InGame, Name oder Email ). Willst du aufhoeren, gebe "End" ein 

echo.
echo    Gebe jetzt ein:
echo.
set /p prf=  

echo.
if "%prf%" == "InGame" goto rp1 
echo.
if "%prf%" == "Name" goto rp2
echo.
if "%prf%" == "Email" goto rp3
echo.
if "%prf%" == "Ja" goto k1
echo.
if "%prf%" == "End" goto end

echo.
echo    Fehler!
echo  Gebe InGame, Name, Email, Ja oder End ein
ping 127.0.0.1 -n 2 >nul
goto Abfrage

:rp1
cls
set bname=
echo.
echo.
echo    Gebe erneut den Benutzer-/Ingame-Name ein.
echo.
set /p bname=
goto r2


:rp2
cls
set rname=
echo.
echo.
echo    Gebe erneut deinen vollstaendigen Namen ein.
echo.
set /p rname=
goto r2


:rp3
cls
set mail=
echo.
echo.
echo    Gebe erneut deine E-Mail Adresse ein.
echo.
set /p mail=
goto r2


:call
call Benutzername\%eingabe%
pause > nul

:q2 
cls 
echo.
echo.
echo       Gib deinen Namen ein
set /p n=
echo.
cls
echo.
echo   Nun deine Beschwerde bitte
echo.
set /p b=
echo Speichern...
echo %b% > Benutzername\Beschwerden\%n%Beschwerde.txt
echo %n% hat eine Beschwerde am %date% gemacht >> Benutzername\Admin\Beschwerden.txt
ping 127.0.0.1 -n 2 >nul
goto h1

:k1
set lpw=
set lapw=
echo.
echo      Passwort Eingabe:
echo.
set /p lpw=
echo.
echo.
echo      Erneute Eingabe des Passworts
echo.
set /p lapw=
if %lapw%==%lpw% goto corpw
cls
echo.
echo      Passwörter stimmen nicht überein!
ping 127.0.0.1 -n 3 >nul
goto k1


:corpw
color 3a
cls
echo.
echo.
echo   Account wird nun erstellt...
ping 127.0.0.1 -n 2 >nul
call Acc.bat


echo.
echo   Erfolgreiches Erstellen deines Accounts
ping 127.0.0.1 -n 4 >nul
goto h1



:nano
echo.
echo     Der Account %eingabe% exsestier nicht!
pause > nul
goto h1

:end
echo Schließen
pause > nul
