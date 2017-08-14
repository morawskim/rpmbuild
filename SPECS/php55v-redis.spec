#
# spec file for package php55v-redis
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

%define pkg_name redis
%define phpize /opt/php/php55v/usr/bin/phpize
%define phpconfig /opt/php/php55v/usr/bin/php-config
%define conf_dir /opt/php/php55v/etc/php5/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php55v-redis
Version:        2.2.7
Release:        3
License:        PHP License, version 3.01
Summary:        API for php to communicate with redis
Url:            https://github.com/nicolasff/phpredis
Group:          Productivity/Networking/Web/Servers
Source:         https://github.com/phpredis/phpredis/archive/%{version}.tar.gz#/%{name}-%{version}
BuildRequires:  php55v-devel
Requires:       redis >= 2.0
Requires:       php55v(api) = %{php_core_api}
Requires:       php55v(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The phpredis extension provides an API for communicating with the Redis
key-value store.

%prep
%setup -qn phpredis-%{version}

%build
export PATH="/opt/php/php55v/usr/bin/:$PATH"
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
%{conf_dir}/%{pkg_name}.ini
%{ext_dir}/%{pkg_name}.so

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.2.7-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Oct 15 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release

