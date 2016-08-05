#
# spec file for package hstr
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

Name:           hstr
Version:        1.19
Release:        1
License:        Apache-2.0
Summary:        BASH History Suggest Box
Url:            https://github.com/dvorka/hstr
Group:          System/Console
Source:         https://github.com/dvorka/%{name}/archive/%{version}.tar.gz
BuildRequires:  ncurses-devel automake pkg-config readline-devel
Requires:       ncurses
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Easily view, navigate, search and use your command history with shell history suggest box for Bash and Zsh

%prep
%setup -n %{name}-%{version}

%build
cd ./dist && ./1-dist.sh && cd ..
./configure
make

%install
make install prefix=%{buildroot}/usr

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/hh
%{_bindir}/hstr
%doc %attr(0644,root,root) /usr/share/man/man1/hh.1.gz
%doc %attr(0444,root,root) /usr/share/man/man1/hstr.1.gz

