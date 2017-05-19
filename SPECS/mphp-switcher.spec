#
# spec file for package mphp-switcher
#
# Copyright (c) 2016 Marcin Morawski <marcin@morawskim.pl>
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
%global commit0 84cc77451fc2f1f12eac612b9a790bba9fae1164
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       mphp-switcher
Version:    0.2.0
Release:    2
License:    MIT
Summary:    Lorem
BuildArch:  noarch
Url:        http://github.com/morawskim/mphp-switcher
Source0:    https://github.com/morawskim/mphp-switcher/archive/%{shortcommit0}.tar.gz
Source1:    https://github.com/wilmoore/php-version/archive/0.12.1.tar.gz
Patch0:     mphp-switcher-fix-path.patch
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Lorem ipsum

%prep
%setup  -qn mphp-switcher-%{commit0}
%{__tar} xf %{S:1} 
%patch0

%build
exit 0

%install
%{__mkdir} -p %{buildroot}/etc/sysconfig
%{__mkdir} -p %{buildroot}/etc/systemd/system
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__mkdir} -p %{buildroot}/etc/bash_completion.d/
%{__mkdir} -p %{buildroot}/opt/php/php/{etc,usr/bin}


%{__cp} mphp-fpm %{buildroot}/etc/sysconfig
%{__cp} mphp-fpm-set-symlink %{buildroot}/%{_sbindir}
%{__cp} switch-php %{buildroot}/%{_sbindir}
%{__cp} php-fpm.service %{buildroot}/etc/systemd/system
%{__cp} php-version-0.12.1/php-version.sh %{buildroot}/etc/bash_completion.d/php-version.sh
%{__cp} php-version-0.12.1/LICENSE LICENSE-php-version
%{__cp} php-version-0.12.1/README.md README-php-version.md

%pre
%service_add_pre php-fpm.service

%postun
%service_del_postun php-fpm.service
%restart_on_update php-fpm
%insserv_cleanup

%preun
%service_del_preun php-fpm.service
%stop_on_removal php-fpm

%post
%service_add_post php-fpm.service
%{fillup_and_insserv -f php-fpm}

%files
%defattr(-,root,root)
%doc README* LICENSE*
%config(noreplace) /etc/sysconfig/mphp-fpm
/etc/systemd/system/php-fpm.service
%attr(0755, root, root) %{_sbindir}/switch-php 
/opt/php/php/etc
/opt/php/php/usr/bin
%attr(0644, root, root) /etc/bash_completion.d/php-version.sh
%attr(0750, root, root) %{_sbindir}/mphp-fpm-set-symlink

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Apr 18 2016 Marcin Morawski <marcin@morawskim.pl>
- Update to commit 84cc77451fc2f1f12eac612b9a790bba9fae1164
- Replace hardcoded /usr/sbin with macro _sbindir

* Sat Apr 16 2016 Marcin Morawski <marcin@morawskim.pl>
- Update to commit eb2385bab700b8fe6819508dd13e404d05149b5f
- add /opt/php/php dir to package
- add /etc/bash_completion.d/php-version.sh
- reformat SPEC file
- change Copyright info
- change url to submit bugfixes or comments