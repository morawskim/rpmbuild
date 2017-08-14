#
# spec file for package par2
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/morawskim/rpmbuild/issues
#

Name:           par2
Version:        0.4
Release:        3
License:        GPL-2.0
Summary:        Create and use partiy files to secure data against loss
Url:            http://sourceforge.net/projects/parchive/
Group:          System/Backup
Source:         http://downloads.sourceforge.net/project/parchive/par2cmdline/%{version}/par2cmdline-%{version}.tar.gz
Patch:          par2-fix-compile.diff
BuildRequires:  gcc-c++ libstdc++-devel dos2unix automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
par2 is a program for creating and using PAR2 files to detect
damage in data files and repair them if necessary. It can be used with
any kind of file.

Author:
  Peter Brian Clements <peterbclements@users.sourceforge.net>


%prep
%setup -n par2cmdline-%{version}
dos2unix ChangeLog AUTHORS ROADMAP README
chmod -x ChangeLog AUTHORS ROADMAP README
%patch -p1
autoreconf -fi
%configure

%build
CXXFLAGS="$RPM_OPT_FLAGS -O3 -Wno-parentheses -Werror -funroll-loops"
%if 0%{?suse_version} >= 1010
CXXFLAGS="$CXXFLAGS -ftree-vectorize"
PROFILE_GENERATE="-fprofile-generate"
PROFILE_USE="-fprofile-use"
%endif
%ifarch x86_64
CXXFLAGS="$CXXFLAGS -momit-leaf-frame-pointer"
%endif
%ifarch %ix86
CXXFLAGS="$CXXFLAGS -momit-leaf-frame-pointer -mmmx"
%endif
make CXXFLAGS="$CXXFLAGS $PROFILE_GENERATE"

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
/usr/bin/par2
/usr/bin/par2create
/usr/bin/par2repair
/usr/bin/par2verify
%doc README AUTHORS ROADMAP ChangeLog


