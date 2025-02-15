###  ###
# FILE #
###  ###

set(FILE_ROOT
  ${CMAKE_SOURCE_DIR}/src/${PROMETHEUS_LANG}/File/File
)

file(GLOB FILE_SOURCES_PUBLIC_TEMP
  ${FILE_ROOT}/public/src/*.cpp
)

file(GLOB FILE_HEADERS_PUBLIC_TEMP
  ${FILE_ROOT}/public/include/*.hpp
)

set(FILE_SOURCES
  ${FILE_SOURCES_PUBLIC_TEMP}
)

set(FILE_HEADERS
  ${FILE_HEADERS_PUBLIC_TEMP}
)

set(FILE_INCLUDEDIR_PUBLIC
  ${FILE_ROOT}/public/include
)

###        ###
# FILEHEADER #
###        ###

set(FILEHEADER_ROOT
  ${CMAKE_SOURCE_DIR}/src/${PROMETHEUS_LANG}/File/FileHeader
)

file(GLOB FILEHEADER_SOURCES_PUBLIC_TEMP
  ${FILEHEADER_ROOT}/public/src/*.cpp
)

file(GLOB FILEHEADER_HEADERS_PUBLIC_TEMP
  ${FILEHEADER_ROOT}/public/include/*.hpp
)

set(FILEHEADER_SOURCES
  ${FILEHEADER_SOURCES_PUBLIC_TEMP}
)

set(FILEHEADER_HEADERS
  ${FILEHEADER_HEADERS_PUBLIC_TEMP}
)

set(FILEHEADER_INCLUDEDIR_PUBLIC
  ${FILEHEADER_ROOT}/public/include
)

###        ###
# FILESOURCE #
###        ###

set(FILESOURCE_ROOT
  ${CMAKE_SOURCE_DIR}/src/${PROMETHEUS_LANG}/File/FileSource
)

file(GLOB FILESOURCE_SOURCES_PUBLIC_TEMP
  ${FILESOURCE_ROOT}/public/src/*.cpp
)

file(GLOB FILESOURCE_HEADERS_PUBLIC_TEMP
  ${FILESOURCE_ROOT}/public/include/*.hpp
)

set(FILESOURCE_SOURCES
  ${FILESOURCE_SOURCES_PUBLIC_TEMP}
)

set(FILESOURCE_HEADERS
  ${FILESOURCE_HEADERS_PUBLIC_TEMP}
)

set(FILESOURCE_INCLUDEDIR_PUBLIC
  ${FILESOURCE_ROOT}/public/include
)

set(FILE_SOURCES
  ${FILE_SOURCES}
  ${FILEHEADER_SOURCES}
  ${FILESOURCE_SOURCES}
  PARENT_SCOPE
)

set(FILE_HEADERS
  ${FILE_HEADERS}
  ${FILEHEADER_HEADERS}
  ${FILESOURCE_HEADERS}
  PARENT_SCOPE
)

set(FILE_INCLUDEDIR_PUBLIC
  ${FILE_INCLUDEDIR_PUBLIC}
  ${FILEHEADER_INCLUDEDIR_PUBLIC}
  ${FILESOURCE_INCLUDEDIR_PUBLIC}
  PARENT_SCOPE
)
