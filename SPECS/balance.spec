#
# spec file for package balance
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

Name:           balance
Version:        3.57
Release:        1
License:        GPLv2
Summary:        TCP load-balancing proxy server with round robin and failover mechanisms
Url:            http://www.inlab.de/balance.html
Group:          Applications/Internet
Source:         https://www.inlab.net/wp-content/uploads/2018/05/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms.  The program behaviour can
be controlled at runtime using a simple command line syntax.

%debug_package

%prep
%setup -q

%build
%{__make} %{?_smp_mflags} CFLAGS="%optflags"

%install
%{__mkdir} -p %{buildroot}%{_localstatedir}/run/%{name}
%{__install} -Dp -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
%{__install} -Dp -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%post

%postun

%files
%defattr(-,root,root)
%doc README COPYING
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%dir %{_localstatedir}/run/%{name}

%changelog
* Mon Jun 04 2018 Marcin Morawski <marcin@morawskim.pl>
-  Update to 3.57 and change source url

* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 3.52-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Thu Apr 13 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
