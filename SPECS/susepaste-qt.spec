#
# spec file for package susepaste-qt
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

Name:           susepaste-qt
Version:        0.1.0
Release:        3
License:        MIT
Summary:        Simple GUI for susepaste cli
Url:            https://github.com/morawskim/susepaste-qt
Group:          Applications/Productivity
Source:         https://github.com/morawskim/susepaste-qt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  update-desktop-files
Requires:       susepaste
Provides:       susepaste-gui
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Simple GUI for susepas

%prep
%setup -q

%build
%{__cmake} CMakeLists.txt
make

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
%{__install} -D -m0644 susepaste-qt.desktop %{buildroot}%{_datadir}/applications/susepaste-qt.desktop
%{__install} -D susepaste-qt %{buildroot}%{_bindir}/susepaste-qt

%post
%{desktop_database_post}

%postun
%{desktop_database_postun}

%files
%defattr(-,root,root)
%{_datadir}/applications/susepaste-qt.desktop
%attr(644,root,root) %{_kde4_servicesdir}/ServiceMenus/susepaste-qt_paste.desktop
%{_bindir}/susepaste-qt


%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 0.1.0-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Thu Sep 15 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
