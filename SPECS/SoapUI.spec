#
# spec file for package SoapUI
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

# If you change soapui_root, remember to edit desktop file too.
%define soapui_root /usr/lib/SoapUI

Name:           SoapUI
Version:        5.3.0
Release:        1
License:        EUPL
Summary:        SoapUI, is the world leading Open Source Functional Testing tool for API Testing
Url:            https://www.soapui.org/
Group:          Applications/Internet
Source0:        http://cdn01.downloads.smartbear.com/soapui/%{version}/SoapUI-%{version}-linux-bin.tar.gz
Source1:        https://smartbear.com/SmartBear/media/images/Home/SUI-Icon-Color.svg
Source2:        %{name}.desktop
Source3:        %{name}-logo.png
Provides:       soapui
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SoapUI is the world's most widely-used open source API testing tool for SOAP
and REST APIs. SoapUI offers SOAP Web Services functional testing, REST API
functional testing, WSDL coverage, message assertion testing and test
refactoring. With over 10 years of experience backed by a vast open source
community, SoapUI is the de facto method for ensuring quality when developing
APIs and Web Services.

%prep
%setup -q

%build

%install
%{__mkdir} -p %{buildroot}/%{soapui_root}
cp -r . %{buildroot}/%{soapui_root}
%{__install} -D -m0644 %{S:2} %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -D -m0644 %{S:1} %{buildroot}/%{soapui_root}
%{__install} -D -m0644 %{S:3} %{buildroot}/%{soapui_root}/icon.png

%post
%{desktop_database_post}

%postun
%{desktop_database_postun}

%files
%defattr(-,root,root)
%doc RELEASENOTES.txt README.md LICENSE.md
%{soapui_root}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Apr 19 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
