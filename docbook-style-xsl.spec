Summary:	XSL stylesheets for DocBook XML DTD
Summary(pl):	Arkusze stylistyczne XSL dla DocBook XML DTD
Name:		docbook-style-xsl
Version:	1.53.0
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://telia.dl.sourceforge.net/docbook/docbook-xsl-%{version}.tar.gz
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
BuildRequires:	libxml2-progs /usr/bin/xmlcatalog
Requires(post,preun):	/usr/bin/xmlcatalog
Requires:	libxml2
AutoReqProv:	0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define xsl_path %{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
%define catalog  %{xsl_path}/catalog.xml

# please look into docbook-dtd42-xml.spec
%define xmlcat_add_rewrite()	/usr/bin/xmlcatalog --noout --add rewriteSystem %1 %2 %3
%define xmlcat_create()			/usr/bin/xmlcatalog --noout --create %1

%description
Highly customizable XSL stylesheets for DocBook XML DTD. The
stylesheets allow to produce documents in XSL FO, HTML or XHTML
formats.

%description -l pl
Konfigurowalne arkusze stylistyczne dla DocBook XML DTD. Arkusze
stylistyczne, zawarte w tym pakiecie, umo¿liwiaj± tworzenie dokumentów
w formacie XSL FO, HTML lub XHTML.

%prep
%setup -q -n docbook-xsl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xsl_path},%{_sysconfdir}/xml}

cp -a * $RPM_BUILD_ROOT%{xsl_path}

%xmlcat_create $RPM_BUILD_ROOT%{catalog}

%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/%{version} file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/xmlcatalog --noout --add nextCatalog "" %{catalog} /etc/xml/catalog

%preun
/usr/bin/xmlcatalog --noout --del %{catalog} /etc/xml/catalog

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README
%{catalog}
%dir %{xsl_path}
#%attr(755,root,root) %{xsl_path}/bin/*.pl
%{xsl_path}/VERSION
%{xsl_path}/common
#%{xsl_path}/contrib
#%{xsl_path}/doc
#%{xsl_path}/docsrc
%{xsl_path}/extensions
%{xsl_path}/fo
%{xsl_path}/html
%{xsl_path}/images
#%{xsl_path}/indexing
%{xsl_path}/javahelp
%{xsl_path}/lib
%{xsl_path}/template
%{xsl_path}/xhtml
