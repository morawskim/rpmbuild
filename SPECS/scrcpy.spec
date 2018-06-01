#
# spec file for package scrcpy
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           scrcpy
Version:        1.1
Release:        1
License:        Apache-2.0
Summary:        Display and control your Android device
Url:            https://github.com/Genymobile/scrcpy
Group:          Hardware/Mobile
Source0:        https://github.com/Genymobile/scrcpy/archive/v%{version}.tar.gz
Source1:        https://github.com/Genymobile/scrcpy/releases/download/v%{version}/scrcpy-server-v%{version}.jar
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  pkgconfig(sdl2) >= 2.0.4
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This application provides display and control of Android devices connected on
USB. It does not require any root access

%prep
%setup -q

%build
export CFLAGS="%optflags -std=c99" CXXFLAGS="%optflags"
mkdir ./buildtmp
meson --buildtype release --strip -Db_lto=true \
    --prefix=%{_prefix} \
    -Dprebuilt_server=%{S:1} ./buildtmp

cd ./buildtmp
ninja
cd ..

%install
meson configure -Dinstallprefix=%{_usr}
cd ./buildtmp
DESTDIR=%{buildroot} ninja install

%post

%postun

%files
%defattr(-,root,root)
%doc README.md DEVELOP.md FAQ.md
%license LICENSE

%attr(755, root, root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Jun 01 2018 Marcin Morawski <marcin@morawskim.pl>
-  Fix build error on Leap 15
Argument "prefix" passed as both --prefix and -Dprefix, but only one is allowed

* Sat Mar 17 2018 Marcin Morawski <marcin@morawskim.pl>
- Fix (huge) memory leak (#26)
- Fix segfault on copy/paste (#10)
- Support screens with dimensions not divisible by 8 (#39)
- Fix mouse clicks on LG devices (#18)
- Reverse horizontal scrolling behavior (#49)
- Make it work over tcpip (#5)
- Bind middle- and right-clicks to HOME and BACK
- Remove black borders on double-click

