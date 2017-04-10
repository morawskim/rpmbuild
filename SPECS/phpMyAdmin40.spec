#
# spec file for package phpMyAdmin40
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

%define pkgname phpMyAdmin
%define apxs %{_sbindir}/apxs2
%define ap_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define ap_docroot %(%{apxs} -q PREFIX)/htdocs
%define pma_config %{_sysconfdir}/%{name}/config.inc.php
%define ap_usr wwwrun
%define ap_grp www

Name:           phpMyAdmin40
Version:        4.0.10.18
Release:        1
License:        GPLv2+
Summary:        Handle the administration of MySQL over the World Wide Web
Url:            https://www.phpmyadmin.net/
Group:          Productivity/Networking/Web/Frontends
Source:         https://files.phpmyadmin.net/%{pkgname}/%{version}/%{pkgname}-%{version}-all-languages.tar.xz
Source1:        %{name}.http
Patch0:         %{name}-config.patch
PreReq:         coreutils sed grep
BuildRequires:  apache2-devel
Requires:       mod_php_any
Requires:       php-bz2
Requires:       php-gd
Requires:       php-iconv
Requires:       php-mbstring
Requires:       php-mcrypt
Requires:       php-mysql
Requires:       php-session
Requires:       php-zlib
Provides:       phpmyadmin40 = %{version}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
phpMyAdmin can manage a whole MySQL server (needs a super-user) as well as a
single database. To accomplish the latter you'll need a properly set up MySQL
user who can read/write only the desired database. It's up to you to look up
the appropriate part in the MySQL manual.

Currently phpMyAdmin can:

  * browse and drop databases, tables, views, fields and indexes
  * create, copy, drop, rename and alter databases, tables, fields and indexes
  * maintenance server, databases and tables, with proposals on server
    configuration
  * execute, edit and bookmark any SQL-statement, even batch-queries
  * load text files into tables
  * create^1 and read dumps of tables
  * export^1 data to various formats: CSV, XML, PDF, ISO/IEC 26300 -
    OpenDocument Text and Spreadsheet, Word, Excel and L^AT[E]X formats
  * import data and MySQL structures from Microsoft Excel and OpenDocument
    spreadsheets, as well as XML, CSV, and SQL files
  * administer multiple servers
  * manage MySQL users and privileges
  * check referential integrity in MyISAM tables
  * using Query-by-example (QBE), create complex queries automatically
    connecting required tables
  * create PDF graphics of your Database layout
  * search globally in a database or a subset of it
  * transform stored data into any format using a set of predefined functions,
    like displaying BLOB-data as image or download-link
  * track changes on databases, tables and views
  * support InnoDB tables and foreign keys (see FAQ 3.6)
  * support mysqli, the improved MySQL extension (see FAQ 1.17)
  * communicate in 57 different languages
  * synchronize two databases residing on the same as well as remote servers
    (see FAQ 9.1)


%prep
%setup -qn %{pkgname}-%{version}-all-languages
%patch0

find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
find . -type f -name '*.orig' -exec rm {} \;

%build

%install
%{__install} -d -m0755 $RPM_BUILD_ROOT%{ap_docroot}/%{name}
%{__cp} -dR *.css *.php *.ico js libraries locale themes \
  $RPM_BUILD_ROOT%{ap_docroot}/%{name}
# install config to config dir
%{__install} -D -m0640 $RPM_BUILD_ROOT%{ap_docroot}/%{name}/config.sample.inc.php \
 $RPM_BUILD_ROOT%{pma_config}

# fix libraries/vendor_config.php
%{__sed} -i -e "s,@docdir@,%{_docdir}/%{name},g" -e "s,@sysconfdir@,%{_sysconfdir}/%{name},g" \
  $RPM_BUILD_ROOT%{ap_docroot}/%{name}/libraries/vendor_config.php

# generate file list
find $RPM_BUILD_ROOT%{ap_docroot}/%{name} -mindepth 1 -maxdepth 1 -type d | sed -e "s@$RPM_BUILD_ROOT@@" > FILELIST
find $RPM_BUILD_ROOT%{ap_docroot}/%{name} -maxdepth 1 -type f | grep -v 'config.inc.php' | sed -e "s@$RPM_BUILD_ROOT@@" >> FILELIST
%{__install} -D -m0644 %{S:1} $RPM_BUILD_ROOT%{ap_sysconfdir}/conf.d/%{name}.conf

# fix paths in http config
%{__sed} -i -e "s,@ap_docroot@,%{ap_docroot},g" -e "s,@name@,%{name},g" \
 -e "s,@docdir@,%{_docdir},g" $RPM_BUILD_ROOT%{ap_sysconfdir}/conf.d/%{name}.conf

%post
# Generate a secret key for this installation
sed -e "s/@BLOWFISH_SECRET@/$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)/" \
    -i %{pma_config}

# Set PmaAbsoluteUri
sed -e "s,@FQDN@,$(cat /etc/HOSTNAME)," \
    -i %{pma_config}

%restart_on_update apache2

%postun
%restart_on_update apache2

%files -f FILELIST
%defattr(644,root,root,755)
%doc ChangeLog
%doc LICENSE README RELEASE-DATE*
%doc examples doc
%dir %attr(0750,root,%{ap_grp}) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
%dir %{ap_docroot}/%{name}
%config(noreplace) %{ap_sysconfdir}/conf.d/%{name}.conf


%changelog
* Mon Apr 10 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
