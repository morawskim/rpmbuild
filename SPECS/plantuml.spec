#
# spec file for package plantuml
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

Name:           plantuml
Version:        8045
Release:        3
License:        LGPLv3+
Summary:        Program to generate UML diagram from a text description
Url:            http://plantuml.com/
Source:         http://downloads.sourceforge.net/plantuml/%{name}-lgpl-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  java-1_7_0-openjdk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%prep
%setup -q -c -n plantuml

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README
touch -r README.orig README
rm README.orig

%build
ant

%install
%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true
%__install -D -m0644 plantuml.jar "%{buildroot}%{_javadir}/plantuml.jar"

%postun

%files
%defattr(-,root,root)
%{_bindir}/plantuml
%attr(744, root, root) %{_javadir}/plantuml.jar
%doc README COPYING

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 8045-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Sun Jul 17 2016 Marcin Morawski <marcin@morawskim.pl>
-  Init release
