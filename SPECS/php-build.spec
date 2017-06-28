#
# spec file for package php-build
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

%define commit 981ad08b91d1e9f21455ae6c3d37031600df3abe

Name:           php-build
Version:        20170623
Release:        3
License:        MIT
Summary:        Builds PHP so that multiple versions can be used side by side
Url:            https://php-build.github.io/
Group:          Development/Tools/Building
Source:         https://github.com/php-build/php-build/archive/%{commit}.tar.gz
Requires:       aspell-devel
Requires:       autoconf
Requires:       bison
Requires:       curl
Requires:       libcurl-devel
Requires:       cyrus-sasl-devel
Requires:       libdb-4_8-devel
Requires:       enchant-devel
Requires:       firebird-devel
Requires:       freetds-devel
Requires:       freetype2-devel
Requires:       gcc-c++
Requires:       gd-devel
Requires:       gmp-devel
Requires:       imap-devel
Requires:       krb5-devel
Requires:       libapparmor-devel
Requires:       libbz2-devel
Requires:       libedit-devel
Requires:       libevent-devel
Requires:       libfbclient2-devel
Requires:       libicu-devel
Requires:       libjpeg62-devel
Requires:       libmcrypt-devel
Requires:       libopenssl-devel
Requires:       libtidy-0_99-0-devel
Requires:       libtiff-devel
Requires:       libxslt-devel
Requires:       libzip-devel
Requires:       ncurses-devel
Requires:       net-snmp-devel
Requires:       openldap2-devel
Requires:       pam-devel
Requires:       pcre-devel
Requires:       pkg-config
Requires:       systemd-devel
Requires:       libvpx-devel
Requires:       libXft-devel
Requires:       libXpm-devel
Requires:       postfix
Requires:       re2c
Requires:       sqlite2-devel
Requires:       sqlite3-devel
Requires:       tcpd-devel
Requires:       unixODBC-devel
Requires:       update-alternatives
Requires:       xorg-x11-devel
Requires:       xz
Requires:       postgresql-devel
Requires:       libtool
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
php-build is a utility for building versions of PHP to use them side by side
with each other. The overall structure is loosly borrowed from Sam Stephenson's
ruby-build.

%prep
%setup -qn %{name}-%{commit}

%build

%install
PREFIX=%{buildroot}/%{_prefix} ./install.sh
rm %{buildroot}%{_prefix}/bin/rbenv-*

%post

%postun

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md LICENSE
%{_bindir}/php-build
%{_bindir}/phpenv-install
%{_bindir}/phpenv-uninstall
%{_bindir}/phpenv-update
%dir %{_datarootdir}/%{name}
%dir %{_datarootdir}/%{name}/after-install.d
%dir %{_datarootdir}/%{name}/before-install.d
%dir %{_datarootdir}/%{name}/definitions
%dir %{_datarootdir}/%{name}/extension
%dir %{_datarootdir}/%{name}/patches
%dir %{_datarootdir}/%{name}/plugins.d
%{_datarootdir}/%{name}/after-install.d/.empty
%{_datarootdir}/%{name}/before-install.d/.empty
%{_datarootdir}/%{name}/default_configure_options
%{_datarootdir}/%{name}/definitions/*
%{_datarootdir}/%{name}/extension/definition
%{_datarootdir}/%{name}/extension/extension.sh
%{_datarootdir}/%{name}/patches/gmp.c.patch
%{_datarootdir}/%{name}/patches/php-5.4.6-libxml2-2.9.patch
%{_datarootdir}/%{name}/patches/xp_ssl.c.patch
%{_datarootdir}/%{name}/patches/zip_direct.c.patch
%{_datarootdir}/%{name}/plugins.d/apc.sh
%{_datarootdir}/%{name}/plugins.d/composer.sh
%{_datarootdir}/%{name}/plugins.d/github.sh
%{_datarootdir}/%{name}/plugins.d/uprofiler.sh
%{_datarootdir}/%{name}/plugins.d/xdebug.sh
%{_datarootdir}/%{name}/plugins.d/xhprof.sh
%{_datarootdir}/%{name}/plugins.d/zendopcache.sh
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.5%{?ext_man}


%changelog
* Wed Jun 28 2017 Marcin Morawski <marcin@morawskim.pl>
-  remove rbenv-* bin

* Tue Jun 27 2017 Marcin Morawski <marcin@morawskim.pl>
-  update to commit 981ad08
-  use wildcard to pack all definitions files

* Mon Jun 26 2017 Marcin Morawski <marcin@morawskim.pl>
-  add Requires (they are required to build php)

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
-  add dir macro

* Fri Apr 28 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
