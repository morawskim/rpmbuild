#
# spec file for package php71v-sodium
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

%define pkg_name sodium
%define php_dir_prefix /opt/php/php71v
%define phpize %{php_dir_prefix}/usr/bin/phpize
%define phpconfig %{php_dir_prefix}/usr/bin/php-config
%define conf_dir %{php_dir_prefix}/etc/php7/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php71v-sodium
Version:        2.0.4
Release:        1
License:        BSD2
Summary:        Wrapper for the Sodium cryptographic library
Url:            https://github.com/jedisct1/libsodium-php
Group:          Productivity/Networking/Web/Servers
Source:         https://github.com/jedisct1/libsodium-php/archive/%{version}.tar.gz
BuildRequires:  php71v-devel
BuildRequires:  libsodium-devel
Requires:       php71v(api) = %{php_core_api}
Requires:       php71v(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple, low-level PHP extension for libsodium.


%prep
%setup -qn libsodium-php-%{version}

%build
export PATH="/opt/php/php71v/usr/bin/:$PATH"
%{phpize}
%configure --with-libsodium
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
%doc README.md LICENSE CREDITS

%changelog
* Mon Sep 25 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
