#
# spec file for package snowbox
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

Name:           snowbox
Version:        2.0.2
Release:        1
License:        GPLv3
Summary:        A POP3 server written in Go
Url:            https://kiza.eu/software/snowbox
Group:          Productivity/Networking/Email/Servers
Source:         https://kiza.eu/media/software/snowbox/snowbox-%{version}.tar.gz
Source1:        snowbox.service
BuildRequires:  go
#BuildRequires:  pkgconfig(libsystemd-daemon)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Snowbox is a POP3 server written in Go.

Features:
- Written in a secure language
- APOP authentication
- SSL support
- IPv6
- Small codebase (800 lines)
- Easy setup

%prep
%setup -q

%build
make
%{__cp} %{S:1} %{name}.service
sed -i 's|/usr/local/sbin|%{_sbindir}|g' %{name}.service

%install
install -p -D -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -p -D -m 600 config %{buildroot}%{_sysconfdir}/%{name}/config
install -p -D -m 600 user.auth %{buildroot}%{_sysconfdir}/%{name}/user.auth
install -p -D -m 644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8.gz
install -p -D -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{S:1}

%post
%service_add_post %{S:1}

%preun
%service_del_preun %{S:1}
%stop_on_removal %{name}

%postun
%service_del_postun %{S:1}
%restart_on_update %{name}

%files
%defattr(-,root,root)
%doc changelog README COPYING AUTHOR
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/user.auth
%{_sbindir}/%{name}
%{_mandir}/man8/*.8*
%{_unitdir}/%{name}.service


%changelog
* Fri May 05 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
