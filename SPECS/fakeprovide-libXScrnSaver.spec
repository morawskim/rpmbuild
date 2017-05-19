Name:          fakeprovide-libXScrnSaver
Version:       20160909204244
Release:       2%{?dist}
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
* Fri May 19 2017 Marcin Morawski <marcin@morawskim.pl>
- Rebuild for openSUSE 42.2

* Mon Dec 12 2016 Marcin Morawski <marcin@morawskim.pl>
-  init release
