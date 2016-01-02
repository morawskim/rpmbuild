#
# spec file for package php5-redis
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

%define pkg_name redis
%define conf_dir %{_sysconfdir}/php5/conf.d
%define ext_dir %(%{__php_config} --extension-dir)
Name:           php5-redis
Version: 2.2.7
Release: 1
License: PHP License, version 3.01
Summary: API for php to communicate with redis
Url: https://github.com/nicolasff/phpredis
Source: https://github.com/phpredis/phpredis/archive/%{version}.tar.gz
BuildRequires: php5-devel
Requires: redis >= 2.0
Requires: php(api) = %{php_core_api}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php-api = %{php_core_api}
Requires: php-zend-abi = %{php_zend_api}
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
The phpredis extension provides an API for communicating with the Redis key-value store.

%prep
%setup -qn phpredis-%{version}

%build
%{__phpize}
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

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root)
%{conf_dir}/%{pkg_name}.ini
%{ext_dir}/%{pkg_name}.so

