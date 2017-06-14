#
# spec file for package toxiproxy
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

Name:           toxiproxy
Version:        2.1.1
Release:        1
License:        MIT
Summary:        A TCP proxy to simulate network and system conditions for chaos and resiliency testing
Url:            http://toxiproxy.io
Group:          Applications/Internet
Source:         https://github.com/Shopify/toxiproxy/archive/v%{version}.tar.gz
BuildRequires:  go1.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Toxiproxy is a framework for simulating network conditions. It's made
specifically to work in testing, CI and development environments, supporting
deterministic tampering with connections, but with support for randomized chaos
and customization. Toxiproxy is the tool you need to prove with tests that your
application doesn't have single points of failure. We've been successfully
using it in all development and test environments at Shopify since October,
2014. See our blog post on resiliency for more information.

Toxiproxy usage consists of two parts. A TCP proxy written in Go (what this
repository contains) and a client communicating with the proxy over HTTP. You
configure your application to make all test connections go through Toxiproxy
and can then manipulate their health via HTTP. See Usage below on how to set up
your project.

%prep
%setup -q

%build
export GOPATH="$PWD/go"
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/Shopify
ln -s $PWD $GOPATH/src/github.com/Shopify/toxiproxy

pushd go/src/github.com/Shopify/toxiproxy
make build
popd

%install
%{__install} -Dp -m 755 %{name}-server %{buildroot}%{_bindir}/%{name}
%{__install} -Dp -m 755 %{name}-cli %{buildroot}%{_bindir}/%{name}-cli

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md LICENSE README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-cli

%changelog
* Wed Jun 14 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
