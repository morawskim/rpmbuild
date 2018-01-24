#
# spec file for package httplive
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

%global commit0 72a4717fdc7c62ada1189d8602c9f2a2cdc63f11
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           httplive
Version:        20180122.%{shortcommit0}
Release:        1
License:        MIT
Summary:        HTTP Request & Response Service, Mock HTTP
Url:            https://github.com/gencebay/httplive
Group:          Development/Tools
Source:         https://github.com/gencebay/httplive/archive/%{shortcommit0}.tar.gz
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The HttpLive is a tool for API designers, Proxy, mobile and web application developers to develop and test their applications faster without being dependent on any server or backend applications.

%prep
%setup -q -n %{name}-%{commit0}

%build
export GOPATH="$PWD/go"
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/gencebay/
ln -s $PWD $GOPATH/src/github.com/gencebay/httplive

pushd go/src/github.com/gencebay/httplive
go get -d -v github.com/gin-gonic/gin
go get -d -v github.com/boltdb/bolt
go get -d -v github.com/urfave/cli
go get -d -v github.com/gorilla/websocket
CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o %{name} .
popd

%install
%{__install} -Dp -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}

%changelog
* Wed Jan 24 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
