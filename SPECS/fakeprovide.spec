#
# spec file for package fakeprovide
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

%define commit  012beb6b34bb91d7b7179bf7c2c1aab6e213f3f6

Name:           fakeprovide
Version:        20160729
Release:        3
License:        GPLv3
Summary:        A tool for generating "fake" rpm packages to resolve dependency issues
Url:            https://github.com/larsks/fakeprovide
Group:          Development/Tools
Source:         https://github.com/larsks/fakeprovide/archive/%{commit}.zip#/%{name}-%{version}.zip
BuildRequires:  make
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fakeprovide lets you satisfy RPM dependencies by creating a wrapper package
that provides the named dependency of your choice. You can use this if you are
working with a package from a third party that for some reason has non-critical
unsatisfied dependencies.

%prep
%setup -qn %{name}-%{commit}

%build

%install
make install DESTDIR=%{buildroot}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md COPYING
%{_bindir}/fakeprovide

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20160729-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Nov 26 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
