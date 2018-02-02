@echo off
title 
:start
echo(
echo                                 *PROCURADOR DE GUIAS NO OP.GG 2000*
echo  (Para que a ferramente funcione corretamente e necessario que nao utilize espacos e nem apostrofo [ ' ])
echo(
set /p champion= - Nome do champion: 
set /p lane= - Lane do(a) %champion%: 


echo(
echo  Procurando guias para %champion% %lane%...
start http://www.op.gg/champion/%champion%/statistics/%lane%
TIMEOUT /t 5
cls
goto start