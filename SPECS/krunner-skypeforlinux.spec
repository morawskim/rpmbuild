#
# spec file for package krunner-skypeforlinux
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

%define commit0 4fa35decf9220007802496b08b96480c342815ed

Name:           krunner-skypeforlinux
Version:        20171125
Release:        1
License:        MIT
Summary:        Krunner that search skype contacts and lets the user open chat
Url:            https://github.com/morawskim/krunner-skypeforlinux
Source:         https://github.com/morawskim/krunner-skypeforlinux/archive/%{commit0}.tar.gz
BuildRequires:  cmake
BuildRequires:  krunner-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  extra-cmake-modules
Requires:       plasma5-workspace
Requires:       skypeforlinux
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Krunner that search skype contacts and lets the user open chat

%prep
%setup -q -n %{name}-%{commit0}
#ln -s src/CMakeLists.txt ./CMakeLists.txt 

%build
%cmake_kf5 -d src/build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%make_jobs

%install
%kf5_makeinstall -C src/build

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_kf5_servicesdir}/plasma-runner-skype.desktop
%{_kf5_plugindir}/krunner_skype.so

%changelog
* Sun Nov 26 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
