#
# spec file for package php70v-gearman
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

%define pkg_name gearman
%define php_dir_prefix /opt/php/php70v
%define phpize %{php_dir_prefix}/usr/bin/phpize
%define phpconfig %{php_dir_prefix}/usr/bin/php-config
%define conf_dir %{php_dir_prefix}/etc/php7/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php70v-gearman
Version:        2.0.1
Release:        4
License:        PHP License, version 3.01
Summary:        Wrapper to the gearman library
Url:            https://github.com/wcgallego/pecl-gearman
Group:          Productivity/Networking/Web/Servers
Source:         https://github.com/wcgallego/pecl-gearman/archive/gearman-%{version}.tar.gz
BuildRequires:  php70v-devel
BuildRequires:  gearmand-devel
Requires:       php70v(api) = %{php_core_api}
Requires:       php70v(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Gearman PHP Extension provides a wrapper to libgearman. This
gives the user the ability to write fully featured Gearman clients
and workers in PHP, allowing them to quickly develop distributed
applications.

For more information about Gearman, see: http://www.gearman.org/

%prep
%setup -qn pecl-gearman-gearman-%{version}

%build
export PATH="/opt/php/php70v/usr/bin/:$PATH"
%{phpize}
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
%{__mkdir} -p %{buildroot}/%{conf_dir}
cat > %{buildroot}/%{conf_dir}/%{pkg_name}.ini <<EOF
;comment out next line to disable %{pkg_name} extension in php
extension = %{pkg_name}.so
EOF

%post

%postun

%files
%defattr(0644,root,root)
%config(noreplace) %{conf_dir}/%{pkg_name}.ini
%{ext_dir}/%{pkg_name}.so
%doc README LICENSE CREDITS ChangeLog examples

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.0.1-4
- Rebuild for openSUSE 42.3

* Wed May 24 2017 Marcin Morawski <marcin@morawskim.pl>
-  Remove dependency on libgearman7. Rpmbuild will itself add dependency in the
   required version

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun May 07 2017 Marcin Morawski <marcin@morawskim.pl>
-  changed package name from php7-gearman to php70v-gearman

* Sat Apr 01 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
