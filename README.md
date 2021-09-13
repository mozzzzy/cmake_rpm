# cmake_rpm
Config files to build rpm packages of cmake.

## Download package from Github Release
### RPM package
```bash
$ curl -s https://api.github.com/repos/mozzzzy/cmake_rpm/releases | \
  jq '.[].assets[] | select(.name == "self-built-cmake-3.20.0-1.el7.x86_64.rpm")' | \
  jq '.url' | \
  xargs curl -vLJO -H 'Accept: application/octet-stream'
```

## Build
### Get source code of gcc
```bash
$ git submodule update --init
```

### Build rpm packages
```bash
$ make all
```
Then the rpm packages are created in `rpmbuild/RPMS/x86_64` and `rpmbuild/SRPMS`.
```bash
$ tree rpmbuild -I BUILD
rpmbuild
|-- BUILDROOT
|-- RPMS
|   `-- x86_64
|       |-- self-built-cmake-3.20.0-1.el7.x86_64.rpm
|       `-- self-built-cmake-debuginfo-3.20.0-1.el7.x86_64.rpm
|-- SOURCES
|   `-- CMake.tar.gz
|-- SPECS
|   `-- self-built-cmake.spec
`-- SRPMS
    `-- self-built-cmake-3.20.0-1.el7.src.rpm

6 directories, 5 files
```
