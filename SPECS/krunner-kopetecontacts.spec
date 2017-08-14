#
# spec file for package krunner-kopetecontacts
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

%global commit0 ad1152fdb49557318c03e1225e95f6e942597957

Name:           krunner-kopetecontacts
Version:        0.1
Release:        3
License:        GPL
Summary:        Search contacts from kopete in krunner
Url:            https://github.com/morawskim/kopetecontacts
Group:          System/X11/Utilities
Source:         https://github.com/morawskim/kopetecontacts/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  kopete-devel
BuildRequires:  patterns-openSUSE-devel_kde
BuildRequires:  patterns-openSUSE-devel_C_C++
BuildRequires:  patterns-openSUSE-devel_basis
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Searches your Kopete buddylist for contacts matching your phase.

%prep
%setup -qn kopetecontacts-%{commit0}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
cd build
make install DESTDIR=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_kde4_servicesdir}/plasma-runner-kopetecontacts.desktop
%{_kde4_modulesdir}/krunner_kopetecontacts.so

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 0.1-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Nov 20 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
