Summary:	The DotGNU Portable .NET library
Summary(pl):	Biblioteka Portable .NET z projektu DotGNU
Name:		pnetlib
Version:	0.5.6
Release:	1
License:	GPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-interpreter
BuildRequires:	pnet-compiler >= 0.5.6
BuildRequires:	pnet-tools
Requires:	pnet-interpreter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pnetlib is DotGNU's implementation of the CLI (".NET") standard
Base Class Library. It is designed to be used with programs targeted
at the CLI and locally executed in the pnet-interpreter.

%description -l pl
pnetlib jest implementacj�, w ramach projektu DotGNU, Standardowej
Biblioteki Klass CLI (".NET"). Jest zaprojektowana w celu u�ycia w
programach napisanych dla CLI i uruchamianych lokalnie przez
pnet-interpreter.

%package tools
Summary:	Miscellaneous tools for DotGNU Portable .NET library
Summary(pl):	R�ne narz�dzia bilioteki Portable .NET z projektu DotGNU
Group:		Development/Tools
Requires:	pnetlib = %{version}

%description tools
Miscellaneous tools for DotGNU Portable .NET library.

%description tools -l pl
R�ne narz�dzia bilioteki Portable .NET z projektu DotGNU.

%prep
%setup -q

%build
%{__aclocal}
%{__automake} --ignore-deps
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%{_libdir}/cscc/lib

%files tools
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README doc/*
%attr(755,root,root) %{_bindir}/*
