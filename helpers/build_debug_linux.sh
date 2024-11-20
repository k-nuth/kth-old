#!/bin/bash

BUILD_C_API=OFF
WITH_TESTS=OFF
WITH_CONSOLE=ON

# rm -rf build
# conan lock create conanfile.py --version="0.1" --update -s build_type=Debug
# conan lock create conanfile.py --version "0.1" -s build_type=Debug --lockfile=conan.lock --lockfile-out=build/conan.lock
# conan install conanfile.py -s build_type=Debug --lockfile=build/conan.lock -of build --build=missing

cmake --preset conan-debug \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DBINLOG=OFF \
         -DWITH_CONSOLE_CAPI=ON \
         -DWITH_CONSOLE=$WITH_CONSOLE \
         -DBUILD_C_API=$BUILD_C_API \
         -DDB_READONLY_MODE=OFF \
         -DENABLE_TESTS=$WITH_TESTS \
         -DWITH_TESTS=$WITH_TESTS \
         -DWITH_TOOLS=OFF \
         -DENABLE_ECMULT_STATIC_PRECOMPUTATION=OFF \
         -DLOG_LIBRARY="spdlog" \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Debug

cmake --build --preset conan-debug \
         -j4 \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DBINLOG=OFF \
         -DWITH_CONSOLE_CAPI=ON \
         -DBUILD_C_API=$BUILD_C_API \
         -DWITH_CONSOLE=$WITH_CONSOLE \
         -DDB_READONLY_MODE=OFF \
         -DENABLE_TESTS=$WITH_TESTS \
         -DWITH_TESTS=$WITH_TESTS \
         -DWITH_TOOLS=OFF \
         -DENABLE_ECMULT_STATIC_PRECOMPUTATION=OFF \
         -DLOG_LIBRARY="spdlog" \
         -DGLOBAL_BUILD=ON \
         -DCMAKE_BUILD_TYPE=Debug



# mkdir -p build_debug
# cd build_debug
# conan install .. -s build_type=Debug --build=missing

# cmake .. -GNinja \
#          -DCMAKE_VERBOSE_MAKEFILE=ON \
#          -DBINLOG=OFF \
#          -DWITH_CONSOLE_CAPI=ON \
#          -DBUILD_C_API=ON \
#          -DDB_READONLY_MODE=OFF \
#          -DENABLE_TESTS=OFF \
#          -DWITH_TESTS=OFF \
#          -DWITH_TOOLS=OFF \
#          -DENABLE_ECMULT_STATIC_PRECOMPUTATION=OFF \
#          -DDB_NEW=ON \
#          -DDB_NEW_BLOCKS=OFF \
#          -DDB_NEW_FULL=OFF \
#          -DLOG_LIBRARY="spdlog" \
#          -DCMAKE_BUILD_TYPE=Debug

# # cmake .. -DCMAKE_VERBOSE_MAKEFILE=ON -DWITH_CONSOLE_CAPI=OFF -DDB_READONLY_MODE=OFF  -DDB_NEW=ON  -DDB_NEW_BLOCKS=ON -DENABLE_TESTS=OFF -DWITH_TESTS=OFF -DWITH_TOOLS=OFF -DENABLE_ECMULT_STATIC_PRECOMPUTATION=OFF -DCMAKE_BUILD_TYPE=Debug
# ninja -j4
# # cmake --build .


