#
# spec file for package owasp-zap
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

%define _owaspdir  /usr/share/owasp-zap

Name:           owasp-zap
Version:        2.6.0
Release:        1
License:        Apachev2
Summary:        Zed Attack Proxy
Url:            http://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project
Group:          System/Security
Source0:        https://github.com/zaproxy/zaproxy/releases/download/2.6.0/ZAP_%{version}_Linux.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Requires:       java-1_8_0-openjdk >= 1.8.0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing
tool for finding vulnerabilities in web applications. It is designed to be used
by people with a wide range of security experience and as such is ideal for
developers and functional testers who are new to penetration testing. ZAP
provides automated scanners as well as a set of tools that allow you to find
security vulnerabilities manually.

%prep
%setup -q -n ZAP_%{version}

%build

%install
install -d $RPM_BUILD_ROOT%{_owaspdir}
cp -r db lang lib license plugin scripts xml $RPM_BUILD_ROOT%{_owaspdir}
cp README $RPM_BUILD_ROOT%{_owaspdir}
install -m 644 zap-%{version}.jar $RPM_BUILD_ROOT%{_owaspdir}
install -m 755 zap.sh $RPM_BUILD_ROOT%{_owaspdir}
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
install -m 644 $RPM_SOURCE_DIR/%{name}.png $RPM_BUILD_ROOT/usr/share/pixmaps
install -d %{buildroot}/usr/share/applications/
install -m 644 $RPM_SOURCE_DIR/%{name}.desktop %{buildroot}/usr/share/applications/

%post

%postun

%files
%defattr(-,root,root)
%doc README
%{_owaspdir}/*
%dir %{_datadir}/applications/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/owasp-zap
