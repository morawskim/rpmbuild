Name:		fakeprovide-libgdbm_compat4
Version:	20180721095337
Release:	1%{?dist}
Summary:	Fake provide for libgdbm_compat4.

Group:		Fake
License:	GPL
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Source:		libgdbm_compat4.README
Provides:	libgdbm_compat4



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

