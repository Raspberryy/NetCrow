@echo off 
color 02

copy Benutzername\Vorlagen\aci.txt Benutzername\Aci%bname%.bat
copy Benutzername\Vorlagen\passwort.txt Benutzername\%bname%.bat
mkdir Benutzername\%bname%
echo . > Benutzername\%bname%\%lapw%.txt
echo %rname% > Benutzername\%bname%\Informationen.txt
echo %email% >> Benutzername\%bname%\Informationen.txt
echo Geheime Dateien von %bname% > Benutzername\%bname%\info.txt
echo %bname% Erstellt am %date% >> Benutzername\Admin\Erstellliste.txt


