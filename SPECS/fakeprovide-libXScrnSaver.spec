Name:          fakeprovide-libXScrnSaver
Version:       20160909204244
Release:       3%{?dist}
Summary:       libXScrnSaver fakeprovide for slack

Group:         Fake
License:       GPL
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source:        %{name}.README
Provides:      libXScrnSaver
Requires:      libXss1
BuildArch:     x86_64

%description
%{summary}

%prep
%setup -c -T

%build
cp %{SOURCE0} .


%install

%files
%defattr(-,root,root,-)
%doc %{name}.README

%changelog
* Mon Aug 14 2017 Marcin Morawski <marcin@morawskim.pl> - 20160909204244-3
- Rebuild for openSUSE 42.3

* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Dec 12 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
