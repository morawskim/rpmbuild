#
# spec file for package greenmail
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

Name:           greenmail
Version:        1.5.5
Release:        2
License:        Apache-2.0
Summary:        Suite of email servers for testing purposes
Url:            http://www.icegreen.com/greenmail
Group:          Development/Tools
Source:         https://github.com/greenmail-mail-test/greenmail/archive/release-%{version}.tar.gz
BuildRequires:  java-1_8_0-openjdk-devel
BuildRequires:  maven
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GreenMail is an intuitive and easy-to-use test suite of email servers for
testing purposes.  It supports SMTP, POP3, IMAP with SSL socket support.
GreenMail also provides a JBoss GreenMail Service.

%prep
%setup -qn %{name}-release-%{version}

%build
export LC_CTYPE="en_US.UTF-8"
mvn -DskipITs clean install

%install
%{__install} -Dp -m 644 greenmail-standalone/target/greenmail-standalone-1.5.5.jar %{buildroot}/%{_javadir}/greenmail.jar

%post

%postun

%files
%defattr(-,root,root)
%doc README.md license.txt
%{_javadir}/greenmail.jar

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 1.5.5-2
- Rebuild for openSUSE 42.3

* Thu Jun 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
