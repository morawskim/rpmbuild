#
# spec file for package tcpproxy
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

Name:           tcpproxy
Version:        1.0
Release:        1
License:        MIT
Summary:        A simple golang tcp proxy
Url:            https://github.com/kahlys/tcpproxy
Group:          System/Management
Source:         https://github.com/kahlys/tcpproxy/archive/v%{version}.tar.gz
BuildRequires:  go1.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Simple tcp proxy package and executable binary in Golang. The executable provides both TCP and TCP/TLS connection.

%prep
%setup -q

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
export GOROOT='/usr/lib64/go/1.7'
mkdir -p $local_go/src/github.com/kahlys
ln -s $PWD $local_go/src/github.com/kahlys/tcpproxy

pushd $local_go/src/github.com/kahlys/tcpproxy
go build ./cmd/tcpproxy/
popd

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Nov 22 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
