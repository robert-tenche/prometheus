cmake_minimum_required(VERSION 3.30.0)

# Compiler
if (${PROMETHEUS_COMPILER} STREQUAL "clang++")
  include(cmake/compiler/${PROMETHEUS_COMPILER}.cmake)
else()
  message(FATAL_ERROR "PROMETHEUS_COMPILER='${PROMETHEUS_COMPILER}' is not supported!")
endif()

# Language
if (${PROMETHEUS_LANG} STREQUAL "ANSI_C")
  # ok
else()
  message(FATAL_ERROR "PROMETHEUS_LANG='${PROMETHEUS_LANG}' is not supported!")
endif()

project(prometheus)

add_subdirectory(src/pch)
add_subdirectory(src/${PROMETHEUS_LANG})
add_subdirectory(src/sandbox)
