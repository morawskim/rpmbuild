#
# spec file for package caddy
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

# Original SPEC file borrowed from https://fedora.pkgs.org/27/fedora-x86_64/caddy-0.10.10-1.fc27.x86_64.rpm.html

# caddy
%global import_path github.com/mholt/caddy

Name:           caddy
Version:        0.10.10
Release:        1
License:        ASL 2.0 and MIT
Summary:        HTTP/2 web server with automatic HTTPS
Url:            https://caddyserver.com
Group:          Productivity/Networking/Web/Servers
Source0:        https://%{import_path}/archive/v%{version}/caddy-%{version}.tar.gz
Source10:       %{name}.conf
Source11:       %{name}.service
Source12:       %{name}-index.html
BuildRequires:  go >= 1.8
BuildRequires:  go1.8
BuildRequires:  systemd
Provides:       webserver
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Caddy is the HTTP/2 web server with automatic HTTPS.  Official Caddy builds
with customized plugins can be downloaded from https://caddyserver.com.

%prep
%setup -q

%build
local_go=$PWD/go
export GOPATH="$local_go:$GOPATH"
export GOROOT='/usr/lib64/go/1.8'
mkdir -p $local_go/src/%(dirname %{import_path})
ln -s $PWD $local_go/src/%{import_path}

export LDFLAGS="-X %{import_path}/caddy/caddymain.gitTag=v%{version}"
go build -o bin/caddy ./caddy

%install
install -D -m 0755 bin/caddy %{buildroot}%{_bindir}/caddy
install -D -m 0644 %{S:10} %{buildroot}%{_sysconfdir}/caddy/caddy.conf
install -D -m 0644 %{S:11} %{buildroot}%{_unitdir}/caddy.service
install -D -m 0644 %{S:12} %{buildroot}%{_datadir}/caddy/index.html
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/conf.d
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

%pre
/usr/sbin/groupadd -r caddy >/dev/null 2>/dev/null || :

if ! /usr/bin/getent passwd caddy &>/dev/null; then
  echo "Creating caddy user"
    /usr/sbin/useradd -c "Caddy web server" -g caddy -d /var/lib/empty \
        -s /sbin/nologin -r -M caddy 2> /dev/null || :
fi

# systemd requirment
%service_add_pre caddy.service

%post
# systemd requirment
%service_add_post caddy.service

%preun
%service_del_preun caddy.service
%stop_on_removal caddy

%postun
%service_del_postun caddy.service
%restart_on_update caddy

%files
%defattr(-,root,root)
%doc dist/README.txt LICENSE.txt
%{_bindir}/caddy
%{_datadir}/caddy
%{_unitdir}/caddy.service
%dir %{_sysconfdir}/caddy
%dir %{_sysconfdir}/caddy/conf.d
%config(noreplace) %{_sysconfdir}/caddy/caddy.conf
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy

%changelog
* Wed Dec 27 2017 Marcin Morawski <marcin@morawskim.pl>
-  Init release
