#
# spec file for package adobe-source-code-pro-fonts
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

%global fontname adobe-source-code-pro
%global version_roman  2.030
%global version_italic 1.050

Name:           %{fontname}-fonts
Version:        %{version_roman}.%{version_italic}
Release:        3
License:        OFL
Summary:        A set of mono-spaced OpenType fonts designed for coding environments
Url:            https://github.com/adobe-fonts/source-code-pro
Group:          System/X11/Fonts
Source:         https://github.com/adobe-fonts/source-code-pro/archive/%{version_roman}R-ro%2f%{version_italic}R-it.tar.gz#/SourceCodePro-%{version_roman}R-ro-%{version_italic}R-it.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%reconfigure_fonts_prereq

%description
This font was designed by Paul D. Hunt as a companion to Source Sans. It has
the same weight range as the corresponding Source Sans design.  It supports
a wide range of languages using the Latin script, and includes all the
characters in the Adobe Latin 4 glyph set.

%prep
%setup -qn source-code-pro-%{version_roman}R-ro-%{version_italic}R-it
sed -i 's/\r//' LICENSE.txt
chmod 644 LICENSE.txt

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README.md LICENSE.txt
%{_ttfontsdir}/

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Nov 06 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
