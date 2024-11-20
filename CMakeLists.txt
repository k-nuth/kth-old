# Copyright (c) 2016-2024 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

cmake_minimum_required(VERSION 3.15)

project(kth VERSION 0.0.0 LANGUAGES CXX C)

set(CMAKE_VERBOSE_MAKEFILE ON)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CURRENCY "BCH" CACHE STRING "Specify the Cryptocurrency (BCH|BTC|LTC).")
if (${CURRENCY} STREQUAL "BCH")
    add_definitions(-DKTH_CURRENCY_BCH)
elseif (${CURRENCY} STREQUAL "BTC")
    add_definitions(-DKTH_CURRENCY_BTC)
elseif (${CURRENCY} STREQUAL "LTC")
    add_definitions(-DKTH_CURRENCY_LTC)
else()
    message(FATAL_ERROR "Invalid Cryptocurrency: ${CURRENCY}")
endif()

message(STATUS "Knuth: Cryptocurrency: ${CURRENCY}")

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(BUILD_NODE_EXE "Build the node executable." ON)
option(BUILD_C_API "Build the C-API." OFF)
option(ENABLE_POSITION_INDEPENDENT_CODE "Enable POSITION_INDEPENDENT_CODE property" ON)
option(WITH_CONSOLE "Compile console application." OFF)
option(WITH_LOCAL_MINING "Compile with local mining." ON)
option(ENABLE_TEST "Compile with enable test." OFF)
option(ENABLE_TESTS "Compile with enable test." OFF)
option(ENABLE_MODULE_RECOVERY "Compile with enable module recovery." ON)
option(WITH_TOOLS "Compile with tools." OFF)
option(WITH_CONSOLE_NODE_CINT "" OFF)
option(WITH_TESTS "Compile with unit tests." OFF)
option(WITH_EXAMPLES "Compile with examples." OFF)
option(ENABLE_SHARED "" OFF)
option(ENABLE_SHARED_NODE_CINT "" ON)

set(WITH_BIGNUM "no" CACHE STRING "Specify Bignum Implementation (gmp|no|auto).")
set(ENABLE_POSITION_INDEPENDENT_CODE ON)
# set(WITH_CONSOLE OFF)
set(WITH_LOCAL_MINING OFF)
set(ENABLE_TEST OFF)
set(ENABLE_TESTS OFF)
set(ENABLE_MODULE_RECOVERY ON)
set(WITH_TOOLS OFF)
# set(WITH_TESTS OFF)
set(WITH_EXAMPLES OFF)
set(ENABLE_SHARED OFF)
set(ENABLE_SHARED_NODE_CINT ON)

if (WITH_LOCAL_MINING)
	add_definitions(-DWITH_LOCAL_MINING)
endif()

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/ci_utils/cmake)
include(KnuthTools)

if (NOT DEFINED ENABLE_MODULE_RECOVERY)
  set(ENABLE_MODULE_RECOVERY ON CACHE BOOL "Enable ECDSA pubkey recovery module.")
endif()

find_package(gmp REQUIRED)

add_subdirectory(secp256k1)
add_subdirectory(infrastructure)
add_subdirectory(domain)
# add_subdirectory(consensus)
# add_subdirectory(network)
# add_subdirectory(database)
# add_subdirectory(blockchain)
# add_subdirectory(node)

# if (BUILD_NODE_EXE)
#     add_subdirectory(node-exe)
# endif()

# if (BUILD_C_API)
#     add_subdirectory(c-api)
# endif()

if (WITH_TESTS)
  enable_testing()
endif()
