#
# spec file for package MozillaFirefoxDeveloperEdition
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
%define firefox_root /opt/firefox-developer-edition

Name:           MozillaFirefoxDeveloperEdition
Version:        60.0b16
Release:        1
License:        MPL
Summary:        Mozilla Firefox Developer Edition Web Browser
Url:            https://www.mozilla.org/pl/firefox/developer/
Group:          Productivity/Networking/Web/Browsers
Source:         https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/pl/firefox-%{version}.tar.bz2
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -qn firefox

%build

%install
mkdir -p %{buildroot}/%{firefox_root}
cp -r . %{buildroot}/%{firefox_root}

%post

%postun

%files
%defattr(-,root,root)
%dir %{firefox_root}
%{firefox_root}/*

%changelog
* Sun Apr 29 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
