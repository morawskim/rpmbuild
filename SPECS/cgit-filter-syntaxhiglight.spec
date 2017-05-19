#
# spec file for package cgit-filter-syntaxhiglight
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
%global commit0 a8c2ba24bc4a43584c1d46a0909a7ff57c8c0268
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           cgit-filter-syntaxhiglight
Version:        20160430
Release:        2
License:        MIT
Summary:        CSS highlighting styles for cgit
Url:            https://github.com/morawskim/cgit-filter-syntaxhiglight
Source:         https://github.com/morawskim/cgit-filter-syntaxhiglight/archive/%{commit0}.tar.gz
BuildArch:      noarch
Requires:       cgit
Requires:       highlight >= 3.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CSS style for cgit.

%prep
%setup  -qn cgit-filter-syntaxhiglight-%{commit0}

%build
exit 0

%install
%{__install} -D -p -m 0644 cgit-with-highlight.css %{buildroot}/srv/www/htdocs/cgit/cgit-with-highlight.css
%{__install} -D -p -m 0644 highlight.css %{buildroot}/srv/www/htdocs/cgit/highlight.css
%{__install} -D -p -m 0655 syntax-highlighting3.sh %{buildroot}/usr/lib/cgit/filters/syntax-highlighting3.sh

%post
exit 0

%postun
exit 0

%files
%defattr(-,root,root)
/srv/www/htdocs/cgit/cgit-with-highlight.css
/srv/www/htdocs/cgit/highlight.css
/usr/lib/cgit/filters/syntax-highlighting3.sh

%changelog
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sat Apr 30 2016 marcin@morawskim.pl
- Initial release
