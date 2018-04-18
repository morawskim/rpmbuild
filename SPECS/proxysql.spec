#
# spec file for package proxysql
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

Name:           proxysql
Version:        1.4.8
Release:        1
License:        GPLv3+
Summary:        High-performance MySQL proxy
Url:            http://www.proxysql.com
Group:          Development/Tools
Source0:        https://github.com/sysown/proxysql/archive/v%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.1
BuildRequires:  openssl-devel
BuildRequires:  cmake
BuildRequires:  systemd
BuildRequires:  libconfig-devel
BuildRequires:  libdaemon-devel
BuildRequires:  sqlite-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ProxySQL is a high performance, high availability, protocol aware proxy for
MySQL and forks (like Percona Server and MariaDB).

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -p -D -m 0755 src/proxysql -t %{buildroot}%{_bindir}
install -p -D -m 0640 etc/proxysql.cnf -t %{buildroot}%{_sysconfdir}
install -p -D -m 0755 tools/proxysql_galera_checker.sh -t %{buildroot}%{_datadir}/%{name}/tools
install -p -D -m 0755 tools/proxysql_galera_writer.pl -t %{buildroot}%{_datadir}/%{name}/tools
install -p -D -m 0644 %{SOURCE1} -t %{buildroot}%{_unitdir}
install -p -D -m 0644 %{SOURCE2} -t %{buildroot}%{_mandir}/man1
install -d -D -m 0755 %{buildroot}/var/lib/proxysql

%pre
/usr/sbin/groupadd -r proxysql >/dev/null 2>&1 || :
/usr/sbin/useradd  -g proxysql -r -d /var/lib/proxysql -s /sbin/nologin \
    -c "ProxySQL" proxysql >/dev/null 2>&1 || :

%service_add_pre proxysql.service


%post
%service_add_post proxysql.service

%preun
%service_del_preun proxysql.service
%stop_on_removal mailhog

%postun
%service_del_postun proxysql.service
%restart_on_update proxysql


%files
%defattr(-,root,root)
%doc LICENSE README.md RUNNING.md FAQ.md doc/
%{_bindir}/*
%{_unitdir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%defattr(-,proxysql,proxysql,-)
/var/lib/%{name}
%defattr(-,proxysql,root,-)
%config(noreplace) %{_sysconfdir}/%{name}.cnf


%changelog
* Wed Apr 18 2018 Marcin Morawski <marcin@morawskim.pl>
-  init release
