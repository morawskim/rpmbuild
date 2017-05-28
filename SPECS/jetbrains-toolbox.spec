#
# spec file for package jetbrains-toolbox
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

Name:           jetbrains-toolbox
Version:        1.3.2421
Release:        1
License:        Commercial
Summary:        A control panel for your tools and projects
Url:            https://www.jetbrains.com/toolbox/app
Group:          Development/Tools/Other
Source:         https://download.jetbrains.com/toolbox/jetbrains-toolbox-%{version}.tar.gz
BuildArch:      x86_64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Manage product updates with ease

The pace of technologies and software updates is ever-accelerating. Stay
up-to-date without compromising your productivity with the Toolbox App: easily
maintain several versions of the same tool, install updates, and roll them back
instantly if needed.


Multiple product versions and EAPs

Toolbox App makes handling several versions of a product easy and painless. No
more worries about where to install or how to remove your favorite tool.
Curious enough to try new features? Toolbox supports Early Access Programs too.


All your projects — in one place

The Toolbox App knows which IDE you use for which project. It shows all your
projects in one list with one-click open action inside the right IDE, and in
its right version if you have several installed. Even if you use a single IDE
and have multiple projects, the Toolbox App will save you clicks opening them.


Login only once and for all

The Toolbox app remembers your JetBrains Account and uses it to automatically
log you into other tools you install.

%prep
%setup -q

%build

%install
%{__install} -D -p -m 0755 jetbrains-toolbox   %{buildroot}/%{_bindir}/jetbrains-toolbox

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/jetbrains-toolbox

%changelog
* Sun May 28 2017 Marcin Morawski <marcin@morawskim.pl>
- Update to 1.3.2421

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Feb 04 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
