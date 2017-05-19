#
# spec file for package mailhog
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

%define mailhoguser mailhog
%define mailhoggroup mailhog

Name:           mailhog
Version:        0.2.0
Release:        2
License:        MIT
Summary:        Web and API based SMTP testing
Url:            https://github.com/mailhog/MailHog
Group:          Development/Tools/SMTP
Source0:        https://github.com/mailhog/MailHog/archive/v%{version}.tar.gz
Source1:        https://github.com/mailhog/MailHog/releases/download/v%{version}/MailHog_linux_amd64
Source2:        mailhog.service
Source3:        mailhog-http.SuSEfirewall
BuildRequires:  go
BuildRequires:  bzr
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MailHog is an email testing tool for developers:

* Configure your application to use MailHog for SMTP delivery
* View messages in the web UI, or retrieve them with the JSON API
* Optionally release messages to real SMTP servers for delivery

%prep
%setup  -qn MailHog-%{version}

%build

%install
%__install -D -m0755 "%{SOURCE1}" "%{buildroot}%{_bindir}/%{name}"
%__install -D -m0644 "%{SOURCE2}" "%{buildroot}/usr/lib/systemd/system/%{name}.service"
%__install -D -m0644 "%{SOURCE3}" "%{buildroot}/etc/sysconfig/SuSEfirewall2.d/services/%{name}"

%pre

/usr/sbin/groupadd -r %mailhoggroup >/dev/null 2>/dev/null || :

if ! /usr/bin/getent passwd %mailhogduser &>/dev/null; then
  echo "Creating %mailhoguser user"
    /usr/sbin/useradd -c "Mailhog" -g %mailhoggroup -d /var/lib/empty \
        -s /sbin/nologin -r -M %mailhoguser 2> /dev/null || :
fi

# systemd requirment
%if 0%{?suse_version} >= 1210
%service_add_pre mailhog.service
%endif

%post
# systemd requirment
%if 0%{?suse_version} >= 1210
%service_add_post mailhog.service
%endif

%preun
%service_del_preun mailhog.service
%stop_on_removal mailhog

%postun
%service_del_postun mailhog.service
%restart_on_update mailhog

%files
%defattr(-,root,root)
%doc LICENSE.md README.md docs/
%attr(0755, root, root) %{_bindir}/%{name}
%attr(0644, root, root) /usr/lib/systemd/system/%{name}.service
%attr(0644, root, root) /etc/sysconfig/SuSEfirewall2.d/services/%{name}

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Fri Apr 14 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
