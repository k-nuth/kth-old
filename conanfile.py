# Copyright (c) 2016-2024 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import os
from conan import ConanFile
from conan.tools.build.cppstd import check_min_cppstd
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy
from kthbuild import KnuthConanFileV2, option_on_off

required_conan_version = ">=2.0"
def option_on_off(option):
    return "ON" if option else "OFF"

class KnuthConan(ConanFile):
    version="0.1"
    name = "kth"
    license = "http://www.boost.org/users/license.html"
    url = "https://github.com/k-nuth/kth"
    description = "Bitcoin Cross-Platform C++ Development Toolkit"
    settings = "os", "compiler", "build_type", "arch"

    options = {"shared": [True, False],
               "fPIC": [True, False],
               "tests": [True, False],
               "with_examples": [True, False],
               "with_icu": [True, False],
               "with_png": [True, False],
               "with_litecoin": [True, False],
               "with_qrencode": [True, False],
               "enable_benchmark": [True, False],
               "enable_tests": [True, False],
               "enable_openssl_tests": [True, False],
               "enable_experimental": [True, False],
               "enable_endomorphism": [True, False],
               "enable_ecmult_static_precomputation": [True, False],
               "enable_module_ecdh": [True, False],
               "enable_module_schnorr": [True, False],
               "enable_module_recovery": [True, False],
               "currency": ['BCH', 'BTC', 'LTC']
    }
            #    "with_asm": ['x86_64', 'arm', 'no', 'auto'],
            #    "with_field": ['64bit', '32bit', 'auto'],
            #    "with_scalar": ['64bit', '32bit', 'auto'],
            #    "with_bignum": ['gmp', 'no', 'auto'],


    default_options = {
        "shared": False,
        "fPIC": True,
        "tests": False,
        "with_examples": False,
        "with_icu": False,
        "with_png": False,
        "with_litecoin": False,
        "with_qrencode": False,
        "enable_benchmark": False,
        "enable_tests": True,
        "enable_openssl_tests": False,
        "enable_experimental": False,
        "enable_endomorphism": False,
        "enable_ecmult_static_precomputation": True,
        "enable_module_ecdh": False,
        "enable_module_schnorr": True,
        "enable_module_recovery": True,
        "currency": "BCH"
    }

        # "with_asm='auto'",
        # "with_field='auto'",
        # "with_scalar='auto'"
        # "with_bignum='auto'"

    # generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "cmake/*", "kth-coreConfig.cmake.in", "include/*", "test/*"
    # package_files = "build/lkth-core.a"
    # build_policy = "missing"

    def build_requirements(self):
        if self.options.tests:
            self.test_requires("catch2/3.6.0")

    def requirements(self):
        # self.requires("secp256k1/0.16.0", transitive_headers=True, transitive_libs=True)
        self.requires("boost/1.86.0", transitive_headers=True, transitive_libs=True)
        self.requires("fmt/10.2.1", transitive_headers=True, transitive_libs=True)
        self.requires("spdlog/1.14.1", transitive_headers=True, transitive_libs=True)
        self.requires("lmdb/0.9.32", transitive_headers=True, transitive_libs=True)
        self.requires("gmp/6.3.0", transitive_headers=True, transitive_libs=True)
        self.requires("expected-lite/0.8.0", transitive_headers=True, transitive_libs=True)
        self.requires("ctre/3.9.0", transitive_headers=True, transitive_libs=True)

        # self.requires("unordered/cci.20230612", transitive_headers=True, transitive_libs=True)

        # self.requires("infrastructure/0.25.0", transitive_headers=True, transitive_libs=True)
        # self.requires("domain/0.27.0", transitive_headers=True, transitive_libs=True)
        # self.requires("database/0.31.0", transitive_headers=True, transitive_libs=True)
        # self.requires("consensus/0.25.0", transitive_headers=True, transitive_libs=True)
        # self.requires("blockchain/0.29.0", transitive_headers=True, transitive_libs=True)
        # self.requires("network/0.34.0", transitive_headers=True, transitive_libs=True)
        # self.requires("node/0.34.0", transitive_headers=True, transitive_libs=True)

        # if self.options.with_png:
        #     self.requires("libpng/1.6.34@kth/stable", transitive_headers=True, transitive_libs=True)

        # if self.options.with_qrencode:
        #     self.requires("libqrencode/4.0.0@kth/stable", transitive_headers=True, transitive_libs=True)

        # if self.options.asio_standalone:
        #     self.requires("asio/1.24.0", transitive_headers=True, transitive_libs=True)


    def validate(self):
        if self.settings.os == "Linux" and self.settings.compiler == "gcc" and self.settings.compiler.libcxx == "libstdc++":
            raise ConanInvalidConfiguration("We just support GCC C++11ABI.\n**** Please run `conan profile update settings.compiler.libcxx=libstdc++11 default`")

    def configure(self):
        self.options["fmt/*"].header_only = True
        self.options["spdlog/*"].header_only = True


    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        # tc.variables["CMAKE_VERBOSE_MAKEFILE"] = True
        # tc.variables["WITH_MEMPOOL"] = option_on_off(self.options.mempool)
        # tc.variables["DB_READONLY_MODE"] = option_on_off(self.options.db_readonly)
        # tc.variables["LOG_LIBRARY"] = self.options.log
        # tc.variables["USE_LIBMDBX"] = option_on_off(self.options.use_libmdbx)
        # tc.variables["STATISTICS"] = option_on_off(self.options.statistics)
        # tc.variables["CONAN_DISABLE_CHECK_COMPILER"] = option_on_off(True)

        tc.variables["USE_CONAN"] = "ON"
        tc.variables["NO_CONAN_AT_ALL"] = "OFF"
        tc.variables["CMAKE_VERBOSE_MAKEFILE"] = "ON"
        tc.variables["ENABLE_SHARED"] = option_on_off(self.options.shared)
        tc.variables["ENABLE_POSITION_INDEPENDENT_CODE"] = option_on_off(self.options.fPIC)
        tc.variables["WITH_TESTS"] = option_on_off(self.options.tests)
        tc.variables["WITH_EXAMPLES"] = option_on_off(self.options.with_examples)
        tc.variables["WITH_ICU"] = option_on_off(self.options.with_icu)
        tc.variables["WITH_PNG"] = option_on_off(self.options.with_png)
        tc.variables["WITH_LITECOIN"] = option_on_off(self.options.with_litecoin)
        tc.variables["WITH_QRENCODE"] = option_on_off(self.options.with_qrencode)

        # Secp256k1 --------------------------------------------
        tc.variables["ENABLE_POSITION_INDEPENDENT_CODE"] = option_on_off(self.options.fPIC)
        tc.variables["ENABLE_BENCHMARK"] = option_on_off(self.options.enable_benchmark)
        tc.variables["ENABLE_TESTS"] = option_on_off(self.options.enable_tests)
        tc.variables["ENABLE_OPENSSL_TESTS"] = option_on_off(self.options.enable_openssl_tests)
        tc.variables["ENABLE_EXPERIMENTAL"] = option_on_off(self.options.enable_experimental)
        tc.variables["ENABLE_ENDOMORPHISM"] = option_on_off(self.options.enable_endomorphism)
        tc.variables["ENABLE_ECMULT_STATIC_PRECOMPUTATION"] = option_on_off(self.options.enable_ecmult_static_precomputation)
        tc.variables["ENABLE_MODULE_ECDH"] = option_on_off(self.options.enable_module_ecdh)
        tc.variables["ENABLE_MODULE_SCHNORR"] = option_on_off(self.options.enable_module_schnorr)
        tc.variables["ENABLE_MODULE_RECOVERY"] = option_on_off(self.options.enable_module_recovery)

        if self.settings.os == "Windows":
            tc.variables["WITH_BIGNUM"] = "no"
            if self.settings.compiler == "Visual Studio" and (self.settings.compiler.version != 12):
                tc.variables["ENABLE_TESTS"] = "OFF"   #Workaround. test broke MSVC
        else:
            tc.variables["WITH_BIGNUM"] = "gmp"

        # tc.variables["WITH_ASM"] = option_on_off(self.options.with_asm)
        # tc.variables["WITH_FIELD"] = option_on_off(self.options.with_field)
        # tc.variables["WITH_SCALAR"] = option_on_off(self.options.with_scalar)
        # tc.variables["WITH_BIGNUM"] = option_on_off(self.options.with_bignum)
        # Secp256k1 -------------------------------------------- (END)

        tc.variables["CURRENCY"] = self.options.currency

        # tc.variables["KTH_BUILD_NUMBER"] = os.getenv('KTH_BUILD_NUMBER', '-')
        # cmake.configure(source_dir=self.conanfile_directory)
        tc.variables["KTH_BUILD_NUMBER"] = os.getenv('KTH_BUILD_NUMBER', '-')

        tc.generate()
        tc = CMakeDeps(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.h", "", "include")

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.ipp", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = ["kth-core"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
