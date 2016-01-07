#
# spec file for package mphp-switcher
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%global commit0 579abc5c09198962f13d4b8bba28377f72e5dea0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           mphp-switcher
Version:	0.1.0
Release:	1
License:	MIT
Summary:	Lorem
BuildArch: 	noarch
Url:		http://github.com/morawskim/mphp-switcher
Source0:	https://github.com/morawskim/mphp-switcher/archive/%{shortcommit0}.tar.gz
Source1:	https://github.com/wilmoore/php-version/archive/0.12.1.tar.gz
Patch0:		mphp-switcher-fix-path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%{__mkdir} -p %{buildroot}/usr/sbin
%{__mkdir} -p %{buildroot}/etc/profile.d/


%{__cp} mphp-fpm %{buildroot}/etc/sysconfig
%{__cp} mphp-fpm-set-symlink %{buildroot}/usr/sbin
%{__cp} php-fpm.service %{buildroot}/etc/systemd/system
%{__cp} php-version-0.12.1/php-version.sh %{buildroot}/etc/profile.d/
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
/etc/profile.d/php-version.sh
%attr(0750, root, root) /usr/sbin/mphp-fpm-set-symlink


