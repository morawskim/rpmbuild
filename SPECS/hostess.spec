#
# spec file for package hostess
#
# Copyright (c) 2018 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           hostess
Version:        0.3.0
Release:        1
License:        MIT
Summary:        An idempotent command-line utility for managing your hosts file
Url:            https://github.com/cbednarski/hostess
Group:          Productivity/Networking/Other
Source:         https://github.com/cbednarski/hostess/archive/v%{version}.tar.gz
BuildRequires:  go >= 1.4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An idempotent command-line utility for managing your /etc/hosts file.

hostess add local.example.com 127.0.0.1
hostess add staging.example.com 10.0.2.16

Why? Because you edit /etc/hosts for development, testing, and debugging.
Because sometimes DNS doesn't work in production. And because editing
/etc/hosts by hand is a pain. Put hostess in your Makefile or deploy scripts
and call it a day.

%prep
%setup -q

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
mkdir -p $local_go/src/github.com/cbednarski
ln -s $PWD $local_go/src/github.com/cbednarski/hostess
pushd $local_go/src/github.com/cbednarski/hostess
make build
popd

%install
make install prefix=%{buildroot}%{_usr} mandir=%{buildroot}%{_mandir}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Fri May 04 2018 Marcin Morawski <marcin@morawskim.pl>
-  init relase
