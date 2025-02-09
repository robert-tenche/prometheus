@echo off

cmake -S . -B _cmake_build -G "Unix Makefiles" -D PROMETHEUS_COMPILER=clang++ -D PROMETHEUS_LANG=C89 -D CMAKE_BUILD_TYPE=Debug

if %ERRORLEVEL% NEQ 0 exit

cmake --build _cmake_build --parallel 8

