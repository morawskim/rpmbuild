#
# spec file for package selenium-chromedriver
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

Name:           selenium-chromedriver
Version:        2.29
Release:        4
License:        BSD-3-Clause
Summary:        WebDriver for Google Chrome/Chromium
Url:            http://code.google.com/p/chromedriver/
Group:          Development/Tools/Other
Source:         http://chromedriver.storage.googleapis.com/%{version}/chromedriver_linux64.zip
Requires:       google-chrome-stable >= 56
Requires:       selenium = 2.53.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
WebDriver is an open source tool for automated testing of webapps across many
browsers. It provides capabilities for navigating to web pages, user input,
JavaScript execution, and more. ChromeDriver is a standalone server which
implements WebDriver's wire protocol for Chromium. It is being developed by
members of the Chromium and WebDriver teams.

%prep
%setup -q -c -n chromedriver

%build


%install
%__install -D -m0644 "chromedriver" "%{buildroot}%{_prefix}/chromedriver"

%post

%postun

%files
%defattr(-,root,root)
%attr(755, root, root) %{_prefix}/chromedriver

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 2.29-4
- Rebuild for openSUSE 42.3

* Sun May 28 2017 Marcin Morawski <marcin@morawskim.pl>
- Remove Require google-chrome-stable <= 58, because this block update for
  chrome

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon May 15 2017 Marcin Morawski <marcin@morawskim.pl>
-  upgrade to 2.29 (support chrome 56-58)

* Tue Jun 21 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
