
# spec file for package extract-x509-cert
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

%global commit0 f2785afbee62923b82dd97429e722ba71f71c2ac
%global gist    6c9eeb09ad9e4ad6f6e8

Name:           extract-x509-cert
Version:        20150628
Release:        1
License:        MIT license
Summary:        Shell script to extract x509 certificate
Url:            https://gist.github.com/morawskim/%{gist}
Source0:        https://gist.github.com/morawskim/%{gist}/archive/%{commit0}.zip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Shell script to extract x509 certificate

%prep
%setup  -qn %{gist}-%{commit0}

%build
exit 0

%install
%{__install} -D -p -m 0755  extract_x509_cert.sh  %{buildroot}/%{_bindir}/extract-x509-cert

%post
exit 0

%postun
exit 0

%files
%defattr(0755,root,root)
%{_bindir}/extract-x509-cert

%changelog
* Wed May 25 2016 Marcin Morawski <marcin@morawskim.pl>
- init release
