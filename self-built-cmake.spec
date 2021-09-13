Name:    self-built-cmake
Version: 3.20.0
Release: 1%{?dist}
Summary: Cross-platform make system
License: BSD and MIT and zlib
URL:     http://www.cmake.org
Source0: CMake.tar.gz

BuildRequires:  make
BuildRequires:  openssl-devel

# Avoid "No build ID note found" error
%undefine _missing_build_ids_terminate_build

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%prep
%setup -q -n CMake


%build
./bootstrap --prefix=/opt
make %{?_smp_mflags}


%install
%make_install


%files
/opt/bin/*
/opt/doc/*
/opt/share/*


%changelog
