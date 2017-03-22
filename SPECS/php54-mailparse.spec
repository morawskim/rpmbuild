#
# spec file for package php54-mailparse
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

%define pkg_name mailparse
%define php_dir_prefix /opt/php/php54
%define phpize %{php_dir_prefix}/usr/bin/phpize
%define phpconfig %{php_dir_prefix}/usr/bin/php-config
%define conf_dir %{php_dir_prefix}/etc/php5/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php54-mailparse
Version:        2.1.6
Release:        1
License:        PHP-2.2
Summary:        Email Message Manipulation
Url:            https://pecl.php.net/package/mailparse
Group:          Productivity/Networking/Web/Servers
Source:         http://pecl.php.net/get/%{pkg_name}-%{version}.tgz
Patch1:         %{name}.fix_mbstring_requirement.patch
BuildRequires:  php54-devel
BuildRequires:  re2c
Requires:       php54(api) = %{php_core_api}
Requires:       php54(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.

%prep
%setup -qn mailparse-%{version}
%patch1

%build
export PATH="/opt/php/php54/usr/bin/:$PATH"
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
%doc README CREDITS

%changelog
* Wed Mar 22 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
