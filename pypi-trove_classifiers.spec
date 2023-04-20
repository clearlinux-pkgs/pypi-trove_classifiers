#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-trove_classifiers
Version  : 2023.4.20
Release  : 11
URL      : https://files.pythonhosted.org/packages/f1/11/510639e751169550c933c98cba5947415301879e62fde97239d94cedad8c/trove-classifiers-2023.4.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/11/510639e751169550c933c98cba5947415301879e62fde97239d94cedad8c/trove-classifiers-2023.4.20.tar.gz
Summary  : Canonical source for classifiers on PyPI (pypi.org).
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-trove_classifiers-license = %{version}-%{release}
Requires: pypi-trove_classifiers-python = %{version}-%{release}
Requires: pypi-trove_classifiers-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Canonical source for [classifiers][1] on [PyPI][2].
Classifiers [categorize projects][3] per [PEP 301][4]. Use this package to
validate classifiers in packages for PyPI upload or download.

%package license
Summary: license components for the pypi-trove_classifiers package.
Group: Default

%description license
license components for the pypi-trove_classifiers package.


%package python
Summary: python components for the pypi-trove_classifiers package.
Group: Default
Requires: pypi-trove_classifiers-python3 = %{version}-%{release}

%description python
python components for the pypi-trove_classifiers package.


%package python3
Summary: python3 components for the pypi-trove_classifiers package.
Group: Default
Requires: python3-core
Provides: pypi(trove_classifiers)

%description python3
python3 components for the pypi-trove_classifiers package.


%prep
%setup -q -n trove-classifiers-2023.4.20
cd %{_builddir}/trove-classifiers-2023.4.20
pushd ..
cp -a trove-classifiers-2023.4.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682011976
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-trove_classifiers
cp %{_builddir}/trove-classifiers-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-trove_classifiers/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-trove_classifiers/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
