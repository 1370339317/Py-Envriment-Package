rd /s /q "./Python27 Environment"
del /q /s "./Python27Environment.zip"
xcopy "./Python27 Environment Source" "./Python27 Environment" /Y /E /I /Q
cd "./Python27 Environment"
start cmd /c clean.bat
TIMEOUT /T 4

@del /q /s "*.py"

cd ../
7z a -tZip Python27Environment.zip "./Python27 Environment" -mx8
rd /s /q "./Python27 Environment"