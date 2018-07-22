Name:		gdbm-lang
Version:	20180721100642
Release:	1%{?dist}
Summary:	Fake provide for gdbm-lang.

Group:		Fake
License:	GPL
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source:		gdbm-lang.README
Provides:	gdbm-lang



BuildArch:	noarch

%description
%{summary}

%prep
%setup -c -T

%build
cp %{SOURCE0} README


%install

%files
%defattr(-,root,root,-)
%doc README



%changelog

