#
# spec file for package php55v-imagick
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

%define pkg_name imagick
%define php_dir_prefix /opt/php/php55
%define phpize %{php_dir_prefix}/usr/bin/phpize
%define phpconfig %{php_dir_prefix}/usr/bin/php-config
%define conf_dir %{php_dir_prefix}/etc/php5/conf.d
%define ext_dir %(%{phpconfig} --extension-dir)
%define php_core_api %(%{phpize} --version | sed -n '/PHP Api Version:/{s/^[^0-9]*//;p;}')
%define php_zend_api %(%{phpize} --version | sed -n  '/Zend Module Api No:/{s/^[^0-9]*//;p;}')

Name:           php55v-imagick
Version:        3.4.1
Release:        2
License:        PHP License, version 3.01
Summary:        Wrapper to the ImageMagick/GraphicsMagick library
Url:            http://pecl.php.net/package/imagick
Group:          Productivity/Networking/Web/Servers
Source:         http://pecl.php.net/get/imagick-%{version}.tgz
BuildRequires:  php55v-devel
BuildRequires:  ImageMagick-devel >= 6.5.3.10
BuildRequires:  pkgconfig
Requires:       php55v(api) = %{php_core_api}
Requires:       php55v(zend-abi) = %{php_zend_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides a wrapper to the ImageMagick/GraphicsMagick library.

%package devel
Summary:        Header files for imagick development
Group:          Development/C

%description devel
This package contains necessary header files for imagick development.

%prep
%setup -qn imagick-%{version}

%build
export PATH="/opt/php/php55/usr/bin/:$PATH"
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
%dir %{php_dir_prefix}/%{_includedir}/php5/ext/imagick
%doc CREDITS LICENSE

%files devel
%defattr(-,root,root,-)
%{php_dir_prefix}/%{_includedir}/php5/ext/imagick/*.h

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Thu Oct 27 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release

