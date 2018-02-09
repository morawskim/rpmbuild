#
# spec file for package php-docs
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

%define current_date %(date +\%Y\%m\%d)

Name:           php-docs
Version:        %{current_date}
Release:        2
License:        MIT
Summary:        The PHP Manual in xhtml and man pages formats
Url:            http://doc.php.net
Group:          Development/Languages/PHP
BuildRequires:  git, subversion
BuildRequires:  php >= 5.4
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The PHP Manual in xhtml and man pages formats

%prep
%setup -c %{name} -T

svn co https://svn.php.net/repository/phpdoc/modules/doc-en doc-en
git clone http://git.php.net/repository/phd.git

%build
php doc-en/doc-base/configure.php

# Build man pages
php -dmemory_limit=512M ./phd/render.php --docbook ./doc-en/doc-base/.manual.xml --package PHP --format manpage --output docs/man

# Build xhtml
php -dmemory_limit=512M ./phd/render.php --docbook ./doc-en/doc-base/.manual.xml --package PHP --format xhtml --outputfilename html --output docs/xhtml

%install
mkdir -p %{buildroot}/opt/php/docs/man

cp -r docs/xhtml/php-chunked-xhtml/ %{buildroot}/opt/php/docs/xhtml
cp -r docs/man/php-functions/ %{buildroot}/opt/php/docs/man/man3

%post

%postun

%files
%defattr(-,root,root)
%doc doc-en/doc-base/README doc-en/doc-base/LICENSE
%docdir /opt/php/docs/man/man3
%docdir /opt/php/docs/xhtml
/opt/php/docs/man/man3
/opt/php/docs/xhtml

%changelog
* Fri Feb 09 2018 Marcin Morawski <marcin@morawskim.pl>
-  Change BuildDependiences to php instead php5

* Tue Oct 17 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
