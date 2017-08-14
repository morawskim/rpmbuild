#
# spec file for package selenium
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

%define _prefix %{_usr}/lib/selenium
%define version_major 2.53

Name:           selenium
Version:        %{version_major}.0
Release:        4
License:        ASL 2.0
Summary:        Selenium automates browsers
Url:            http://seleniumhq.org/
Group:          Development/Tools
Source0:        http://selenium-release.storage.googleapis.com/%{version_major}/selenium-server-standalone-%{version}.jar
Source1:        selenium.service
Source2:        selenium.sysconfig
Requires:       xvfb-run
Requires:       java >= 1.7.0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Selenium automates browsers. That's it. What you do with that power is entirely
up to you. Primarily it is for automating web applications for testing purposes,
but is certainly not limited to just that. Boring web-based administration tasks
can (and should!) also be automated as well.

Selenium has the support of some of the largest browser vendors who have taken
(or are taking) steps to make Selenium a native part of their browser. It is
also the core technology in countless other browser automation tools, APIs and
frameworks.

%prep
%setup -q -T -c

%build


%install
%__install -D -m0644 "%{SOURCE0}" "%{buildroot}%{_prefix}/selenium-server-standalone-%{version}.jar"
%__install -D -m0644 "%{SOURCE1}" "%{buildroot}/usr/lib/systemd/system/%{name}.service"
%__install -D -m0644 "%{SOURCE2}" "%{buildroot}/etc/sysconfig/%{name}"
%__sed -i 's,@@JAR@@,%{_prefix}/selenium-server-standalone-%{version}.jar,g' "%{buildroot}/usr/lib/systemd/system/%{name}.service"

%pre
/usr/sbin/groupadd -r selenium &>/dev/null || :
/usr/sbin/useradd -g selenium -s /bin/false -r -c "Selenium server" \
    -d "%{_prefix}" selenium &>/dev/null || :

%post

%postun

%files
%defattr(-,root,root)
%dir %{_prefix}
%{_prefix}/selenium-server-standalone-%{version}.jar
/usr/lib/systemd/system/%{name}.service
%config(noreplace) /etc/sysconfig/%{name}

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.53.0-4
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Tue Jun 21 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
