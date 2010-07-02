set(DOC_DISABLED FALSE)
if(NOT QT_MOBILITY_SRC_DIR)
    message(WARNING "QT_MOBILITY_SRC_DIR variable not set, apidoc generation targets disabled.")
    set(DOC_DISABLED TRUE)
endif()

find_program(graphviz_exec NAME dot PATHS "/usr/bin/")
if(${graphviz_exec} STREQUAL "graphviz_exec-NOTFOUND")
    message(WARNING "Missing graphviz tool (dot), apidoc generation targets disabled.")
    set(DOC_DISABLED TRUE)
endif()

if(NOT DOC_DISABLED)
    add_custom_target(apidoc
                      COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}/rst
                      COMMAND sphinx-build -b html  ${CMAKE_CURRENT_BINARY_DIR}/rst htmldocs
                     )

    #create conf.py based on conf.py.in
    configure_file("conf.py.in" "rst/conf.py" @ONLY)

    #copy pysidem.qdocconf to mobility source dir.
    configure_file("pysidem.qdocconf" "${QT_MOBILITY_SRC_DIR}/doc/src/pysidem.qdocconf" @ONLY)
    set(DOC_DATA_DIR "${CMAKE_CURRENT_BINARY_DIR}/qt4xmldoc")
    add_custom_target(qdoc3
                      COMMAND qdoc3 pysidem.qdocconf
                      WORKING_DIRECTORY "${QT_MOBILITY_SRC_DIR}/doc/src/"
                      COMMENT "Running qdoc3 against QtMobility source code..."
                      SOURCE "pysidem.qdocconf")

    macro(create_doc module typesystem_path include_dir)
        string(REGEX REPLACE "^Qt" "" module_name ${module})
        string(TOLOWER ${module_name} module_name)
        add_custom_target("${module}-apidoc"
                            COMMAND ${GENERATOR} ${mobility_SOURCE_DIR}/global.h
                            ${mobility_SOURCE_DIR}/${module}/typesystem_${module_name}.xml
                            --generatorSet=qtdoc
                            --include-paths=${QT_INCLUDE_DIR}:${include_dir}:${QT_MOBILITY_INCLUDE_DIR}
                            --typesystem-paths=${PYSIDE_TYPESYSTEMS}
                            --library-source-dir=${QT_MOBILITY_SRC_DIR}
                            --documentation-only
                            --documentation-data-dir=${DOC_DATA_DIR}
                            --documentation-out-dir=${CMAKE_CURRENT_BINARY_DIR}/rst
                            --documentation-code-snippets-dir=${CMAKE_CURRENT_SOURCE_DIR}/codesnippets
                            WORKING_DIRECTORY ${${module}_SOURCE_DIR}
                            COMMENT "Running generator to generate documentation of ${module}..."
                         )
        add_dependencies("${module}-apidoc" qdoc3)
        add_dependencies(apidoc "${module}-apidoc")
    endmacro(create_doc module)

    create_doc(Bearer ${Bearer_SOURCE_DIR} ${QT_MOBILITY_BEARER_INCLUDE_DIR})
    create_doc(Contacts ${Contacts_SOURCE_DIR} ${QT_MOBILITY_CONTACTS_INCLUDE_DIR})
    create_doc(Location ${Location_SOURCE_DIR} ${QT_MOBILITY_LOCATION_INCLUDE_DIR})
    create_doc(MultimediaKit ${MultimediaKit_SOURCE_DIR} ${QT_MOBILITY_MULTIMEDIAKIT_INCLUDE_DIR})
    create_doc(Sensors ${Sensors_SOURCE_DIR} ${QT_MOBILITY_SENSORS_INCLUDE_DIR})
    create_doc(SystemInfo ${SystemInfo_SOURCE_DIR} ${QT_MOBILITY_SYSTEMINFO_INCLUDE_DIR})

    #install files
    add_custom_target(apidocinstall
        COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/share/doc/${BINDING_NAME} && cp -rv ${CMAKE_BINARY_DIR}/apidoc/* ${CMAKE_INSTALL_PREFIX}/share/doc/${BINDING_NAME}
    )

endif()
