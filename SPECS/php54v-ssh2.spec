#
# spec file for package php54v-ssh2
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

%define         pkg_name    ssh2
%define         phpize /opt/php/php54v/usr/bin/phpize
%define         phpconfig /opt/php/php54v/usr/bin/php-config
%define         conf_dir /opt/php/php54v/etc/php5/conf.d
%define         ext_dir %(%{phpconfig} --extension-dir)
%define         php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define         php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php54v-ssh2
Version:        0.12
Release:        3
License:        PHP-3.01
Summary:        Bindings for the libssh2 Library
Url:            http://pecl.php.net/ssh2
Group:          Productivity/Networking/Web/Servers
Source:         https://pecl.php.net/get/%{pkg_name}-%{version}.tgz
BuildRequires:  libssh2-devel
BuildRequires:  php54v-devel
Provides:       php54v-ssh2 = %{version}
Obsoletes:      php54v-ssh2 < %{version}
Requires:       php54v(api) = %{php_core_api}
Requires:       php54v(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides bindings to the functions of libssh2 which implements the SSH2
protocol.

%prep
%setup -q -n %{pkg_name}-%{version}
mkdir %{name}

%build
export PATH="/opt/php/php54v/usr/bin:$PATH"
%{phpize}
pushd %{name}
export CFLAGS="%{optflags} -fno-strict-aliasing -fstack-protector"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -fstack-protector"
../configure --with-ssh2=%{_prefix} --with-libdir=%{_lib}
make %{?_smp_mflags}
popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} -C %{name} INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{conf_dir}
echo "; comment out next line to disable ssh2 extension in php" > %{buildroot}%{conf_dir}/%{pkg_name}.ini
echo 'extension = %{pkg_name}.so' >> %{buildroot}%{conf_dir}/%{pkg_name}.ini

%check
pushd %{name}
make %{?_smp_mflags} test
popd

%post

%postun

%files
%defattr(-,root,root,-)
%doc LICENSE
%{ext_dir}/%{pkg_name}.so
%config(noreplace) %{conf_dir}/%{pkg_name}.ini
