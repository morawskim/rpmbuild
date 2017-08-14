#
# spec file for package icdiff
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

Name:           icdiff
Version:        1.9.0
Release:        2
License:        GPL
Summary:        improved colored diff
Url:            http://www.jefftk.com/icdiff
Group:          Productivity/Text/Utilities
Source:         https://github.com/jeffkaufman/icdiff/archive/release-1.9.0.tar.gz
BuildRequires:  python-virtualenv
BuildRequires:  python-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Improved colored diff

%prep
%setup -qn %{name}-release-%{version}

%build
virtualenv-2.7 --clear --verbose venv2.7
source ./venv2.7/bin/activate
pip install pyinstaller
pyinstaller -F icdiff

%install
%__install -D -m0755 "dist/%{name}" "%{buildroot}/%{_bindir}/%{name}"

%post

%postun

%files
%defattr(-,root,root)
%doc ChangeLog README.md
%attr(0755, root, root) %{_bindir}/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.9.0-2
- Rebuild for openSUSE 42.3

* Fri Jun 16 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
