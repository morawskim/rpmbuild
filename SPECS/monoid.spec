#
# spec file for package monoid
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

Name:           monoid
Version:        0.61
Release:        3
License:        MIT
Summary:        Open Source Coding Font
Url:            http://larsenwork.com/monoid/
Group:          System/X11/Fonts
Source:         https://cdn.rawgit.com/larsenwork/monoid/138e2bd5a459265522f0471ec7fa5401525b660b/Monoid-Dollar-0-1-l.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{reconfigure_fonts_prereq}

%description
Customisable coding font with alternates, ligatures and contextual positioning. 
Crazy crisp at 12px/9pt. http://larsenwork.com/monoid/

%prep
%setup -q -c -n Monoid-Dollar-0-1-l

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc Readme+License.html
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Jun 19 2016 Marcin Morawski <marcin@morawskim.pl>
-  Init release
