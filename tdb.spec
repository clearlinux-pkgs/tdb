#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tdb
Version  : 1.4.2
Release  : 16
URL      : https://www.samba.org/ftp/tdb/tdb-1.4.2.tar.gz
Source0  : https://www.samba.org/ftp/tdb/tdb-1.4.2.tar.gz
Summary  : A Trivial Database similar to GDBM but allows simultaneous commits
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
This subsystem ensures that we can always use a certain core set of
functions and types, that are either provided by the OS or by replacement
functions / definitions in this subsystem. The aim is to try to stick
to POSIX functions in here as much as possible. Convenience functions
that are available on no platform at all belong in other subsystems
(such as LIBUTIL).

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
%setup -q -n tdb-1.4.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571005613
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --disable-rpath --disable-rpath-install
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1571005613
rm -rf %{buildroot}
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/lib/python2.7/site-packages/tdb.so
rm -f %{buildroot}/usr/lib/python2.7/site-packages/_tdb_text.py

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
/usr/lib64/libtdb.so.1.4.2

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
