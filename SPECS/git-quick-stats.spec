#
# spec file for package git-quick-stats
#
# Copyright (c) 2019 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           git-quick-stats
Version:        2.0.9
Release:        1
License:        MIT
Summary:        Git quick statistics is a simple and efficient way to access various statistics in git repository
Url:            https://github.com/arzzen/git-quick-stats
Source:         https://github.com/arzzen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       git
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
git-quick-stats is a simple and efficient way to access various statistics in
git repository.

Any git repository contains tons of information about commits, contributors,
and files. Extracting this information is not always trivial, mostly because of
a gadzillion options to a gadzillion git commands – I don’t think there is a
single person alive who knows them all. Probably not even Linus Torvalds
himself :).

%prep
%setup -q

%build


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 git-quick-stats   %{buildroot}%{_bindir}
install -m 644 git-quick-stats.1 %{buildroot}%{_mandir}/man1

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/git-quick-stats
%attr(644,root,root) %{_mandir}/man1/*

%changelog
* Fri Sep 20 2019 Marcin Morawski <marcin@morawskim.pl>
-  init release

