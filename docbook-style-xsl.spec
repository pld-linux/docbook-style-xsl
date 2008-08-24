Summary:	Norman Walsh's modular stylesheets for DocBook
Summary(pl.UTF-8):	Arkusze stylistyczne XSL dla DocBook DTD
Summary(pt_BR.UTF-8):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.74.0
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/docbook/docbook-xsl-%{version}.tar.bz2
# Source0-md5:	a56b598decd006d5d39e4544c0bfbc6a
Source1:	http://dl.sourceforge.net/docbook/docbook-xsl-doc-%{version}.tar.bz2
# Source1-md5:	3a38cdcfadfacd75ebd1ab6c423d4fd6
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
BuildRequires:	libxml2-progs
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/xmlcatalog
Requires(post,postun):	/etc/xml/catalog
# workaround for rpm/poldek
Requires:	libxml2-progs
Requires:	/etc/xml/catalog
Requires:	sgml-common >= 0.5
AutoReqProv:	no
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java
%define		xsl_path	%{_datadir}/sgml/docbook/xsl-stylesheets
%define		catalog		%{xsl_path}/catalog.xml

%description
Highly customizable XSL stylesheets for DocBook XML DTD. The
stylesheets allow to produce documents in XSL FO, HTML or XHTML
formats.

%description -l pl.UTF-8
Konfigurowalne arkusze stylistyczne dla DocBook XML DTD. Arkusze
stylistyczne, zawarte w tym pakiecie, umożliwiają tworzenie dokumentów
w formacie XSL FO, HTML lub XHTML.

%description -l pt_BR.UTF-8
Stylesheets modulares do Norman Walsh para DocBook.

%package xalan-extensions
Summary:	DocBook Xalan extensions
Summary(pl.UTF-8):	Rozszerzenia DocBook Xalan
Group:		Applications/Publishing/XML
Requires:	xalan-j

%description xalan-extensions
DocBook Xalan extensions.

%description xalan-extensions -l pl.UTF-8
Rozszerzenia DocBook Xalan.

%package saxon-extensions
Summary:	DocBook Saxon extensions
Summary(pl.UTF-8):	Rozszerzenia DocBook Saxon
Group:		Applications/Publishing/XML
Requires:	saxon

%description saxon-extensions
DocBook Saxon extensions.

%description saxon-extensions -l pl.UTF-8
Rozszerzenia DocBook Saxon.

%prep
%setup -q -n docbook-xsl-%{version} -b1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xsl_path},%{_sysconfdir}/xml} \
	$RPM_BUILD_ROOT%{_javalibdir}

cp -a * $RPM_BUILD_ROOT%{xsl_path}

install extensions/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%xmlcat_create $RPM_BUILD_ROOT%{catalog}

%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/%{version} file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}
%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/current file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}

rm -rf $RPM_BUILD_ROOT%{xsl_path}/doc \
	$RPM_BUILD_ROOT%{xsl_path}/BUGS \
	$RPM_BUILD_ROOT%{xsl_path}/ChangeLog \
	$RPM_BUILD_ROOT%{xsl_path}/README \
	$RPM_BUILD_ROOT%{xsl_path}/RELEASE-NOTES.html \
	$RPM_BUILD_ROOT%{xsl_path}/RELEASE-NOTES.xml \
	$RPM_BUILD_ROOT%{xsl_path}/TODO \
	$RPM_BUILD_ROOT%{xsl_path}/WhatsNew \
	$RPM_BUILD_ROOT%{xsl_path}/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{xsl_path} ] ; then
	rm -rf %{xsl_path}
fi

%post
if ! grep -q %{catalog} /etc/xml/catalog ; then
	%xmlcat_add %{catalog}
fi

%preun
if [ "$1" = "0" ] ; then
	%xmlcat_del %{catalog}
fi

%files
%defattr(644,root,root,755)
%doc doc AUTHORS BUGS COPYING NEWS README RELEASE-NOTES.{html,txt} TODO
%{xsl_path}

%files xalan-extensions
%defattr(644,root,root,755)
%{_javalibdir}/xalan*.jar

%files saxon-extensions
%defattr(644,root,root,755)
%{_javalibdir}/saxon*.jar
