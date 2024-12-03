@echo off

cmake -S . -B _cmake_build -G "Unix Makefiles" -D PROMETHEUS_COMPILER=clang++ -D CMAKE_BUILD_TYPE=Debug

cd _cmake_build

make

cd ..
