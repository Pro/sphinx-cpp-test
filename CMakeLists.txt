
project(sphinx-test C CXX)
cmake_minimum_required(VERSION 3.19)

add_library(test_lib
        include/BaseClass.hpp
        include/SubClass.hpp
        )
set_target_properties(test_lib PROPERTIES LINKER_LANGUAGE CXX)
target_compile_features(test_lib PRIVATE cxx_std_17)