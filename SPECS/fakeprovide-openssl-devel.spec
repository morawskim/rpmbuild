#
# spec file for package fakeprovide-openssl-devel
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

Name:           fakeprovide-openssl-devel
Version:        20170529183151
Release:        2%{?dist}
License:        GPL
Summary:        Fake provide for openssl-devel
Group:          Fake
Source:         %{name}
Requires:       libressl-devel
Provides:       openssl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{summary}

%prep
%setup -c -T

%build
cp %{SOURCE0} README

%install

%post

%postun

%files
%defattr(-,root,root)
%doc README

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20170529183151-2
- Rebuild for openSUSE 42.3

* Mon May 29 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
