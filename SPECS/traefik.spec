#
# spec file for package traefik
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

Name:           traefik
Version:        1.2.3
Release:        2
License:        MIT
Summary:        Træfik, a modern reverse proxy
Url:            https://traefik.io
Group:          Applications/Internet
Source:         https://github.com/containous/traefik/archive/v%{version}.tar.gz
BuildRequires:  go1.7
BuildRequires:  glide
BuildRequires:  golang-github-jteeuwen-go-bindata
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Træfik (pronounced like traffic) is a modern HTTP reverse proxy and load
balancer made to deploy microservices with ease. It supports several backends
(Docker, Swarm, Kubernetes, Marathon, Mesos, Consul, Etcd, Zookeeper, BoltDB,
Eureka, Amazon DynamoDB, Rest API, file...) to manage its configuration
automatically and dynamically.

%prep
%setup -q

%build
export GOPATH="$PWD/go"
export PATH="$GOPATH/bin:$PATH"
mkdir -p $GOPATH/src/github.com/containous
ln -s $PWD $GOPATH/src/github.com/containous/traefik
pushd go/src/github.com/containous/traefik
glide install --strip-vendor --strip-vcs

go generate
go build
popd

%install
install -D traefik %{buildroot}/%{_bindir}/%{name}
install -D traefik.sample.toml %{buildroot}/%{_sysconfdir}/%{name}/traefik.sample.toml

%pre
/usr/sbin/groupadd -r %name >/dev/null 2>/dev/null || :

if ! /usr/bin/getent passwd %name &>/dev/null; then
  echo "Creating %name user"
    /usr/sbin/useradd -c "%name" -g %name -d %{_sharedstatedir}/%{name} \
        -s /sbin/nologin -r -M %name 2> /dev/null || :
fi

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE.md traefik.sample.toml docs/ examples/
%{_bindir}/%{name}
%config(noreplace) %attr(640, %name, %name) %{_sysconfdir}/%{name}/traefik.sample.toml

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.2.3-2
- Rebuild for openSUSE 42.3

* Tue Jul 25 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release

