%define		pnet_version	0.6.10
Summary:	The DotGNU Portable .NET library
Summary(pl):	Biblioteka Portable .NET z projektu DotGNU
Name:		pnetlib
Version:	0.6.10
Release:	1
License:	GPL plus linking exception
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	126ee95edda10a5865bd215bf831ccec
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	pnet-compiler-csharp = %{pnet_version}
BuildRequires:	pnet-tools = %{pnet_version}
BuildRequires:	treecc >= 0.3.0
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

%description -l pl
pnetlib jest implementacj±, w ramach projektu DotGNU, Standardowej
Biblioteki Klass CLI (".NET"). Jest zaprojektowana w celu u¿ycia w
programach napisanych dla CLI i uruchamianych lokalnie przez
pnet-interpreter.

Jest to metapakiet zawieraj±cy wszystko co znajduje siê w dystrybucji
pnetlib.

%package base
Summary:	DotGNU Portable .NET library - base files
Summary(pl):	Biblioteka Portable .NET z projektu DotGNU - podstawowe pliki
Group:		Libraries
Requires:	%{name}-ssl = %{version}
Requires:	pnet-interpreter = %{pnet_version}

%description base
This is the standard library of the Portable.Net platform. It is built
according to the ECMA specification for BCL (Ecma-334).

These are the base files for pnetlib -- you need these if you need
anything else from pnetlib. For apps that only use the standard
library, this is all you need.

%description base -l pl
pnetlib jest implementacj±, w ramach projektu DotGNU, Standardowej
Biblioteki Klass CLI (".NET"). Jest zaprojektowana w celu u¿ycia w
programach napisanych dla CLI i uruchamianych lokalnie przez
pnet-interpreter.

W tym pakiecie znajduj± siê podstawowe pliki dla pnetlib. S± one
potrzebne, ¿eby robiæ cokolwiek z pnetlib. Dla programów
wykorzystuj±cych tylko standardowe biblioteki jest to wszystko czego
potrzeba.

%package xsharp
Summary:	XFree86 bindings for DotGNU Portable .NET
Summary(pl):	Wi±zania XFree86 dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description xsharp
Bindings to various X11 libraries: X11, Xext, and imlib. Install if
you would like to develop or run Portable .NET programs that deal
directly with the X libraries.

This was also written as a torture test for Portable .NET's "pinvoke"
native code calling mechanism. The source code may be useful if you
are interested in using PInvoke.

%description xsharp -l pl
Nak³adki na ró¿ne biblioteki X11: X11, Xext i imlib. S± potrzebne do
tworzenia aplikacji lub uruchamiania programów Portable .NET
korzystaj±cych bezpo¶rednio z biblotek X11.

Biblioteka zosta³a napisana jako test torturuj±cy dla mechanizmu
wywo³añ bezpo¶rednich "pinvoke" Portable .NET. Kod ¼ród³owy mo¿e byæ
przydatny dla zainteresowanych korzystaniem z PInvoke.

%package ziplib
Summary:	ziplib library for DotGNU Portable .NET
Summary(pl):	Biblioteka ziplib dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description ziplib
Library to support compression for Portable .NET .

%description ziplib -l pl
Biblioteka do obs³ugi kompresji dla Portable .NET .

%package openssl
Summary:	OpenSSL support for DotGNU Portable .NET
Summary(pl):	Obs³uga OpenSSL dla DotGNU Portable .NET
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

%description openssl -l pl
Ten pakiet zawiera wersjê silnika SSL wymaganego przez pnetlib
wymagaj±c± biblioteki OpenSSL.

Zaleca siê nie korzystaæ z tego w oprogramowaniu GPL, poniewa¿ OpenSSL
nie ma licencji zgodnej z GPL. Zamiast tego zaleca siê dodaæ obs³ugê
innego silnika SSL do pnetlib. Preferowany jest GNU TLS.

%package winforms
Summary:	Windows.Forms for DotGNU Portable .NET
Summary(pl):	Windows.Forms dla DotGNU Portable .NET
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

%description winforms -l pl
Winforms to biblioteka GUI (graficznego interfejsu u¿ytkownika) dla
aplikacji Portable .NET. Wymaga System.Drawing, które z kolei wymaga
XSharp.

Ten pakiet zawiera System.Windows.Forms, System.Drawing oraz
System.Drawing.Xsharp, czyli backend ³±cz±cy z XSharp. XSharp znajduje
siê w pakiecie pnetlib-xsharp.

Ten pakiet nale¿y zainstalowaæ aby tworzyæ lub uruchamiaæ aplikacje
oparte na Portable .NET oraz Winforms.

%package visualbasic
Summary:	Visual Basic support library for DotGNU Portable .NET
Summary(pl):	Obs³uga Visual Basic dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description visualbasic
This is the standard runtime library for Visual Basic programs in
Portable .NET .

Install this package if you wish to build or run programs written in
Visual Basic. Package pnet-compiler-visualbasic includes VB support
for cscc.

%description visualbasic -l pl
To jest standardowa biblioteka uruchomieniowa dla programów w Visual
Basicu w ¶rodowisku Portable .NET .

Ten pakiet nale¿y zainstalowaæ aby tworzyæ lub uruchamiaæ programy
napisane w Visual Basicu. Obs³uga VB dla cscc znajduje siê w pakiecie
pnet-compiler-visualbasic.

%package irda
Summary:	IrDA support for DotGNU Portable .NET
Summary(pl):	Obs³uga IrDA dla DotGNU Portable .NET
Group:		Libraries
Requires:	%{name}-base = %{version}

%description irda
This library adds support for infrared devices to the DotGNU Portable
.NET library.

%description irda -l pl
Ten pakiet dodaje do biblioteki DotGNU Portable .NET obs³ugê urz±dzeñ
komunikuj±cych siê przez podczerwieñ.

%package -n pnet-jscript
Summary:	JScript runtime for DotGNU Portable .NET
Summary(pl):	Biblioteki uruchomieniowe JScript dla DotGNU Portable .NET
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

%description -n pnet-jscript -l pl
To jest implementacja JScriptu dla Portable .NET . Zosta³a tak
zaprojektowana, aby by³a zgodna z "Microsoft.JScript" z .NET Framework
SDK.

Pakiet zawiera bibliotekê JScript, opis jak osadzaæ j± we w³asnych
aplikacjach oraz narzêdzie jsrun, przy pomocy którego mo¿na uruchamiaæ
skrypty z linii poleceñ.

%package -n pnet-ilinstall
Summary:	IL Assembly Installer
Summary(pl):	Instalator zbiorów IL
Group:		Libraries
Requires:	%{name}-base = %{version}

%description -n pnet-ilinstall
IL Assembly Installer.

%description -n pnet-ilinstall -l pl
Instalator zbiorów IL.

%package -n csunit
Summary:	Simple unit testing suit for DotGNU Portable .NET
Summary(pl):	Prosty zestaw do testowania modu³ów dla DotGNU Portable .NET
Group:		Development
Requires:	%{name}-base = %{version}

%description -n csunit
A unit testing driver program based on JUnit. Install this if you wish
to run the test suites that come with Portable .NET programs, or write
your own.

Included are a command-line tool to run tests, which should be built
as DLLs, and a library containing csunit's functionality.

%description -n csunit -l pl
Program s³u¿±cy do testowania modu³ów oparty na JUnit. Nale¿y go
zainstalowaæ aby uruchamiaæ zbiory testów dostarczane z programami
Portable .NET lub pisaæ w³asne testy.

Pakiet zawiera narzêdzie do uruchamiania testów z linii poleceñ, które
powinny byæ budowane jako DLL-e oraz bibliotekê zawieraj±c±
funkcjonalno¶æ csunit.

%package compat
Summary:	Deprecated .NET compatibility libraries for Portable .NET
Summary(pl):	Nie zalecane biblioteki .NET zachowane dla zgodno¶ci
Group:		Libraries
Requires:	%{name}-base = %{version}

%description compat
These assemblies exist to provide compatibility with minor Microsoft
assemblies within the .NET Framework SDK. We do not recommend using
these assemblies in portable code, or in fact at all.

%description compat -l pl
Te zbiory istniej± dla zapewnienia zgodno¶ci z pomniejszymi zbiorami
Microsoftu z .NET Framework SDK. Ich u¿ywanie jest nie zalecane w
przeno¶nym kodzie, a najlepiej nie u¿ywaæ ich w ogóle.

%prep
%setup -q

%build
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
rm -rf ${RPM_BUILD_ROOT}

%files base
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/cscc/lib
%dir %{_libdir}/cscc/lib/de
%dir %{_libdir}/cscc/lib/ca
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
