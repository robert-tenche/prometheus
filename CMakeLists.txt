cmake_minimum_required(VERSION 3.30.0)

if (${PROMETHEUS_COMPILER} STREQUAL "clang++")
  include(cmake/compiler/${PROMETHEUS_COMPILER}.cmake)
endif()

project(prometheus)

add_subdirectory(src/sandbox)
