#
# spec file for package json-tools
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

%define commit df1456e88cc5ee457e64f86f5f61ed458488de89

Name:           json-tools
Version:        20131118
Release:        2
License:        Public Domain
Summary:        JSON Utilities
Url:            https://github.com/larsks/json-tool
Group:          Productivity/Text/Utilities
Source:         https://github.com/larsks/json-tools/archive/%{commit}.tar.gz
Provides:       jsonx
Provides:       jsong
Requires:       python-dpath
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a small set of utilities for interacting with JSON on the command line.
I find it particularly useful for working with JSON-enabled REST APIs -- such
as those used by OpenStack -- on the command line.

%prep
%setup -qn %{name}-%{commit}

%build

%install
%{__install} -D -p -m 0755 jsong   %{buildroot}/%{_bindir}/jsong
%{__install} -D -p -m 0755 jsonx   %{buildroot}/%{_bindir}/jsonx

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/jsong
%{_bindir}/jsonx

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Fri Nov 25 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
