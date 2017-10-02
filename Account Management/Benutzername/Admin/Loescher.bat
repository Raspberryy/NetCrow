@echo off
title Loeschen
color 02
set eins=1
set zwei=2
set drei=3
set vier=4
set ja=Ja
set no=Nein



 
:loeschen
cls
echo.
echo         1 Account Loschen
echo         2 Account-Liste
echo         3 Back
echo.
set /p loeng=
if %loeng%==%eins% goto accloa
if %loeng%==%zwei% goto accla
if %loeng%==%drei% goto back
goto loeschen

:accloa
cls
echo.
echo      Accountname:
echo.
set /p accload=
cls
echo.
echo       SIND SIE SICH SICHER %accload% ZU LOESCHEN?
echo.
echo.
echo                      Ja    Nein
set /p entsch=
if %entsch%==%no% goto loeschen
@echo off 
color 02
del Benutzername\Aci%accload%.bat
del Benutzername\%accload%.bat
del /S Benutzername\%accload%
delBenutzername\%accload%
echo DER ACCOUNT %accload% WURDE GELOESCHT AM %date% >> Benutzername\Admin\Erstellliste.txt
cls
echo.
echo     ALLES WURDE GELOESCHT
pause > nul 
goto loeschen

:accla
start Benutzername\Admin\Erstellliste.txt
goto loeschen

:back
call Benutzername\%eingabe%.bat




