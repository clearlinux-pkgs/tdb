#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tdb
Version  : 1.4.5
Release  : 33
URL      : https://www.samba.org/ftp/tdb/tdb-1.4.5.tar.gz
Source0  : https://www.samba.org/ftp/tdb/tdb-1.4.5.tar.gz
Summary  : A trivial database
Group    : Development/Tools
License  : LGPL-3.0+
Requires: tdb-bin = %{version}-%{release}
Requires: tdb-lib = %{version}-%{release}
Requires: tdb-man = %{version}-%{release}
Requires: tdb-python = %{version}-%{release}
Requires: tdb-python3 = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : python3-dev
Patch1: 0001-add-mock-disable-static-option.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package bin
Summary: bin components for the tdb package.
Group: Binaries

%description bin
bin components for the tdb package.


%package dev
Summary: dev components for the tdb package.
Group: Development
Requires: tdb-lib = %{version}-%{release}
Requires: tdb-bin = %{version}-%{release}
Provides: tdb-devel = %{version}-%{release}
Requires: tdb = %{version}-%{release}

%description dev
dev components for the tdb package.


%package lib
Summary: lib components for the tdb package.
Group: Libraries

%description lib
lib components for the tdb package.


%package man
Summary: man components for the tdb package.
Group: Default

%description man
man components for the tdb package.


%package python
Summary: python components for the tdb package.
Group: Default
Requires: tdb-python3 = %{version}-%{release}

%description python
python components for the tdb package.


%package python3
Summary: python3 components for the tdb package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tdb package.


%prep
%setup -q -n tdb-1.4.5
cd %{_builddir}/tdb-1.4.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629846486
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-rpath \
--disable-rpath-install
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1629846486
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tdbbackup
/usr/bin/tdbdump
/usr/bin/tdbrestore
/usr/bin/tdbtool

%files dev
%defattr(-,root,root,-)
/usr/include/tdb.h
/usr/lib64/libtdb.so
/usr/lib64/pkgconfig/tdb.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtdb.so.1
/usr/lib64/libtdb.so.1.4.5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/tdbbackup.8
/usr/share/man/man8/tdbdump.8
/usr/share/man/man8/tdbrestore.8
/usr/share/man/man8/tdbtool.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
