#
# spec file for package jmeter
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

%define _jmeter_prefix %{_usr}/lib/jmeter

Name:           jmeter
Version:        3.0
Release:        2
License:        Apache License 2.0
Summary:        Apache JMeter
Url:            http://jmeter.apache.org/
Group:          Development/Tools
Source0:        http://ftp.piotrkosoft.net/pub/mirrors/ftp.apache.org//jmeter/binaries/apache-jmeter-%{version}.tgz
Source1:        jmeter.desktop
Requires:       java >= 1.7.0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Apache JMeter is a 100% pure Java desktop application 
designed to load test functional behavior and measure 
performance. It was originally designed for testing 
Web Applications but has since expanded to other test 
functions.

%package docs
Summary:    Documents for %{name}
Group:      Development/Documentation

%description docs
Documents for %{name}.

%prep
%setup -q -n apache-%{name}-%{version}

%build


%install
%__install -d -m 755 %{buildroot}%{_jmeter_prefix}/bin
%__install -d -m 755 %{buildroot}%{_jmeter_prefix}/lib
%__install -d -m 755 %{buildroot}%{_jmeter_prefix}/extras
%__install -d -m 755 %{buildroot}%{_jmeter_prefix}/licenses
%__install -d -m 755 %{buildroot}%{_bindir}
%__install -d -m 755 %{buildroot}%_datarootdir/applications

%__cp -pr bin/* "%{buildroot}%{_jmeter_prefix}/bin"
%__cp -pr lib/* "%{buildroot}%{_jmeter_prefix}/lib"
%__cp -pr extras/* %{buildroot}%{_jmeter_prefix}/extras
%__cp -pr licenses/* "%{buildroot}%{_jmeter_prefix}/licenses"
%__cp -p docs/images/jmeter_square.svg %{buildroot}%{_jmeter_prefix}/bin/jmeter_square.svg
%__cp -p %{SOURCE1} %{buildroot}%_datarootdir/applications/%{name}.desktop
ln -s %{_jmeter_prefix}/bin/jmeter %{buildroot}%{_bindir}/%{name}

# create filelist
find %{buildroot}%{_jmeter_prefix}/bin -mindepth 1 -maxdepth 1 -type d | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find %{buildroot}%{_jmeter_prefix}/bin -maxdepth 1 -type f | grep -v '/jmeter$' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST

%pre

%post

%postun

%files -f FILELIST
%defattr(-,root,root)
%dir %{_jmeter_prefix}
%{_jmeter_prefix}/lib
%{_jmeter_prefix}/extras
%{_jmeter_prefix}/licenses
%attr(755, root, root) %{_jmeter_prefix}/bin/jmeter
%{_bindir}/%{name}
%_datarootdir/applications/%{name}.desktop
%doc LICENSE NOTICE README

%files docs
%defattr(-,root,root)
%doc docs/ printable_docs/

%changelog
* Sat Oct 29 2016 Marcin Morawski <marcin@morawskim.pl>
-  Change desktop file

* Sat Jun 25 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
