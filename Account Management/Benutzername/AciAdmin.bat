@echo off
:l
set %agpw%=
set %newpw%=
set %aktpw%=
color 06
title Account Infos
cls
echo.
echo    Aktuellespasswort:                 
echo       %pw%                          
echo.                                    
echo          Benutzername:               
echo             %eingabe%              
echo.                                  
echo.
echo                      **************************
echo                      * 1   Passwort ändern    *
echo                      * 2   Benutzername ändern*
echo                      * 3   Zurueck zum Account*
echo                      * 4   Logout             *
echo                      **************************
echo.
set /p asw=
if %asw%==%eins% goto z1
if %asw%==%zwei% goto z2
if %asw%==%drei% goto z3
if %asw%==%vier% goto z4


:none
cls
echo.
echo      Inkorrekte Eingabe!
pause > nul
goto l

:z1
cls 
echo.
echo       Gebe aktuelles Passwort ein 
set /p aktpw=
if not exist Benutzername\%eingabe%\%aktpw%.txt goto none
title Neuses Passwort
color 8a
echo.
cls
echo.
echo       Gebe Neues Passwort ein:
echo.
set /p newpw= 
echo.
echo.
echo   Wiedehole dein Passwort bitte
echo.
set /p agpw=
if not %newpw%==%agpw% goto none
cls
echo.
echo       Bitte warten
rename Benutzername\%eingabe%\%pw%.txt %newpw%.txt
set pw=%newpw%
ping 127.0.0.1 -n 2 >nul
goto l




:z2
cls 
echo.
echo       Gebe aktuellen Namen ein 
set /p aktname=
if not exist Benutzername\%aktname%.bat goto none
title Neuer Name
color 8a
echo.
cls 
echo.
echo       Gebe Neuen Namen ein:
echo.
set /p newname= 
echo.
echo.
echo   Wiedehole deinen Namen bitte
echo.
set /p agname=
if not %newname%==%agname% goto none
cls
echo.
echo       Bitte warten
rename Benutzername\%aktname% %newname%
rename Benutzername\%aktname%.bat %newname%.bat
rename Benutzername\Aci%aktname%.bat Aci%newname%.bat
goto l

:z3
call Benutzername\%eingabe%

:z4
call Launcher
