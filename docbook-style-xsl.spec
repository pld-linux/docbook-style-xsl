# TODO: unpackaged files:
#    /usr/share/java/lucene-analyzers-3.0.0.jar
#    /usr/share/java/lucene-core-3.0.0.jar
#    /usr/share/java/tagsoup-1.2.1.jar
#    /usr/share/java/webhelpindexer.jar
# (all as webhelpidexer-externsions? -n java-webhelpindexer? use java-lucene.spec after upgrade?)
Summary:	Norman Walsh's modular stylesheets for DocBook
Summary(pl.UTF-8):	Arkusze stylów XSL dla DocBooka
Summary(pt_BR.UTF-8):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.79.0
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Source0:	http://downloads.sourceforge.net/docbook/docbook-xsl-%{version}.tar.bz2
# Source0-md5:	7a55c875fe0e5f67991c662bf6715603
Source1:	http://downloads.sourceforge.net/docbook/docbook-xsl-doc-%{version}.tar.bz2
# Source1-md5:	d1fb7ef57a3e138859e53ba516843316
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
BuildRequires:	libxml2-progs
BuildRequires:	unzip
Requires(post,postun):	/etc/xml/catalog
Requires(post,postun):	/usr/bin/xmlcatalog
# workaround for rpm/poldek
Requires:	/etc/xml/catalog
Requires:	libxml2-progs
Requires:	sgml-common >= 0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
AutoReqProv:	no

%define		_javalibdir	%{_datadir}/java
%define		xsl_path	%{_datadir}/sgml/docbook/xsl-stylesheets
%define		catalog		%{xsl_path}/catalog.xml

%description
Highly customizable XSL stylesheets for DocBook XML DTD. The
stylesheets allow to produce documents in XSL FO, HTML or XHTML
formats.

%description -l pl.UTF-8
Konfigurowalne arkusze stylów dla DocBook XML DTD. Arkusze stylów,
zawarte w tym pakiecie, umożliwiają tworzenie dokumentów w formacie
XSL FO, HTML lub XHTML.

%description -l pt_BR.UTF-8
Stylesheets modulares do Norman Walsh para DocBook.

%package doc
Summary:	Documentation for DocBook XSL stylesheets
Summary(pl.UTF-8):	Dokumentacja do arkuszy stylów DocBook XSL
Group:		Documentation

%description doc
Documentation for DocBook XSL stylesheets.

%description doc -l pl.UTF-8
Dokumentacja do arkuszy stylów DocBook XSL.

%package xalan-extensions
Summary:	DocBook Xalan extensions
Summary(pl.UTF-8):	Rozszerzenia DocBook Xalan
Group:		Applications/Publishing/XML
Requires:	java-xalan

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

cp -a $(find . -mindepth 1 -maxdepth 1 -type d -a ! -name extensions) $RPM_BUILD_ROOT%{xsl_path}
cp -p VERSION.xsl $RPM_BUILD_ROOT%{xsl_path}

cp -p extensions/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%xmlcat_create $RPM_BUILD_ROOT%{catalog}

%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/%{version} file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}
%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/current file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -L %{xsl_path} ] ; then
	rm -rf %{xsl_path}
fi

%post
if ! grep -q %{catalog} %{_sysconfdir}/xml/catalog ; then
	%xmlcat_add %{catalog}
fi

%preun
if [ "$1" = "0" ] ; then
	%xmlcat_del %{catalog}
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING NEWS README RELEASE-NOTES.{html,txt} TODO
%{xsl_path}

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files xalan-extensions
%defattr(644,root,root,755)
%{_javalibdir}/xalan*.jar

%files saxon-extensions
%defattr(644,root,root,755)
%{_javalibdir}/saxon*.jar
