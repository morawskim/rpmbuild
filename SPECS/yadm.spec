#
# spec file for package yadm
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

Name:           yadm
Version:        1.04
Release:        2
License:        GPLv3
Summary:        Yet Another Dotfiles Manager
Url:            https://github.com/TheLocehiliosan/yadm
Group:          Development/Tools
Source:         https://github.com/TheLocehiliosan/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       git
Requires:       bash
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
yadm is a dotfile management tool with 3 main features: Manages files across
systems using a single Git repository. Provides a way to use alternate files on
a specific OS or host. Supplies a method of encrypting confidential data so it
can safely be stored in your repository.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 yadm   %{buildroot}%{_bindir}
install -m 644 yadm.1 %{buildroot}%{_mandir}/man1

%post

%postun

%files
%defattr(-,root,root)
%doc README.md yadm.md LICENSE CHANGES
%attr(755,root,root) %{_bindir}/yadm
%attr(644,root,root) %{_mandir}/man1/*

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Wed Aug 24 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release

