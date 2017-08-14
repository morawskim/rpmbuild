#
# spec file for package undocker
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

Name:           undocker
Version:        4
Release:        3
License:        GPLv3
Summary:        Unpacks a Docker image
Url:            https://github.com/larsks/undocker
Group:          Development/Tools/Building
Source:         https://github.com/larsks/undocker/archive/%{name}-%{version}.tar.gz
BuildRequires:  python-base
BuildRequires:  python-setuptools
Requires:       python-base
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unpacks a Docker image.

%prep
%setup -qn %{name}-%{name}-%{version}

%build
pwd
python ./setup.py build

%install
%{__install} -D -p -m 0755 ./build/lib/undocker.py   %{buildroot}/%{_bindir}/undocker

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/undocker

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 4-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed Nov 23 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
