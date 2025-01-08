add_library(pch STATIC
  ${CMAKE_CURRENT_SOURCE_DIR}/public/src/pch.cpp
  ${CMAKE_CURRENT_SOURCE_DIR}/public/include/pch.hpp
)

target_precompile_headers(pch
  PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/public/src/pch.cpp
)

target_include_directories(pch PUBLIC
  ${CMAKE_CURRENT_SOURCE_DIR}/public/include
)
