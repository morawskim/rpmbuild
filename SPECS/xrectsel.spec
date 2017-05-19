#
# spec file for package xrectsel
#
# Copyright (c) 2017 Marcin Morawski <marcin@morawskim.pl>.
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

%define commit0 3f38859ddd88dbc2bb2c5268f80bd04fe1467cc8

Name:           xrectsel
Version:        0.1.0
Release:        2
License:        BSD
Summary:        Select a screen area with mouse and return the geometry of this area
Url:            https://bbs.archlinux.org/viewtopic.php?id=85378
Group:          System/X11/Utilities
Source:         https://github.com/morawskim/xrectsel/archive/%{commit0}.zip
BuildRequires:  libX11-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Select a screen area with mouse and return the geometry of this area

%prep
%setup -qn %{name}-%{commit0}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/xrectsel

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Jan 23 2017 Marcin Morawski <marcin@morawskim.pl>
-  init
