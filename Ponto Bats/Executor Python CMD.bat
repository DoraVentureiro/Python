@echo off

:start
color A
cd C:\Users\Public\Documents\Python
set /p num1= Número? 

cls
@echo(
@echo  Executando Número %num1%
@echo(

call py n%num1%.py
pause
cls
goto start
