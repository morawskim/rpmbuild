#
# spec file for package libpuzzle
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
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
%global ini_name     %{name}.ini

Name:           libpuzzle
Version:        0.11
Release:        1
License:        BSD
Summary:        Library to quickly find visually similar images (gif, png, jpg)
Url:            http://libpuzzle.pureftpd.org/project/libpuzzle
Source0:        http://download.pureftpd.org/pub/pure-ftpd/misc/libpuzzle/releases/%{name}-%{version}.tar.bz2
Source1:        puzzle.pc.in
Patch0:          libpuzzle-pkgconfig.patch
Requires:       gd
BuildRequires:  gd-devel
Provides:       puzzle-diff = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Puzzle library is designed to quickly find visually similar images
(gif, png, jpg), even if they have been resized, recompressed,
recolored or slightly modified. The library is free, lightweight yet
very fast, configurable, easy to use and it has been designed with
security in mind.

%package        devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} puzzle.pc.in
%patch0

%build
%{__cat} <<'EOF' >%{ini_name}
extension=libpuzzle.so
EOF

%__autoconf
%configure --disable-static
make %{?_smp_mflags}
make DESTDIR=%{_builddir}/%{name}-%{version} install INSTALL="install -p"

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -m 644 -D puzzle.pc %{buildroot}%{_libdir}/pkgconfig/puzzle.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README THANKS
%{_libdir}/*.so.*
%{_mandir}/man8/*
%{_bindir}/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/puzzle.pc
%{_mandir}/man3/*
