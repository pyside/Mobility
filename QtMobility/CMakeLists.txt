project(mobility)

install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
        DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")

link_directories(${QT_MOBILITY_LIBRARY_DIR})

# Old macro without support for custom typesystem paths and guesses the
# typesystem from the module name.
macro(CREATE_PYSIDE_MODULE MODULE_NAME MODULE_INCLUDE_DIR SRCS INC_DIRS LINK_LIBS)
    STRING(TOLOWER ${MODULE_NAME} LOWER_MODULE_NAME)
    CREATE_PYSIDE_MODULE_WITH_TYPESYSTEM(${MODULE_NAME}
                                         ${MODULE_INCLUDE_DIR}
                                         ${SRCS}
                                         ${INC_DIRS}
                                         ${LINK_LIBS}
                                         ""
                                         ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_${LOWER_MODULE_NAME}.xml)
endmacro(CREATE_PYSIDE_MODULE)

# New macro that accepts the typesystem and typesystem paths explicitly
macro(CREATE_PYSIDE_MODULE_WITH_TYPESYSTEM MODULE_NAME MODULE_INCLUDE_DIR SRCS INC_DIRS LINK_LIBS TYPESYSTEM_PATHS TYPESYSTEM)
    STRING(TOLOWER ${MODULE_NAME} LOWER_MODULE_NAME)
    STRING(TOLOWER ${BINDING_NAME} LOWER_BINDING_NAME)
    include_directories(${MODULE_NAME} ${${INC_DIRS}})
    add_library(${MODULE_NAME} MODULE ${${SRCS}})
    set_property(TARGET ${MODULE_NAME} PROPERTY PREFIX "")
    target_link_libraries(${MODULE_NAME} ${${LINK_LIBS}})

    add_custom_command(OUTPUT ${${SRCS}}
                        COMMAND ${GENERATOR} ${GENERATOR_EXTRA_FLAGS}
                        ${CMAKE_SOURCE_DIR}/${BINDING_NAME}/global.h
                        --include-paths=${MODULE_INCLUDE_DIR}:${QT_MOBILITY_INCLUDE_DIR}:${QT_MOBILITY_PARENT_INCLUDE_DIR}:${QT_INCLUDE_DIR}
                        --typesystem-paths=${${TYPESYSTEM_PATHS}}:${PYSIDE_TYPESYSTEMS}
                        --output-directory=${CMAKE_CURRENT_BINARY_DIR}
                        --license-file=${CMAKE_CURRENT_SOURCE_DIR}/../licensecomment.txt
                        ${TYPESYSTEM}
                        --api-version="QtMobility*,${QT_MOBILITY_MAJOR_VERSION}.${QT_MOBILITY_MINOR_VERSION}|PySide*,${QT_VERSION_MAJOR}.${QT_VERSION_MINOR}"
                        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                        COMMENT "Running generator for ${MODULE_NAME}..."
                       )

    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}${CMAKE_DEBUG_POSTFIX}.so DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")
    install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}/${MODULE_NAME}/${LOWER_BINDING_NAME}_${LOWER_MODULE_NAME}_python.h
            DESTINATION include/Py${BINDING_NAME}/${MODULE_NAME}/)

    execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_BINARY_DIR}/${MODULE_NAME}${CMAKE_DEBUG_POSTFIX}${CMAKE_SHARED_MODULE_SUFFIX}"
                                                               "${CMAKE_BINARY_DIR}/${BINDING_NAME}/${MODULE_NAME}${CMAKE_SHARED_MODULE_SUFFIX}")
endmacro(CREATE_PYSIDE_MODULE_WITH_TYPESYSTEM)


execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
                                                           "${CMAKE_BINARY_DIR}/${BINDING_NAME}/__init__.py")

macro(add_if_found component)
    STRING(TOUPPER ${component} _COMPONENT)
    IF(${QT_MOBILITY_${_COMPONENT}_FOUND})
        message("Module ${component} found.")
        add_subdirectory(${component})
    ELSE()
        message("Module ${component} not found. ${component} support disabled.")
    ENDIF()
endmacro()

IF(${QTVERSION} VERSION_LESS 4.7.0)
    add_if_found(Bearer)
ENDIF()

add_if_found(Contacts)
add_if_found(Connectivity)
add_if_found(Feedback)
add_if_found(Gallery)
add_if_found(Location)
add_if_found(Messaging)
add_if_found(MultimediaKit)
add_if_found(Organizer)
add_if_found(PublishSubscribe)
add_if_found(Sensors)
add_if_found(ServiceFramework)
add_if_found(SystemInfo)
add_if_found(Versit)

