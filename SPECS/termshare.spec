#
# spec file for package termshare
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>.
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

Name:           termshare
Version:        0.2.0
Release:        1
License:        BSD
Summary:        Quick and easy terminal sharing
Url:            https://termsha.re
Group:          Productivity/Networking/Other
Source0:        https://github.com/progrium/termshare/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.SuSEfirewall
Source3:        %{name}.sysconfig
Patch0:         %{name}-websocket-package-name.patch
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Quick and easy terminal sharing for getting quick help or pair sysadmin'ing.

Share interactive control with a copilot and/or a readonly view of your
terminal with others. Copilots and viewers can use the client or a web-based
terminal.

The service is run by the support of the community via Gittip donations.

%prep
%setup -q
%patch0 -p0

%build
go get -v golang.org/x/net/websocket
go get -v github.com/heroku/hk/term
go get -v github.com/kr/pty
go get -v github.com/nu7hatch/gouuid
make

%install
%{__install} -p -D -m 755 %{name}-%{version} %{buildroot}/%{_bindir}/%{name}
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/usr/lib/systemd/system/%{name}.service"
%__install -D -m0644 "%{SOURCE2}" "%{buildroot}/etc/sysconfig/SuSEfirewall2.d/services/%{name}"
%__install -D -m0644 "%{SOURCE3}" "%{buildroot}/etc/sysconfig/%{name}"

%pre
%service_add_pre termshare.service

%post
%service_add_post termshare.service

%preun
%service_del_preun termshare.service
%stop_on_removal termshare

%postun
%service_del_postun termshare.service
%restart_on_update termshare

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}
%attr(0644, root, root) /usr/lib/systemd/system/%{name}.service
%attr(0644, root, root) /etc/sysconfig/SuSEfirewall2.d/services/%{name}
%config(noreplace) /etc/sysconfig/%{name}

%changelog
* Wed Nov 16 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
