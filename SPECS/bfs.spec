#
# spec file for package bfs
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

Name:           bfs
Version:        1.1
Release:        2
License:        WTFPL
Summary:        Breadth-first version of find
Url:            https://github.com/tavianator/bfs
Group:          Productivity/File utilitie
Source:         https://github.com/tavianator/bfs/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Breadth-first search for your files.

bfs is a variant of the UNIX find command that operates breadth-first rather
than depth-first. It is otherwise intended to be compatible with GNU find. If
you're not familiar with find, have a look at the GNU find manual to get
acquainted first.

%prep
%setup -q

%build
make release %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc RELEASES.md README.md COPYING
%{_bindir}/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.1-2
- Rebuild for openSUSE 42.3

* Sun Jul 23 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
