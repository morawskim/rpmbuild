#
# spec file for package php7-xdebug
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

%define pkg_name xdebug
%define phpize /opt/php/php7/usr/bin/phpize
%define phpconfig /opt/php/php7/usr/bin/php-config
%define conf_dir /opt/php/php7/etc/php7/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php7-xdebug
Version:        2.5.0
Release:        1
License:        BSD-3-Clause
Summary:        Extended PHP debugger
Url:            http://www.xdebug.org/
Group:          Development/Libraries/PHP
Source0:        http://www.xdebug.org/files/%{pkg_name}-%{version}.tgz
Source1:        https://raw.githubusercontent.com/%{pkg_name}/%{pkg_name}/XDEBUG_%(c=%{version}; echo ${c//./_})/%{pkg_name}.ini
BuildRequires:  php7
BuildRequires:  php7-devel
BuildRequires:  php7-soap
Requires:       php7(api) = %{php_core_api}
Requires:       php7(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Xdebug extension helps you debugging your script by providing a lot of
valuable debug information. The debug information that Xdebug can provide
includes the following:

* stack and function traces in error messages with:
o full parameter display for user defined functions
o function name, file name and line indications
o support for member functions
* memory allocation
* protection for infinite recursions

Xdebug also provides:

* profiling information for PHP scripts
* script execution analysis
* capabilities to debug your scripts interactively with a debug client

%prep
%setup -q -n %{pkg_name}-%{version}
%{__mkdir} %{name}
install -m 644 %{SOURCE1} xdebug.ini

%build
export PATH="/opt/php/php7/usr/bin:$PATH"
%{phpize}
pushd %{name}
export CFLAGS="%{optflags}"
../configure --enable-xdebug
#sed -i -e 's|PHP_EXECUTABLE = %{_bindir}/php-cgi|PHP_EXECUTABLE = %{_bindir}/php|' Makefile
make %{?_smp_mflags}
popd
sed -i -e "s|; This is a generated file, do not modify by hand|zend_extension = \"%{ext_dir}/%{pkg_name}.so\"|g" xdebug.ini

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install %{?_smp_mflags} -C %{name} INSTALL_ROOT=%{buildroot}
%{__mkdir} -p %{buildroot}%{conf_dir}
install -m 644 xdebug.ini %{buildroot}%{conf_dir}/xdebug.ini

%post

%postun

%files
%defattr(0644,root,root)
%{ext_dir}/%{pkg_name}.so
%config(noreplace) %{conf_dir}/%{pkg_name}.ini

%changelog
* Mon Apr 03 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
