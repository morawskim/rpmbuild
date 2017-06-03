#
# spec file for package nerd-fonts
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

Name:           nerd-fonts
Version:        1.0.0
Release:        3
License:        MIT
Summary:        Collection of 35+ patched fonts
Url:            http://nerdfonts.com
Group:          System/X11/Fonts
Source:         https://github.com/ryanoasis/nerd-fonts/archive/v1.0.0.tar.gz
BuildRequires:  fontpackages-devel
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%package Monoid
Summary:        Monoid nerd fonts
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description Monoid
Monoid nerd fonts


%package SourceCodePro
Summary:        SourceCodePro nerd fonts
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description SourceCodePro
SourceCodePro nerd fonts

%description
Nerd Fonts is a project that patches developer targeted fonts with a high
number of glyphs (icons). Specifically to add a high number of extra glyphs
from popular 'iconic fonts'.

Collection of 35+ patched fonts (over 74.5k possible variations) with a
FontForge font patcher Python script for Powerline, Font Awesome, Octicons,
Devicons, and other icon fonts. Includes fonts: SourceCodePro, Hack, Droid
Sans, Meslo, AnonymousPro, ProFont, Inconsolata, and more http://nerdfonts.com

%prep
%setup -q

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -m 0644 patched-fonts/Monoid/complete/*.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 patched-fonts/SourceCodePro/Bold/complete/*.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 patched-fonts/SourceCodePro/Light/complete/*.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 patched-fonts/SourceCodePro/Medium/complete/*.ttf %{buildroot}%{_ttfontsdir}
install -m 0644 patched-fonts/SourceCodePro/Regular/complete/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -c -n %{name}-Monoid

%reconfigure_fonts_scriptlets -c -n %{name}-SourceCodePro

%files
%defattr(-,root,root)
%doc readme.md LICENSE

%files Monoid
%{_ttfontsdir}/Monoid*.ttf

%files SourceCodePro
%{_ttfontsdir}/Sauce*.ttf

%changelog
* Sat Jun 03 2017 Marcin Morawski <marcin@morawskim.pl>
-  init release
