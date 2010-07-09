project(mobility)

install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
        DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")

link_directories(${QT_MOBILITY_LIBRARY_DIR})

macro(CREATE_PYSIDE_MODULE MODULE_NAME MODULE_INCLUDE_DIR SRCS INC_DIRS LINK_LIBS)
    STRING(TOLOWER ${MODULE_NAME} LOWER_MODULE_NAME)
    STRING(TOLOWER ${BINDING_NAME} LOWER_BINDING_NAME)
    include_directories(${MODULE_NAME} ${${INC_DIRS}})
    add_library(${MODULE_NAME} MODULE ${${SRCS}})
    set_property(TARGET ${MODULE_NAME} PROPERTY PREFIX "")
    target_link_libraries(${MODULE_NAME} ${${LINK_LIBS}})

    add_custom_command(OUTPUT ${${SRCS}}
                        COMMAND ${GENERATOR} ${GENERATOR_EXTRA_FLAGS}
                        ${CMAKE_SOURCE_DIR}/${BINDING_NAME}/global.h
                        --include-paths=${QT_INCLUDE_DIR}:${QT_MOBILITY_INCLUDE_DIR}:${MODULE_INCLUDE_DIR}
                        --typesystem-paths=${typesystem_path}:${PYSIDE_TYPESYSTEMS}
                        --output-directory=${CMAKE_CURRENT_BINARY_DIR}
                        --license-file=${CMAKE_CURRENT_SOURCE_DIR}/../licensecomment.txt
                        ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_${LOWER_MODULE_NAME}.xml
                        --api-version=${QT_MOBILITY_MAJOR_VERSION}.${QT_MOBILITY_MINOR_VERSION}
                        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                        COMMENT "Running generator for ${MODULE_NAME}..."
                       )

    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}${CMAKE_DEBUG_POSTFIX}.so DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/${MODULE_NAME}/${LOWER_BINDING_NAME}_${LOWER_MODULE_NAME}_python.h
            DESTINATION include/Py${BINDING_NAME}/${MODULE_NAME}/)

    execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}${CMAKE_DEBUG_POSTFIX}${CMAKE_SHARED_MODULE_SUFFIX}"
                                                               "${CMAKE_BINARY_DIR}/${BINDING_NAME}/${MODULE_NAME}${CMAKE_SHARED_MODULE_SUFFIX}")
endmacro(CREATE_PYSIDE_MODULE)


execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
                                                           "${CMAKE_BINARY_DIR}/${BINDING_NAME}/__init__.py")

IF(${QTVERSION} VERSION_LESS 4.7.0)
    add_subdirectory(Bearer)
ENDIF()
add_subdirectory(Contacts)
add_subdirectory(Location)
add_subdirectory(Messaging)
IF(${QT_MOBILITY_VERSION} VERSION_GREATER 1.0.0)
    add_subdirectory(MultimediaKit)
ENDIF()
add_subdirectory(PublishSubscribe)
add_subdirectory(Sensors)
add_subdirectory(ServiceFramework)
add_subdirectory(SystemInfo)
add_subdirectory(Versit)

