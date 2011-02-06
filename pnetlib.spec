%define		pnet_version	0.7.4
Summary:	The DotGNU Portable .NET library
Summary(pl.UTF-8):	Biblioteka Portable .NET z projektu DotGNU
Name:		pnetlib
Version:	0.7.4
Release:	2
License:	GPL plus linking exception
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	cab8de4301bea6e4777ca95cc8a860bd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	pnet-compiler-csharp = %{pnet_version}
BuildRequires:	pnet-tools = %{pnet_version}
BuildRequires:	treecc >= 0.3.6
Requires:	csunit = %{version}
Requires:	pnet-interpreter = %{pnet_version}
Requires:	pnet-jscript = %{version}
Requires:	pnet-ilinstall = %{version}
Requires:	pnetlib-base = %{version}
Requires:	pnetlib-compat = %{version}
Requires:	pnetlib-irda = %{version}
Requires:	pnetlib-openssl = %{version}
Requires:	pnetlib-visualbasic = %{version}
Requires:	pnetlib-winforms = %{version}
Requires:	pnetlib-xsharp = %{version}
Provides:	pnetlib-tools
# configure scripts don't work with BA: noarch
# BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pnetlib is DotGNU's implementation of the CLI (".NET") standard
Base Class Library. It is designed to be used with programs targeted
at the CLI and locally executed in the pnet-interpreter.

This is a metapackage that requires everything included with the
pnetlib distribution.

%description -l pl.UTF-8
pnetlib jest implementacją, w ramach projektu DotGNU, Standardowej
Biblioteki Klass CLI (".NET"). Jest zaprojektowana w celu użycia w
programach napisanych dla CLI i uruchamianych lokalnie przez
pnet-interpreter.

Jest to metapakiet zawierający wszystko co znajduje się w dystrybucji
pnetlib.

%package base
Summary:	DotGNU Portable .NET library - base files
Summary(pl.UTF-8):	Biblioteka Portable .NET z projektu DotGNU - podstawowe pliki
Group:		Libraries
Requires:	%{name}-ssl = %{version}
Requires:	pnet-interpreter = %{pnet_version}

%description base
This is the standard library of the Portable.Net platform. It is built
according to the ECMA specification for BCL (Ecma-334).

These are the base files for pnetlib -- you need these if you need
anything else from pnetlib. For apps that only use the standard
library, this is all you need.

%description base -l pl.UTF-8
pnetlib jest implementacją, w ramach projektu DotGNU, Standardowej
Biblioteki Klass CLI (".NET"). Jest zaprojektowana w celu użycia w
programach napisanych dla CLI i uruchamianych lokalnie przez
pnet-interpreter.

W tym pakiecie znajdują się podstawowe pliki dla pnetlib. Są one
potrzebne, żeby robić cokolwiek z pnetlib. Dla programów
wykorzystujących tylko standardowe biblioteki jest to wszystko czego
potrzeba.

%package xsharp
Summary:	XFree86 bindings for DotGNU Portable .NET
Summary(pl.UTF-8):	Wiązania XFree86 dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description xsharp
Bindings to various X11 libraries: X11, Xext, and imlib. Install if
you would like to develop or run Portable .NET programs that deal
directly with the X libraries.

This was also written as a torture test for Portable .NET's "pinvoke"
native code calling mechanism. The source code may be useful if you
are interested in using PInvoke.

%description xsharp -l pl.UTF-8
Nakładki na różne biblioteki X11: X11, Xext i imlib. Są potrzebne do
tworzenia aplikacji lub uruchamiania programów Portable .NET
korzystających bezpośrednio z biblotek X11.

Biblioteka została napisana jako test torturujący dla mechanizmu
wywołań bezpośrednich "pinvoke" Portable .NET. Kod źródłowy może być
przydatny dla zainteresowanych korzystaniem z PInvoke.

%package ziplib
Summary:	ziplib library for DotGNU Portable .NET
Summary(pl.UTF-8):	Biblioteka ziplib dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description ziplib
Library to support compression for Portable .NET .

%description ziplib -l pl.UTF-8
Biblioteka do obsługi kompresji dla Portable .NET .

%package openssl
Summary:	OpenSSL support for DotGNU Portable .NET
Summary(pl.UTF-8):	Obsługa OpenSSL dla DotGNU Portable .NET
Group:		Libraries
License:	GPL (but see description)
Requires:	%{name}-base = %{version}
Provides:	%{name}-ssl = %{version}

%description openssl
This is a version of the SSL support engine required by pnetlib that
depends on OpenSSL.

It's recommended not use it in GPL software, as OpenSSL is not
licensed under a GPL-compatible license. Instead, add support for
another SSL engine to pnetlib, preferably the nascent GNU TLS.

%description openssl -l pl.UTF-8
Ten pakiet zawiera wersję silnika SSL wymaganego przez pnetlib
wymagającą biblioteki OpenSSL.

Zaleca się nie korzystać z tego w oprogramowaniu GPL, ponieważ OpenSSL
nie ma licencji zgodnej z GPL. Zamiast tego zaleca się dodać obsługę
innego silnika SSL do pnetlib. Preferowany jest GNU TLS.

%package winforms
Summary:	Windows.Forms for DotGNU Portable .NET
Summary(pl.UTF-8):	Windows.Forms dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}
Requires:	%{name}-compat = %{version}
Requires:	%{name}-xsharp = %{version}
Requires:	%{name}-ziplib = %{version}

%description winforms
Winforms is a GUI library for Portable .NET applications. It depends
on System.Drawing, which in turn depends on XSharp.

This package includes System.Windows.Forms, System.Drawing, and
System.Drawing.Xsharp, a backend that connects it to XSharp. XSharp is
in package pnetlib-xsharp.

Install this package if you wish to build or run applications based on
Portable .NET and Winforms.

%description winforms -l pl.UTF-8
Winforms to biblioteka GUI (graficznego interfejsu użytkownika) dla
aplikacji Portable .NET. Wymaga System.Drawing, które z kolei wymaga
XSharp.

Ten pakiet zawiera System.Windows.Forms, System.Drawing oraz
System.Drawing.Xsharp, czyli backend łączący z XSharp. XSharp znajduje
się w pakiecie pnetlib-xsharp.

Ten pakiet należy zainstalować aby tworzyć lub uruchamiać aplikacje
oparte na Portable .NET oraz Winforms.

%package visualbasic
Summary:	Visual Basic support library for DotGNU Portable .NET
Summary(pl.UTF-8):	Obsługa Visual Basic dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description visualbasic
This is the standard runtime library for Visual Basic programs in
Portable .NET .

Install this package if you wish to build or run programs written in
Visual Basic. Package pnet-compiler-visualbasic includes VB support
for cscc.

%description visualbasic -l pl.UTF-8
To jest standardowa biblioteka uruchomieniowa dla programów w Visual
Basicu w środowisku Portable .NET .

Ten pakiet należy zainstalować aby tworzyć lub uruchamiać programy
napisane w Visual Basicu. Obsługa VB dla cscc znajduje się w pakiecie
pnet-compiler-visualbasic.

%package irda
Summary:	IrDA support for DotGNU Portable .NET
Summary(pl.UTF-8):	Obsługa IrDA dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description irda
This library adds support for infrared devices to the DotGNU Portable
.NET library.

%description irda -l pl.UTF-8
Ten pakiet dodaje do biblioteki DotGNU Portable .NET obsługę urządzeń
komunikujących się przez podczerwień.

%package -n pnet-jscript
Summary:	JScript runtime for DotGNU Portable .NET
Summary(pl.UTF-8):	Biblioteki uruchomieniowe JScript dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}
Requires:	%{name}-compat = %{version}

%description -n pnet-jscript
This is the JScript implementation for Portable .NET . It is designed
to be compatible with the "Microsoft.JScript" assembly from the .NET
Framework SDK.

We include a JScript library, instructions on how to embed it into
your own applications, and a tool, `jsrun', with which to run scripts
from the command line.

%description -n pnet-jscript -l pl.UTF-8
To jest implementacja JScriptu dla Portable .NET . Została tak
zaprojektowana, aby była zgodna z "Microsoft.JScript" z .NET Framework
SDK.

Pakiet zawiera bibliotekę JScript, opis jak osadzać ją we własnych
aplikacjach oraz narzędzie jsrun, przy pomocy którego można uruchamiać
skrypty z linii poleceń.

%package -n pnet-ilinstall
Summary:	IL Assembly Installer
Summary(pl.UTF-8):	Instalator zbiorów IL
Group:		Libraries
Requires:	%{name}-base = %{version}

%description -n pnet-ilinstall
IL Assembly Installer.

%description -n pnet-ilinstall -l pl.UTF-8
Instalator zbiorów IL.

%package -n csunit
Summary:	Simple unit testing suit for DotGNU Portable .NET
Summary(pl.UTF-8):	Prosty zestaw do testowania modułów dla DotGNU Portable .NET
Group:		Development
Requires:	%{name}-base = %{version}

%description -n csunit
A unit testing driver program based on JUnit. Install this if you wish
to run the test suites that come with Portable .NET programs, or write
your own.

Included are a command-line tool to run tests, which should be built
as DLLs, and a library containing csunit's functionality.

%description -n csunit -l pl.UTF-8
Program służący do testowania modułów oparty na JUnit. Należy go
zainstalować aby uruchamiać zbiory testów dostarczane z programami
Portable .NET lub pisać własne testy.

Pakiet zawiera narzędzie do uruchamiania testów z linii poleceń, które
powinny być budowane jako DLL-e oraz bibliotekę zawierającą
funkcjonalność csunit.

%package compat
Summary:	Deprecated .NET compatibility libraries for Portable .NET
Summary(pl.UTF-8):	Nie zalecane biblioteki .NET zachowane dla zgodności
Group:		Libraries
Requires:	%{name}-base = %{version}

%description compat
These assemblies exist to provide compatibility with minor Microsoft
assemblies within the .NET Framework SDK. We do not recommend using
these assemblies in portable code, or in fact at all.

%description compat -l pl.UTF-8
Te zbiory istnieją dla zapewnienia zgodności z pomniejszymi zbiorami
Microsoftu z .NET Framework SDK. Ich używanie jest nie zalecane w
przenośnym kodzie, a najlepiej nie używać ich w ogóle.

%prep
%setup -q

%build
if [ -x /usr/bin/pnet-resgen ]; then
RESGEN=/usr/bin/pnet-resgen
export RESGEN
fi
%{__libtoolize}
%{__aclocal}
%{__automake} --ignore-deps
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_libdir}/cscc/lib/
ln -sf */OpenSystem.Platform.dll */System.Design.dll .

%clean
rm -rf $RPM_BUILD_ROOT

%files base
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/cscc/lib
%dir %{_libdir}/cscc/lib/de
%dir %{_libdir}/cscc/lib/ca
%dir %{_libdir}/cscc/lib/0.81.0.1407
%dir %{_libdir}/cscc/lib/2.0.0.0
%dir %{_libdir}/cscc/lib/2.0.0.0/ca
%dir %{_libdir}/cscc/lib/2.0.0.0/de
%dir %{_libdir}/cscc/lib/8.0.50727.42
%dir %{_libdir}/cscc/lib/8.0.50727.42/ca
%dir %{_libdir}/cscc/lib/8.0.50727.42/de
%{_libdir}/cscc/lib/I18N*
%{_libdir}/cscc/lib/*/I18N*
%{_libdir}/cscc/lib/*/ca/I18N.resources.dll
%{_libdir}/cscc/lib/OpenSystem.*.dll
%{_libdir}/cscc/lib/*/OpenSystem.*.dll
%{_libdir}/cscc/lib/System.Xml.dll
%{_libdir}/cscc/lib/*/System.Xml.dll
%{_libdir}/cscc/lib/*/System.Xml.resources.dll
%{_libdir}/cscc/lib/*/ca/System.Xml.resources.dll
%{_libdir}/cscc/lib/System.dll
%{_libdir}/cscc/lib/*/System.dll
%{_libdir}/cscc/lib/*/System.resources.dll
%{_libdir}/cscc/lib/*/ca/System.resources.dll
%{_libdir}/cscc/lib/System.EnterpriseServices.dll
%{_libdir}/cscc/lib/*/System.EnterpriseServices.dll
%{_libdir}/cscc/lib/ISymWrapper.dll
%{_libdir}/cscc/lib/*/ISymWrapper.dll
#%{_libdir}/cscc/lib/de/*.dll
%{_libdir}/cscc/lib/*/de/*.dll
%{_libdir}/cscc/lib/mscorlib.dll
%{_libdir}/cscc/lib/*/mscorlib.dll
%{_libdir}/cscc/lib/*/mscorlib.resources.dll
%{_libdir}/cscc/lib/*/ca/mscorlib.resources.dll
#%{_libdir}/cscc/lib/pnetlib.here
%{_libdir}/cscc/lib/*/DotGNU.Terminal.*
%{_libdir}/cscc/lib/*/DotGNU.XmlRpc.dll
%{_libdir}/cscc/lib/*/DotGNU.Misc.dll
%{_datadir}/cscc

%files xsharp
%defattr(644,root,root,755)
%{_libdir}/cscc/lib/libXsharpSupport.*
%{_libdir}/cscc/lib/Xsharp.dll
%{_libdir}/cscc/lib/*/Xsharp.resources.dll
%{_libdir}/cscc/lib/*/Xsharp.dll
%{_libdir}/cscc/lib/*/ca/Xsharp.resources.dll

%files openssl
%defattr(644,root,root,755)
%doc DotGNU.SSL/README
%{_libdir}/cscc/lib/DotGNU.SSL.dll
%{_libdir}/cscc/lib/*/DotGNU.SSL.dll

%files ziplib
%defattr(644,root,root,755)
%doc SharpZipLib/README
%{_libdir}/cscc/lib/ICSharpCode.SharpZipLib.dll
%{_libdir}/cscc/lib/*/ICSharpCode.SharpZipLib.dll

%files winforms
%defattr(644,root,root,755)
%doc System.Windows.Forms/HACKING
%{_libdir}/cscc/lib/System.Drawing.*
%{_libdir}/cscc/lib/System.Windows.*
%{_libdir}/cscc/lib/DotGNU.Images.*
%{_libdir}/cscc/lib/System.Design.dll
%{_libdir}/cscc/lib/*/System.Drawing.*
%{_libdir}/cscc/lib/*/ca/System.Drawing.*
%{_libdir}/cscc/lib/*/System.Windows.*
%{_libdir}/cscc/lib/*/ca/System.Windows.*
%{_libdir}/cscc/lib/*/DotGNU.Images.*
%{_libdir}/cscc/lib/*/System.Design.*
%{_libdir}/cscc/lib/*/pinvoke.map
%{_libdir}/cscc/lib/*/System.Deployment.*

%files visualbasic
%defattr(644,root,root,755)
%{_libdir}/cscc/lib/Microsoft.VisualBasic.dll
%{_libdir}/cscc/lib/*/Microsoft.VisualBasic.resources.dll
%{_libdir}/cscc/lib/*/Microsoft.VisualBasic.dll
%{_libdir}/cscc/lib/*/ca/Microsoft.VisualBasic.resources.dll

%files irda
%defattr(644,root,root,755)
%{_libdir}/cscc/lib/System.Net.IrDA.dll
%{_libdir}/cscc/lib/*/System.Net.IrDA.resources.dll
%{_libdir}/cscc/lib/*/System.Net.IrDA.dll
%{_libdir}/cscc/lib/*/ca/System.Net.IrDA.resources.dll

%files -n pnet-jscript
%defattr(644,root,root,755)
%doc JScript/README doc/JScript-embed.txt doc/JScript-internals.txt
%attr(755,root,root) %{_bindir}/jsrun*
%attr(755,root,root) %{_libdir}/cscc/lib/*/jsrun*
%{_libdir}/cscc/lib/Microsoft.JScript.dll
%{_libdir}/cscc/lib/*/Microsoft.JScript.dll

%files -n pnet-ilinstall
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ilinstall*
%attr(755,root,root) %{_libdir}/cscc/lib/*/ilinstall*
%{_libdir}/cscc/lib/System.Configuration.Install.dll
%{_libdir}/cscc/lib/*/System.Configuration.Install.resources.dll
%{_libdir}/cscc/lib/*/System.Configuration.Install.dll
%{_libdir}/cscc/lib/*/ca/System.Configuration.Install.resources.dll

%files -n csunit
%defattr(644,root,root,755)
%doc doc/csunit_howto.html
%attr(755,root,root) %{_bindir}/csunit*
%attr(755,root,root) %{_libdir}/cscc/lib/*/csunit*
%{_libdir}/cscc/lib/cstest.dll
%{_libdir}/cscc/lib/*/cstest.dll

%files compat
%defattr(644,root,root,755)
%{_libdir}/cscc/lib/Microsoft.VisualC.dll
%{_libdir}/cscc/lib/Microsoft.Vsa.dll
%{_libdir}/cscc/lib/Accessibility.dll
%{_libdir}/cscc/lib/cscompmgd.dll
%{_libdir}/cscc/lib/*/Microsoft.VisualC.dll
%{_libdir}/cscc/lib/*/Microsoft.Vsa.dll
%{_libdir}/cscc/lib/*/Accessibility.dll
%{_libdir}/cscc/lib/*/cscompmgd.dll
%{_libdir}/cscc/lib/*/sysglobl.dll
