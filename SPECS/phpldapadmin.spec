#
# spec file for package phpldapadmin
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

%define serverroot /srv/www/htdocs/

Name:           phpldapadmin
Version:        1.2.3
Release:        3
License:        GPL
Summary:        A web interface for LDAP server administration
Url:            http://phpldapadmin.sourceforge.net/
Group:          Productivity/Networking/Web/Frontends
Source:         http://iweb.dl.sourceforge.net/project/phpldapadmin/phpldapadmin-php5/%{version}/phpldapadmin-%{version}.tgz
Patch:          phpldapadmin-fix-php5.5-support.patch
BuildRequires:  coreutils
BuildRequires:  tar
BuildRequires:  bzip2
Requires:       mod_php_any php-ldap php-gettext php-openssl php-xml php-pcre php-session
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
phpLDAPadmin (also known as PLA) is a web-based LDAP client. It provides easy, anywhere-accessible, multi-language administration for your LDAP server.

Its hierarchical tree-viewer and advanced search functionality make it intuitive to browse and administer your LDAP directory. Since it is a web application, this LDAP browser works on many platforms, making your LDAP server easily manageable from any location.

phpLDAPadmin is the perfect LDAP browser for the LDAP professional and novice alike. Its user base consists mostly of LDAP administration professionals.

%prep
%setup
%patch -p1
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
find . -type f -name '.cvsignore' -exec rm {} \;
find . \( -name "*.orig" -o -name "*~" -o -name .gitignore \) -print0 | \
                                xargs -0 rm -f

%build


%install
install -m 755 -d $RPM_BUILD_ROOT%{serverroot}%{name}
cp -dR *.php config hooks htdocs lib locale templates $RPM_BUILD_ROOT%{serverroot}%{name}
touch $RPM_BUILD_ROOT%{serverroot}%{name}/config/config.php
# generate file list
find $RPM_BUILD_ROOT%{serverroot}%{name} -mindepth 1 -maxdepth 1 -type d | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find $RPM_BUILD_ROOT%{serverroot}%{name} -maxdepth 1 -type f | grep -v 'config.inc.php' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST
#install -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT/etc/apache2/conf.d/phpldapadmin.conf


%post

%postun

%files -f FILELIST
%defattr(-,root,root)
%doc INSTALL LICENSE VERSION
%doc doc/*
%dir %{serverroot}%{name}
# we don't need to install config/config.php, but we have to keep it
# in the filelist so that an update doesn't delete it
%ghost %{serverroot}%{name}/config/config.php

%changelog
* Thu Jun 16 2016 Marcin Morawski <marcin@morawskim.pl>
-  add patch for php5.5

* Fri May 27 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
