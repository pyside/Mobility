project(mobility)

install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/__init__.py"
        DESTINATION "${SITE_PACKAGE}/${BINDING_NAME}")

macro(CREATE_PYSIDE_MODULE MODULE_NAME SRCS INC_DIRS LINK_LIBS)
    STRING(TOLOWER ${MODULE_NAME} LOWER_MODULE_NAME)
    STRING(TOLOWER ${BINDING_NAME} LOWER_BINDING_NAME)
    include_directories(${MODULE_NAME} ${${INC_DIRS}})
    add_library(${MODULE_NAME} MODULE ${${SRCS}})
    set_property(TARGET ${MODULE_NAME} PROPERTY PREFIX "")
    target_link_libraries(${MODULE_NAME} ${${LINK_LIBS}})

    add_custom_command(OUTPUT ${${SRCS}}
                        COMMAND ${GENERATOR} ${GENERATOR_EXTRA_FLAGS}
                        ${CMAKE_SOURCE_DIR}/${BINDING_NAME}/global.h
                        --include-paths=${QT_INCLUDE_DIR}:${QT_MOBILITY_INCLUDE_DIR}:${CMAKE_SOURCE_DIR}/${BINDING_NAME}
                        --typesystem-paths=${typesystem_path}:${PYSIDE_TYPESYSTEMS}
                        --output-directory=${CMAKE_CURRENT_BINARY_DIR}
                        --license-file=${CMAKE_CURRENT_SOURCE_DIR}/../licensecomment.txt
                        ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_${LOWER_MODULE_NAME}.xml
                        --api-version=${SUPPORTED_QT_VERSION}
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

add_subdirectory(SystemInfo)
