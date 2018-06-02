#
# spec file for package nullmailer
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

Name:           nullmailer
Version:        2.0
Release:        2
License:        GPLv2+
Summary:        Simple relay-only mail transport agent
Url:            http://untroubled.org/nullmailer/
Group:          System/Base
Source0:        http://untroubled.org/nullmailer/archive/nullmailer-%{version}.tar.gz
Source1:        %{name}.service
BuildRequires:  gcc-c++ gnutls-devel
PreReq:         permissions
Requires:       systemd
Provides:       smtp_daemon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is nullmailer, a sendmail/qmail/etc replacement MTA for hosts which
relay to a fixed set of smart relays.  It is designed to be simple to
configure, secure, and easily extendable.

%prep
%setup -q

%build
%configure --enable-tls
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
mkdir -p %{buildroot}/var/spool/nullmailer/queue
mkdir -p %{buildroot}/var/spool/nullmailer/tmp

%verifyscript
%verify_permissions -e /usr/sbin/nullmailer-queue
%verify_permissions -e /usr/bin/mailq

%pre
%service_add_pre %{name}.service
/usr/sbin/groupadd -f -r nullmailer||:
/usr/sbin/useradd -s /bin/nologin -M -r -d /var/spool/nullmailer -c "nullmailer" -g nullmailer nullmailer ||:

%post
%set_permissions /usr/sbin/nullmailer-queue
%set_permissions /usr/bin/mailq
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO doc/DIAGRAM
%dir %{_sysconfdir}/%{name}
%attr(4711,nullmailer,nullmailer)%{_sbindir}/nullmailer-queue
%attr(4711,nullmailer,nullmailer)%{_bindir}/mailq
%{_sbindir}/sendmail
%{_sbindir}/nullmailer-send
%{_bindir}/nullmailer-*
%{_unitdir}/%{name}.service
%dir /usr/lib/%{name}/
/usr/lib/%{name}/*
%doc %{_mandir}/*/*
%attr(0750,nullmailer,nullmailer)/var/spool/nullmailer
%attr(0750,nullmailer,nullmailer)/var/spool/nullmailer/queue
%attr(0750,nullmailer,nullmailer)/var/spool/nullmailer/tmp
%attr(0640,nullmailer,nullmailer)/var/spool/nullmailer/trigger

%changelog
* Sat Jun 02 2018 Marcin Morawski <marcin@morawskim.pl>
-  Change provide to smtp_daemon

* Thu Dec 21 2017 Marcin Morawski <marcin@morawskim.pl>
-  Init release
